# EasyShip API Analysis

Analysis and integration testing workspace for the [Easyship API](https://developers.easyship.com/) (v2024-09).

## Layout

- `docs/INDEX.md` — full index of the downloaded documentation (mirrors the official site)
- `docs/guides/` — integration guides (sandbox, rates at checkout, tracking, returns, OAuth, etc.)
- `docs/reference/` — all 202 API reference pages; each embeds its full OpenAPI 3.0.3 definition (paths, schemas, examples)
- `docs/recipes/` — step-by-step recipes
- `.env` — API credentials and base URLs (gitignored, never commit)

## API basics

- Production base URL: `https://public-api.easyship.com`
- Sandbox base URL: `https://public-api-sandbox.easyship.com`
- Auth: `Authorization: Bearer <token>` (tokens in `.env`)
- Versioned paths, e.g. `GET /2024-09/account`

Both tokens verified working against `GET /2024-09/account`.
