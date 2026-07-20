# How to Create a Return Shipment

If you need to process a return for an item, it's efficient to create a return shipment using the Easyship [Shipments API](https://developers.easyship.com/reference/return_shipments_create) instead of generating an entirely new shipment. The return shipment request is specifically designed to reuse shipment data, saving both time and computational resources on your end.

To initiate a return shipment, include the `easyship_shipment_id` of the original shipment that needs to be returned to the merchant.

## Request body parameters

The request body comprises the following essential fields:

1. `destination_address_id`: select a return address ID if the destination address for a return differs from the shipment `return_address` or `return_address_id`. Leave this field blank if the return address remains the same.
2. `courier_selection`: specify the preferred courier for the return shipment.
3. `parcels`: include parcel details for the return shipment.
4. `shipping_settings.additional_services`: configure additional services as needed.

> 📘
>
> For in-depth information on the `destination_address_id`, `courier_selection`, `parcels` and  `shipping_settings.additional_services` fields consult our [How to Create a Shipment](https://developers.easyship.com/recipes/how-to-create-a-shipment) guide.

Return shipments support the full range of Easyship shipping features: [shipping rules](https://dash.readme.com/project/easyship/v2023.01/docs/how-to-automate-your-shipments), tracking and corresponding webhooks.