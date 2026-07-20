"""Generate an Obsidian vault mapping the Easyship API from the mirrored docs."""
import json, re, sys
from pathlib import Path
from collections import defaultdict

ROOT = Path(r"D:\EasyShip-API-Analysis")
DOCS = ROOT / "docs"
VAULT = ROOT / "vault"

# ---------- helpers ----------------------------------------------------------

def sanitize(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|#^\[\]{}]', "-", name).strip()
    return re.sub(r"\s+", " ", name)

def read(p: Path) -> str:
    return p.read_text(encoding="utf-8", errors="replace")

def title_of(text: str, fallback: str) -> str:
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else fallback

def intro_of(text: str) -> str:
    """First prose paragraph between the title and the OpenAPI section."""
    body = re.split(r"^# OpenAPI definition", text, flags=re.M)[0]
    body = re.sub(r"^# .+$", "", body, count=1, flags=re.M)
    for para in re.split(r"\n\s*\n", body):
        para = para.strip()
        if para and not para.startswith(("#", ">", "|", "```", "<")):
            para = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", para)
            return (para[:400] + "…") if len(para) > 400 else para
    return ""

def openapi_of(text: str):
    m = re.search(r"# OpenAPI definition\s*```json\n(.*?)\n```", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return None

# Foreign-key field -> resource (tag name) it points at
FK_MAP = [
    (r'courier_service_id', "Courier Services"),
    (r'courier_id', "Couriers"),
    (r'easyship_shipment_id|"shipment_id"', "Shipments"),
    (r'address_id', "Addresses"),
    (r'"box_id"', "Boxes"),
    (r'"product_id"|"sku"', "Products"),
    (r'"pickup_id"', "Pickups"),
    (r'"batch_id"', "Batches"),
    (r'"manifest_id"', "Manifests"),
    (r'payment_source_id', "Payment Sources"),
    (r'"webhook_id"', "Webhooks"),
    (r'tracking_number', "Trackings"),
    (r'item_category_id|"category_id"', "Item Categories"),
    (r'"hs_code"', "HS codes"),
    (r'"state_id"', "States"),
    (r'"store_id"', "Stores"),
    (r'"company_id"', "Companies"),
    (r'"organization_id"', "Organizations"),
    (r'shipping_rule_id|"rule_id"', "Shipping Rules"),
    (r'"country_id"', "Countries"),
    (r'"tag_ids"', "Tags"),
]

def family_of(spec, raw):
    urls = " ".join(s.get("url", "") for s in (spec.get("servers") or [])) if spec else ""
    if not urls:  # fall back to raw text
        urls = raw[:4000]
    if "enterprise-api" in urls: return "Enterprise API"
    if "auth.easyship.com" in urls or "/oauth2/" in urls: return "Partner Auth"
    if "public-api" in urls: return "Public API"
    return "Legacy API"

# ---------- pass 1: parse every reference page --------------------------------

endpoints = {}   # slug -> dict
concepts = {}    # slug -> dict (no OpenAPI paths)
anomalies = []

for f in sorted((DOCS / "reference").glob("*.md")):
    slug = f.stem
    raw = read(f)
    title = title_of(raw, slug)
    spec = openapi_of(raw)
    ops = []
    if spec and spec.get("paths"):
        for path, methods in spec["paths"].items():
            for method, op in methods.items():
                if method.lower() not in ("get", "post", "put", "patch", "delete"):
                    continue
                ops.append({
                    "method": method.upper(), "path": path,
                    "tags": op.get("tags") or ["(untagged)"],
                    "summary": op.get("summary", title),
                })
    if not ops:
        concepts[slug] = {"title": title, "raw": raw, "file": f}
        continue
    scopes = sorted(set(re.findall(r"`((?:public|enterprise)\.[a-z_0-9]+:[a-z_]+)`", raw)))
    refs = sorted({res for pat, res in FK_MAP if re.search(pat, raw)})
    endpoints[slug] = {
        "title": title, "intro": intro_of(raw), "ops": ops,
        "tag": ops[0]["tags"][0], "family": family_of(spec, raw),
        "scopes": scopes, "refs": refs, "slug": slug,
    }

# webhook-event stubs among concepts (they describe event payloads)
EVENT_HINTS = {"batchfinished": "Batches", "batchstarted": "Batches",
    "creditbalancelow": "Credit", "externalshipmentinsured": "Shipments",
    "oauthauthorizationrevoked": "Authorization", "shipmentcancelled": "Shipments",
    "shipmentlabelfailed": "Shipments", "shipmentwarehousestateupdated": "Shipments"}
event_slugs = {s for s in concepts if s in EVENT_HINTS or
               re.match(r"^(shipment|batch|credit|oauth|external)[a-z]+$", s)}

# ---------- pass 2: names & dedupe -------------------------------------------

used = {}
def unique_name(base, disamb):
    name = sanitize(base)
    if name.lower() in used:
        name = sanitize(f"{base} ({disamb})")
        i = 2
        while name.lower() in used:
            name = sanitize(f"{base} ({disamb} {i})"); i += 1
    used[name.lower()] = True
    return name

resources = defaultdict(list)          # tag -> [slug]
for slug, e in endpoints.items():
    resources[e["tag"]].append(slug)

res_family = {}
for tag, slugs in resources.items():
    fams = [endpoints[s]["family"] for s in slugs]
    res_family[tag] = max(set(fams), key=fams.count)

# resource + family + home names claim their titles first
HOME = "Easyship API Brain"
used[HOME.lower()] = True
fam_note = {}
for fam in sorted({e["family"] for e in endpoints.values()}):
    fam_note[fam] = unique_name(f"Easyship {fam}", "family")
res_note = {tag: unique_name(tag, "resource") for tag in resources}
for slug, e in endpoints.items():
    e["note"] = unique_name(e["title"], "Enterprise" if e["family"] == "Enterprise API" else slug)
for slug, c in concepts.items():
    c["note"] = unique_name(c["title"], slug)

# guides
guides = {}
for f in sorted((DOCS / "guides").glob("*.md")) + sorted((DOCS / "recipes").glob("*.md")):
    slug = f.stem
    raw = read(f)
    guides[slug] = {"title": title_of(raw, slug), "raw": raw,
                    "note": None, "file": f}
for slug, g in guides.items():
    g["note"] = unique_name(g["title"], slug)

# ---------- pass 3: write vault ----------------------------------------------

for sub in ("resources", "endpoints", "guides", "concepts", "events"):
    (VAULT / sub).mkdir(parents=True, exist_ok=True)

def link(name): return f"[[{name}]]"

# endpoint notes
for slug, e in endpoints.items():
    op = e["ops"][0]
    fm_scopes = "".join(f'\n  - "{s}"' for s in e["scopes"]) or " []"
    lines = [
        "---",
        f"method: {op['method']}",
        f'endpoint: "{op["path"]}"',
        f"api: {e['family']}",
        f"slug: {slug}",
        f"scopes:{fm_scopes}",
        "---",
        f"# {e['title']}",
        "",
        f"**`{op['method']} {op['path']}`** · {link(res_note[e['tag']])} · {link(fam_note[e['family']])}",
        "",
    ]
    if e["intro"]:
        lines += [e["intro"], ""]
    extra_ops = e["ops"][1:]
    if extra_ops:
        lines += ["Also defines: " + ", ".join(f"`{o['method']} {o['path']}`" for o in extra_ops), ""]
    refs = [r for r in e["refs"] if r in res_note and r != e["tag"]]
    if refs:
        lines += ["## References", ""]
        lines += [f"- {link(res_note[r])}" for r in refs]
        lines += [""]
    lines += ["## Source", "",
              f"- [Official docs](https://developers.easyship.com/reference/{slug})",
              f"- Local mirror: `docs/reference/{slug}.md`", ""]
    (VAULT / "endpoints" / f"{e['note']}.md").write_text("\n".join(lines), encoding="utf-8")

# resource notes
incoming = defaultdict(set)   # resource -> set of resources that reference it
for e in endpoints.values():
    for r in e["refs"]:
        if r in res_note and r != e["tag"]:
            incoming[r].add(e["tag"])

for tag, slugs in resources.items():
    outgoing = sorted({r for s in slugs for r in endpoints[s]["refs"]
                       if r in res_note and r != tag})
    lines = ["---", f"api: {res_family[tag]}", "type: resource", "---",
             f"# {tag}", "",
             f"Part of {link(fam_note[res_family[tag]])}.", "",
             f"## Endpoints ({len(slugs)})", ""]
    for s in sorted(slugs, key=lambda s: (endpoints[s]['ops'][0]['path'], endpoints[s]['ops'][0]['method'])):
        e = endpoints[s]
        op = e["ops"][0]
        lines.append(f"- `{op['method']}` {link(e['note'])} — `{op['path']}`")
    if outgoing:
        lines += ["", "## References", ""] + [f"- {link(res_note[r])}" for r in outgoing]
    if incoming[tag]:
        lines += ["", "## Referenced by", ""] + [f"- {link(res_note[r])}" for r in sorted(incoming[tag])]
    lines.append("")
    (VAULT / "resources" / f"{res_note[tag]}.md").write_text("\n".join(lines), encoding="utf-8")

# concept + event notes
slug_to_note = {s: e["note"] for s, e in endpoints.items()}
for slug, c in concepts.items():
    is_event = slug in event_slugs
    folder = "events" if is_event else "concepts"
    body = re.split(r"^# .+$", c["raw"], 1, re.M)[-1].strip()
    # rewrite doc-site links to wikilinks where we have the note
    def swap(m):
        s2 = m.group(2).removesuffix(".md")
        if s2 in slug_to_note: return link(slug_to_note[s2])
        if s2 in guides: return link(guides[s2]["note"])
        if s2 in concepts: return link(concepts[s2]["note"])
        return m.group(0)
    body = re.sub(r"\[([^\]]+)\]\(https://developers\.easyship\.com/(?:docs|reference)/([a-z0-9_\-]+)(?:\.md)?\)", swap, body)
    lines = ["---", f"type: {'webhook-event' if is_event else 'concept'}", "---",
             f"# {c['title']}", ""]
    if is_event:
        rel = EVENT_HINTS.get(slug)
        rel_l = f" · {link(res_note[rel])}" if rel and rel in res_note else ""
        lines += [f"Webhook event · {link(res_note['Webhooks'])}{rel_l}", ""]
    lines += [body, ""]
    (VAULT / folder / f"{c['note']}.md").write_text("\n".join(lines), encoding="utf-8")

# guide notes
for slug, g in guides.items():
    ref_hits = [h.removesuffix(".md") for h in
                re.findall(r"developers\.easyship\.com/reference/([a-z0-9_\-.]+)", g["raw"])]
    path_hits = re.findall(r'"?/(?:2024-09|2023-01)/([a-z_]+)"?', g["raw"])
    mentioned = sorted({h for h in ref_hits + path_hits if h in slug_to_note})
    # also connect by resource keyword mention in title
    res_hits = sorted({tag for tag in resources
                       if re.search(rf"\b{re.escape(tag.lower().rstrip('s'))}", g["title"].lower())})
    lines = ["---", "type: guide", "---", f"# {g['title']}", ""]
    ep_links = sorted({slug_to_note[s2] for s2 in mentioned})
    if ep_links:
        lines += ["## Endpoints used", ""] + [f"- {link(n)}" for n in ep_links] + [""]
    if res_hits:
        lines += ["## Related resources", ""] + [f"- {link(res_note[t])}" for t in res_hits] + [""]
    lines += ["## Source", "", f"- Local mirror: `docs/{g['file'].parent.name}/{slug}.md`",
              f"- [Official docs](https://developers.easyship.com/docs/{slug})", ""]
    (VAULT / "guides" / f"{g['note']}.md").write_text("\n".join(lines), encoding="utf-8")

# family notes
for fam, note in fam_note.items():
    tags = sorted(t for t in resources if res_family[t] == fam)
    lines = ["---", "type: api-family", "---", f"# {note}", "",
             f"Part of {link(HOME)}.", "", "## Resources", ""]
    lines += [f"- {link(res_note[t])} ({len(resources[t])} endpoints)" for t in tags]
    lines.append("")
    (VAULT / f"{note}.md").write_text("\n".join(lines), encoding="utf-8")

# core flow note
FLOW = ["Rates", "Shipments", "Couriers", "Pickups", "Manifests", "Trackings"]
flow_l = [f"1. Request rates → {link(res_note['Rates'])}" if False else None]
flow_lines = ["---", "type: concept", "---", "# Core Shipping Flow", "",
    "The happy path for shipping with Easyship:", "",
    f"1. Validate addresses → {link(res_note['Addresses'])}",
    f"2. Request rates → {link(res_note['Rates'])}",
    f"3. Create shipment (+ buy label) → {link(res_note['Shipments'])}",
    f"4. Pick courier / services → {link(res_note['Couriers'])} · {link(res_note['Courier Services'])}",
    f"5. Schedule pickup → {link(res_note['Pickups'])}",
    f"6. Generate manifest → {link(res_note['Manifests'])}",
    f"7. Track delivery → {link(res_note['Trackings'])}",
    f"8. Get notified → {link(res_note['Webhooks'])}",
    ""]
(VAULT / "concepts" / "Core Shipping Flow.md").write_text("\n".join(flow_lines), encoding="utf-8")

# home note
lines = ["---", "type: home", "---", f"# {HOME}", "",
         "Map of the entire Easyship API surface. Open Obsidian's **Graph view** to see the brain map.", "",
         "## API families", ""]
lines += [f"- {link(n)}" for n in fam_note.values()]
lines += ["", "## Start here", "", f"- [[Core Shipping Flow]]",
          "", "## Guides", ""]
lines += [f"- {link(g['note'])}" for g in guides.values()]
lines += ["", "## Concepts", ""]
lines += [f"- {link(c['note'])}" for s, c in concepts.items() if s not in event_slugs]
lines.append("")
(VAULT / f"{HOME}.md").write_text("\n".join(lines), encoding="utf-8")

# graph color config
obsidian = VAULT / ".obsidian"
obsidian.mkdir(exist_ok=True)
graph = {
  "collapse-filter": True, "search": "", "showTags": False, "showAttachments": False,
  "hideUnresolved": False, "showOrphans": True,
  "collapse-color-groups": False,
  "colorGroups": [
    {"query": "path:endpoints", "color": {"a": 1, "rgb": 5431473}},
    {"query": "path:resources", "color": {"a": 1, "rgb": 16744192}},
    {"query": "path:guides", "color": {"a": 1, "rgb": 4964035}},
    {"query": "path:concepts", "color": {"a": 1, "rgb": 11621088}},
    {"query": "path:events", "color": {"a": 1, "rgb": 16766720}},
    {"query": "path:\"/\" -path:endpoints -path:resources -path:guides -path:concepts -path:events", "color": {"a": 1, "rgb": 15277667}},
  ],
  "collapse-display": False, "showArrow": True, "textFadeMultiplier": -0.4,
  "nodeSizeMultiplier": 1.2, "lineSizeMultiplier": 0.6,
  "collapse-forces": False, "centerStrength": 0.4, "repelStrength": 12,
  "linkStrength": 0.9, "linkDistance": 180, "scale": 0.35,
}
(obsidian / "graph.json").write_text(json.dumps(graph, indent=2), encoding="utf-8")
(obsidian / "app.json").write_text("{}", encoding="utf-8")

# ---------- report ------------------------------------------------------------
print(f"endpoints: {len(endpoints)}")
print(f"resources: {len(resources)}")
print(f"guides:    {len(guides)}")
print(f"concepts:  {len(concepts) - len(event_slugs)}  events: {len(event_slugs)}")
fam_counts = defaultdict(int)
for e in endpoints.values(): fam_counts[e["family"]] += 1
print("families: ", dict(fam_counts))
edge_count = sum(len([r for r in e['refs'] if r in res_note and r != e['tag']]) + 1 for e in endpoints.values())
print(f"endpoint->resource edges (incl membership): ~{edge_count}")
if anomalies: print("ANOMALIES:", anomalies)
