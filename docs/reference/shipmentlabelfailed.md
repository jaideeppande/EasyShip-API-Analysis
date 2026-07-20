# shipment.label.failed

When a label fails to be generated, you'll get the event payload as below:

```json
{
  "event_type": "shipment.label.failed",
  "resource_type": "shipment",
  "resource_id": "ESTEST00000",
  "data": {
    "easyship_shipment_id": "ESTEST00000",
    "platform_order_number": "#100001",
    "status": "failed"
  }
}
```