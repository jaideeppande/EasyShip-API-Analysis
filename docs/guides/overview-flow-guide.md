# Overview Flow Guide

This guide will walk you through a streamlined process for using Easyship shipping API to seamlessly integrate and manage your shipments from start to finish.

By following this guide, you'll quickly dive into essential functionality and learn how to collect shipment details, retrieve shipping rates, select a courier, create shipments, generate labels, and keep track of your shipments through real-time updates. Whatever needs you have, Easyship will simplify your shipping experience.

## Before you begin

As a prerequisite on your side, you will need sender and recipient addresses, dimensions of a package, weight of all items to be delivered and delivery terms to create a shipment.

## Step-by-step description

1. **Create a shipment**. Use [Create a Shipment](https://developers.easyship.com/reference/shipments_create) to create a new shipment. The rates will be included in the `rates` section.
   * Here's a [How to Create a Shipment](https://developers.easyship.com/recipes/how-to-create-a-shipment) guide to help you.
   * To save time and optimise your costs, you can create [batches of shipments](https://developers.easyship.com/reference/batch_shipments_create).
   * By adding parameters `buy_label` and `buy_label_synchronous`(not supported in batch creation), you can decide the label generation behavior in the same request. However, this might extend the processing time depending on the couriers' response.
     <br />
2. **Retrieve rates**. Retrieve a list of available shipping options and their corresponding costs from the `shipment.rates` section. The rates are calculated based on shipment destination, package, total dimensions, and weight.
   * The `courier_service_id` to include in the `generate label` requests will be included in `shipment.rates.[]courier_service`.
     <br />
3. **Update shipments**. Use [Update a Shipment](https://developers.easyship.com/reference/shipments_update) to update the details of a shipment.
   * Updating courier selection under `shipment.courier_service_id` is not mandatory. You will be able to provide the selected `courier_service_id` when generating labels.
     <br />
4. **Generate label**. Once the shipment is created, use [Create a Batch of Labels](https://developers.easyship.com/reference/batch_labels_create)(asynchronously) or [Create Label](https://developers.easyship.com/reference/shipment_labels_create)(synchronously) to confirm the shipment and generate a shipping label with other shipping documents. Generating the label will trigger delivery. From this step, shipment information will be transferred to the courier.
   * By setting up [Webhooks](https://developers.easyship.com/reference/webhooks-guide) ([shipment.label.created](https://developers.easyship.com/reference/shipmentlabelcreated) and  [shipment.label.failed](https://developers.easyship.com/reference/shipmentlabelfailed) events): Easyship will automatically send information updates to your service whenever the shipment status changes.
     <br />
5. Obtain **tracking updates**. You can track the shipment status in two ways:
   * Via the [Trackings](https://developers.easyship.com/reference/shipments_trackings_index) API: send requests from your service to obtain real-time information about shipment location and status.
   * By setting up [Webhooks](https://developers.easyship.com/reference/webhooks-guide) ([shipment.tracking.checkpointscreated](https://developers.easyship.com/reference/shipmenttrackingcheckpointscreated) and  [shipment.tracking.statuschanged](https://developers.easyship.com/reference/shipmenttrackingstatuschanged) events): Easyship will automatically send information updates to your service whenever the shipment status changes.

<br />