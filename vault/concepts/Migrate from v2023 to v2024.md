---
type: concept
---
# Migrate from v2023 to v2024

We have introduced several essential updates in Public API `2024-09`, including:

* Transitioning label creation to a batch process
* Redirects API
* Implementing new scopes that give you flexibility to manage access to each APIs
* Bug fixes
* We encourage you to upgrade to the latest version to take full advantage of these enhancements and improve your integration experience.

To use the new Public API `2024-09`, you must set up a new API Integration (see [[Scopes]]).

## Labels

Label creation has been updated from `2023-01` to the `2024-09` Batch Labels API. If you’re using `2023-01`, no changes are required.

### 2023-01

For label creation in `2023-01`, the request body looks like this:

```Text json
{
  "shipments": [
    {
      "easyship_shipment_id": "ESSG10006001",
      "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001"
    }
  ]
}
```

The request is sent via:`POST /2023-01/labels`

### 2024-09

In `2024-09`, the request body should look like this:

```Text json
{
  "shipments": [
    {
      "easyship_shipment_id": "ESSG10006001",
      "courier_service_id": "01563646-58c1-4607-8fe0-cae3e33c0001"
    }
  ]
}
```

The request is now sent via: `POST /2024-09/batches/labels`

Refer to the [[Create a Batch of Labels]] documentation for complete usage details.

<br />

## Courier Accounts and Couriers Migration

<br />

### Courier Accounts

We are changing **courier accounts** to **couriers** starting in `2024-09`. The changes involve parameters that we send through the request body, response body, and path name.

#### Key Changes

