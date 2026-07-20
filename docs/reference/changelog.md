# Changelog

This changelog details the ongoing improvements to the Easyship Public API, your gateway to powerful shipping solutions. Explore the latest changes and leverage our API for seamless integration.

## Releases

### October, 2025

#### October 30

* **(Breaking Change)** New domain for sandbox environment. The production environment will no longer accept sandbox access tokens. Simplified domain information in [documentation](https://developers.easyship.com/docs/introduction-2).

### September, 2025

#### September 23rd

* **(Feature)** **New fields `official_name` and `nickname` in courier service endpoint**\
  The courier service endpoint now includes official\_name and nickname fields to provide flexibility in displaying courier service names.\\

  Read the documentation [here](https://developers.easyship.com/reference/courier_services_index).

#### September 16th

* **(Change)** **Update sandbox rate limit**\
  The sandbox environment rate limit has been updated to 6 requests per minute and 1 request per second.

#### September 11th

* **(Feature)** **New field tracking\_rating in courier service endpoint**\
  The courier service endpoint now includes a tracking\_rating field to provide quality of tracking information.\
  Read the documentation [here](https://developers.easyship.com/reference/courier_services_index).

### August, 2025

#### August 14th

* **(Feature)** **New Endpoint for searching Canada Post post offices**\
  Learn more about Canada Post location endpoint [here](https://developers.easyship.com/reference/locations_canada_post_index)

### April, 2025

#### April 10th

* **(Feature)** **Improvements on Manifests Creation**\
  Manifests for USPS couriers can be created when shipments do not require pickups or drop-offs.\
  Learn more about creating manifest [here](https://developers.easyship.com/reference/manifests_create).

### March, 2025

#### March 25th

* **(Feature)** **Adding New Filter to List all Addresses**\
  We are adding a filter to select addresses based on their default status.\
  Learn more about the changes [here](https://developers.easyship.com/reference/addresses_index).
* **(Feature)** **Endpoint for Tracking Update in Sandbox Environment**\
  Users can now update tracking information through the Sandbox environment. This endpoint is specifically for testing tracking status updates and is exclusively available within Sandbox environment. Read the documentation [here](https://developers.easyship.com/reference/sandbox_trackings_update).
* **(Feature)** **`accepts`filter on List all Courier Services**\
  Now we can use `accepts` filter for listing all courier services. The documentation is available [here](https://developers.easyship.com/reference/courier_services_index).

#### March 11th

* **(Feature)** **Generate Label within Sandbox Environment**\
  Users can now generate label with QR code within Sandbox environment.

***

## New API for v2024-09

* New [Scopes](https://developers.easyship.com/reference/scopes) with support for `read` and `write` access.
* Enhanced [Errors](https://developers.easyship.com/reference/errors) responses with links to our documentation and knowledge base.
* [Redirects API](https://developers.easyship.com/reference/redirects)
* [Validate a single address](https://developers.easyship.com/reference/addresses_validation) (requires an updated contract with Easyship)
* [Create a Batch of Labels](https://developers.easyship.com/reference/batch_labels_create)
* [Locations API](https://developers.easyship.com/reference/locations) for UPS and USPS
* [Credit API](https://developers.easyship.com/reference/credit) for a top-up or refund of your available credit.
* [Payment Sources API](https://developers.easyship.com/reference/payment-sources)
* [Manifests API](https://developers.easyship.com/reference/manifests)
* [Shipping Rules API](https://developers.easyship.com/reference/shipping-rules) with [Shipping Rule's Conditions](https://developers.easyship.com/reference/shipping-rules-conditions-1) and [Shipping Rule's Actions](https://developers.easyship.com/reference/shipping-rules-actions)
* Track shipments created outside of us with [Trackings API](https://developers.easyship.com/reference/trackings) (requires an updated contract with Easyship)

## Breaking changes for v2024-09

* View [Migration guide](https://developers.easyship.com/reference/migration-guide-from-2023-01-and-older) for more details
* All beta endpoints from 2023-01 are now deprecated and moved to this version.
* [Labels API](https://developers.easyship.com/v2023.01/reference/labels_create)  was deprecated in favor of Batch API ( [Create a Batch of Labels](https://developers.easyship.com/reference/batch_labels_create)).
* [Bulk update of Courier Account's Couriers](https://developers.easyship.com/v2023.01/reference/courier_accounts_couriers_bulk_update)  was deprecated.
* Renamings of **Courier Accounts** and **Couriers**. All references (in requests, responses, and URL paths are affected).
  * The renaming
    * **Courier Account** => **Courier**
    * **Courier** => **Courier Service**
  * Changed paths
    * `/2023-01/couriers` to `/2024-09/courier_services`
    * `/2023-01/courier_accounts/:courier_account_id/couriers` to `/2024-09/couriers/:courier_id/courier_services`
    * `/2023-01/couriers/:courier_id/pickup_slots` to `/2024-09/courier_services/:courier_service_id/pickup_slots`
    * `/2023-01/couriers/:courier_id/estimated_delivery_dates` to `/2024-09/courier_services/:courier_service_id/estimated_delivery_dates`
    * `/2023-01/courier_accounts` to `/2024-09/couriers`
    * `/2023-01/courier_accounts/:courier_account_id` to `/2024-09/couriers/:courier_id`
    * `/2023-01/courier_accounts/:courier_account_id/couriers` to `/2024-09/couriers/:courier_id/courier_services`
  * Changed attributes
    * `courier_id` to `courier_service_id`
    * `courier_account_id` to `courier_id`
  * Webhooks now support both namings where you can pick which version you want during the webhook creation (or update).