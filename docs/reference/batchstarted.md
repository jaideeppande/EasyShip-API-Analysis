# batch.started

When a batch is created and scheduled for processing, you will get the event payload as below:

```json
{
  "event_type": "batch.started",
  "resource_type": "shipment_batch",
  "resource_id": "3ed3d05f-7ba8-404d-97b1-5a50de300001",
  "data": {
    "started_at": "2023-01-25T11:30:00.000Z",
    "items": 2
  }
}
```