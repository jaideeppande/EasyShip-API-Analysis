# How to Create a Shipment

```shell Shell
{
  "origin_address": {
    "line_1": "Kennedy Town",
    "line_2": "Block 3",
    "state": "Yuen Long",
    "city": "Hong Kong",
    "postal_code": "0",
    "country_alpha2": "HK",
    "company_name": "Easyship",
    "contact_name": "Eese Shipper",
    "contact_phone": "+852-3008-5678",
    "contact_email": "eese.shipper@gmail.com",
    "originTag": "eese"
  },
  "sender_address": {
    "line_1": "Friendship Court",
    "city": "Hong Kong",
    "state": "Hong Kong Island",
    "postal_code": "0",
    "country_alpha2": "HK",
    "company_name": "Cat Deliveries",
    "contact_name": "Brother Cream",
    "contact_phone": "+852-3008-5678",
    "contact_email": "brother.cream@catmail.io",
    "senderTag": "cream",
    "line_2": "12-22 Blue Pool Rd"
  },
  "return_address": {
    "line_1": "Kennedy Town",
    "line_2": "Block 2",
    "state": "Yuen Long",
    "city": "Hong Kong",
    "postal_code": "0",
    "country_alpha2": "HK",
    "company_name": "Easyship Returns",
    "contact_name": "Super Shipper",
    "contact_phone": "+852-3008-5678",
    "contact_email": "super.shipper@gmail.com",
    "returnTag": "super"
  },
  "destination_address": {
    "line_1": "10 Downing Street",
    "city": "London",
    "postal_code": "SW1A 2AA",
    "country_alpha2": "GB",
    "company_name": "Prime Minister's Office",
    "contact_name": "Larry Cat",
    "contact_phone": "+440834748199",
    "contact_email": "larry.cat@catmail.io",
    "state": "Greater London"
  },
  "metadata": {
    "shipmentTag": "cats"
  },
  "regulatory_identifiers": {
    "eori": "GB123456123456",
    "ioss": "IM0123456789",
    "vat_number": "GB987654321"
  },
  "incoterms": "DDU",
  "insurance": {
    "is_insured": true,
    "insured_amount": 100,
    "insured_currency": "GBP"
  },
  "order_data": {
    "platform_name": "Brother Cream Market",
    "platform_order_number": "bc-1100111",
    "seller_notes": "Fragile",
    "buyer_notes": "Meow"
  },
  "courier_settings": {
    "allow_courier_fallback": true,
    "apply_shipping_rules": true,
    "courier_service_id": "72e648aa-a8f4-4ae5-909d-cb28e31f4s53",
    "list_unavailable_couriers": false
  },
  "shipping_settings": {
    "additional_services": {
      "qr_code": "qr_code",
      "delivery_confirmation": "ups_delivery_confirmation_signature_required"
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
    },
    "custom_markup_rate": 0
  },
  "return": false,
  "set_as_residential": false,
  "parcels": [
    {
      "box": {
        "length": 10,
        "width": 20,
        "height": 10
      },
      "items": [
        {
          "dimensions": {
            "length": 10,
            "width": 20,
            "height": 10
          },
          "description": "Cat food",
          "category": "Treats",
          "sku": "19910",
          "contains_battery_pi966": false,
          "contains_battery_pi967": false,
          "contains_liquids": false,
          "hs_code": "23091090",
          "origin_country_alpha2": "HK",
          "quantity": 1,
          "actual_weight": 3,
          "declared_currency": "USD",
          "declared_customs_value": 100
        }
      ],
      "total_actual_weight": 3
    }
  ]
}
```

