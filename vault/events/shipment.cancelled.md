---
type: webhook-event
---
# shipment.cancelled

Webhook event · [[Webhooks]] · [[Shipments]]

When your shipment is cancelled, you'll get the event payload as below:

```json
{
  "event_type": "shipment.cancelled",
  "resource_type": "shipment",
  "resource_id": "ESTEST00000",
  "data": {
    "easyship_shipment_id": "ESTEST00000",
    "platform_order_number": "#100001",
    "status": "cancelled"
  }
}
```
