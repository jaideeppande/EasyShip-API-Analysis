---
api: Enterprise API
type: resource
---
# Shipping Rules

Part of [[Easyship Enterprise API]].

## Endpoints (16)

- `GET` [[List all Shipping Rules (shipping_rules_index)]] — `/2024-09/shipping_rules`
- `POST` [[Create a Shipping Rule (shipping_rules_create)]] — `/2024-09/shipping_rules`
- `GET` [[List all Platform Names (shipping_rule_platforms_index)]] — `/2024-09/shipping_rules/platforms`
- `POST` [[Activate a Shipping Rule (shipping_rule_activate)]] — `/2024-09/shipping_rules/{id}/activate`
- `POST` [[Deactivate a Shipping Rule (shipping_rule_deactivate)]] — `/2024-09/shipping_rules/{id}/deactivate`
- `DELETE` [[Delete a Shipping Rule (shipping_rules_delete)]] — `/2024-09/shipping_rules/{shipping_rule_id}`
- `GET` [[Get a Shipping Rule (shipping_rules_show)]] — `/2024-09/shipping_rules/{shipping_rule_id}`
- `PATCH` [[Update a Shipping Rule (shipping_rules_update)]] — `/2024-09/shipping_rules/{shipping_rule_id}`
- `GET` [[List all Shipping Rules]] — `/2024-11/organizations/{organization_id}/shipping_rules`
- `POST` [[Create a Shipping Rule]] — `/2024-11/organizations/{organization_id}/shipping_rules`
- `GET` [[List all Platform Names]] — `/2024-11/shipping_rules/platforms`
- `DELETE` [[Delete a Shipping Rule]] — `/2024-11/shipping_rules/{shipping_rule_id}`
- `GET` [[Get a Shipping Rule]] — `/2024-11/shipping_rules/{shipping_rule_id}`
- `PATCH` [[Update a Shipping Rule]] — `/2024-11/shipping_rules/{shipping_rule_id}`
- `POST` [[Activate a Shipping Rule]] — `/2024-11/shipping_rules/{shipping_rule_id}/activate`
- `POST` [[Deactivate a Shipping Rule]] — `/2024-11/shipping_rules/{shipping_rule_id}/deactivate`

## References

- [[Addresses]]
- [[Courier Services]]
- [[HS codes]]
- [[Organizations]]

## Referenced by

- [[Shipping Rule's Actions]]
- [[Shipping Rule's Conditions]]