```json Response Example
{
    "shipment": {
        "easyship_shipment_id": "ESGB12911830",
        "consignee_tax_id": null,
        "courier": {
            "id": "d1c9b55d-5b0a-4fa7-be01-53f520a190dc",
            "name": "UPS - Standard"
        },
        "created_at": "2023-07-26T21:07:53Z",
        "currency": "HKD",
        "delivery_state": "not_created",
        "destination_address": {
            "city": "London",
            "company_name": "Test Plc.",
            "contact_email": "asd@asd.com",
            "contact_name": "Foo Bar",
            "contact_phone": "+85230085678",
            "country_alpha2": "GB",
            "line_1": "30 Bond Street",
            "line_2": "Flat 3",
            "postal_code": "W1 5AA",
            "state": null
        },
        "eei_reference": null,
        "incoterms": "DDU",
        "insurance": {
            "is_insured": false,
            "insured_amount": 80.45,
            "insured_currency": "HKD"
        },
        "label_generated_at": null,
        "label_paid_at": null,
        "label_state": "not_created",
        "last_failure_http_response_messages": [],
        "metadata": {},
        "order_created_at": null,
        "order_data": {
            "platform_name": null,
            "platform_order_number": null,
            "order_tag_list": [],
            "seller_notes": null,
            "buyer_notes": null
        },
        "origin_address": {
            "city": "London",
            "company_name": "Test Plc.",
            "contact_email": "asd@asd.com",
            "contact_name": "Foo Bar",
            "contact_phone": "+852-3008-5678",
            "country_alpha2": "GB",
            "line_1": "30 Bond Street",
            "line_2": "Flat 3",
            "postal_code": "W15AA",
            "state": null
        },
        "parcels": [
            {
                "box": {
                    "id": null,
                    "name": null,
                    "outer_dimensions": {
                        "length": 10,
                        "width": 10,
                        "height": 10
                    },
                    "slug": null,
                    "type": "box",
                    "weight": 0
                },
                "items": [
                    {
                        "actual_weight": 1,
                        "category": null,
                        "contains_battery_pi966": null,
                        "contains_battery_pi967": null,
                        "contains_liquids": null,
                        "declared_currency": "USD",
                        "declared_customs_value": 1,
                        "description": "Foobar",
                        "dimensions": {
                            "length": 5,
                            "width": 5,
                            "height": 5
                        },
                        "hs_code": "07051100",
                        "origin_country_alpha2": "US",
                        "origin_currency": "HKD",
                        "origin_customs_value": 7.79138,
                        "quantity": 1,
                        "sku": "111"
                    }
                ],
                "total_actual_weight": 1
            }
        ],
        "pickup_state": "not_requested",
        "rates": [
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "dropoff",
                    "paid_pickup"
                ],
                "cost_rank": 3,
                "courier_id": "d1c9b55d-5b0a-4fa7-be01-53f520a190dc",
                "courier_name": "UPS - Standard",
                "courier_remarks": null,
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 1,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 15.86,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": null,
                "min_delivery_time": null,
                "minimum_pickup_fee": 0,
                "other_surcharges": null,
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 1.53,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 1.4,
                    "shipment_charge": 5.46,
                    "shipment_charge_total": 6.99,
                    "total_charge": 8.39,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 14.53,
                "shipment_charge": 56.66,
                "shipment_charge_total": 72.53,
                "total_charge": 87.06,
                "tracking_rating": 3,
                "value_for_money_rank": 1,
                "warehouse_handling_fee": 0
            },
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "dropoff",
                    "paid_pickup"
                ],
                "cost_rank": 1,
                "courier_id": "d70f503c-905b-4e28-a015-d27069a09e0c",
                "courier_name": "Evri - Parcelshop",
                "courier_remarks": "Pickup option available in checkout",
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 3,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 0,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": 2,
                "min_delivery_time": 1,
                "minimum_pickup_fee": 0,
                "other_surcharges": null,
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 0,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 0.7,
                    "shipment_charge": 3.49,
                    "shipment_charge_total": 3.49,
                    "total_charge": 4.19,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 7.26,
                "shipment_charge": 36.22,
                "shipment_charge_total": 36.22,
                "total_charge": 43.48,
                "tracking_rating": 1,
                "value_for_money_rank": 2,
                "warehouse_handling_fee": 0
            },
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "dropoff"
                ],
                "cost_rank": 2,
                "courier_id": "b861d548-1a6b-4b38-b283-fe0c8956a177",
                "courier_name": "Evri - Next Day Parcelshop",
                "courier_remarks": "Drop off before 12noon (Monday to Friday)",
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 4,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 0,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": 2,
                "min_delivery_time": 1,
                "minimum_pickup_fee": 0,
                "other_surcharges": null,
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 0,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 0.82,
                    "shipment_charge": 4.09,
                    "shipment_charge_total": 4.09,
                    "total_charge": 4.91,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 8.51,
                "shipment_charge": 42.44,
                "shipment_charge_total": 42.44,
                "total_charge": 50.95,
                "tracking_rating": 1,
                "value_for_money_rank": 3,
                "warehouse_handling_fee": 0
            },
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "dropoff"
                ],
                "cost_rank": 4,
                "courier_id": "1ea01124-ba24-4f94-b533-6861d9fcc9ca",
                "courier_name": "DPD - Next Day",
                "courier_remarks": null,
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 6,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 9.85,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": 3,
                "min_delivery_time": 3,
                "minimum_pickup_fee": 0,
                "other_surcharges": {
                    "details": [
                        {
                            "fee": 2.08,
                            "name": "Hgv Surcharge",
                            "origin_fee": 0.2
                        }
                    ],
                    "total_fee": 2.08
                },
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 0.95,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 1.49,
                    "shipment_charge": 6.33,
                    "shipment_charge_total": 7.47,
                    "total_charge": 8.96,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 15.46,
                "shipment_charge": 65.64,
                "shipment_charge_total": 77.56,
                "total_charge": 93.02,
                "tracking_rating": 2,
                "value_for_money_rank": 4,
                "warehouse_handling_fee": 0
            },
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "dropoff"
                ],
                "cost_rank": 5,
                "courier_id": "ed5f4ab5-85a7-4c4c-9705-81dabc9332ac",
                "courier_name": "Parcelforce - Express 09:00",
                "courier_remarks": null,
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 2,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 28.47,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": 1,
                "min_delivery_time": 1,
                "minimum_pickup_fee": 0,
                "other_surcharges": null,
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 2.74,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 4.21,
                    "shipment_charge": 18.29,
                    "shipment_charge_total": 21.03,
                    "total_charge": 25.24,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 43.69,
                "shipment_charge": 189.8,
                "shipment_charge_total": 218.27,
                "total_charge": 261.96,
                "tracking_rating": 1,
                "value_for_money_rank": 5,
                "warehouse_handling_fee": 0
            },
            {
                "additional_services_surcharge": 0,
                "available_handover_options": [
                    "paid_pickup"
                ],
                "cost_rank": 6,
                "courier_id": "2fdfcb4d-b239-4400-b7a8-279213029b1d",
                "courier_name": "Evri - Light and Large",
                "courier_remarks": null,
                "currency": "HKD",
                "ddp_handling_fee": 0,
                "delivery_time_rank": 5,
                "description": null,
                "discount": {
                    "amount": 0,
                    "origin_amount": 0
                },
                "easyship_rating": null,
                "estimated_import_duty": 0,
                "estimated_import_tax": 0,
                "fuel_surcharge": 0,
                "full_description": null,
                "import_duty_charge": 0,
                "import_tax_charge": 0,
                "import_tax_non_chargeable": 0,
                "incoterms": "DDU",
                "insurance_fee": 0,
                "is_above_threshold": false,
                "max_delivery_time": 3,
                "min_delivery_time": 1,
                "minimum_pickup_fee": 0,
                "other_surcharges": null,
                "oversized_surcharge": 0,
                "payment_recipient": "Easyship",
                "provincial_sales_tax": 0,
                "rates_in_origin_currency": {
                    "additional_services_surcharge": 0,
                    "currency": null,
                    "ddp_handling_fee": 0,
                    "estimated_import_duty": 0,
                    "estimated_import_tax": 0,
                    "fuel_surcharge": 0,
                    "import_duty_charge": 0,
                    "import_tax_charge": 0,
                    "import_tax_non_chargeable": 0,
                    "insurance_fee": 0,
                    "minimum_pickup_fee": 0,
                    "oversized_surcharge": 0,
                    "provincial_sales_tax": 0,
                    "remote_area_surcharge": 0,
                    "residential_discounted_fee": null,
                    "residential_full_fee": null,
                    "sales_tax": 4.91,
                    "shipment_charge": 24.54,
                    "shipment_charge_total": 24.54,
                    "total_charge": 29.45,
                    "warehouse_handling_fee": 0
                },
                "remote_area_surcharge": 0,
                "remote_area_surcharges": null,
                "residential_discounted_fee": null,
                "residential_full_fee": null,
                "sales_tax": 50.95,
                "shipment_charge": 254.66,
                "shipment_charge_total": 254.66,
                "total_charge": 305.61,
                "tracking_rating": 1,
                "value_for_money_rank": 6,
                "warehouse_handling_fee": 0
            }
        ],
        "regulatory_identifiers": {
            "eori": null,
            "ioss": null,
            "vat_number": null
        },
        "return": false,
        "return_address": {
            "city": "London",
            "company_name": "Test Plc.",
            "contact_email": "asd@asd.com",
            "contact_name": "Foo Bar",
            "contact_phone": "+852-3008-5678",
            "country_alpha2": "GB",
            "line_1": "30 Bond Street",
            "line_2": "Flat 3",
            "postal_code": "W15AA",
            "state": null
        },
        "sender_address": {
            "city": "London",
            "company_name": "Acme Inc.",
            "contact_email": "asd@asd.com",
            "contact_name": "John Doe",
            "contact_phone": "+852-3008-5678",
            "country_alpha2": "GB",
            "line_1": "29 Bond Street",
            "line_2": "Flat 2",
            "postal_code": "W15AA",
            "state": null
        },
        "set_as_residential": false,
        "shipment_state": "created",
        "shipping_documents": [],
        "tracking_page_url": "https://www.trackmyshipment.co/shipment-tracking/ESGB12911830",
        "trackings": [],
        "updated_at": "2023-07-26T21:07:54Z",
        "warehouse_state": "none"
    },
    "meta": {
        "unavailable_couriers": []
    }
}
```

