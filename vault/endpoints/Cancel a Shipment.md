---
method: POST
endpoint: "/2024-09/shipments/{easyship_shipment_id}/cancel"
api: Public API
slug: shipments_cancel
scopes:
  - "public.shipment:write"
---
# Cancel a Shipment

**`POST /2024-09/shipments/{easyship_shipment_id}/cancel`** · [[Shipments]] · [[Easyship Public API]]

Cancel a shipment after a label has been requested, as long as the shipment is not yet in transit.

## Source

- [Official docs](https://developers.easyship.com/reference/shipments_cancel)
- Local mirror: `docs/reference/shipments_cancel.md`
