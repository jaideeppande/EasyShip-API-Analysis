---
type: webhook-event
---
# shipment.warehouse.stateupdated

Webhook event · [[Webhooks]] · [[Shipments]]

When your shipment's warehouse state has been updated, you'll get the event payload as below:

```json
{
  "event_type": "shipment.warehouse.state.updated",
  "resource_type": "shipment",
  "resource_id": "ESTEST00000",
  "data": {
    "easyship_shipment_id": "ESTEST00000",
    "platform_order_number": "#100001",
    "warehouse_state": "none"
  }
}
```
