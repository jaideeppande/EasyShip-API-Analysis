---
type: webhook-event
---
# batch.finished

Webhook event · [[Webhooks]] · [[Batches]]

When a batch has completed processing, you'll get the event payload as below:

```json
{
  "event_type": "batch.finished",
  "resource_type": "shipment_batch",
  "resource_id": "3ed3d05f-7ba8-404d-97b1-5a50de300001",
  "data": {
    "started_at": "2023-01-25T11:30:00.000Z",
    "finished_at": "2023-01-25T11:31:00.000Z",
    "state": "processed",
    "items": 2,
    "failed_items": 2
  }
}
```