# Addresses. Origin address

<!-- shell@2-14 -->

Specify the origin address of the shipment using `address` object or the `origin_address_id` field if the address was created via the Easyship `/addresses` API and has a proper address ID.

# Addresses. Sender address

<!-- shell@15-27 -->

Specify the sender address if different from the origin address.  
This option is available only for couriers supporting different addresses to be shown on a parcel.  
This also can be done via `address object` or `sender_address_id` field.

# Addresses. Return address

<!-- shell@28-40 -->

Specify the return address if different from the origin address, also using `address` object or the `return_address_id` field.

# Addresses. Destination address

<!-- shell@41-51 -->

Specify the destination address of the shipment using `address` object.

# Packaging

<!-- shell@99-128 -->

Provide the packaging details.

# Couriers

<!-- shell@72-77 -->

Specify the courier in the `courier_settings` object:

- `courier_service_id ` — courier ID obtained via the Rates API

- `allow_courier_fallback` — set to true if you want to select the next best courier option in case selected courier is unavailable

- `apply_shipping_rules` — set to false if you don’t want to assign shipping rules to this shipment

- `list_unavailable_couriers` — if set to true, the endpoint will return a list with all unavailable couriers and reasons for their unavailability

# Additional shipment details

<!-- shell@52-54,97 -->

