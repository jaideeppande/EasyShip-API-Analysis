# How to Track a Shipment

You can seamlessly create shipment trackings and update shipment statuses through the API or webhooks with Easyship. Follow the high-level schedule outlined below to streamline your tracking workflow.

To track shipments created outside of Easyship, please contact our support team to discuss your needs.

## 1. List couriers supporting tracking

Before creating tracking for a shipment, ensure that the Easyship tracking feature supports the courier for your shipment. Execute the following request:

`GET https://api.easyship.com/2024-09/trackings/supported_couriers`

This request can be filtered by two parameters:

1. `umbrella_name`: courier company umbrella name, e.g., `DHL`.
2. `origin_country_alpha2`: comma-separated country codes in the Alpha-2 format.

In the response, you obtain the `couriers` object containing the couriers available for tracking.

Response example:

```
{
    "couriers": [
        {
            "id": "137a79e8-ae1c-4369-9855-44cf8ff784c4",
            "origin_country_alpha2": "US",
            "umbrella_name": "USPS"
        }
    ]
}
```

## 2. Create a new tracking

Proceed to create tracking for a desired shipment using the following request:

`POST https://api.easyship.com/2024-09/trackings`

The request body contains the following fields:

1. `tracking_number`: unique tracking identifier generated on your side.
2. `courier_id`: ID of the shipment courier.
3. `platform_order_number`: order number from the e-commerce platform.
4. `origin_address_id`: origin address of the shipment. Leave blank if the origin address is not added via the Addresses API and fill the `origin_address` object instead.
5. `origin_address`: origin address object corresponding with the `address` object of the Addresses API.
6. `destination_address`: shipment destination address object.
7. `items`: shipment items, each with `description` and `quantity`.

Request Example:

```
{
  "destination_address": {
    "line_1": "123 Test Street",
    "line_2": "Block 3",
    "state": "Singapore",
    "city": "Singapore",
    "postal_code": "247964",
    "country_alpha2": "SG",
    "company_name": "Test Plc.",
    "contact_name": "Foo Bar",
    "contact_phone": "+65 6910 1185",
    "contact_email": "asd@asd.com"
  },
  "items": [
    {
      "description": "iPhone",
      "quantity": 1
    }
  ],
  "tracking_number": "0114827",
  "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0002",
  "platform_order_number": "28659826843658326431264",
  "origin_address_id": "5636-13as-8264-8fe0-9s63"
}
```

In the response, receive the `tracking` object including details such as `ID`, courier `tracking_number`, `source`, `platform_order_number`, origin and destination country codes, tracking status, and more.

Possible `tracking_status` values:

* `pending`
* `created`
* `active`
* `completed`
* `overwritten_by_admin`

## 3. Show existing trackings

To display all trackings created with your shipments, execute the following request:

`GET https://api.easyship.com/2024-09/trackings`

This request can be filtered by parameters such as `origin_country_alpha2`, `destination_country_alpha2`, `source`, and `tracking_state` based on the `tracking_status` field above.

For a specific tracking, add its `tracking_id` to the request:

`GET https://api.easyship.com/2023-01/trackings/{tracking_id}`

## 4. Webhook messages with tracking updates

Easyship API webhooks support the following messages for tracking:

* `shipment.tracking.status.changed`
* `shipment.racking.checkpoints.created`

Refer to this quickstart guide to learn more about setting up webhooks on your end for real-time tracking updates.