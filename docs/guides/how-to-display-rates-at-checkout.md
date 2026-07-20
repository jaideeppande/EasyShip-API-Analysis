# How to Display Rates at Checkout

The **Rates at Checkout** (RaC) feature allows you to provide end customers with multiple shipping options before the order is placed. This feature can be easily integrated into your shopping website.

> 📘
>
> This guide covers the **Rates at Checkout** feature API integration into your custom website.
>
> To learn more about the Rates at Checkout integration workflow for e-commerce platforms with list of supported stores, refer to our [Shipping Rates at Checkout Feature](https://support.easyship.com/hc/en-us/articles/115003453151-Shipping-Rates-at-Checkout-Feature) Help Centre article.

## Endpoint description

The RaC feature is available via the [Rates](https://developers.easyship.com/reference/rates_request) API and requires the `Rate` authorisation scope.

```
POST https://api.easyship.com/2023-01/rates
```

In request body, this API method requires the shipment details below.

1. Origin address is an origin `address` object. Use [Addresses](https://developers.easyship.com/reference/addresses_index) API to get the origin `address` object.
2. Destination address is an `address` object from the data provided by the end customer. To make sure the customer’s address is valid and correct, use our [Address Validation](https://developers.easyship.com/docs/how-to-validate-addresses) feature.
3. Parcel details is a `parcel` object with the following required fields:
   * `items` — array of `item` objects describing items to be shipped. Item objects can be filled from scratch or assigned by product IDs in case you have pre-filled [Products](https://developers.easyship.com/reference/products_index) API
   * `box` —  object with shipment packaging details. Box can be specified explicitly as a `custom` one or assigned by a `slug` from predefined options available via the [Box](https://developers.easyship.com/reference/boxes_index) API
   * `total_actual_weight` — total weight of a shipment in kilograms

In response, you will obtain the `rates` object containing an array of available couriers with their applicable shipment rates and additional data.

Courier rates are scored by Easyship and returned in ascending order by a total shipment charge and in descending order by best value for money. This array allows you to display the cheapest, fastest and best value for money options to your end customer.

## International shipping

Depending on the shipment type and conditions, you can display different breakdown of costs at checkout for your end user. For international shipments, you may have the following duties payment options:

1. **Delivered Duty Unpaid** (**DDU**) where the buyer is responsible for paying any taxes, duties, or import fees on the shipment.
2. **Delivered Duty Paid** (**DDP**) where the seller is responsible for paying any taxes, duties, or import fees on the shipment.\
   To learn more about DDP and DDU Incoterms, see our [DDU vs. DDP: Understanding the Differences](https://www.easyship.com/blog/ddu-vs-ddp?ref=easyship.ghost.io) Help Centre article.\
   DDP terms are different depending on whether your business uses the IOSS system or not.
3. **Import One Stop Shop** (**IOSS**) is an electronic portal in the European Union that businesses can use to pay any Import VAT on commercial goods shipped into the EU, under the value of €150,00 (euros).

To learn more about IOSS system and how it will affect you as an international shipper, see our [What is IOSS](https://support.easyship.com/hc/en-us/articles/4407846885389-What-is-IOSS-Import-One-Stop-Shop-) Help Centre article.

Refer to our [How to Calculate Taxes and Duties](https://developers.easyship.com/docs/how-to-calculate-taxes-and-duties) API guide to obtain an easy-to-understand taxes and duties price breakdown.

Below, you will find the request and response body schemas, as well as complete request and response examples.

## Request body parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field name
      </th>

      <th>
        Data type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `origin_address`
      </td>

      <td>
        Object (Address)
      </td>

      <td>
        `Address` object for shipment origin ([Address](https://developers.easyship.com/reference/addresses_index) API).
      </td>
    </tr>

    <tr>
      <td>
        `destination_address`
      </td>

      <td>
        Object (Address)
      </td>

      <td>
        `Address` object for shipment destination ([Address](https://developers.easyship.com/reference/addresses_index) API).
      </td>
    </tr>

    <tr>
      <td>
        `parcels`
      </td>

      <td>
        Array of objects:  

        `items` (Object)\
        `box` (Object)\
        `total_actual_weight` (Integer)
      </td>

      <td>
        Shipment items:  

        The `items` object for shipment items  

        The `box` object for shipment packaging ([Box](https://developers.easyship.com/reference/boxes_index) API)  

        `total_actual_weight` of a shipment
      </td>
    </tr>
  </tbody>
</Table>

## Response body parameters

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field name
      </th>

      <th>
        Data type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `courier_id`
      </td>

      <td>
        String
      </td>

      <td>
        Courier service identifier on the Easyship platform.
      </td>
    </tr>

    <tr>
      <td>
        `courier_name`
      </td>

      <td>
        String
      </td>

      <td>
        Name of the courier service.
      </td>
    </tr>

    <tr>
      <td>
        `courier_remarks`
      </td>

      <td>
        String
      </td>

      <td>
        Additional details of the courier service.
      </td>
    </tr>

    <tr>
      <td>
        `description`
      </td>

      <td>
        String
      </td>

      <td>
        Short courier service description.
      </td>
    </tr>

    <tr>
      <td>
        `full_description`
      </td>

      <td>
        String
      </td>

      <td>
        Full courier service description.
      </td>
    </tr>

    <tr>
      <td>
        `easyship_rating`
      </td>

      <td>
        Integer
      </td>

      <td>
        Average ratings of the courier service provided by Easyship users and end customers.
      </td>
    </tr>

    <tr>
      <td>
        `cost_rank`
      </td>

      <td>
        Integer
      </td>

      <td>
        Result of the Easyship cost scoring for a specified shipment: `1` is the best option.
      </td>
    </tr>

    <tr>
      <td>
        `delivery_time_rank`
      </td>

      <td>
        Integer
      </td>

      <td>
        Result of the Easyship delivery time scoring based on minimal delivery time estimation: `1` is the best option.
      </td>
    </tr>

    <tr>
      <td>
        `tracking_rating`
      </td>

      <td>
        Integer
      </td>

      <td>
        Courier’s rating based on number and accuracy of tracking details provided (from `1` to `5` in descending order).
      </td>
    </tr>

    <tr>
      <td>
        `value_for_money_rank`
      </td>

      <td>
        Integer
      </td>

      <td>
        Combined rank calculated by comparison of cost and delivery time ranks: `1` is the best option.
      </td>
    </tr>

    <tr>
      <td>
        `available_handover_options`
      </td>

      <td>
        Array (Enum (String))
      </td>

      <td>
        Options provided by a courier for delivery handover:  

        `dropoff`\
        `free_pickup`\
        `paid_pickup`
      </td>
    </tr>

    <tr>
      <td>
        `incoterms`
      </td>

      <td>
        Enum (String)
      </td>

      <td>
        Applicable Incoterms: `DDU` or `DDP`
      </td>
    </tr>

    <tr>
      <td>
        `max_delivery_time`
      </td>

      <td>
        Integer
      </td>

      <td>
        Upper bound of the delivery window (working days).
      </td>
    </tr>

    <tr>
      <td>
        `min_delivery_time`
      </td>

      <td>
        Integer
      </td>

      <td>
        Lower bound of the delivery window (working days).
      </td>
    </tr>

    <tr>
      <td>
        `is_above_threshold`
      </td>

      <td>
        Boolean
      </td>

      <td>
        `True` if the purchase price of the shipment exceeds the customs threshold specified by an import country. In this case, the following charges will be applicable:  

        `import_tax_charge`\
        `import_duty_charge`\
        `estimated_import_tax`\
        If `false`, these charges will be `0`.
      </td>
    </tr>

    <tr>
      <td>
        `currency`
      </td>

      <td>
        Enum (String)
      </td>

      <td>
        ISO-4217 three-letter alphabetic currency code.
      </td>
    </tr>

    <tr>
      <td>
        `payment_recipient`
      </td>

      <td>
        Enum (String)
      </td>

      <td>
        Payment recipient for a shipment:  

        `Easyship`\
        `EasyshipPayOnScan`\
        `Courier`
      </td>
    </tr>

    <tr>
      <td>
        `discount`
      </td>

      <td>
        Object
      </td>

      <td>
        Applicable courier discount (amount or percentage):  

        `amount` — fixed discount amount  

        `origin_amount` — discount percentage
      </td>
    </tr>

    <tr>
      <td>
        `shipment_charge`
      </td>

      <td>
        Number
      </td>

      <td>
        Base courier service charge.
      </td>
    </tr>

    <tr>
      <td>
        `shipment_charge_total`
      </td>

      <td>
        Number
      </td>

      <td>
        Subtotal of the following charges:  

        `shipment_charge`\
        `fuel_surcharge`\
        `residential_full_fee`\
        `residential_discounted_fee`\
        `remote_area_surcharge`\
        `additional_services_surcharge`\
        `oversized_surcharge`
      </td>
    </tr>

    <tr>
      <td>
        `total_charge`
      </td>

      <td>
        Number
      </td>

      <td>
        Total charge including `shipment_charge_total` and all applicable fees, taxes and duties.
      </td>
    </tr>

    <tr>
      <td>
        `additional_services_surcharge`
      </td>

      <td>
        Number
      </td>

      <td>
        Charges applicable for additional delivery services (e.g. delivery confirmation).
      </td>
    </tr>

    <tr>
      <td>
        `ddp_handling_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Additional fees for the DDP option: courier pays import taxes and duties on buyer’s behalf. DDP handling fee is not charged if the IOSS scheme is in place and an order value is less than 150 euro.
      </td>
    </tr>

    <tr>
      <td>
        `estimated_import_duty`
      </td>

      <td>
        Number
      </td>

      <td>
        Estimated shipment import duty in case of DDU Incoterms.
      </td>
    </tr>

    <tr>
      <td>
        `estimated_import_tax`
      </td>

      <td>
        Number
      </td>

      <td>
        Estimated shipment import tax, in case of DDU Incoterms.
      </td>
    </tr>

    <tr>
      <td>
        `import_duty_charge`
      </td>

      <td>
        Number
      </td>

      <td>
        Shipment import duty for DDP Incoterms.
      </td>
    </tr>

    <tr>
      <td>
        `import_tax_charge`
      </td>

      <td>
        Number
      </td>

      <td>
        Shipment import duty for DDP Incoterms.
      </td>
    </tr>

    <tr>
      <td>
        `fuel_surcharge`
      </td>

      <td>
        Number
      </td>

      <td>
        Fuel surcharge applicable for a shipment.
      </td>
    </tr>

    <tr>
      <td>
        `import_tax_non_chargeable`
      </td>

      <td>
        Number
      </td>

      <td>
        IOSS amount of import tax. This tax is not charged while shipping and is displayed for information purposes only.
      </td>
    </tr>

    <tr>
      <td>
        `insurance_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Applicable delivery insurance fee.
      </td>
    </tr>

    <tr>
      <td>
        `minimum_pickup_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Minimal estimated delivery pickup fee (for the `paid_pickup` handover option if available).
      </td>
    </tr>

    <tr>
      <td>
        `oversized_surcharge`
      </td>

      <td>
        Number
      </td>

      <td>
        Surcharge for an oversized package, if applicable.
      </td>
    </tr>

    <tr>
      <td>
        `provincial_sales_tax`
      </td>

      <td>
        Number
      </td>

      <td>
        State, province or local government taxes, if applicable.
      </td>
    </tr>

    <tr>
      <td>
        `remote_area_surcharge`
      </td>

      <td>
        Number
      </td>

      <td>
        Total remote area surcharge for origin and destination areas (see `remote_area_surcharges` below).
      </td>
    </tr>

    <tr>
      <td>
        `remote_area_surcharges`
      </td>

      <td>
        Object
      </td>

      <td>
        Additional surcharge payable if delivery is specified for distant areas (e.g. islands or highlands):  

        `origin` for a shipment origin\
        `destination` for a shipment destination  

        Both `origin` and `destination` objects include the following fields:  

        `name` — name of the distant area\
        `base` — amount payable
      </td>
    </tr>

    <tr>
      <td>
        `residential_discounted_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Discounted fee provided by the courier if a recipient’s delivery address corresponds with their residential address.
      </td>
    </tr>

    <tr>
      <td>
        `residential_full_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Full fee payable if a recipient’s delivery address corresponds with their residential address.
      </td>
    </tr>

    <tr>
      <td>
        `sales_tax`
      </td>

      <td>
        Number
      </td>

      <td>
        National government sales tax.
      </td>
    </tr>

    <tr>
      <td>
        `warehouse_handling_fee`
      </td>

      <td>
        Number
      </td>

      <td>
        Fee added by a fulfilment service for warehouse operations.
      </td>
    </tr>

    <tr>
      <td>
        `other_surcharges`
      </td>

      <td>
        Object
      </td>

      <td>
        Other applicable surcharges:  

        `total_fee` — total amount of other surcharges  

        `details`:  

        `name` — surcharge name\
        `fee` — surcharge amount in the currency of the shipment\
        `origin_fee` — surcharge amount in the currency of the origin country
      </td>
    </tr>

    <tr>
      <td>
        `rates_in_origin_currency`
      </td>

      <td>
        Object
      </td>

      <td>
        Fees and charges in the currency of the shipment origin country:  

        `currency`\
        `shipment_charge`\
        `shipment_charge_total`\
        `total_charge`\
        `additional_services_surcharge`\
        `ddp_handling_fee`\
        `estimated_import_duty`\
        `estimated_import_tax`\
        `import_duty_charge`\
        `import_tax_charge`\
        `fuel_surcharge`\
        `import_tax_non_chargeable`\
        `insurance_fee`\
        `minimum_pickup_fee`\
        `oversized_surcharge`\
        `provincial_sales_tax`\
        `remote_area_surcharge`\
        `residential_discounted_fee`\
        `residential_full_fee`\
        `sales_tax`\
        `warehouse_handling_fee`
      </td>
    </tr>
  </tbody>
</Table>

## Examples

### Request body

```
{
    "origin_address": {
        "line_1": "55 Prospect St",
        "line_2": "Unit 401",
        "state": "NY",
        "city": "Sydney",
        "postal_code": "11201",
        "country_alpha2": "US"
    },
    "destination_address": {
        "line_1": "1 quai de Jemmapes",
        "line_2": "Porte A",
        "state": "CA",
        "city": "Paris",
        "postal_code": "75010",
        "country_alpha2": "FR"
        },
        "output_currency": "HKD"
    },
    "parcels": [
            "items": [
                {
                    "description": "Silk dress",
                    "category": "fashion",
                    "sku": "test01",
                    "quantity": 2,
                    "dimensions": {
                        "length": null,
                        "width": null,
                        "height": null
                    },
                    "actual_weight": 10,
                    "declared_currency": "USD",
                    "declared_customs_value": 20
                }
            ]
        }
    ]
}
```

### Response body

```
{
    "status": "success",
    "rates": [
        {
            "courier_id": "a6d078fd-e662-40ce-9efe-84caaa639bf7",
            "courier_name": "USPS - First Class International",
            "min_delivery_time": 5,
            "max_delivery_time": 9,
            "value_for_money_rank": 1.0,
            "delivery_time_rank": 5.0,
            "currency": "HKD",
            "shipment_charge": 200.86,
            "fuel_surcharge": 0.0,
            "remote_area_surcharge": 0.0,
            "remote_area_surcharges": {},
            "other_surcharges": {},
            "oversized_surcharge": 0.0,
            "additional_services_surcharge": 0.0,
            "residential_full_fee": 0.0,
            "residential_discounted_fee": 0.0,
            "shipment_charge_total": 200.86,
            "warehouse_handling_fee": 0.0,
            "insurance_fee": 0.0,
            "sales_tax": 0.0,
            "provincial_sales_tax": 0.0,
            "ddp_handling_fee": 0.0,
            "import_tax_charge": 0.0,
            "import_tax_non_chargeable": 0.0,
            "import_duty_charge": 0.0,
            "total_charge": 200.86,
            "is_above_threshold": true,
            "incoterms": "DDU",
            "estimated_import_tax": 102.94,
            "estimated_import_duty": 0.0,
            "minimum_pickup_fee": 0.0,
            "available_handover_options": "dropoff,free_pickup",
            "tracking_rating": 1,
            "easyship_rating": 3.5,
            "courier_remarks": null,
            "payment_recipient": "Easyship",
            "discount": {
                "amount": 0,
                "code": null,
                "percentage": null,
                "expires_at": null,
                "origin_amount": 0
            },
            "description": "Estimated  102.94 tax & duty due on delivery (Tax handling fees may apply)",
            "full_description": "USPS - First Class International (5-9 working days) Estimated  102.94 tax & duty due on delivery (Tax handling fees may apply)"
        }
```

To learn more about the calculation process, refer to our [How Shipping Rates Are Calculated at Checkout](https://support.easyship.com/hc/en-us/articles/360060201371) Help Center article.