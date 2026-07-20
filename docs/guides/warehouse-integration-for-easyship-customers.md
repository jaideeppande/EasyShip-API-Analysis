# Warehouse Integration for Easyship customers

This document outlines the integration flow for partner warehouses to fulfill the orders of existing Easyship customers.

## Push vs. Pull

Two options are available to synchronize the new orders between Easyship and the WMS:

<Image title="Screen Shot 2018-08-02 at 12.46.32.png" alt={1958} src="https://files.readme.io/8fed585-Screen_Shot_2018-08-02_at_12.46.32.png">
  Flow option 1: Easyship pushes new orders
</Image>

<Image title="Screen Shot 2018-08-02 at 12.46.48.png" alt={1956} src="https://files.readme.io/e1f74da-Screen_Shot_2018-08-02_at_12.46.48.png">
  Flow option 2: Warehouse pulls new orders
</Image>

## Step 1 - Order purchase and Easyship sync

* After the customer makes a purchase, the order is created on Easyship, usually by syncing orders from the client's store
* The client then confirms the shipments and buys the shipping labels

## Step 2 - Order Creation on the WMS

## Option 1 (push)

When the shipping label is successfully generated, Easyship sends a callback to a webhook (POST endpoint to be set on the WMS side), specifying the internal reference of the shipment (easyship\_shipment\_id)

* Documentation: [validate the callback url](https://developers.easyship.com/v1.0/reference#section-validate-the-callback-url)
* When the WMS receives the callback it should send back a 200 response, which will trigger a change of status on Easyship side ("created", see below on the status update).
* A retry mechanism is in place in case a 200 hasn't been received

*Note*: the POST request that Easyship sends as a callback contains the company's reference ID in the headers. This allows you to use one single callback URL for all clients

*Note*: during the client on-boarding, the client needs to subscribe on the Easyship dashboard to the `shipment.label.created` webhook using the endpoint defined by the warehouse

## Option 2 (pull)

The alternative to receiving the callback is to run a cron job to fetch the new orders regularly.

* Documentation: [GET shipment/v1/shipments](https://developers.easyship.com/v1.0/reference#get-shipments), using filters such as label\_generated\_at\_from/to or warehouse\_state:pending

*Note*: if you use this option, we ask you to send a status update for the newly created orders ("created", see below on the status update). For instance if there are 10 new orders fetched for the period, you will create 10 orders or your database and then make a status update call with the 10 reference ids of the orders (easyship\_shipment\_id)

*Note*: the get multiples shipments call provides all the information about the orders, but not the shipping documents

## Step 3 - get order information and shipping documents

The WMS uses the Easyship API to fetch the shipment information, which will include 1) the order info (order #, receiver), 2) the items (SKU...), 3) the shipping documents (options to specify the format and size)

* Documentation: [GET shipment/v1/shipments/\{easyship\_shipment\_id}](https://developers.easyship.com/v1.0/reference?showHidden=e05e2#get-a-shipment)
* Note: the endpoint is currently in beta (and its documentation not public)
* Available format: URL (default, link to .pdf file), PDF (string), PNG (string)
* Available sizes:
* label: A4 (default), 4x6
* commercial\_invoice: A4 (default), 4x6 - only when required
* others (battery declaration): A4 - only when required
* packing\_slip: none (default), A4, 4x6 - only when requested

## Step 4 - status update

When the order is processed (created/packed/shipped), the WMS updates the shipment on Easyship to notify of the change of status

* Documentation: [POST shipment/v1/shipments/update\_warehouse\_state](https://developers.easyship.com/reference#update-shipment-warehouse-status)
* Available statuses:
* ***pending*** : means that the order is ready to be fulfilled and the label is generated. Use this to filter the shipments by `warehouse_state` in GET shipments method (option 2). Note that you can't update a shipment to this status as it is the initial state of the shipment
* ***created*** : already triggered upon positive feedback from the callback that we send. If you don't use the callback to get the new shipments but decided to fetch regularly our get shipments API, this update is mandatory to notify us that the order is being processed in your warehouse
* ***creation\_failed*** : means that the order creation was rejected for an internal reason. This can happen for instance if the order information doesn't meet the WMS' requirements, or a product SKU is not defined in your WMS. A message can be added using the `error_message` parameter - this will allow the client and Easyship to understand the reason for rejection.
* ***packed*** : optional, to let the merchant and buyer know that order is being processed
* ***shipped*** : mandatory for us to trigger the update of the order status on the merchant's store. This usually sends out an email to the buyer. We'll also start tracking the package from that moment
* ***cancelled*** : trigger this update if the order has been cancelled in the warehouse management system. Note: This status update will cancel the shipment in Easyship.
* ***cancelled\_no\_stock*** : The order has been cancelled in the warehouse management system because the products are out of stock. *Note*: This status update will trigger Easyship to cancel the shipment.
* ***backorder\_no\_stock*** : The order is set as backorder because of the products are out of stock. It may be packed and shipped at a later date.
* ***returned*** : trigger this update if the package has been returned by the courier or by the receiver, and received at the warehouse.

## New Client On-boarding

Before a client starts fulfilling their orders through a warehouse, this information needs to be gathered:

* Get the client's own production API token to use the Easyship API: the API can be created by the client from the [Connect page](https://app-staging.easyship.com/connect)
* If you are using the option 1 (push), create a webhook on the Easyship portal with the relevant endpoint, in the [Webhooks page](https://app-staging.easyship.com/webhooks). Knowing the company's Easyship ID (e.g. CUS1234567) will also be necessary to validate the authenticity of the webhooks
* Notify Easyship before the client starts shipping, to make sure that the company is linked to the warehouse in the Easyship system