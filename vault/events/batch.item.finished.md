---
type: webhook-event
---
# batch.item.finished

Webhook event · [[Webhooks]]

When a batch item has completed processing, you'll get the event payload as below:

```json
{
  "event_type": "batch.item.finished",
  "resource_type": "shipment_batch_item",
  "resource_id": "7c16f6aa-2183-45eb-a18d-cdaf09500001",
  "data": {
    "batch_id": "3ed3d05f-7ba8-404d-97b1-5a50de3c00001",
    "started_at": "2023-01-25T11:30:00.000Z",
    "finished_at": "2023-01-25T11:31:00.000Z",
    "record_type": "Shipment",
    "record_id": "329c2604-33ff-49b3-9a08-b7c8754a00001",
    "reference_id": "reference_id",
    "state": "failed",
    "processing_errors": ["error"]
  }
}
```
