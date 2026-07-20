---
type: webhook-event
---
# external.shipment.insured

Webhook event · [[Webhooks]] · [[Shipments]]

When your external shipment is eligible for insurance and successfully tracked by Easyship tracking service, you'll get the event payload as below:

```json
{
  "resource_type": "shipment",
  "resource_id": "ESTEST00000",
  "shipment": {
    "easyship_insurance_id": "IPTEST000000",
    "easyship_shipment_id": "ESTEST00000",
    "insurance_fee": 1.5,
    "total_insured_value": 11.0,
    "tracking_number": "TEST_TRACKING_NUMBER"
  }
}
```
