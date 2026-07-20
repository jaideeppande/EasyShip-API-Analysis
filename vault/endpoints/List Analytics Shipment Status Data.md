---
method: GET
endpoint: "/2024-09/analytics/shipment_status"
api: Public API
slug: analytics_shipment_status_index
scopes:
  - "public.analytics:read"
---
# List Analytics Shipment Status Data

**`GET /2024-09/analytics/shipment_status`** · [[Analytics]] · [[Easyship Public API]]

Retrieve shipment status. Possible statuses:
- Label Pending
- Label Rejected
- Label Ready
- Pickup/Drop-off in Progress
- In Transit to Customer
- Failed Delivery Attempt
- Exception

## Source

- [Official docs](https://developers.easyship.com/reference/analytics_shipment_status_index)
- Local mirror: `docs/reference/analytics_shipment_status_index.md`
