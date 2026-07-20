---
type: concept
---
# Migrate from v1 to v2024

This guide highlights changes required for migrating APIs from v1 (legacy version) to v2024-09 (latest version)

# Getting ready for version 2024-09

Fetch new **access\_token** and  setup **authorization scopes** for the new version.

## Fetch Your New Access Token

Follow the steps to setup an integration that allows you to access Public API(2024-09) via the generated **access\_token**

1. Click Connect on the sidebar from easyship dashboard.

   ![Connect](https://storage.googleapis.com/easyship-assets/support/store%20page/connect_section_on_sidebar.png)

2. Click API Integration on the bottom of the page.

3. When the popup is shown, select **"I'm developing a custom integration."** from the **Integration Type** dropdown options.

   ![Custom Integration](https://storage.googleapis.com/easyship-assets/support/store%20page/public_api_token_creation.png)

4. Select API version "2024-09 and newer".

5. Click "Connect" button.

6. The generated **Access Token** with the **Standard Scopes** are generated.

<Callout icon="🚧" theme="warn">
  Easyship Public APIs for 2024-09 and newer versions will only work with the access token created in this way.
</Callout>

![Access Token Generated](https://storage.googleapis.com/easyship-assets/support/store%20page/generated_access_token.png)

The scopes attached to the access\_token can be updated on this screen.
More details on <Anchor label="Scopes" target="_blank" href="https://developers.easyship.com/reference/scopes">Scopes</Anchor>

# Migration Details

**Domain** - <Anchor label="https://public-api.easyship.com/" target="_blank" href="https://public-api.easyship.com/"><https://public-api.easyship.com/></Anchor>

**Version** - 2024-09

## 📦 Pickup APIs

The newer version of the the Pickup APIs involve changes in request body, response structure. The details for the same can be found below

| Action | V1                                            | 2024-09                                                                |
| :----- | :-------------------------------------------- | :--------------------------------------------------------------------- |
| Read   | **GET** /pickup/v1/pickup\_slots/:courier\_id | **GET** /2024-09/courier\_services/:courier\_service\_id/pickup\_slots |
| Create | **POST** /pickup/v1/pickups                   | **POST** /2024-09/pickups                                              |

### Pickup Slots - List available pickup slots

Use this API to retrieve a list of pickup slots in local time for the coming seven days.

<Callout theme="default">
  Old Endpoint:  **GET** /pickup/v1/pickup_slots/:courier_id

New Endpoint: **GET** /2024-09/courier\_services/:courier\_service\_id/pickup\_slots </Callout>

**Request Comparison**

V1 Request Body

```
GET https://api.easyship.com/pickup/v1/pickup_slots/:courier_id/pickup_slots?origin_address_id=origin_address_id
```

2024-09 Request Body

```
GET https://public-api-staging.easyship.com/2024-09/courier_services/courier_service_id/pickup_slots?origin_address_id=origin_address_id
```

**Mapping from older version to new version**

| Field/Attribute   | V1                          | 2024-09                      |
| :---------------- | :-------------------------- | :--------------------------- |
| Courier ID        | `courier_id` (string)       | `courier_service_id`(string) |
| Origin Address ID | `origin_address_id`(string) | `origin_address_id`(string)  |

**Response Structure (2024-09)**

Checkout the updated response structure - <Anchor label="List Available Pickup Slots" target="_blank" href="https://developers.easyship.com/reference/courier_services_pickup_slots_index">List Available Pickup Slots</Anchor>

***

### Schedule/Create Pickup

Create or schedule a Pickup with the desired courier

> Only available if your courier provides pickup options.

<Callout theme="default">
  Old Endpoint:  **POST** /pickup/v1/pickups

New Endpoint: **POST** /2024-09/pickups </Callout>

**Request Comparison**

V1 Request Body

```json
{
    "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
    "preferred_date": "2022-02-23",
    "preferred_min_time": "2022-02-23T10:00",
    "preferred_max_time": "2022-02-23T13:00",
    "easyship_shipment_ids": [
        "ESSG10006001"
    ],
    "pickup": {
        "easyship_shipment_ids": [
            "ESSG10006001"
        ],
        "preferred_min_time": "2022-02-23T10:00",
        "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
        "preferred_max_time": "2022-02-23T13:00",
        "preferred_date": "2022-02-23"
    }
}
```

2024-09 Request Body

```json
{
  "courier_service_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
  "selected_date": "2022-02-23",
  "selected_from_time": "12:00",
  "selected_to_time": "16:00",
  "easyship_shipment_ids": [
    "ESSG10006001"
  ]
}

```

**Mapping from older version to new version**

| Field/Attribute      | V1                              | 2024-09                         | Notes                                                                           |
| :------------------- | :------------------------------ | :------------------------------ | :------------------------------------------------------------------------------ |
| Courier ID           | `courier_id` (string)           | `courier_service_id` (string)   | Use courier\_service\_id in place of courier\_id                                |
| Easyship Shipment ID | `easyship_shipment_ids` (array) | `easyship_shipment_ids` (array) | Unchanged                                                                       |
| Selected Date        | `selected_date` (string)        | `selected_date` (string)        | Unchanged                                                                       |
| Preferred Date       | `preferred_date` (string)       | `selected_date` (string)        | Use **selected\_date** in place of **preferred\_date**                          |
| Preferred Min Time   | `preferred_min_time` (string)   | Deprecated :x:                  | Use **selected\_from\_time** in place of **preferred\_min\_time**               |
| Preferred Max Time   | `preferred_max_time` (string)   | Deprecated :x:                  | Use **selected\_to\_time** in place of **preferred\_max\_time**                 |
| Selected From Time   | `selected_from_time` (string)   | `selected_from_time` (string)   | Unchanged                                                                       |
| Selected To Time     | `selected_to_time` (string)     | `selected_to_time` (string)     | Unchanged                                                                       |
| Time Slot ID         | :x:                             | time\_slot\_id (string)         | Use either of **time\_slot\_id** OR (selected\_from\_time & selected\_to\_time) |

**Mapping Details**

`time_slot_id` can be fetched from <Anchor label="List Available Pickup Slots" target="_blank" href="https://developers.easyship.com/reference/courier_services_pickup_slots_index">List Available Pickup Slots</Anchor> . Either  `time_slot_id` or `selected_from_time`& `selected_to_time` can be used to specify pickup timings

**Response Structure (2024-09)**

Checkout the updated response structure - <Anchor label="Create a Pickup" target="_blank" href="https://developers.easyship.com/reference/pickups_create">Create a Pickup</Anchor>

***

### Directly Handover - Mark as directly handed over

API Endpoint **`POST /pickup/v1/direct_handover`**

<Callout icon="❗️" theme="error">
  This endpoint will not be available as part of 2024-09 version.
</Callout>

***
