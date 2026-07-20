---
type: webhook-event
---
# shipment.tracking.checkpointscreated

Webhook event · [[Webhooks]]

When your shipment's checkpoints increased, you'll get the event payload as below:

```json
{
  "event_type": "shipment.tracking.checkpoints.created",
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
    "tracking_page_url": "https://www.trackmyshipment.co/shipment-tracking/ESTEST00000",
    "checkpoints": [
      {
        "order_number": 102,
        "handler": "Usps",
        "message": "Arrived at Regional Facility",
        "location": "CITY, STATE, 12345, USA",
        "city": "CITY",
        "country_name": "United States", 
        "country_iso3": "USA",
        "state": "STATE",
        "postal_code": "12345",
        "checkpoint_time": "2025-01-01T12:00:00.000Z",
        "primary_status": "In Transit to Customer"
      },
      {
        "order_number": 109,
        "handler": "Usps",
        "message": "Arrived at Post Office",
        "location": "CITY, STATE, 12345, USA",
        "city": "CITY",
        "country_name": "United States", 
        "country_iso3": "USA",
        "state": "STATE",
        "postal_code": "12345",
        "checkpoint_time": "2025-01-02T10:00:00.000Z",
        "primary_status": "In Transit to Customer"
      },
      {
        "order_number": 112,
        "handler": "Usps",
        "message": "Delivered, In/At Mailbox",
        "location": "CITY, STATE, 12345, USA",
        "city": "CITY",
        "country_name": "United States", 
        "country_iso3": "USA",
        "state": "STATE",
        "postal_code": "12345",
        "checkpoint_time": "2025-01-03T08:00:00.000Z",
        "primary_status": "Delivered"
      }
    ]
  }
}
```

Here is the details of each fields.

| Field Name                           | Data Type | Description                                                                                                                                       |
| ------------------------------------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `event_type`                         | String    | The type of event that triggered this webhook notification. In this case, it indicates new tracking checkpoints have been created for a shipment. |
| `resource_type`                      | String    | The type of resource that this event pertains to. Here, it's a `shipment`.                                                                        |
| `resource_id`                        | String    | The unique identifier of the specific shipment resource.                                                                                          |
| `data`                               | Object    | An object containing the details of the shipment and the newly created tracking checkpoints.                                                      |
| `data.easyship_shipment_id`          | String    | Easyship shipment ID.                                                                                                                             |
| `data.platform_order_number`         | String    | The order number associated with this shipment from the e-commerce platform.                                                                      |
| `data.origin`                        | String    | Country Code in Alpha-2 format (ISO 3166-1).                                                                                                      |
| `data.destination`                   | String    | Country Code in Alpha-2 format (ISO 3166-1).                                                                                                      |
| `data.company_order_number`          | String    | The order number assigned to this shipment by the company or seller.                                                                              |
| `data.status`                        | String    | The current overall status of the shipment (e.g., "Delivered").                                                                                   |
| `data.tracking_number`               | String    | The tracking number assigned to the shipment by the carrier.                                                                                      |
| `data.tracking_page_url`             | String    | A URL that leads to a tracking page where more detailed information about the shipment can be found.                                              |
| `data.checkpoints`                   | Array     | An array of checkpoint objects, each representing a specific event in the shipment's journey.                                                     |
| `data.checkpoints[].order_number`    | Integer   | A sequential number indicating the order of this checkpoint in the shipment's history.                                                            |
| `data.checkpoints[].handler`         | String    | The name of the shipping carrier or handler responsible for this checkpoint (e.g., "USPS").                                                       |
| `data.checkpoints[].message`         | String    | A brief message describing the event at this checkpoint (e.g., "Arrived at Regional Facility").                                                   |
| `data.checkpoints[].location`        | String    | A string containing the location details of this checkpoint, often including city, state, and postal code.                                        |
| `data.checkpoints[].city`            | String    | The city where this checkpoint occurred.                                                                                                          |
| `data.checkpoints[].country_name`    | String    | The full name of the country where this checkpoint occurred (e.g., "United States").                                                              |
| `data.checkpoints[].country_iso3`    | String    | The ISO 3166-1 alpha-3 code for the country (e.g., "USA").                                                                                        |
| `data.checkpoints[].state`           | String    | The state or province where this checkpoint occurred.                                                                                             |
| `data.checkpoints[].postal_code`     | String    | The postal or zip code of the location.                                                                                                           |
| `data.checkpoints[].checkpoint_time` | String    | The timestamp indicating when this checkpoint event occurred, in ISO 8601 format (UTC).                                                           |
| `data.checkpoints[].primary_status`  | String    | A high-level status category for this specific checkpoint (e.g., "In Transit to Customer", "Delivered").                                          |
