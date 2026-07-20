# Easyship - Shipping MCP

<style>
  /* ─── Easyship MCP Docs (ReadMe Custom Page) ─── */
  .es-mcp { font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif; color: #1A1F2B; line-height: 1.6; max-width: 820px; margin: 0 auto; padding: 20px 0 60px; }
  .es-mcp h1 { font-size: 30px; font-weight: 700; color: #0D1117; margin-bottom: 8px; letter-spacing: -0.02em; }
  .es-mcp .subtitle { font-size: 16px; color: #6B7280; margin-bottom: 36px; line-height: 1.5; }
  .es-mcp h2 { font-size: 20px; font-weight: 700; color: #0D1117; margin: 44px 0 16px; padding-top: 20px; border-top: 1px solid #F3F4F6; letter-spacing: -0.01em; }
  .es-mcp section:first-of-type h2 { border-top: none; margin-top: 0; padding-top: 0; }
  .es-mcp h3 { font-size: 16px; font-weight: 700; color: #0D1117; margin: 28px 0 10px; }
  .es-mcp h4 { font-size: 14.5px; font-weight: 600; color: #0D1117; margin: 20px 0 8px; }
  .es-mcp p { margin-bottom: 14px; font-size: 14.5px; color: #374151; }
  .es-mcp a { color: #0052FF; text-decoration: none; }
  .es-mcp a:hover { text-decoration: underline; }
  .es-mcp strong { color: #0D1117; }

  /* Callout */
  .es-mcp .callout { background: #E8F0FF; border-left: 3px solid #0052FF; padding: 12px 16px; border-radius: 0 8px 8px 0; margin: 16px 0; font-size: 13.5px; color: #374151; }
  .es-mcp .callout strong { color: #0D1117; }
  .es-mcp .callout.warn { background: #FEF3C7; border-left-color: #F59E0B; }
  .es-mcp .callout.tip { background: #D1FAE5; border-left-color: #10B981; }

  /* Code */
  .es-mcp pre { background: #0D1117; color: #E5E7EB; border-radius: 8px; padding: 18px 20px; overflow-x: auto; font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace; font-size: 13px; line-height: 1.65; margin: 12px 0 20px; }
  .es-mcp pre .comment { color: #6B7280; }
  .es-mcp pre .string { color: #86EFAC; }
  .es-mcp pre .key { color: #93C5FD; }
  .es-mcp code { font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace; font-size: 12.5px; background: #F3F4F6; padding: 2px 6px; border-radius: 4px; color: #1A1F2B; }
  .es-mcp pre code { background: none; padding: 0; color: inherit; }

  /* Connect Section Containers */
  .es-mcp .connect-method { border: 1px solid #E5E7EB; border-radius: 8px; padding: 20px 24px; margin-bottom: 24px; background: #F9FAFB; }
  .es-mcp .connect-method h3 { margin-top: 0; color: #0052FF; border-bottom: 1px solid #E5E7EB; padding-bottom: 12px; margin-bottom: 16px; }

  /* Tables */
  .es-mcp table { width: 100%; border-collapse: collapse; font-size: 13.5px; margin: 12px 0 24px; }
  .es-mcp th { text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase; letter-spacing: 0.05em; color: #6B7280; padding: 10px 12px; border-bottom: 2px solid #E5E7EB; background: #F9FAFB; }
  .es-mcp td { padding: 8px 12px; border-bottom: 1px solid #F3F4F6; vertical-align: top; font-size: 13.5px; }
  .es-mcp tr:hover td { background: #F9FAFB; }
  .es-mcp .resource-label { font-weight: 700; color: #0D1117; font-size: 13px; }
  .es-mcp .tool-name { font-family: 'JetBrains Mono', 'SF Mono', Consolas, monospace; font-size: 12.5px; color: #0052FF; font-weight: 500; }
  .es-mcp .tool-desc { color: #374151; font-size: 13px; }
  .es-mcp .scope-badge { font-family: 'JetBrains Mono', monospace; font-size: 11px; background: #F3F4F6; padding: 2px 7px; border-radius: 4px; color: #374151; white-space: nowrap; }

  /* Badges */
  .es-mcp .badge { font-size: 11px; font-weight: 600; padding: 2px 8px; border-radius: 4px; white-space: nowrap; }
  .es-mcp .badge-green { background: #D1FAE5; color: #065F46; }
  .es-mcp .badge-blue { background: #E8F0FF; color: #0052FF; }
  .es-mcp .badge-gray { background: #F3F4F6; color: #374151; }
  .es-mcp .badge-amber { background: #FEF3C7; color: #92400E; }

  /* Prompt cards */
  .es-mcp .prompt-grid { display: grid; grid-template-columns: 1fr; gap: 10px; margin: 14px 0 20px; }
  .es-mcp .prompt-card { background: #F9FAFB; border: 1px solid #E5E7EB; border-radius: 8px; padding: 14px 16px; font-size: 13px; color: #374151; line-height: 1.45; transition: border-color 0.15s; }
  .es-mcp .prompt-card:hover { border-color: #0052FF; }
  .es-mcp .prompt-card .label { font-size: 10.5px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.04em; color: #6B7280; margin-bottom: 4px; }
  .es-mcp .prompt-card .tool-tag { font-family: 'JetBrains Mono', monospace; font-size: 11px; color: #0052FF; background: #E8F0FF; padding: 1px 6px; border-radius: 3px; margin-left: 6px; }
  .es-mcp .prompt-card .prompt-text { color: #374151; font-style: italic; }

  /* Steps */
  .es-mcp .steps { counter-reset: step; margin: 16px 0 24px; }
  .es-mcp .step { display: flex; gap: 14px; margin-bottom: 16px; }
  .es-mcp .step::before { counter-increment: step; content: counter(step); flex-shrink: 0; width: 28px; height: 28px; background: #0052FF; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 700; margin-top: 2px; }
  .es-mcp .step-content { flex: 1; font-size: 14px; color: #374151; }
  .es-mcp .step-content strong { color: #0D1117; }

  /* FAQ (Sequential Layout) */
  .es-mcp .faq-item { border-bottom: 1px solid #F3F4F6; padding: 20px 0; }
  .es-mcp .faq-q { font-weight: 700; font-size: 15px; color: #0D1117; margin-bottom: 10px; }
  .es-mcp .faq-a { font-size: 14.5px; color: #374151; }

  /* Feedback */
  .es-mcp .feedback-box { background: linear-gradient(135deg, #E8F0FF 0%, #F0F4FF 100%); border: 1px solid #C7D7FF; border-radius: 10px; padding: 24px 28px; margin-top: 8px; }
  .es-mcp .feedback-box p { margin-bottom: 14px; }
  .es-mcp .feedback-box .feedback-cta { display: inline-block; background: #0052FF; color: #fff; font-weight: 600; font-size: 13.5px; padding: 9px 20px; border-radius: 6px; text-decoration: none; transition: background 0.15s; }
  .es-mcp .feedback-box .feedback-cta:hover { background: #0041CC; text-decoration: none; }
</style>

<div class="es-mcp">

<section id="overview">
<p class="subtitle">Integrate shipping operations directly into AI-powered workflows using natural language. Compare rates, create shipments, buy labels, schedule pickups, track deliveries, and analyze data — across 550+ couriers in 200+ countries.</p>

<p>The Easyship <a href="https://modelcontextprotocol.io" target="_blank" rel="noopener noreferrer">Model Context Protocol (MCP)</a> server provides tools that AI agents can use to interact with the Easyship API. Instead of manually orchestrating API calls, developers connect an MCP-compatible client and let the AI assistant handle end-to-end logistics tasks.</p>

<div class="callout">
 <strong>What is MCP?</strong> Model Context Protocol is an open standard that allows AI clients to connect to external tools and services. The AI assistant discovers available tools, executes structured operations, and maintains context across workflows. <a href="https://modelcontextprotocol.io" target="_blank" rel="noopener noreferrer">Learn more →</a>
</div>
</section>

<section id="platforms">
<h2>Supported platforms</h2>

<h3>AI coding environments</h3>
<table>
  <thead><tr><th>Platform</th><th>How to connect</th></tr></thead>
  <tbody>
    <tr><td>Cursor</td><td><span class="badge badge-green">Plugin</span><a href="https://cursor.directory/plugins/easyship-shipping-mcp" target="_blank" rel="noopener noreferrer">Cursor Directory</a> · <a href="https://cursor.com/marketplace" target="_blank" rel="noopener noreferrer">Cursor Marketplace</a> or manual config</td></tr>
    <tr><td>VS Code</td><td><span class="badge badge-blue">MCP config</span> <code>.vscode/mcp.json</code></td></tr>
    <tr><td>Windsurf</td><td><span class="badge badge-blue">MCP config</span> Manual MCP setup</td></tr>
  </tbody>
</table>

<h3>Chat &amp; assistant apps</h3>
<table>
  <thead><tr><th>Platform</th><th>How to connect</th></tr></thead>
  <tbody>
    <tr><td>Claude Desktop</td><td><span class="badge badge-green">Plugin</span> Config file or <a href="https://github.com/easyship/easyship-mcp-plugin" target="_blank" rel="noopener noreferrer">via Plugin</a></td></tr>
    <tr><td>Claude Code</td><td><span class="badge badge-green">Plugin</span> <code>/plugin install</code> or CLI command</td></tr>
		<tr><td>Grok</td><td><span class="badge badge-green">OAuth</span> <a href="https://support.easyship.com/hc/en-us/articles/36080398584338-How-to-Connect-Grok-to-the-Easyship-MCP-Server" target="_blank" rel="noopener noreferrer">Setup guide</a></td></tr>
    <tr><td>ChatGPT</td><td><span class="badge badge-amber">Coming soon</span></td></tr>
  </tbody>
</table>

<h3>Cloud AI &amp; APIs (for builders)</h3>
<table>
  <thead><tr><th>Platform</th><th>How to connect</th></tr></thead>
  <tbody>
    <tr><td>OpenAI Responses API / Agents SDK</td><td>Pass Bearer token in <code>headers</code></td></tr>
    <tr><td>Gemini CLI</td><td><span class="badge badge-green">Extension</span> <code>gemini extensions install</code></td></tr>
    <tr><td>Codex CLI</td><td><span class="badge badge-blue">MCP config</span> <code>~/.codex/config.toml</code></td></tr>
  </tbody>
</table>

<h3>Workflow automation</h3>
<table>
  <thead><tr><th>Platform</th><th>How to connect</th></tr></thead>
  <tbody>
    <tr><td>n8n</td><td><span class="badge badge-blue">MCP client</span> Native MCP Client Tool Action</td></tr>
    <tr><td>Activepieces</td><td><span class="badge badge-blue">MCP client</span> Native MCP Client Tool Action</td></tr>
    <tr><td>Zapier</td><td><span class="badge badge-blue">MCP client</span> Native MCP Client Tool Action</td></tr>
  </tbody>
</table>

<h3>Skills-first / hybrid</h3>
<table>
  <thead><tr><th>Platform</th><th>How to connect</th></tr></thead>
  <tbody>
    <tr><td>OpenClaw / Perplexity</td><td><span class="badge badge-gray">Skill</span> <a href="https://clawhub.ai/paulld/easyship-official" target="_blank" rel="noopener noreferrer">ClawHub skill</a></td></tr>
  </tbody>
</table>
</section>

<section id="setup">
<h2>Setup guide</h2>

<h3>Prerequisites</h3>
<p>Before connecting, you need:</p>
<table>
  <tbody>
    <tr><td><strong>Easyship account</strong></td><td><a href="https://www.easyship.com" target="_blank" rel="noopener noreferrer">Sign up free</a></td></tr>
    <tr><td><strong>API token</strong></td><td>With required scopes — see <a href="#scopes">Authorization scopes</a></td></tr>
    <tr><td><strong>MCP-compatible client</strong></td><td>See <a href="#platforms">Supported platforms</a> above</td></tr>
    <tr><td><strong>Python 3.8+</strong> <em>(local mode only)</em></td><td>With <a href="https://docs.astral.sh/uv/" target="_blank" rel="noopener noreferrer">uv</a> installed. Not needed for remote.</td></tr>
  </tbody>
</table>

<h3>Get your API token</h3>
<div class="steps">
  <div class="step"><div class="step-content">Go to <a href="https://app.easyship.com/connect" target="_blank" rel="noopener noreferrer">Easyship Dashboard → Connect</a> and click <strong>New Integration</strong></div></div>
  <div class="step"><div class="step-content">Scroll to <strong>API Integration</strong></div></div>
  <div class="step"><div class="step-content">Select <strong>"I am developing a custom integration"</strong></div></div>
  <div class="step"><div class="step-content">Name the key <strong>Easyship MCP</strong> for easy reference</div></div>
  <div class="step"><div class="step-content">Keep the default version <strong>2024-09</strong> and click <strong>Connect</strong></div></div>
  <div class="step"><div class="step-content">Click <strong>Access Token</strong> and copy it using the copy button</div></div>
</div>

<div class="callout tip">
  <strong>Tip:</strong> The remote server at <code>mcp.easyship.com</code> is always available — no installation or local setup required. Just point your MCP client to the URL with your token.
</div>
</section>

<section id="connect">
<h2>Connect to the MCP server</h2>

<p>Two connection methods are available:</p>
<table style="margin-bottom:32px">
  <tr><td><strong>Remote</strong></td><td>Connects to <code>mcp.easyship.com</code> — no dependencies needed</td></tr>
  <tr><td><strong>Local</strong></td><td>Runs <code>easyship-mcp</code> on your machine via <code>uvx</code> — requires <a href="https://docs.astral.sh/uv/" target="_blank" rel="noopener noreferrer">uv</a> + Python 3.8+</td></tr>
</table>
<div class="callout">
  <strong>⚠️ Security Note:</strong> Never share your API token in the chat window. If you accidentally paste it in a prompt, revoke and rotate your API key immediately in the Easyship Dashboard.
</div>

<div class="connect-method">
  <h3>Cursor</h3>
  <p>Add to <code>.cursor/mcp.json</code> (project) or <code>~/.cursor/mcp.json</code> (global):</p>
<pre><code>{
  <span class="key">"mcpServers"</span>: {
    <span class="key">"easyship"</span>: {
      <span class="key">"url"</span>: <span class="string">"https://mcp.easyship.com/mcp"</span>,
      <span class="key">"headers"</span>: {
        <span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_TOKEN"</span>
      }
    }
  }
}</code></pre>
  <p>Replace <code>YOUR_TOKEN</code> with your API token. Save and restart Cursor.</p>
</div>

<div class="connect-method">
  <h3>Claude Code</h3>
  <h4>Remote (recommended)</h4>
<pre><code>claude mcp add --transport http easyship \
  https://mcp.easyship.com/mcp \
  --header <span class="string">'Authorization:Bearer YOUR_TOKEN'</span></code></pre>
  <h4>Local (uvx)</h4>
<pre><code>export EASYSHIP_API_ACCESS_TOKEN=<span class="string">"YOUR_TOKEN"</span>
claude mcp add easyship -- uvx easyship-mcp</code></pre>
  <h4>Via plugin</h4>
<pre><code>/plugin marketplace add easyship/easyship-ai-toolkit
/plugin install easyship-plugin@easyship-ai-toolkit</code></pre>
</div>

<div class="connect-method">
  <h3>Claude Desktop</h3>
  <p>Edit <code>~/Library/Application Support/Claude/claude_desktop_config.json</code> (macOS) or <code>%APPDATA%\Claude\claude_desktop_config.json</code> (Windows):</p>
<pre><code>{
  <span class="key">"mcpServers"</span>: {
    <span class="key">"easyship"</span>: {
      <span class="key">"command"</span>: <span class="string">"uvx"</span>,
      <span class="key">"args"</span>: [<span class="string">"easyship-mcp"</span>],
      <span class="key">"env"</span>: {
        <span class="key">"EASYSHIP_API_ACCESS_TOKEN"</span>: <span class="string">"YOUR_TOKEN"</span>
      }
    }
  }
}</code></pre>
  <p>Replace <code>YOUR_TOKEN</code>. Save and <strong>fully restart</strong> Claude Desktop (quit, don't just close the window).</p>
  <div class="callout">
    <strong>Note:</strong> Claude Desktop uses the local (uvx) method, which requires <a href="https://docs.astral.sh/uv/" target="_blank" rel="noopener noreferrer">uv</a> and Python 3.8+ installed on your machine.
  </div>
</div>

<div class="connect-method">
  <h3>VS Code</h3>
  <p>Add to <code>.vscode/mcp.json</code> in your project:</p>
<pre><code>{
  <span class="key">"servers"</span>: {
    <span class="key">"easyship"</span>: {
      <span class="key">"type"</span>: <span class="string">"http"</span>,
      <span class="key">"url"</span>: <span class="string">"https://mcp.easyship.com/mcp"</span>,
      <span class="key">"headers"</span>: {
        <span class="key">"Authorization"</span>: <span class="string">"Bearer YOUR_TOKEN"</span>
      }
    }
  }
}</code></pre>
</div>

<div class="connect-method">
  <h3>Gemini CLI</h3>
<pre><code>gemini extensions install https://github.com/easyship/easyship-ai-toolkit</code></pre>
  <p>Or add manually:</p>
<pre><code>gemini mcp add --transport http easyship \
  https://mcp.easyship.com/mcp \
  --header <span class="string">'Authorization:Bearer YOUR_TOKEN'</span></code></pre>
</div>

<div class="connect-method">
  <h3>Codex CLI</h3>
  <p>Add to <code>~/.codex/config.toml</code>:</p>
<pre><code>[mcp_servers.easyship]
url = <span class="string">"https://mcp.easyship.com/mcp"</span>
bearer_token_env_var = <span class="string">"EASYSHIP_API_ACCESS_TOKEN"</span></code></pre>
  <p>Then set the environment variable: <code>export EASYSHIP_API_ACCESS_TOKEN="YOUR_TOKEN"</code></p>
</div>

<div class="connect-method">
  <h3>OpenAI API</h3>
  <p>Use the Easyship MCP server with <a href="https://platform.openai.com/docs/guides/tools-connectors-mcp" target="_blank" rel="noopener noreferrer">OpenAI's Responses API</a>:</p>
<pre><code><span class="comment"># Python</span>
from openai import OpenAI

client = OpenAI()
resp = client.responses.create(
model=<span class="string">"gpt-4.1"</span>,
tools=\[{
        <span class="string">"type"</span>: <span class="string">"mcp"</span>,
        <span class="string">"server_label"</span>: <span class="string">"easyship"</span>,
        <span class="string">"server_url"</span>: <span class="string">"https://mcp.easyship.com/mcp"</span>,
        <span class="string">"require_approval"</span>: <span class="string">"never"</span>,
        <span class="string">"headers"</span>: {
            <span class="string">"Authorization"</span>: <span class="string">"Bearer YOUR_EASYSHIP_TOKEN"</span>
        }
    }],
input=<span class="string">"What are the cheapest shipping options from HK to NYC for a 1.5kg package?"</span>
)
print(resp.output\_text)</code></pre>

  <div class="callout">
    <strong>Note:</strong> This works with the Responses API and Agents SDK today. For ChatGPT consumer UI (chat.openai.com), OAuth support is required — coming soon.
  </div>
</div>

<div class="connect-method">
  <h3>Other Clients</h3>
  <p>For any MCP client that supports <a href="https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http" target="_blank" rel="noopener noreferrer">Streamable HTTP</a>:</p>
<pre><code>URL:    https://mcp.easyship.com/mcp
Header: Authorization: Bearer YOUR_TOKEN</code></pre>
  <p>For <strong>stdio-based clients</strong>, run <code>uvx easyship-mcp</code> with <code>EASYSHIP_API_ACCESS_TOKEN</code> set in the environment.</p>
</div>

</section>

<section id="tools">
<h2>Tools</h2>

<p>The server exposes the following <a href="https://modelcontextprotocol.io/docs/concepts/tools" target="_blank" rel="noopener noreferrer">MCP tools</a>. Each tool maps to one or more Easyship API endpoints.</p>

<table>
  <thead><tr><th>Resource</th><th>Tool</th><th>Description</th></tr></thead>
  <tbody>
    <tr>
      <td><span class="resource-label">Rates</span></td>
      <td><span class="tool-name">get_rates</span></td>
      <td class="tool-desc">Compare courier options with prices, delivery times, and duty estimates</td>
    </tr>
    <tr><td colspan="3" style="padding:0;border:none;height:4px"></td></tr>
    <tr>
      <td rowspan="9"><span class="resource-label">Shipments</span></td>
      <td><span class="tool-name">create_shipment</span></td>
      <td class="tool-desc">Create a shipment and optionally buy a label in one call</td>
    </tr>
    <tr><td><span class="tool-name">create_label</span></td><td class="tool-desc">Buy a shipping label for an existing shipment by shipment ID</td></tr>
    <tr><td><span class="tool-name">get_shipment</span></td><td class="tool-desc">Get full details including label, packing slip, and invoice URLs</td></tr>
    <tr><td><span class="tool-name">list_shipments</span></td><td class="tool-desc">List and filter shipments by state, date, country, and more</td></tr>
    <tr><td><span class="tool-name">update_shipment</span></td><td class="tool-desc">Update address, parcel, courier, or shipping settings</td></tr>
    <tr><td><span class="tool-name">delete_shipment</span></td><td class="tool-desc">Delete a shipment that hasn't shipped yet</td></tr>
    <tr><td><span class="tool-name">cancel_shipment</span></td><td class="tool-desc">Cancel a shipped shipment (pre-transit only)</td></tr>
    <tr><td><span class="tool-name">track_shipment</span></td><td class="tool-desc">Track by shipment ID or order number with checkpoint history</td></tr>
    <tr><td><span class="tool-name">get_shipment_documents</span></td><td class="tool-desc">Retrieve commercial invoice metadata</td></tr>
    <tr><td colspan="3" style="padding:0;border:none;height:4px"></td></tr>
    <tr>
      <td rowspan="6"><span class="resource-label">Pickups</span></td>
      <td><span class="tool-name">get_pickup_slots</span></td>
      <td class="tool-desc">Get available pickup time slots for a courier</td>
    </tr>
    <tr><td><span class="tool-name">create_pickup</span></td><td class="tool-desc">Schedule a pickup for one or more shipments</td></tr>
    <tr><td><span class="tool-name">list_pickups</span></td><td class="tool-desc">List pickups with filters (courier, date, state)</td></tr>
    <tr><td><span class="tool-name">get_pickup</span></td><td class="tool-desc">Get details of a specific pickup</td></tr>
    <tr><td><span class="tool-name">cancel_pickup</span></td><td class="tool-desc">Cancel a scheduled pickup</td></tr>
    <tr><td><span class="tool-name">list_pickup_shipments</span></td><td class="tool-desc">List all shipments in a pickup</td></tr>
    <tr><td colspan="3" style="padding:0;border:none;height:4px"></td></tr>
    <tr>
      <td><span class="resource-label">Address</span></td>
      <td><span class="tool-name">validate_address</span></td>
      <td class="tool-desc">Validate US domestic and international addresses</td>
    </tr>
    <tr><td colspan="3" style="padding:0;border:none;height:4px"></td></tr>
    <tr>
      <td rowspan="2"><span class="resource-label">Billing</span></td>
      <td><span class="tool-name">list_transactions</span></td>
      <td class="tool-desc">List transactions by type, date range, or shipment</td>
    </tr>
    <tr><td><span class="tool-name">list_billing_transactions</span></td><td class="tool-desc">List transactions for a billing document</td></tr>
    <tr><td colspan="3" style="padding:0;border:none;height:4px"></td></tr>
    <tr>
      <td rowspan="6"><span class="resource-label">Analytics</span></td>
      <td><span class="tool-name">analytics_shipments</span></td>
      <td class="tool-desc">Shipment volume overview with daily trends</td>
    </tr>
    <tr><td><span class="tool-name">analytics_shipped</span></td><td class="tool-desc">Shipped (label-generated) shipment data for a date range</td></tr>
    <tr><td><span class="tool-name">analytics_shipment_status</span></td><td class="tool-desc">Status distribution — in-transit, delivered, exception, etc.</td></tr>
    <tr><td><span class="tool-name">analytics_top_destinations</span></td><td class="tool-desc">Top destinations ranked by volume</td></tr>
    <tr><td><span class="tool-name">analytics_top_couriers</span></td><td class="tool-desc">Top couriers ranked by shipment count</td></tr>
    <tr><td><span class="tool-name">analytics_sale_channels</span></td><td class="tool-desc">Volume by sales channel (Shopify, WooCommerce, API, etc.)</td></tr>
  </tbody>
</table>

</section>

<section id="prompts">
<h2>Sample prompts</h2>
<p>Once connected, interact with Easyship using natural language. Here are examples for each tool category:</p>

<div class="prompt-grid">
  <div class="prompt-card">
    <div class="label">Compare rates <span class="tool-tag">get_rates</span></div>
    <div class="prompt-text">"I want to ship a 2 kg parcel (30×20×15 cm) from New York, US 10001 to Toronto, Canada M5B 2H1. Category is books_collectibles, declared value $8 USD. Show cheapest and fastest options."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Validate address <span class="tool-tag">validate_address</span></div>
    <div class="prompt-text">"Is this address valid for shipping: 1600 Amphitheatre Parkway, Mountain View, CA 94043, US? Show any suggested corrections."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Create draft shipment <span class="tool-tag">create_shipment</span></div>
    <div class="prompt-text">"Create a draft shipment (don't buy a label yet). From: Acme LLC, Jane Sender, jane@acme.com, +1 212-555-0147, 350 5th Ave, New York, NY 10001, US. To: John Doe, john@example.com, +1 416-555-0199, 220 Yonge St, Toronto, ON M5B 2H1, CA. Package: 0.12 kg, 22×15×3 cm. Item: paperback book, 1 unit, $8 USD, category books_collectibles. DDU."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Buy a label <span class="tool-tag">create_shipment</span></div>
    <div class="prompt-text">"Ship a 2 kg parcel from SF to NYC with the cheapest courier. Buy the label and give me the download link."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Label an existing shipment <span class="tool-tag">create_label</span></div>
    <div class="prompt-text">"Buy a label for shipment ESSG10006001 and give me the download link."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Track a shipment <span class="tool-tag">track_shipment</span></div>
    <div class="prompt-text">"Track shipment ESSG10006001 — what's the latest status, ETA, and last three tracking events?"</div>
  </div>
  <div class="prompt-card">
    <div class="label">Get shipment details <span class="tool-tag">get_shipment</span></div>
    <div class="prompt-text">"Pull up shipment ESSG10006001. I need the full details with document links as URLs — 4×6 label and packing slip, A4 commercial invoice."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Schedule a pickup <span class="tool-tag">get_pickup_slots → create_pickup</span></div>
    <div class="prompt-text">"Schedule a pickup for shipments ESSG10006001 and ESSG10006002. Get the courier ID from the first shipment, find available slots, and book the earliest one."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Analytics <span class="tool-tag">analytics_top_couriers</span></div>
    <div class="prompt-text">"For the last 3 months, which couriers did I use the most? Rank them with counts and share of volume."</div>
  </div>
  <div class="prompt-card">
    <div class="label">Transaction history <span class="tool-tag">list_transactions</span></div>
    <div class="prompt-text">"Pull my transactions from March 2026, type shipment, 50 per page. Give me a summary of charges."</div>
  </div>
</div>
</section>

<section id="scopes">
<h2>Authorization scopes</h2>
<p>Each tool requires specific API token scopes. When creating your token, enable the scopes needed for the tools you plan to use. See <a href="https://developers.easyship.com/reference/scopes" target="_blank" rel="noopener noreferrer">API Scopes</a> for full details.</p>

<table>
  <thead><tr><th>Scope</th><th>Used by</th></tr></thead>
  <tbody>
    <tr><td><span class="scope-badge">public.shipment:read</span></td><td class="tool-desc">list_shipments, get_shipment, track_shipment, list_pickup_shipments</td></tr>
    <tr><td><span class="scope-badge">public.shipment:write</span></td><td class="tool-desc">create_shipment, update_shipment, delete_shipment, cancel_shipment</td></tr>
    <tr><td><span class="scope-badge">public.label:write</span></td><td class="tool-desc">create_shipment (when buying a label), create_label</td></tr>
    <tr><td><span class="scope-badge">public.pickup:read</span></td><td class="tool-desc">get_pickup_slots, list_pickups</td></tr>
    <tr><td><span class="scope-badge">public.pickup:write</span></td><td class="tool-desc">create_pickup, get_pickup, cancel_pickup</td></tr>
    <tr><td><span class="scope-badge">public.shipment_document:read</span></td><td class="tool-desc">get_shipment_documents</td></tr>
    <tr><td><span class="scope-badge">public.transaction_record:read</span></td><td class="tool-desc">list_transactions, list_billing_transactions</td></tr>
    <tr><td><span class="scope-badge">public.analytics:read</span></td><td class="tool-desc">All analytics_* tools</td></tr>
    <tr><td><span class="scope-badge">public.address_validation:write</span></td><td class="tool-desc">validate_address (international)</td></tr>
    <tr><td><span class="scope-badge">public.address_validation_domestic:write</span></td><td class="tool-desc">validate_address (US)</td></tr>
  </tbody>
</table>

</section>

<section id="troubleshooting">
<h2>Troubleshooting</h2>

<h3>Server Visibility Issues</h3>
<p>Save the config file and fully restart the client app. For Claude Desktop, quit and reopen — closing the window isn't enough.</p>

<h3>Resolving Authentication Errors</h3>
<p>Re-check your token at <a href="https://app.easyship.com/connect/api" target="_blank" rel="noopener noreferrer">Dashboard → Connect → API</a>. Ensure there are no extra spaces or line breaks. Verify the token has the required <a href="#scopes">scopes</a> for the tools you're using.</p>

<h3>Incomplete Tool Loading</h3>
<p>Verify your API token is valid and active. Restart your MCP client/session. If the issue persists, check your network connection and ensure you're connecting to <code>https://mcp.easyship.com/mcp</code>.</p>

<h3>Missing Dependencies — <code>uvx</code> not found? (local mode only)</h3>
<p>Install <a href="https://docs.astral.sh/uv/" target="_blank" rel="noopener noreferrer">uv</a> first:</p>
<pre><code><span class="comment"># macOS / Linux</span>
curl -LsSf https://astral.sh/uv/install.sh | sh

<span class="comment"># Windows</span>

powershell -ExecutionPolicy ByPass -c "irm <https://astral.sh/uv/install.ps1> | iex"</code></pre>

<h3>Remote mode not connecting?</h3>
<p>Verify your client supports <a href="https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http" target="_blank" rel="noopener noreferrer">Streamable HTTP</a> transport. If not, use the local (uvx) method.</p>

<h3>Need Further Assistance?</h3>
<p>If you're experiencing an error that isn't covered above, <a href="https://form.typeform.com/to/MEjsiWKS#tool=xxxxx&error_code=xxxxx&request_id=xxxxx&easyship_company_id=xxxxx" target="_blank" rel="noopener noreferrer">submit a bug report</a>. Include the tool name, error code, and request ID from the error response — these help us diagnose the issue faster.</p>

<div class="callout" style="margin-top:28px">
  <strong>Security:</strong> Never commit API tokens to version control. Use environment variables or a secrets manager. Rotate tokens periodically from the <a href="https://app.easyship.com/connect/api" target="_blank" rel="noopener noreferrer">dashboard</a>.
</div>
</section>

<section id="faq">
<h2>FAQ</h2>

<div class="faq-item">
  <div class="faq-q">Do I need coding experience to use the Easyship MCP Server?</div>
  <div class="faq-a">Basic technical familiarity helps, but deep coding experience isn't required. If you can install tools, manage API keys, and follow setup instructions, you can use the MCP server.</div>
</div>

<div class="faq-item">
  <div class="faq-q">Is there a native Easyship plugin for ChatGPT?</div>
  <div class="faq-a">Not yet. ChatGPT Apps require OAuth support on the MCP server, which is on our roadmap. In the meantime, developers can use the Easyship MCP server via <a href="https://platform.openai.com/docs/guides/tools-connectors-mcp" target="_blank" rel="noopener noreferrer">OpenAI's Responses API</a> by passing the Easyship API token as a Bearer token — no OAuth needed for API access.</div>
</div>

<div class="faq-item">
  <div class="faq-q">Can I create a shipment without immediately buying a label?</div>
  <div class="faq-a">Yes. Omit <code>buy_label</code> or set it to <code>false</code> in the shipment data. The shipment is created in draft state and you can buy the label later with <code>create_label</code> when ready.</div>
</div>

<div class="faq-item">
  <div class="faq-q">How do I schedule or cancel a courier pickup?</div>
  <div class="faq-a">To schedule: use <code>get_shipment</code> to get the courier service ID, then <code>get_pickup_slots</code> to see available times, then <code>create_pickup</code> with your chosen slot. All shipments in a pickup must use the same courier. To cancel: use <code>cancel_pickup</code> with the pickup ID.</div>
</div>

<div class="faq-item">
  <div class="faq-q">Can I use the same API token across multiple MCP clients?</div>
  <div class="faq-a">Yes. Be mindful of rate limits and avoid conflicting operations (e.g., modifying the same shipment from two clients simultaneously).</div>
</div>

<div class="faq-item">
  <div class="faq-q">What should I do if not all tools load after connecting?</div>
  <div class="faq-a">Verify your API token is valid and has all required scopes. Restart your MCP client. Check your network connection. If using the local method, ensure you have the latest version: <code>pip install --upgrade easyship-mcp</code>.</div>
</div>

</section>

<section id="feedback">
<h2>Feedback</h2>
<div class="feedback-box">
  <p>We'd love to hear how you're using the Easyship MCP Server. If you've built a workflow, automated a shipping process, or found a great use case, we want to know about it.</p>
  <p style="margin-bottom:20px">Your feedback directly shapes what we build next: new tools, new platform integrations, and better prompts.</p>
  <a href="https://form.typeform.com/to/Ep0lvsW3" target="_blank" rel="noopener noreferrer" class="feedback-cta">Share your feedback →</a>
</div>
</section>

<p style="margin-top:40px;font-size:13px;color:#6B7280">
  API version: <strong>v2024-09</strong> ·
  Package: <a href="https://pypi.org/project/easyship-mcp/" target="_blank" rel="noopener noreferrer">easyship-mcp</a> on PyPI ·
  <a href="https://registry.modelcontextprotocol.io/?q=easyship" target="_blank" rel="noopener noreferrer">MCP Registry</a> ·
  <a href="https://github.com/easyship/easyship-mcp-plugin" target="_blank" rel="noopener noreferrer">Plugin on GitHub</a>
</p>

</div>

<br />