Configure additional shipment details:

- set the `return` field as true if the shipment is for returning a product to the sender

- specify additional key-value fields in the `metadata` object

# Customs and regulations

<!-- shell@55-58,60 -->

Specify the customs and regulatory information:

- for customs clearance in certain countries, such as China or Brazil, specify the consignee’s tax identification number or EIN in the `consignee_tax_id field`

- if sending goods over 2500 USD in value from the US, specify the Electronic Export Identifier (EEI) in the `eei_reference` field

- fill corresponding fields in the `regulatory_identifiers` object for applicable Economic Operators Registration and Identification (EORI), Import One Stop Shop (IOSS), or Value-Added Tax (VAT) numbers

- specify applicable incoterms (`DDU`, `DDP`, or `null` if not applied) in the `incoterms` ENUM

# Insurance

<!-- shell@61-64 -->

Provide the insurance information:

- to add shipment insurance, set true for the `is_insured` field of the `insurance` object

- specify insured amount — `insured_amount` — and insurance currency — `insured_currency`— as an ISO-4217 three-letter alphabetic currency code

# Additional data

<!-- shell@66-71 -->

Use the `order_data` object to add any additional data:

- `platform_name` — name of your platform

- `platform_order_number` — corresponding order number on your side

- `order_tag_list` — custom tags as an array of strings

- `seller_notes` — text added by a merchant (not shown to the shipment recipient)

- `buyer_notes` — text added by a buyer while ordering and checking out (will be displayed on the package)

# Settings

<!-- shell@78-94 -->

Use the `shipping_settings` object to configure:

1. `additional_services`:

- `delivery_confirmation` — set to true if you want to obtain a delivery confirmation from a courier
- `qr_code` — generate a QR code while generating a label (currently, for USPS only)

2. `units`:

- `weight` — kg / g / lb / oz (kg by default)
- `dimensions` — cm / in (cm by default)

3. `buy_label` — buy label together with the creation of this shipment (false by default).

4. `buy_label_synchronous` — synchronous generation of a shipment label (false by default).

5. `printing_options`:

- `format`— png, pdf, url (png by default)
- `label` — 4x6 / A4 / A5 (4x6 by default)
- `commercial_invoice` — 4x6 / A4 (A4 by default)
- `packing_slip` — 4x6 / A4 (4x6 by default)
- `remarks` — customized commercial invoice remarks with a priority over remarks from company settings