* **List all couriers in courier accounts:**
  * `2023-01`: [List couriers in courier accounts](https://developers.easyship.com/v2023.01/reference/courier_accounts_couriers_index "https://developers.easyship.com/v2023.01/reference/courier_accounts_couriers_index")
  * `2024-09`: [List couriers](https://developers.easyship.com/reference/courier_courier_services_index "https://developers.easyship.com/reference/courier_courier_services_index")

* **Deactivate a courier account:**
  * `2023-01`: [Deactivate a courier account](https://developers.easyship.com/v2023.01/reference/courier_accounts_deactivate "https://developers.easyship.com/v2023.01/reference/courier_accounts_deactivate")
  * `2024-09`: [Deactivate a courier](https://developers.easyship.com/reference/couriers_deactivate "https://developers.easyship.com/reference/couriers_deactivate")

* **List all courier accounts:**
  * `2023-01`: [List courier accounts](https://developers.easyship.com/v2023.01/reference/courier_accounts_index "https://developers.easyship.com/v2023.01/reference/courier_accounts_index")
  * `2024-09`: [List couriers](https://developers.easyship.com/reference/couriers_index "https://developers.easyship.com/reference/couriers_index")

* **Create a courier account:**
  * `2023-01`: [Create a courier account](https://developers.easyship.com/v2023.01/reference/courier_accounts_create "https://developers.easyship.com/v2023.01/reference/courier_accounts_create")
  * `2024-09`: [Create a courier](https://developers.easyship.com/reference/couriers_create "https://developers.easyship.com/reference/couriers_create")

* **Update a courier account:**
  * `2023-01`: [Update a courier account](https://developers.easyship.com/v2023.01/reference/courier_accounts_update "https://developers.easyship.com/v2023.01/reference/courier_accounts_update")
  * `2024-09`: [Update a courier](https://developers.easyship.com/reference/couriers_update "https://developers.easyship.com/reference/couriers_update")

* **Get a courier account:**
  * `2023-01`: [Get a courier account](https://developers.easyship.com/v2023.01/reference/courier_accounts_show "https://developers.easyship.com/v2023.01/reference/courier_accounts_show")
  * `2024-09`: [Get a courier](https://developers.easyship.com/reference/couriers_show "https://developers.easyship.com/reference/couriers_show")

* **Bulk update couriers in an account:**
  * `2023-01`: [Bulk update couriers](https://developers.easyship.com/v2023.01/reference/courier_accounts_couriers_bulk_update "https://developers.easyship.com/v2023.01/reference/courier_accounts_couriers_bulk_update")
  * `2024-09`: Deprecated

#### Path name and parameter changes

You may recognize that on `2023-01`, we used the parameters `courier_account_id` on the courier accounts endpoints. In `2024-09`, we renamed it to `courier_id`.

Let's take “**Get a Courier Account”** as an example. Here is the path that we are using for `2023-01`.

```
GET https://api.easyship.com/2023-01/courier_accounts/{courier_account_id}
```

We can see that we are using the `courier_account` path with the `courier_account_id` as the path param on the URL

In `2024-09`, we change it to:

```
GET https://api.easyship.com/2024-09/couriers/{courier_id}
```

The new version changes the path and parameters to `courier` and `courier_id`.

#### Webhook Changes

When using version `2024-09`, clients must update the `courier_account_state_changed` event type to `courier_state_changed`. That applies when creating and updating a webhook. These are the examples:

##### Creating or updating a webhook

* **v2023-01**

Here is the example creating `courier_account_state_changed` event in the version `2023-01`.

```json
// POST https://api.easyship.com/2023-01/webhooks

{
  "event_types": [
    "courier_account_state_changed"
  ],
  "version": "2023-01"
}
```

* **v2024-09**

In the version `2024-09`, `courier_account_state_changed` changes to `courier_state_changed`.

```json
// POST https://api.easyship.com/2024-09/webhooks

{
  "event_types": [
    "courier_state_changed"
  ],
  "version": "2024-09"
}
```

<br />

<br />

### Couriers

We are changing **couriers** to **courier services** starting in 2024-09. The changes involve parameters that we send through the request and response bodies and path names.

#### Key Changes

* **List estimated delivery dates for a courier:**
  * `2023-01`: [List estimated delivery dates](https://developers.easyship.com/v2023.01/reference/courier_estimated_delivery_dates_index "https://developers.easyship.com/v2023.01/reference/courier_estimated_delivery_dates_index")
  * `2024-09`: [List estimated delivery dates for a courier service](https://developers.easyship.com/reference/courier_service_estimated_delivery_dates_index "https://developers.easyship.com/reference/courier_service_estimated_delivery_dates_index")

* **List available pickup slots:**
  * `2023-01`: [List pickup slots](https://developers.easyship.com/v2023.01/reference/couriers_pickup_slots_index "https://developers.easyship.com/v2023.01/reference/couriers_pickup_slots_index")
  * `2024-09`: [List pickup slots for a courier service](https://developers.easyship.com/reference/courier_services_pickup_slots_index "https://developers.easyship.com/reference/courier_services_pickup_slots_index")

* **List all couriers:**
  * `2023-01`: [List couriers](https://developers.easyship.com/v2023.01/reference/couriers_index "https://developers.easyship.com/v2023.01/reference/couriers_index")
  * `2024-09`: [List courier services](https://developers.easyship.com/reference/courier_services_index "https://developers.easyship.com/reference/courier_services_index")

#### Path name and parameters change

In the new version, we are changing the path from `couriers` to `courier_services`. Here is an example of **Listing estimated delivery dates for a courier**.

What we have on `2023-01`. We are still using `couriers` and `courier_id` as the path parameters.

```
https://api.easyship.com/2023-01/couriers/{courier_id}/estimated_delivery_dates
```

In `2024-09`, we change it to this.

```
https://public-api.easyship.com/2024-09/courier_services/{courier_service_id}/estimated_delivery_dates
```

We change `couriers` to `courier_services` and path params to `courier_service_id`.

<br />

### Shipments

#### Creating a Shipment

On the shipment creation, we also updated the params for `courier_selection` on the `2024-09`. On the `2023-01`, we have this as request body params.

```json
{
  "incoterms": "DDU",
  "insurance": {
    "is_insured": false
  },
  "courier_selection": {
    "selected_courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
    "allow_courier_fallback": false,
    "apply_shipping_rules": true
  },
  "shipping_settings": {
    "additional_services": {
      "qr_code": "none"
    },
    "units": {
      "weight": "kg",
      "dimensions": "cm"
    },
    "buy_label": false,
    "buy_label_synchronous": false,
    "printing_options": {
      "format": "png",
      "label": "4x6",
      "commercial_invoice": "A4",
      "packing_slip": "4x6"
    }
  }
}
```

You can see that we are using `selected_courier_id` under `courier_selection` to select courier service on the `2023-01`. But, on the new version, we rename the `courier_selection` to `courier_settings`. Please see the example of request body below for the `2024-09`.

```json
{
  "incoterms": "DDU",
  "insurance": {
    "is_insured": false
  },
  "courier_settings": {
    "courier_service_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
    "allow_fallback": false,
    "apply_shipping_rules": true
  },
  "shipping_settings": {
    "additional_services": {
      "qr_code": "none"
    },
    "units": {
      "weight": "kg",
      "dimensions": "cm"
    },
    "buy_label": false,
    "buy_label_synchronous": false,
    "printing_options": {
      "format": "png",
      "label": "4x6",
      "commercial_invoice": "A4",
      "packing_slip": "4x6"
    }
  }
}
```

We rename the `selected_courier_id` to `courier_service_id` under the `courier_settings`.

Please visit this [page](https://developers.easyship.com/v2023.01/reference/shipments_create "https://developers.easyship.com/v2023.01/reference/shipments_create") to create a shipment for `2023-01` or this [page](https://developers.easyship.com/reference/shipments_create "https://developers.easyship.com/reference/shipments_create") for `2024-09`.

<br />

### Requesting Rates

When requesting rates on the `2023-01`, we use `courier_selection` on the request body.

```json
{
  "destination_address": {
    "country_alpha2": "AD"
  },
  "incoterms": "DDU",
  "insurance": {
    "is_insured": false
  },
  "courier_selection": {
    "show_courier_logo_url": false,
    "apply_shipping_rules": true
  },
  "shipping_settings": {
    "units": {
      "weight": "kg",
      "dimensions": "cm"
    }
  },
  "parcels": [
    {
      "items": [
        {
          "contains_battery_pi966": true,
          "contains_battery_pi967": true,
          "contains_liquids": true,
          "origin_country_alpha2": "AD",
          "quantity": 1,
          "declared_currency": "AED"
        }
      ]
    }
  ]
}
```

In `2024-09`, we renamed it to `courier_settings`. Here is an example of the request body on the new version:

```json
{
  "destination_address": {
    "country_alpha2": "AD"
  },
  "incoterms": "DDU",
  "insurance": {
    "is_insured": false
  },
  "courier_settings": {
    "show_courier_logo_url": false,
    "apply_shipping_rules": true
  },
  "shipping_settings": {
    "units": {
      "weight": "kg",
      "dimensions": "cm"
    }
  },
  "parcels": [
    {
      "items": [
        {
          "contains_battery_pi966": true,
          "contains_battery_pi967": true,
          "contains_liquids": true,
          "origin_country_alpha2": "AD",
          "quantity": 1,
          "declared_currency": "AED"
        }
      ]
    }
  ]
}
```
