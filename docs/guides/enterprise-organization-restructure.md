# Enterprise Organization Restructure

We are simplifying the structure of our Enterprise API by deprecating the multi-organization feature. This change will streamline the API and make it easier to use. The modifications apply to both the `2024-11` and `2023-09` versions.

## What is changing?

Previously, enterprise API users could create and manage multiple organizations, each with its own set of companies. We are moving to a single-organization model, where one Easyship account can only have one organization that contains all companies.

## What will no longer be supported?

The following features will no longer be supported:

* Create an organization under enterprise Easyship account.
* Update an organization under enterprise Easyship account.
* Delete an organization under enterprise Easyship account.

## Deprecated Endpoints and Replacements

Users will no longer need to specify the `organization_id` when interacting with their organization.

The following endpoints are now deprecated. While they are still supported, they will be removed in a future version of the API. We recommend migrating to the new endpoints as soon as possible.

### Deprecated Endpoints

* `GET /:version/organizations`
* `GET /:version/organizations/{organization_id}/companies`
* `POST /:version/organizations/{organization_id}/webhooks/{webhook_id}/activate`
* `POST /:version/organizations/{organization_id}/webhooks/{webhook_id}/deactivate`
* `POST /:version/organizations/{organization_id}/webhooks/{webhook_id}/test`
* `GET /:version/organizations/{organization_id}/webhooks`
* `POST /:version/organizations/{organization_id}/webhooks`
* `GET /:version/organizations/{organization_id}/webhooks/{webhook_id}`
* `PATCH /:version/organizations/{organization_id}/webhooks/{webhook_id}`
* `DELETE /:version/organizations/{organization_id}/webhooks/{webhook_id}`
* `GET /:version/organizations/{organization_id}/shipping_rules`
* `POST /:version/organizations/{organization_id}/shipping_rules`

### Replacements

* `GET /:version/organization/companies`
* `POST /:version/organization/webhooks/{webhook_id}/activate`
* `POST /:version/organization/webhooks/{webhook_id}/deactivate`
* `POST /:version/organization/webhooks/{webhook_id}/test`
* `GET /:version/organization/webhooks`
* `POST /:version/organization/webhooks`
* `GET /:version/organization/webhooks/{webhook_id}`
* `PATCH /:version/organization/webhooks/{webhook_id}`
* `DELETE /:version/organization/webhooks/{webhook_id}`
* `GET /:version/organization/shipping_rules`
* `POST /:version/organization/shipping_rules`

## Action Needed

During migration, all non-primary organizations will be removed and their associated companies will be deactivated. No action is required on your part for data migration.