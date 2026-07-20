---
api: Public API
type: resource
---
# Shipments

Part of [[Easyship Public API]].

## Endpoints (14)

- `GET` [[List All Shipments of Specific Pickup]] — `/2024-09/pickups/{pickup_id}/shipments`
- `GET` [[List all Shipments]] — `/2024-09/shipments`
- `POST` [[Create a Shipment]] — `/2024-09/shipments`
- `GET` [[List all Trackings]] — `/2024-09/shipments/trackings`
- `DELETE` [[Delete a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}`
- `GET` [[Get a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}`
- `PATCH` [[Update a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}`
- `POST` [[Cancel a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}/cancel`
- `GET` [[List All Documents]] — `/2024-09/shipments/{easyship_shipment_id}/documents`
- `POST` [[Buy Insurance for a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}/insure`
- `POST` [[Create a Return Shipment]] — `/2024-09/shipments/{easyship_shipment_id}/return`
- `GET` [[List Transaction Records for a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}/transaction_records`
- `GET` [[List Unavailable Couriers for a Shipment]] — `/2024-09/shipments/{easyship_shipment_id}/unavailable_couriers`
- `POST` [[Create Label]] — `/2024-09/shipments/{shipment_id}/label`

## References

- [[Addresses]]
- [[Courier Services]]
- [[Couriers]]
- [[HS codes]]
- [[Pickups]]
- [[Products]]
- [[Trackings]]

## Referenced by

- [[Batches]]
- [[Billing Documents]]
- [[Insurance]]
- [[Manifests]]
- [[Pickups]]
- [[Rates]]
- [[Trackings]]
- [[Transaction Records]]
- [[eFulfillment]]
