# shipment.tracking.statuschanged

When your shipment's tracking status changed, you'll get the event payload as below:

```json
{
  "event_type": "shipment.tracking.status.changed",
  "resource_type": "shipment",
  "resource_id": "ESTEST00000",
  "data": {
    "easyship_shipment_id": "ESTEST00000",
    "platform_order_number": "#100001",
    "origin": "US",
    "destination": "CA",
    "company_order_number": "#100001",
    "status": "Delivered",
    "tracking_number": "12345",
    "tracking_page_url": "https://www.trackmyshipment.co/shipment-tracking/ESTEST00000"
  }
}
```

A shipment's tracking status can change to any of the following values:

* `Arrived at Consolidation Center`
* `Delivered`
* `Delivery Expected (End of Updates)`
* `Exception`
* `Failed Delivery Attempt`
* `In Transit to Consolidation Center`
* `In Transit to Customer`
* `Liquidated`
* `Lost by Courier`
* `No Recent Tracking Updates`
* `Out for Delivery`
* `Processing at Consolidation Center`
* `Shipped (No Tracking Provided)`
* `Shipped`
* `To be returned`
* `Uncancelled`