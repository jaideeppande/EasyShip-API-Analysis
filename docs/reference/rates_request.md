# Request Rates

Request a list of shipping quotes for a prospective shipment.

Required authorization scope: `public.rate:read`

> Compare couriers to see the cheapest, fastest and best value for money, or a combination of speed, price and reliability.

## Input city and state

If you are shipping to or within the United States, Canada, Mexico or Australia, we recommend that you always input the origin and destination `city` and `state`. This information is required by certain couriers to return accurate rates.

## Calculate dimensions and total weight

You can calculate dimensions and total weight of your shipment in three ways:

* Provide `total_actual_weight` and `box` objects for the shipment.
* Specify `actual_weight` and `dimensions` for each item of the `items` object: in this case, total weight and box size will be calculated automatically.
* Specify `sku` for each item of the `items` object: in this case, actual weight and dimensions for calculations will be taken as set for the product.

> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).

Calls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Easyship Public API",
    "version": "v2024-09",
    "description": "## Powerful Shipping API for Ecommerce\nEasyship provides a powerful shipping API for you to add hassle free worldwide shipping options to your website and end to end shipping functionality to your warehouse, ERP or platform.\n\n### Craft an amazing checkout experience\nProvide instant access to heavily discounted shipping with a single integration. Let end customers choose their preferred shipping method and cost, all within your own UI. Once they've selected and paid, confirm the shipment and all costs are guaranteed by us.\n\n### Write less code, have more options\nYou don’t need to be a shipping expert. We continuously add new shipping solutions to our platform to provide better pricing and service to our users. You don’t need to open direct accounts or write multiple integrations, once we’ve added them, they’re available to you instantly.\n\n### Streamline your processes\nInteract with the Easyship platform from any interface. Whether it’s your ecommerce platform, warehouse/wms, ERP or order management system, you can get rates, create shipments, download labels and track deliveries, without leaving your main business system.",
    "termsOfService": "https://www.easyship.com/legal/terms/overview",
    "contact": {
      "name": "Easyship Support",
      "url": "https://www.easyship.com/contact"
    }
  },
  "externalDocs": {
    "description": "Find out more about Easyship API",
    "url": "https://developers.easyship.com/"
  },
  "tags": [
    {
      "name": "Rates"
    }
  ],
  "paths": {
    "/2024-09/rates": {
      "post": {
        "summary": "Request Rates",
        "tags": [
          "Rates"
        ],
        "operationId": "rates_request",
        "description": "Request a list of shipping quotes for a prospective shipment.\n\nRequired authorization scope: `public.rate:read`\n\n> Compare couriers to see the cheapest, fastest and best value for money, or a combination of speed, price and reliability.\n\n## Input city and state\n\nIf you are shipping to or within the United States, Canada, Mexico or Australia, we recommend that you always input the origin and destination `city` and `state`. This information is required by certain couriers to return accurate rates.\n\n## Calculate dimensions and total weight\n\nYou can calculate dimensions and total weight of your shipment in three ways:\n\n* Provide `total_actual_weight` and `box` objects for the shipment.\n* Specify `actual_weight` and `dimensions` for each item of the `items` object: in this case, total weight and box size will be calculated automatically.\n* Specify `sku` for each item of the `items` object: in this case, actual weight and dimensions for calculations will be taken as set for the product.\n\n> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).\n\nCalls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "rates without taxes and duties when calculate_tax_and_duties is false",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "rates": [
                        {
                          "additional_services_surcharge": 0,
                          "available_handover_options": [],
                          "cost_rank": 1,
                          "courier_remarks": null,
                          "courier_service": {
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "logo": null,
                            "name": "Courier 1",
                            "umbrella_name": "Courier 1"
                          },
                          "currency": "HKD",
                          "ddp_handling_fee": 0,
                          "delivery_time_rank": 2,
                          "description": "Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "discount": {
                            "amount": 1,
                            "origin_amount": 1
                          },
                          "easyship_rating": 2,
                          "estimated_import_duty": 0,
                          "estimated_import_tax": 65.96,
                          "fuel_surcharge": 14,
                          "full_description": "Courier 1 (19-39 working days) Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "import_duty_charge": 0,
                          "import_duty_details": null,
                          "import_tax_charge": 0,
                          "import_tax_non_chargeable": 0,
                          "incoterms": "DDU",
                          "insurance_fee": 0,
                          "is_above_duty_threshold": null,
                          "is_above_threshold": true,
                          "max_delivery_time": 39,
                          "min_delivery_time": 19,
                          "minimum_pickup_fee": 0,
                          "other_surcharges": {
                            "details": [
                              {
                                "fee": 1,
                                "name": "Surcharge Name",
                                "origin_fee": 1
                              }
                            ],
                            "total_fee": 2
                          },
                          "oversized_surcharge": 0,
                          "payment_recipient": "Easyship",
                          "provincial_sales_tax": 0,
                          "rates_in_origin_currency": {
                            "additional_services_surcharge": 0,
                            "currency": "HKD",
                            "ddp_handling_fee": 0,
                            "estimated_import_duty": 0,
                            "estimated_import_tax": 65.96,
                            "fuel_surcharge": 14,
                            "import_duty_charge": 0,
                            "import_tax_charge": 0,
                            "import_tax_non_chargeable": 0,
                            "insurance_fee": 0,
                            "minimum_pickup_fee": 0,
                            "oversized_surcharge": 0,
                            "provincial_sales_tax": 0,
                            "remote_area_surcharge": 2,
                            "residential_discounted_fee": 0,
                            "residential_full_fee": 0,
                            "sales_tax": 0,
                            "shipment_charge": 140,
                            "shipment_charge_total": 158,
                            "total_charge": 158,
                            "warehouse_handling_fee": 0
                          },
                          "remote_area_surcharge": 2,
                          "remote_area_surcharges": {
                            "destination": {
                              "name": "Destination Surcharge Name",
                              "base": 1
                            },
                            "origin": {
                              "name": "Origin Surcharge Name",
                              "base": 1
                            }
                          },
                          "residential_discounted_fee": 0,
                          "residential_full_fee": 0,
                          "sales_tax": 0,
                          "shipment_charge": 140,
                          "shipment_charge_total": 158,
                          "total_charge": 158,
                          "tracking_rating": 2,
                          "value_for_money_rank": 1,
                          "warehouse_handling_fee": 0
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "rates"
                  },
                  "rates_with_duty_breakdown": {
                    "value": {
                      "rates": [
                        {
                          "additional_services_surcharge": 0,
                          "available_handover_options": [],
                          "cost_rank": 1,
                          "courier_remarks": null,
                          "courier_service": {
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "logo": null,
                            "name": "Courier 1",
                            "umbrella_name": "Courier 1"
                          },
                          "currency": "HKD",
                          "ddp_handling_fee": 0,
                          "delivery_time_rank": 2,
                          "description": "Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "discount": {
                            "amount": 1,
                            "origin_amount": 1
                          },
                          "easyship_rating": 2,
                          "estimated_import_duty": 0,
                          "estimated_import_tax": 65.96,
                          "fuel_surcharge": 14,
                          "full_description": "Courier 1 (19-39 working days) Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "import_duty_charge": 0,
                          "import_duty_details": [
                            {
                              "hs_code_provided": "42029100",
                              "hs_code_applied": "4202910010",
                              "subheading": false,
                              "duty_origin_country_id_provided": 234,
                              "duty_origin_country_id_applied": 234,
                              "duty_calculation_method": "CIF",
                              "line_item_shipment_value": 100,
                              "applied_rate_type": "general",
                              "additional_rates": [
                                {
                                  "description": "Additional duty surcharge",
                                  "rate": 0.025,
                                  "amount": 2.5
                                }
                              ],
                              "base_duty_rate": 0.05,
                              "base_duty_amount": 5,
                              "line_item_total_duty": 7.5
                            }
                          ],
                          "import_tax_charge": 0,
                          "import_tax_non_chargeable": 0,
                          "incoterms": "DDU",
                          "insurance_fee": 0,
                          "is_above_duty_threshold": true,
                          "is_above_threshold": true,
                          "max_delivery_time": 39,
                          "min_delivery_time": 19,
                          "minimum_pickup_fee": 0,
                          "other_surcharges": {
                            "details": [
                              {
                                "fee": 1,
                                "name": "Surcharge Name",
                                "origin_fee": 1
                              }
                            ],
                            "total_fee": 2
                          },
                          "oversized_surcharge": 0,
                          "payment_recipient": "Easyship",
                          "provincial_sales_tax": 0,
                          "rates_in_origin_currency": {
                            "additional_services_surcharge": 0,
                            "currency": "HKD",
                            "ddp_handling_fee": 0,
                            "estimated_import_duty": 0,
                            "estimated_import_tax": 65.96,
                            "fuel_surcharge": 14,
                            "import_duty_charge": 0,
                            "import_tax_charge": 0,
                            "import_tax_non_chargeable": 0,
                            "insurance_fee": 0,
                            "minimum_pickup_fee": 0,
                            "oversized_surcharge": 0,
                            "provincial_sales_tax": 0,
                            "remote_area_surcharge": 2,
                            "residential_discounted_fee": 0,
                            "residential_full_fee": 0,
                            "sales_tax": 0,
                            "shipment_charge": 140,
                            "shipment_charge_total": 158,
                            "total_charge": 158,
                            "warehouse_handling_fee": 0
                          },
                          "remote_area_surcharge": 2,
                          "remote_area_surcharges": {
                            "destination": {
                              "name": "Destination Surcharge Name",
                              "base": 1
                            },
                            "origin": {
                              "name": "Origin Surcharge Name",
                              "base": 1
                            }
                          },
                          "residential_discounted_fee": 0,
                          "residential_full_fee": 0,
                          "sales_tax": 0,
                          "shipment_charge": 140,
                          "shipment_charge_total": 158,
                          "total_charge": 158,
                          "tracking_rating": 2,
                          "value_for_money_rank": 1,
                          "warehouse_handling_fee": 0
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "rates with duty breakdown"
                  },
                  "insufficient_subscription_tier": {
                    "value": {
                      "rates": [
                        {
                          "additional_services_surcharge": 0,
                          "available_handover_options": [],
                          "cost_rank": 1,
                          "courier_remarks": null,
                          "courier_service": {
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "logo": null,
                            "name": "Courier 1",
                            "umbrella_name": "Courier 1"
                          },
                          "currency": "HKD",
                          "ddp_handling_fee": null,
                          "delivery_time_rank": 2,
                          "description": "",
                          "discount": {
                            "amount": 1,
                            "origin_amount": 1
                          },
                          "easyship_rating": 2,
                          "estimated_import_duty": null,
                          "estimated_import_tax": null,
                          "fuel_surcharge": 14,
                          "full_description": "Courier 1 (19-39 working days)",
                          "import_duty_charge": null,
                          "import_duty_details": null,
                          "import_tax_charge": null,
                          "import_tax_non_chargeable": null,
                          "incoterms": "DDU",
                          "insurance_fee": 0,
                          "is_above_duty_threshold": null,
                          "is_above_threshold": true,
                          "max_delivery_time": 39,
                          "min_delivery_time": 19,
                          "minimum_pickup_fee": 0,
                          "other_surcharges": {
                            "details": [
                              {
                                "fee": 1,
                                "name": "Surcharge Name",
                                "origin_fee": 1
                              }
                            ],
                            "total_fee": 2
                          },
                          "oversized_surcharge": 0,
                          "payment_recipient": "Easyship",
                          "provincial_sales_tax": 0,
                          "rates_in_origin_currency": {
                            "additional_services_surcharge": 0,
                            "currency": "HKD",
                            "ddp_handling_fee": null,
                            "estimated_import_duty": null,
                            "estimated_import_tax": null,
                            "fuel_surcharge": 14,
                            "import_duty_charge": null,
                            "import_tax_charge": null,
                            "import_tax_non_chargeable": null,
                            "insurance_fee": 0,
                            "minimum_pickup_fee": 0,
                            "oversized_surcharge": 0,
                            "provincial_sales_tax": 0,
                            "remote_area_surcharge": 2,
                            "residential_discounted_fee": 0,
                            "residential_full_fee": 0,
                            "sales_tax": 0,
                            "shipment_charge": 140,
                            "shipment_charge_total": 158,
                            "total_charge": 158,
                            "warehouse_handling_fee": 0
                          },
                          "remote_area_surcharge": 2,
                          "remote_area_surcharges": {
                            "destination": {
                              "name": "Destination Surcharge Name",
                              "base": 1
                            },
                            "origin": {
                              "name": "Origin Surcharge Name",
                              "base": 1
                            }
                          },
                          "residential_discounted_fee": 0,
                          "residential_full_fee": 0,
                          "sales_tax": 0,
                          "shipment_charge": 140,
                          "shipment_charge_total": 158,
                          "total_charge": 158,
                          "tracking_rating": 2,
                          "value_for_money_rank": 1,
                          "warehouse_handling_fee": 0
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "rates without taxes and duties due to insufficient subscription tier"
                  },
                  "includes_courier_logo": {
                    "value": {
                      "rates": [
                        {
                          "additional_services_surcharge": 0,
                          "available_handover_options": [],
                          "cost_rank": 1,
                          "courier_remarks": null,
                          "courier_service": {
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "logo": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/aramex.png",
                            "name": "Courier 1",
                            "umbrella_name": "Courier 1"
                          },
                          "currency": "HKD",
                          "ddp_handling_fee": 0,
                          "delivery_time_rank": 2,
                          "description": "Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "discount": {
                            "amount": 1,
                            "origin_amount": 1
                          },
                          "easyship_rating": 2,
                          "estimated_import_duty": 0,
                          "estimated_import_tax": 65.96,
                          "fuel_surcharge": 14,
                          "full_description": "Courier 1 (19-39 working days) Estimated  65.96 tax & duty due on delivery (Tax handling fees may apply)",
                          "import_duty_charge": 0,
                          "import_duty_details": null,
                          "import_tax_charge": 0,
                          "import_tax_non_chargeable": 0,
                          "incoterms": "DDU",
                          "insurance_fee": 0,
                          "is_above_duty_threshold": null,
                          "is_above_threshold": true,
                          "max_delivery_time": 39,
                          "min_delivery_time": 19,
                          "minimum_pickup_fee": 0,
                          "other_surcharges": {
                            "details": [
                              {
                                "fee": 1,
                                "name": "Surcharge Name",
                                "origin_fee": 1
                              }
                            ],
                            "total_fee": 2
                          },
                          "oversized_surcharge": 0,
                          "payment_recipient": "Easyship",
                          "provincial_sales_tax": 0,
                          "rates_in_origin_currency": {
                            "additional_services_surcharge": 0,
                            "currency": "HKD",
                            "ddp_handling_fee": 0,
                            "estimated_import_duty": 0,
                            "estimated_import_tax": 65.96,
                            "fuel_surcharge": 14,
                            "import_duty_charge": 0,
                            "import_tax_charge": 0,
                            "import_tax_non_chargeable": 0,
                            "insurance_fee": 0,
                            "minimum_pickup_fee": 0,
                            "oversized_surcharge": 0,
                            "provincial_sales_tax": 0,
                            "remote_area_surcharge": 2,
                            "residential_discounted_fee": 0,
                            "residential_full_fee": 0,
                            "sales_tax": 0,
                            "shipment_charge": 140,
                            "shipment_charge_total": 158,
                            "total_charge": 158,
                            "warehouse_handling_fee": 0
                          },
                          "remote_area_surcharge": 2,
                          "remote_area_surcharges": {
                            "destination": {
                              "name": "Destination Surcharge Name",
                              "base": 1
                            },
                            "origin": {
                              "name": "Origin Surcharge Name",
                              "base": 1
                            }
                          },
                          "residential_discounted_fee": 0,
                          "residential_full_fee": 0,
                          "sales_tax": 0,
                          "shipment_charge": 140,
                          "shipment_charge_total": 158,
                          "total_charge": 158,
                          "tracking_rating": 2,
                          "value_for_money_rank": 1,
                          "warehouse_handling_fee": 0
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "rates with show_courier_logo_url enabled"
                  },
                  "excludes_tax_and_duties_fields": {
                    "value": {
                      "rates": [
                        {
                          "additional_services_surcharge": 0,
                          "available_handover_options": [],
                          "cost_rank": 1,
                          "courier_remarks": null,
                          "courier_service": {
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "logo": null,
                            "name": "Courier 1",
                            "umbrella_name": "Courier 1"
                          },
                          "currency": "HKD",
                          "ddp_handling_fee": null,
                          "delivery_time_rank": 2,
                          "description": "",
                          "discount": {
                            "amount": 1,
                            "origin_amount": 1
                          },
                          "easyship_rating": 2,
                          "estimated_import_duty": 0,
                          "estimated_import_tax": 0,
                          "fuel_surcharge": 14,
                          "full_description": "Courier 1 (19-39 working days)",
                          "import_duty_charge": null,
                          "import_duty_details": null,
                          "import_tax_charge": null,
                          "import_tax_non_chargeable": null,
                          "incoterms": "DDU",
                          "insurance_fee": 0,
                          "is_above_duty_threshold": null,
                          "is_above_threshold": false,
                          "max_delivery_time": 39,
                          "min_delivery_time": 19,
                          "minimum_pickup_fee": 0,
                          "other_surcharges": {
                            "details": [
                              {
                                "fee": 1,
                                "name": "Surcharge Name",
                                "origin_fee": 1
                              }
                            ],
                            "total_fee": 2
                          },
                          "oversized_surcharge": 0,
                          "payment_recipient": "Easyship",
                          "provincial_sales_tax": 0,
                          "rates_in_origin_currency": {
                            "additional_services_surcharge": 0,
                            "currency": "HKD",
                            "ddp_handling_fee": null,
                            "estimated_import_duty": 0,
                            "estimated_import_tax": 0,
                            "fuel_surcharge": 14,
                            "import_duty_charge": null,
                            "import_tax_charge": null,
                            "import_tax_non_chargeable": null,
                            "insurance_fee": 0,
                            "minimum_pickup_fee": 0,
                            "oversized_surcharge": 0,
                            "provincial_sales_tax": 0,
                            "remote_area_surcharge": 2,
                            "residential_discounted_fee": 0,
                            "residential_full_fee": 0,
                            "sales_tax": 0,
                            "shipment_charge": 140,
                            "shipment_charge_total": 158,
                            "total_charge": 795.45,
                            "warehouse_handling_fee": 0
                          },
                          "remote_area_surcharge": 2,
                          "remote_area_surcharges": {
                            "destination": {
                              "name": "Destination Surcharge Name",
                              "base": 1
                            },
                            "origin": {
                              "name": "Origin Surcharge Name",
                              "base": 1
                            }
                          },
                          "residential_discounted_fee": 0,
                          "residential_full_fee": 0,
                          "sales_tax": 0,
                          "shipment_charge": 140,
                          "shipment_charge_total": 158,
                          "total_charge": 158,
                          "tracking_rating": 2,
                          "value_for_money_rank": 1,
                          "warehouse_handling_fee": 0
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "rates without taxes and duties when calculate_tax_and_duties is false"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/rate_list"
                }
              }
            }
          },
          "402": {
            "description": "insufficient subscription tier for a specific feature",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "insufficient_subscription",
                        "details": [
                          "The DDP RATES feature is not available for free subscription plan, please contact Easyship"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Subscriptions",
                            "url": "https://developers.easyship.com/reference/subscription"
                          },
                          {
                            "kind": "documentation",
                            "name": "Request Rates",
                            "url": "https://developers.easyship.com/reference/rates_request"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Display Rates at Checkout",
                            "url": "https://developers.easyship.com/docs/how-to-display-rates-at-checkout"
                          }
                        ],
                        "message": "You don't have access to this feature. Please upgrade your plan",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "insufficient subscription tier for a specific feature"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "422": {
            "description": "failed validations",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/RateRequest missing required parameters: destination_address"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "failed validations"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RateRequest"
              },
              "examples": {
                "rates": {
                  "summary": "rates",
                  "value": {
                    "origin_address": {
                      "line_1": "Kennedy Town",
                      "line_2": "Block 3",
                      "state": "Yuen Long",
                      "city": "Hong Kong",
                      "postal_code": "0000",
                      "country_alpha2": "HK",
                      "contact_name": "Foo Bar",
                      "company_name": null,
                      "contact_phone": "1234567890",
                      "contact_email": "asd@asd.com"
                    },
                    "destination_address": {
                      "line_1": "Kennedy Town",
                      "line_2": "Block 3",
                      "state": "Yuen Long",
                      "city": "Hong Kong",
                      "postal_code": "0000",
                      "country_alpha2": "HK",
                      "contact_name": "Foo Bar",
                      "company_name": null,
                      "contact_phone": "1234567890",
                      "contact_email": "asd@asd.com"
                    },
                    "parcels": [
                      {
                        "total_actual_weight": 1,
                        "box": null,
                        "items": [
                          {
                            "description": "item",
                            "category": "fashion",
                            "sku": "sku",
                            "origin_country_alpha2": "HK",
                            "quantity": 2,
                            "dimensions": {
                              "length": 1,
                              "width": 2,
                              "height": 3
                            },
                            "actual_weight": 10,
                            "declared_currency": "USD",
                            "declared_customs_value": 20
                          }
                        ]
                      }
                    ]
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://public-api.easyship.com",
      "description": "Production"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "description": "Bearer Token necessary to use API",
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "token"
      }
    },
    "schemas": {
      "rate_list": {
        "type": "object",
        "description": "List of rates",
        "additionalProperties": false,
        "properties": {
          "rates": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Rate"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
          }
        }
      },
      "CourierService": {
        "type": "object",
        "description": "Courier service",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "ID"
          },
          "name": {
            "type": "string",
            "description": "If the courier service is connected through your own courier account, this will be \"{nickname} - {official_name}\". If the courier service is provided by Easyship, this will be the official name of the courier service."
          },
          "umbrella_name": {
            "type": "string",
            "description": "Human-readable name for the courier company that offers this service."
          },
          "official_name": {
            "type": "string",
            "description": "Official name of the courier service."
          },
          "nickname": {
            "type": "string",
            "description": "Nickname you set when creating/updating the courier service. Only applicable for LYOC services.",
            "nullable": true
          },
          "service_name": {
            "type": "string",
            "description": "Service that offered by the courier company."
          },
          "logo_url": {
            "type": "string",
            "description": "Logo of the courier. Deprecated in favor of `courier_logo_url`.",
            "nullable": true,
            "deprecated": true
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "active": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether the courier is active or not."
          },
          "restricted_to_origin_states": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "List of origin states that the service is available for (US only)."
          },
          "restricted_to_destination_states": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "List of destination states that the service is available for (US only)."
          },
          "supported_incoterms": {
            "description": "Terms of Sale\nDDP: Seller pays all import duties/taxes.\nDDU: Buyer pays all import duties/taxes.\n",
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "DDU",
                "DDP"
              ],
              "default": "DDU"
            }
          },
          "ioss_support": {
            "type": "string",
            "nullable": true,
            "enum": [
              "supported_mandatory",
              "supported_optional",
              "not_supported",
              null
            ]
          },
          "customer_reference_id": {
            "type": "string",
            "nullable": true,
            "description": "An identifier for the customer who owns the account. Available only for selected customers."
          },
          "accepts_outbounds": {
            "deprecated": true,
            "type": "boolean",
            "description": "Whether the courier can be used to generate outbound labels."
          },
          "accepts_prepaid_returns": {
            "deprecated": true,
            "type": "boolean",
            "description": "Returns `true` if returns are billed upon label generation."
          },
          "accepts_pay_on_scan_returns": {
            "deprecated": true,
            "type": "boolean",
            "description": "Returns `true` if returns are billed upon label scan."
          },
          "domestic": {
            "type": "boolean",
            "description": "Returns `true` if the courier service is a domestic service. Both `domestic` and `international` can be `true` at the same time."
          },
          "international": {
            "type": "boolean",
            "description": "Returns `true` if the courier service is an international service. Both `domestic` and `international` can be `true` at the same time."
          },
          "courier_id": {
            "type": "string",
            "format": "uuid",
            "description": "The Courier ID is associated with this service."
          },
          "courier_logo_url": {
            "type": "string",
            "description": "The URL of the Courier logo."
          },
          "easyship_courier_service": {
            "type": "boolean",
            "description": "Whether the Courier Service belongs to Easyship or not."
          },
          "accepts": {
            "type": "object",
            "description": "Acceptance criteria for the courier.",
            "properties": {
              "outbounds": {
                "type": "boolean",
                "description": "Whether the courier can be used to generate outbound labels."
              },
              "prepaid_returns": {
                "type": "boolean",
                "description": "Returns `true` if returns are billed upon label generation."
              },
              "pay_on_scan_returns": {
                "type": "boolean",
                "description": "Returns `true` if returns are billed upon label scan."
              },
              "pi965_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi965)."
              },
              "pi966_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi966)."
              },
              "pi967_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi967)."
              },
              "liquids": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts liquids."
              },
              "specific_dangerous_goods": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts other dangerous goods that are not batteries (pi966, pi967, or pi968)."
              },
              "documents": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts documents."
              },
              "parcels": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts parcels."
              }
            }
          },
          "available_handover_options": {
            "type": "array",
            "description": "A list of one or more of `dropoff`, `free_pickup`, and `paid_pickup`",
            "items": {
              "type": "string",
              "enum": [
                "dropoff",
                "free_pickup",
                "paid_pickup"
              ]
            }
          },
          "tracking_rating": {
            "type": "number",
            "description": "Quality of tracking information provided by the courier\n\n-1: No tracking number\n0: Limited\n1: Basic\n2: Regular\n3: Excellent\n",
            "enum": [
              -1,
              0,
              1,
              2,
              3
            ]
          }
        }
      },
      "Error": {
        "type": "object",
        "description": "Error",
        "additionalProperties": false,
        "properties": {
          "error": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "code": {
                "type": "string",
                "description": "A short code that represents the error."
              },
              "type": {
                "type": "string",
                "description": "The type of error returned.",
                "enum": [
                  "invalid_request_error",
                  "api_error"
                ]
              },
              "message": {
                "type": "string",
                "description": "A human-readable message providing brief information about the error."
              },
              "links": {
                "type": "array",
                "description": "Link(s) to Easyship developer resources",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "Name of Easyship documentation"
                    },
                    "url": {
                      "type": "string",
                      "format": "uri",
                      "description": "URL to Easyship documentation"
                    },
                    "kind": {
                      "type": "string",
                      "description": "The kind of easyship documentation"
                    }
                  }
                }
              },
              "details": {
                "type": "array",
                "description": "An array of human-readable messages providing detailed information about the error.",
                "nullable": true,
                "items": {
                  "type": "string"
                }
              },
              "request_id": {
                "type": "string",
                "description": "An unique ID represent the request."
              }
            }
          }
        }
      },
      "Pagination": {
        "type": "object",
        "description": "Pagination",
        "additionalProperties": false,
        "properties": {
          "next": {
            "type": "integer",
            "nullable": true
          },
          "count": {
            "type": "integer",
            "description": "The total number of items. The `null` value is used with countless pagination (used for faster response on large datasets, like shipments).",
            "nullable": true
          },
          "page": {
            "type": "integer",
            "description": "Current page"
          }
        }
      },
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
          }
        }
      },
      "MetaWithPagination": {
        "allOf": [
          {
            "type": "object",
            "properties": {
              "pagination": {
                "$ref": "#/components/schemas/Pagination"
              }
            }
          },
          {
            "$ref": "#/components/schemas/Meta"
          }
        ]
      },
      "Address": {
        "type": "object",
        "properties": {
          "line_1": {
            "type": "string",
            "description": "First line of the street address",
            "maximum": 35
          },
          "line_2": {
            "type": "string",
            "nullable": true,
            "description": "Second line of the street address",
            "maximum": 35
          },
          "state": {
            "type": "string",
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names.",
            "maximum": 200
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "nullable": true,
            "description": "Postal code. Leave it null or 0 if the country does not have postal codes. Mandatory for these countries: AD, AF, AI, AL, AM, AQ, AR, AS, AT, AU, AX, AZ, BA, BB, BD, BE, BG, BL, BM, BN, BQ, BR, BT, BV, BY, CA, CC, CH, CL, CN, CO, CR, CU, CV, CX, CY, CZ, DE, DK, DO, DZ, EC, EE, EG, EH, ES, ET, FI, FK, FM, FO, FR, GA, GB, GE, GF, GG, GI, GL, GP, GR, GS, GT, GU, GW, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JO, JP, KG, KH, KR, KW, KY, KZ, LA, LB, LI, LK, LR, LS, LT, LU, LV, MA, MC, MD, ME, MF, MG, MH, MK, MM, MN, MP, MQ, MT, MV, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NZ, OM, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, RE, RO, RS, RU, SD, SE, SG, SH, SI, SJ, SK, SM, SN, SS, SV, SX, SZ, TC, TD, TH, TJ, TM, TN, TR, TW, UA, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, WF, WS, YT, ZA, ZM."
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 27
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 22
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20,
            "nullable": true
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name\"",
            "maximum": 50
          }
        }
      },
      "DestinationAddress": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "line_1": {
            "type": "string",
            "description": "First line of the street address",
            "maximum": 35
          },
          "line_2": {
            "type": "string",
            "nullable": true,
            "description": "Second line of the street address",
            "maximum": 35
          },
          "state": {
            "type": "string",
            "nullable": true,
            "maximum": 200,
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names."
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "description": "Postal code. Mandatory for most countries (if not applicable, for example Hong Kong, leave null or 0)"
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 50
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 50
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name`",
            "maximum": 50
          },
          "delivery_instructions": {
            "type": "string",
            "description": "Delivery instructions for the address, see [Delivery Instructions](https://developers.easyship.com/page/delivery-instructions).",
            "maximum": 200,
            "nullable": true
          }
        }
      },
      "CountryAlpha2": {
        "type": "string",
        "description": "Country Code in Alpha-2 format (ISO 3166-1)",
        "enum": [
          "AD",
          "AE",
          "AF",
          "AG",
          "AI",
          "AL",
          "AM",
          "AN",
          "AO",
          "AQ",
          "AR",
          "AS",
          "AT",
          "AU",
          "AW",
          "AX",
          "AZ",
          "BA",
          "BB",
          "BD",
          "BE",
          "BF",
          "BG",
          "BH",
          "BI",
          "BJ",
          "BL",
          "BM",
          "BN",
          "BO",
          "BQ",
          "BR",
          "BS",
          "BT",
          "BV",
          "BW",
          "BY",
          "BZ",
          "CA",
          "CC",
          "CD",
          "CF",
          "CG",
          "CH",
          "CI",
          "CK",
          "CL",
          "CM",
          "CN",
          "CO",
          "CR",
          "CU",
          "CV",
          "CW",
          "CX",
          "CY",
          "CZ",
          "DE",
          "DJ",
          "DK",
          "DM",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "EH",
          "ER",
          "ES",
          "ET",
          "FI",
          "FJ",
          "FK",
          "FM",
          "FO",
          "FR",
          "GA",
          "GB",
          "GD",
          "GE",
          "GF",
          "GG",
          "GH",
          "GI",
          "GL",
          "GM",
          "GN",
          "GP",
          "GQ",
          "GR",
          "GS",
          "GT",
          "GU",
          "GW",
          "GY",
          "HK",
          "HM",
          "HN",
          "HR",
          "HT",
          "HU",
          "ID",
          "IE",
          "IL",
          "IM",
          "IN",
          "IO",
          "IQ",
          "IR",
          "IS",
          "IT",
          "JE",
          "JM",
          "JO",
          "JP",
          "KE",
          "KG",
          "KH",
          "KI",
          "KM",
          "KN",
          "KP",
          "KR",
          "KW",
          "KY",
          "KZ",
          "LA",
          "LB",
          "LC",
          "LI",
          "LK",
          "LR",
          "LS",
          "LT",
          "LU",
          "LV",
          "LY",
          "MA",
          "MC",
          "MD",
          "ME",
          "MF",
          "MG",
          "MH",
          "MK",
          "ML",
          "MM",
          "MN",
          "MO",
          "MP",
          "MQ",
          "MR",
          "MS",
          "MT",
          "MU",
          "MV",
          "MW",
          "MX",
          "MY",
          "MZ",
          "NA",
          "NC",
          "NE",
          "NF",
          "NG",
          "NI",
          "NL",
          "NO",
          "NP",
          "NR",
          "NU",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PF",
          "PG",
          "PH",
          "PK",
          "PL",
          "PM",
          "PN",
          "PR",
          "PS",
          "PT",
          "PW",
          "PY",
          "QA",
          "RE",
          "RO",
          "RS",
          "RU",
          "RW",
          "SA",
          "SB",
          "SC",
          "SD",
          "SE",
          "SG",
          "SH",
          "SI",
          "SJ",
          "SK",
          "SL",
          "SM",
          "SN",
          "SO",
          "SR",
          "SS",
          "ST",
          "SV",
          "SX",
          "SY",
          "SZ",
          "TC",
          "TD",
          "TF",
          "TG",
          "TH",
          "TJ",
          "TK",
          "TL",
          "TM",
          "TN",
          "TO",
          "TR",
          "TT",
          "TV",
          "TW",
          "TZ",
          "UA",
          "UG",
          "UM",
          "US",
          "UY",
          "UZ",
          "VA",
          "VC",
          "VE",
          "VG",
          "VI",
          "VN",
          "VU",
          "WF",
          "WS",
          "YE",
          "YT",
          "ZA",
          "ZM",
          "ZW"
        ]
      },
      "CountryAlpha2Nullable": {
        "type": "string",
        "description": "Country Code in Alpha-2 format (ISO 3166-1)",
        "enum": [
          "AD",
          "AE",
          "AF",
          "AG",
          "AI",
          "AL",
          "AM",
          "AN",
          "AO",
          "AQ",
          "AR",
          "AS",
          "AT",
          "AU",
          "AW",
          "AX",
          "AZ",
          "BA",
          "BB",
          "BD",
          "BE",
          "BF",
          "BG",
          "BH",
          "BI",
          "BJ",
          "BL",
          "BM",
          "BN",
          "BO",
          "BQ",
          "BR",
          "BS",
          "BT",
          "BV",
          "BW",
          "BY",
          "BZ",
          "CA",
          "CC",
          "CD",
          "CF",
          "CG",
          "CH",
          "CI",
          "CK",
          "CL",
          "CM",
          "CN",
          "CO",
          "CR",
          "CU",
          "CV",
          "CW",
          "CX",
          "CY",
          "CZ",
          "DE",
          "DJ",
          "DK",
          "DM",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "EH",
          "ER",
          "ES",
          "ET",
          "FI",
          "FJ",
          "FK",
          "FM",
          "FO",
          "FR",
          "GA",
          "GB",
          "GD",
          "GE",
          "GF",
          "GG",
          "GH",
          "GI",
          "GL",
          "GM",
          "GN",
          "GP",
          "GQ",
          "GR",
          "GS",
          "GT",
          "GU",
          "GW",
          "GY",
          "HK",
          "HM",
          "HN",
          "HR",
          "HT",
          "HU",
          "ID",
          "IE",
          "IL",
          "IM",
          "IN",
          "IO",
          "IQ",
          "IR",
          "IS",
          "IT",
          "JE",
          "JM",
          "JO",
          "JP",
          "KE",
          "KG",
          "KH",
          "KI",
          "KM",
          "KN",
          "KP",
          "KR",
          "KW",
          "KY",
          "KZ",
          "LA",
          "LB",
          "LC",
          "LI",
          "LK",
          "LR",
          "LS",
          "LT",
          "LU",
          "LV",
          "LY",
          "MA",
          "MC",
          "MD",
          "ME",
          "MF",
          "MG",
          "MH",
          "MK",
          "ML",
          "MM",
          "MN",
          "MO",
          "MP",
          "MQ",
          "MR",
          "MS",
          "MT",
          "MU",
          "MV",
          "MW",
          "MX",
          "MY",
          "MZ",
          "NA",
          "NC",
          "NE",
          "NF",
          "NG",
          "NI",
          "NL",
          "NO",
          "NP",
          "NR",
          "NU",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PF",
          "PG",
          "PH",
          "PK",
          "PL",
          "PM",
          "PN",
          "PR",
          "PS",
          "PT",
          "PW",
          "PY",
          "QA",
          "RE",
          "RO",
          "RS",
          "RU",
          "RW",
          "SA",
          "SB",
          "SC",
          "SD",
          "SE",
          "SG",
          "SH",
          "SI",
          "SJ",
          "SK",
          "SL",
          "SM",
          "SN",
          "SO",
          "SR",
          "SS",
          "ST",
          "SV",
          "SX",
          "SY",
          "SZ",
          "TC",
          "TD",
          "TF",
          "TG",
          "TH",
          "TJ",
          "TK",
          "TL",
          "TM",
          "TN",
          "TO",
          "TR",
          "TT",
          "TV",
          "TW",
          "TZ",
          "UA",
          "UG",
          "UM",
          "US",
          "UY",
          "UZ",
          "VA",
          "VC",
          "VE",
          "VG",
          "VI",
          "VN",
          "VU",
          "WF",
          "WS",
          "YE",
          "YT",
          "ZA",
          "ZM",
          "ZW",
          null
        ],
        "nullable": true
      },
      "Currency": {
        "type": "string",
        "nullable": false,
        "enum": [
          "AED",
          "AFN",
          "ALL",
          "AMD",
          "ANG",
          "AOA",
          "ARS",
          "AUD",
          "AWG",
          "AZN",
          "BAM",
          "BBD",
          "BDT",
          "BGN",
          "BHD",
          "BIF",
          "BMD",
          "BND",
          "BOB",
          "BRL",
          "BSD",
          "BTN",
          "BWP",
          "BYR",
          "BZD",
          "CAD",
          "CDF",
          "CHF",
          "CLF",
          "CLP",
          "CNY",
          "COP",
          "CRC",
          "CUC",
          "CUP",
          "CVE",
          "CZK",
          "DJF",
          "DKK",
          "DOP",
          "DZD",
          "EGP",
          "ERN",
          "ETB",
          "EUR",
          "FJD",
          "FKP",
          "GBP",
          "GEL",
          "GHS",
          "GIP",
          "GMD",
          "GNF",
          "GTQ",
          "GYD",
          "HKD",
          "HNL",
          "HRK",
          "HTG",
          "HUF",
          "IDR",
          "ILS",
          "INR",
          "IQD",
          "IRR",
          "ISK",
          "JMD",
          "JOD",
          "JPY",
          "KES",
          "KGS",
          "KHR",
          "KMF",
          "KPW",
          "KRW",
          "KWD",
          "KYD",
          "KZT",
          "LAK",
          "LBP",
          "LKR",
          "LRD",
          "LSL",
          "LTL",
          "LVL",
          "LYD",
          "MAD",
          "MDL",
          "MGA",
          "MKD",
          "MMK",
          "MNT",
          "MOP",
          "MRO",
          "MUR",
          "MVR",
          "MWK",
          "MXN",
          "MYR",
          "MZN",
          "NAD",
          "NGN",
          "NIO",
          "NOK",
          "NPR",
          "NZD",
          "OMR",
          "PAB",
          "PEN",
          "PGK",
          "PHP",
          "PKR",
          "PLN",
          "PYG",
          "QAR",
          "RON",
          "RSD",
          "RUB",
          "RWF",
          "SAR",
          "SBD",
          "SCR",
          "SDG",
          "SEK",
          "SGD",
          "SHP",
          "SKK",
          "SLL",
          "SOS",
          "SRD",
          "SSP",
          "STD",
          "SVC",
          "SYP",
          "SZL",
          "THB",
          "TJS",
          "TMT",
          "TND",
          "TOP",
          "TRY",
          "TTD",
          "TWD",
          "TZS",
          "UAH",
          "UGX",
          "USD",
          "UYU",
          "UZS",
          "VES",
          "VND",
          "VUV",
          "WST",
          "XAF",
          "XAG",
          "XAU",
          "XCD",
          "XDR",
          "XOF",
          "XPF",
          "YER",
          "ZAR",
          "ZMW",
          "BTC",
          "JEP",
          "EEK",
          "GHC",
          "MTL",
          "TMM",
          "YEN",
          "ZWD",
          "ZWL",
          "ZWN",
          "ZWR"
        ],
        "example": "USD",
        "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)"
      },
      "ParcelItem": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of the item"
          },
          "description": {
            "type": "string",
            "description": "Description of the item",
            "maximum": 200
          },
          "category": {
            "type": "string",
            "nullable": true,
            "description": "Item Category slug. Use the Item Categories API to retrieve a list of available item categories or use HS Code field.",
            "maximum": 200
          },
          "sku": {
            "type": "string",
            "description": "Item Stock Keeping Unit (SKU) as listed in your store.",
            "maximum": 100,
            "nullable": true
          },
          "platform_product_id": {
            "type": "string",
            "nullable": true,
            "description": "Platform Product ID (PPID). Unique identifier from your store platform (e.g. Shopify variant ID, WooCommerce product ID). Used to link shipment items to product catalog entries for auto-population of product attributes."
          },
          "manufacturer_part_number": {
            "type": "string",
            "nullable": true,
            "description": "Manufacturer Part Number (MPN). The manufacturer's internal code or part number for the product. Useful for wholesale and B2B operations to identify products by their source."
          },
          "global_trade_item_number": {
            "type": "string",
            "nullable": true,
            "description": "Global Trade Item Number (GTIN). Internationally recognized unique identifier for trade items, including UPC (US/Canada), EAN (Europe), JAN (Japan), and ISBN (books). Used by retailers and carriers for product identification and inventory tracking."
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item",
            "nullable": true
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2Nullable"
          },
          "contains_battery_pi966": {
            "type": "boolean",
            "description": "Whether the item contains a PI966 battery (applicable when HS code is used).",
            "nullable": true
          },
          "contains_battery_pi967": {
            "type": "boolean",
            "description": "Whether the item contains a PI967 battery (applicable when HS code is used).",
            "nullable": true
          },
          "contains_liquids": {
            "type": "boolean",
            "description": "Whether the item contains liquids (applicable when HS code is used).",
            "nullable": true
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          },
          "dimensions": {
            "type": "object",
            "description": "Dimensions of the item",
            "additionalProperties": false,
            "properties": {
              "length": {
                "type": "number",
                "description": "Item length; Optional if the Box dimensions are provided."
              },
              "width": {
                "type": "number",
                "description": "Item width; Optional if the Box dimensions are provided."
              },
              "height": {
                "type": "number",
                "description": "Item height; Optional if the Box dimensions are provided."
              }
            }
          },
          "actual_weight": {
            "type": "number",
            "description": "Item actual weight in `kg`, must be greater than 0; Optional if `total_actual_weight` is provided."
          },
          "origin_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Item customs value currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "origin_customs_value": {
            "type": "number",
            "description": "Customs value of the item"
          },
          "declared_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Currency of the item. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "declared_customs_value": {
            "type": "number",
            "description": "Item customs value, must be greater than 0 unless category is `documents`. Please note that this value refers to the unit rather than the total."
          }
        }
      },
      "ParcelReturnItemCreate": {
        "type": "object",
        "description": "Return Item (only available for return shipments)",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Item ID (from the shipment that is being returned)"
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          }
        }
      },
      "Rate": {
        "type": "object",
        "description": "Result of a quote request, including shipping & tax costs for a specific courier service.",
        "additionalProperties": false,
        "properties": {
          "courier_service": {
            "$ref": "#/components/schemas/RateCourierService"
          },
          "min_delivery_time": {
            "type": "integer",
            "description": "The fastest estimate of delivery time for this courier service, in days."
          },
          "max_delivery_time": {
            "type": "integer",
            "description": "The slowest estimate of delivery time for this courier service, in days."
          },
          "value_for_money_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options. 1 indicates the best value for money."
          },
          "delivery_time_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options, in minimum delivery time estimate; 1 indicates the fastest option."
          },
          "cost_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options, in total price; 1 indicates the best value for money."
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "shipment_charge": {
            "type": "number",
            "description": "Base cost of the courier service"
          },
          "fuel_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when fuel costs are high"
          },
          "remote_area_surcharge": {
            "type": "number",
            "description": "Sum of the origin and destination base fees listed in `remote_area_surcharges`"
          },
          "remote_area_surcharges": {
            "description": "Origin and destination remote area surcharges",
            "type": "object",
            "additionalProperties": false,
            "nullable": true,
            "properties": {
              "origin": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "name": {
                    "type": "string",
                    "example": "Pickup Area Surcharge"
                  },
                  "base": {
                    "type": "number"
                  }
                }
              },
              "destination": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "name": {
                    "type": "string",
                    "example": "Delivery Area Surcharge"
                  },
                  "base": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "other_surcharges": {
            "type": "object",
            "nullable": true,
            "description": "Other surcharges",
            "additionalProperties": false,
            "properties": {
              "total_fee": {
                "type": "number",
                "description": "Sum of the surcharge fees, in the currency specified for the shipment"
              },
              "details": {
                "type": "array",
                "description": "An array of individual surcharges being applied",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "Surcharge name, in English, to be displayed to user",
                      "example": "Peak Surcharge"
                    },
                    "fee": {
                      "type": "number",
                      "description": "Surcharge fee in the currency of the shipment"
                    },
                    "origin_fee": {
                      "type": "number",
                      "description": "Surcharge fee in the currency of the shipment's origin country"
                    }
                  }
                }
              }
            }
          },
          "oversized_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when parcels exceed a specified threshold size or weight"
          },
          "additional_services_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when additional services are added (e.g. delivery confirmation)"
          },
          "residential_full_fee": {
            "type": "number",
            "description": "A fee added by the courier when the receiver is at a residential address"
          },
          "residential_discounted_fee": {
            "type": "number",
            "description": "A discounted fee added by the courier when the receiver is at a residential address"
          },
          "shipment_charge_total": {
            "type": "number",
            "description": "Subtotal of `shipment_charge`, `fuel_surcharge`, `residential_*_fee`, `remote_area_surcharge`, `additional_services_surcharge`, & `oversized_surcharge`"
          },
          "warehouse_handling_fee": {
            "type": "number",
            "description": "A fee added by the fulfillment service for managing warehouse operations"
          },
          "insurance_fee": {
            "type": "number",
            "description": "The cost of the insurance policy purchased for this shipment"
          },
          "sales_tax": {
            "type": "number",
            "description": "National government taxes, calculated as a portion of the purchase price"
          },
          "provincial_sales_tax": {
            "type": "number",
            "description": "State, province, or local government taxes, calculated as a portion of the purchase price"
          },
          "ddp_handling_fee": {
            "type": "number",
            "description": "A fee added by the courier when they pay import taxes and duties on the sender's behalf. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_tax_charge": {
            "type": "number",
            "description": "Import tax charge. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_tax_non_chargeable": {
            "type": "number",
            "description": "Import tax non-chargeable. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_duty_charge": {
            "type": "number",
            "description": "Import duty amount collected upfront with the shipment (DDP only). `0` for DDU shipments where the buyer pays duty at customs. Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false.",
            "nullable": true
          },
          "total_charge": {
            "type": "number",
            "description": "The sum of shipping_charge and all applicable fees for this shipment"
          },
          "is_above_threshold": {
            "type": "boolean",
            "nullable": true,
            "description": "True if the purchase price exceeds the threshold set by the import country for customs charges. If `false`, `import_tax_charge`, `import_duty_charge`, `estimated_import_tax`, and `estimated_import_duty` should be zero."
          },
          "is_above_duty_threshold": {
            "type": "boolean",
            "nullable": true,
            "description": "True if the shipment value exceeds the import country's de minimis threshold for duty. Distinct from `is_above_threshold`, which covers the combined tax and duty threshold. May be `true` while `import_duty_charge` is `0` on DDU rates. Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false."
          },
          "import_duty_details": {
            "type": "array",
            "nullable": true,
            "description": "Per line-item duty calculation breakdown in the rate's `currency`, including HS codes used, fallback flags, rates applied, and amounts. On DDU rates, amounts align with `estimated_import_duty`. On DDP rates, amounts align with `import_duty_charge`. Present when a duty calculation was performed, including when the duty amount is zero (e.g. FTA preferential rate). Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false. Only returned on the top-level rate object, not within `rates_in_origin_currency`.",
            "items": {
              "$ref": "#/components/schemas/ImportDutyDetails"
            }
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "estimated_import_tax": {
            "type": "number",
            "description": "An estimate of import taxes that will be charged to the buyer when the shipment clears customs (only applicable for DDU incoterms). Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "estimated_import_duty": {
            "type": "number",
            "description": "An estimate of import duty that will be charged to the buyer when the shipment clears customs (only applicable for DDU incoterms). Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "minimum_pickup_fee": {
            "type": "number",
            "minimum": 0,
            "description": "The minimum fee applied for `paid_pickup` options, for this courier service"
          },
          "available_handover_options": {
            "type": "array",
            "description": "A list of one or more of `dropoff`, `free_pickup`, and `paid_pickup`",
            "items": {
              "type": "string"
            }
          },
          "tracking_rating": {
            "type": "number",
            "description": "A characterization of the level of detail provided by the courier's tracking data.\n  * -1 - No tracking number\n  * 0 - Infrequent tracking events\n  * 1 - Infrequent tracking events\n  * 2 - Tracking main milestones with delivery confirmation\n  * 3 - Tracking all steps of transit with delivery confirmation\n",
            "minimum": -1,
            "maximum": 3
          },
          "easyship_rating": {
            "type": "number",
            "minimum": 0,
            "maximum": 5,
            "description": "Average of customer ratings of this courier service; provided by Easyship users and their buyers."
          },
          "courier_remarks": {
            "type": "string",
            "nullable": true,
            "description": "Additional details relevant to choosing the appropriate courier service"
          },
          "payment_recipient": {
            "type": "string",
            "description": "Who collects payment for this shipment (and when)",
            "enum": [
              "Easyship",
              "EasyshipPayOnScan",
              "Courier"
            ]
          },
          "discount": {
            "$ref": "#/components/schemas/RateDiscount"
          },
          "rates_in_origin_currency": {
            "type": "object",
            "description": "Rates in origin currency",
            "additionalProperties": false,
            "properties": {
              "currency": {
                "$ref": "#/components/schemas/Currency"
              },
              "shipment_charge": {
                "$ref": "#/components/schemas/Rate/properties/shipment_charge"
              },
              "fuel_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/fuel_surcharge"
              },
              "remote_area_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/remote_area_surcharge"
              },
              "additional_services_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/additional_services_surcharge"
              },
              "oversized_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/oversized_surcharge"
              },
              "shipment_charge_total": {
                "$ref": "#/components/schemas/Rate/properties/shipment_charge_total"
              },
              "warehouse_handling_fee": {
                "$ref": "#/components/schemas/Rate/properties/warehouse_handling_fee"
              },
              "insurance_fee": {
                "$ref": "#/components/schemas/Rate/properties/insurance_fee"
              },
              "ddp_handling_fee": {
                "$ref": "#/components/schemas/Rate/properties/ddp_handling_fee"
              },
              "import_tax_charge": {
                "$ref": "#/components/schemas/Rate/properties/import_tax_charge"
              },
              "import_tax_non_chargeable": {
                "$ref": "#/components/schemas/Rate/properties/import_tax_non_chargeable"
              },
              "import_duty_charge": {
                "$ref": "#/components/schemas/Rate/properties/import_duty_charge"
              },
              "residential_discounted_fee": {
                "$ref": "#/components/schemas/Rate/properties/residential_discounted_fee"
              },
              "residential_full_fee": {
                "$ref": "#/components/schemas/Rate/properties/residential_full_fee"
              },
              "total_charge": {
                "$ref": "#/components/schemas/Rate/properties/total_charge"
              },
              "estimated_import_tax": {
                "$ref": "#/components/schemas/Rate/properties/estimated_import_tax"
              },
              "estimated_import_duty": {
                "$ref": "#/components/schemas/Rate/properties/estimated_import_duty"
              },
              "sales_tax": {
                "$ref": "#/components/schemas/Rate/properties/sales_tax"
              },
              "provincial_sales_tax": {
                "$ref": "#/components/schemas/Rate/properties/provincial_sales_tax"
              },
              "minimum_pickup_fee": {
                "$ref": "#/components/schemas/Rate/properties/minimum_pickup_fee"
              }
            }
          },
          "description": {
            "type": "string",
            "description": "Details that the user should know when preparing to hand over the shipment to the courier (e.g. pick-up or drop-off)"
          },
          "full_description": {
            "type": "string",
            "description": "Full description"
          }
        }
      },
      "RateDiscount": {
        "type": "object",
        "description": "A discount applied to the rate. Amount and percentage should not both be defined at the same time",
        "nullable": true,
        "additionalProperties": false,
        "properties": {
          "amount": {
            "type": "number",
            "description": "A fixed amount to discount from the price"
          },
          "origin_amount": {
            "type": "number",
            "description": "Discount origin amount"
          }
        }
      },
      "RateCourierService": {
        "type": "object",
        "description": "Courier Service for Rate",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "unique identifier for a courier service"
          },
          "name": {
            "type": "string",
            "description": "Human-readable name for the courier service used in this rate."
          },
          "courier_id": {
            "type": "string",
            "format": "uuid",
            "description": "The courier ID that the current courier service is associated with"
          },
          "umbrella_name": {
            "type": "string",
            "description": "Human-readable name for the courier company that offers this service."
          },
          "logo": {
            "$ref": "#/components/schemas/CourierService/properties/logo_url"
          },
          "easyship_courier_service": {
            "type": "boolean",
            "description": "Whether the Courier Service belongs to Easyship or not.",
            "nullable": true
          }
        }
      },
      "Shipment": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "type": "string",
            "pattern": "^ES\\w{2}\\d{7,}$",
            "description": "Readable identifier prefixed with ES (Easyship) and destination country code"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was created in the Easyship system"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was most recently modified"
          },
          "label_paid_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When Easyship was paid for the shipment"
          },
          "label_generated_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When label was generated"
          },
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin address"
              }
            ]
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender address"
              }
            ]
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return address"
              }
            ]
          },
          "destination_address": {
            "$ref": "#/components/schemas/DestinationAddress"
          },
          "order_data": {
            "type": "object",
            "description": "Free-form data related to the eCommerce platform",
            "additionalProperties": false,
            "properties": {
              "platform_name": {
                "type": "string",
                "nullable": true,
                "description": "A display-ready sales channel or platform name",
                "maximum": 200
              },
              "platform_order_number": {
                "type": "string",
                "nullable": true,
                "description": "Order number that was either copied from an order synced from an ecommerce platform or manually edited in Easyship's order from",
                "maximum": 200
              },
              "order_created_at": {
                "type": "string",
                "nullable": true,
                "format": "date-time",
                "description": "When the order was created (e.g. in an online store connected to Easyship)"
              },
              "order_tag_list": {
                "type": "array",
                "description": "Tags that have been assigned to this shipment, either as an order on its e-commerce store or within the Easyship app",
                "items": {
                  "type": "string"
                },
                "maxItems": 500
              },
              "seller_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the merchant. Will not be shown to the receiver."
              },
              "buyer_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the buyer during order checkout. Will be displayed on the packing slip."
              },
              "buyer_selected_courier_name": {
                "type": "string",
                "nullable": true,
                "description": "Courier name for shipping rule condition `match_buyer_selected_courier_name`. If the name matches, actions of this shipping rule would apply to the current shipment."
              }
            }
          },
          "last_failure_http_response_messages": {
            "type": "array",
            "description": "This attribute stores the HTTP response of the most recent unsuccessful attempt to interact with an external service, such as a failed label creation.",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "code": {
                  "type": "string",
                  "nullable": true
                },
                "content": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          },
          "metadata": {
            "type": "object",
            "description": "Set of key-value pairs that you can attach to a shipment. This can be useful for storing additional information about the object in a structured format"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "Indicates whether or not the user believes the receiver address qualifies for a residential surcharge."
          },
          "consignee_tax_id": {
            "type": "string",
            "nullable": true,
            "description": "Tax ID for the receiver. Maybe helpful or required for customs clearance, depending on the destination country."
          },
          "eei_reference": {
            "type": "string",
            "nullable": true,
            "description": "References data (Electronic Export Information) filed through one of the systems for goods shipped from the U.S.\nto a foreign country. Currently only used for FedEx shipments. The following possibilities may or may not qualify:\n  * An Automated Export System (AES) citation\n  * A Foreign Trade Regulations (FTR) exemption number\n  * An International Traffic in Arms Reduction (ITAR) exemption code\n  * A US Department of Commerce export license number"
          },
          "regulatory_identifiers": {
            "type": "object",
            "description": "Seller's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "eori": {
                "type": "string",
                "nullable": true,
                "description": "Economic Operators Registration and Identification (EORI) number."
              },
              "ioss": {
                "type": "string",
                "nullable": true,
                "description": "Import One Stop Shop (IOSS) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              }
            }
          },
          "buyer_regulatory_identifiers": {
            "type": "object",
            "description": "Buyer's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "ein": {
                "type": "string",
                "nullable": true,
                "description": "Employer Identification Number (EIN) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              },
              "ssn": {
                "type": "string",
                "nullable": true,
                "description": "Social Security Number (SSN) number."
              }
            }
          },
          "return": {
            "type": "boolean",
            "description": "Whether the shipment is a return shipment or not"
          },
          "incoterms": {
            "description": "Terms of Sale\nDDP: Seller pays all import duties/taxes.\nDDU: Buyer pays all import duties/taxes.\nnull: No incoterm specified; defaults to DDU.\n",
            "type": "string",
            "enum": [
              "DDU",
              "DDP",
              null
            ],
            "default": "DDU",
            "nullable": true
          },
          "insurance": {
            "type": "object",
            "description": "Insurance",
            "nullable": true,
            "additionalProperties": false,
            "properties": {
              "is_insured": {
                "type": "boolean",
                "description": "Indicates if premium insurance has been purchased for this shipment (either by the merchant or buyer).\nBasic, courier-supplied coverage is not applicable.",
                "default": false
              },
              "insured_amount": {
                "type": "number",
                "description": "Amount to insure with Easyship's insurance provider. If not specified, we'll use the sum of customs values and shipping cost."
              },
              "insured_currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "Insurance currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). If not specified, we will use the currency of the account country."
                  }
                ]
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/Parcel"
            }
          },
          "total_customs_value": {
            "type": "number",
            "minimum": 0,
            "description": "Sum of the value assigned to all shipment line items"
          },
          "total_actual_weight": {
            "type": "number",
            "description": "Sum of the specified weights of all *parcels* in the shipment (`parcel.actual_weight`), as measured on a scale in units specified by `company.weight_unit`."
          },
          "shipment_state": {
            "type": "string",
            "description": "The state of the shipment record within the Easyship system",
            "default": "created",
            "nullable": false,
            "enum": [
              "created",
              "draft",
              "calculating",
              "cancelling",
              "cancelled",
              "discarded",
              "deleted"
            ]
          },
          "pickup_state": {
            "type": "string",
            "default": "not_requested",
            "nullable": false,
            "description": "The state of the hand-over from shipper to courier. `pending_handover` applies only to eFulfillment companies."
          },
          "delivery_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the hand-over from courier to receiver.",
            "enum": [
              "not_created",
              "pending",
              "info_received",
              "in_transit_to_customer",
              "out_for_delivery",
              "delivered",
              "failed_attempt",
              "exception",
              "expired",
              "lost_by_courier",
              "returned_to_shipper"
            ]
          },
          "label_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the label(s) meant to be printed and attached to this shipment's parcels",
            "enum": [
              "not_created",
              "pending",
              "generating",
              "generated",
              "printed",
              "failed",
              "technical_failed",
              "reported",
              "voided",
              "void_failed"
            ]
          },
          "warehouse_state": {
            "type": "string",
            "default": "none",
            "nullable": false,
            "description": "The state of the fulfillment process within the warehouse",
            "enum": [
              "none",
              "pending",
              "created",
              "failed",
              "packed",
              "cancelled",
              "cancelled_no_stock",
              "backorder_no_stock",
              "shipped",
              "returned",
              "awaiting_dispatch"
            ]
          },
          "warehouse_code": {
            "type": "string",
            "description": "Warehouse code (warehouse/eFulfilment only)"
          },
          "original_easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "trackings": {
            "type": "array",
            "description": "Sources of tracking data for this shipment",
            "items": {
              "$ref": "#/components/schemas/ShipmentTracking"
            }
          },
          "tracking_page_url": {
            "type": "string",
            "description": "Tracking page URL"
          },
          "shipping_documents": {
            "type": "array",
            "description": "Shipping documents",
            "items": {
              "$ref": "#/components/schemas/ShipmentDocument"
            }
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "courier_service": {
            "type": "object",
            "nullable": true,
            "description": "Selected courier service for this shipment. May be null if no service has been selected yet, or if the shipment was created without selecting a service.\nMore information about the [courier service](https://developers.easyship.com/reference/courier_services_index)",
            "additionalProperties": false,
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              },
              "name": {
                "type": "string"
              },
              "courier_id": {
                "type": "string",
                "format": "uuid",
                "description": "The courier ID that the current courier service is associated with"
              },
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service."
              },
              "easyship_courier_service": {
                "$ref": "#/components/schemas/CourierService/properties/easyship_courier_service"
              }
            }
          },
          "rates": {
            "type": "array",
            "description": "Array of available courier services for this shipment, along with the rates charged. Courier services are excluded if the shipment's contents or destination do not meet each service's eligibility requirements.",
            "items": {
              "$ref": "#/components/schemas/Rate"
            }
          },
          "shipping_settings": {
            "type": "object",
            "description": "Shipping settings",
            "additionalProperties": false,
            "properties": {
              "b13a_filing": {
                "type": "object",
                "description": "B13A filing (currently available only for FedEx)",
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                  "option": {
                    "type": "string",
                    "enum": [
                      "not_required",
                      "fedex_to_stamp",
                      "filed_electronically",
                      "manually_attached",
                      "summary_reporting"
                    ]
                  },
                  "option_export_compliance_statement": {
                    "type": "string",
                    "nullable": true,
                    "description": "Export compliance statement"
                  },
                  "permit_number": {
                    "type": "string",
                    "nullable": true,
                    "description": "Permit number"
                  }
                }
              },
              "label_customization_fields": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/label_customization_fields"
                  },
                  {
                    "type": "array",
                    "minItems": 0
                  }
                ]
              }
            }
          }
        }
      },
      "ShipmentCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "parcels"
        ],
        "properties": {
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin Address",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "origin_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of origin address. Required if the `origin_address` object is not provided. If provided, the origin address will be ignored."
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender Address. Only applies if the courier allows a different address to be displayed on the label. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "sender_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of sender address. Required if the `sender_address` object is not provided."
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return Address. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "return_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of return address. Required if the `return_address` object is not provided."
          },
          "destination_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DestinationAddress"
              },
              {
                "required": [
                  "line_1",
                  "city",
                  "contact_name",
                  "contact_email",
                  "contact_phone"
                ]
              }
            ]
          },
          "return": {
            "type": "boolean",
            "description": "Set the shipment as a return shipment"
          },
          "metadata": {
            "$ref": "#/components/schemas/Shipment/properties/metadata"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "US addresses will be automatically validated when not specified. If specified, the validation will be bypassed."
          },
          "consignee_tax_id": {
            "type": "string",
            "description": "The consignee's tax identification number or EIN. This is required for customs clearance when shipping to certain countries, such as China and Brazil."
          },
          "eei_reference": {
            "type": "string",
            "description": "The Electronic Export Identifier (EEI). This is required when shipping goods over USD2500 in value (Applies to US-outbound shipments only)."
          },
          "regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/regulatory_identifiers"
          },
          "buyer_regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/buyer_regulatory_identifiers"
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "insurance": {
            "$ref": "#/components/schemas/Shipment/properties/insurance"
          },
          "order_data": {
            "$ref": "#/components/schemas/Shipment/properties/order_data"
          },
          "courier_settings": {
            "type": "object",
            "properties": {
              "courier_service_id": {
                "type": "string",
                "description": "Select a specific courier service to create the shipment with, only the rate for this courier service will be returned. If provided, all other courier service lookup parameters (`courier_umbrella`, `courier_service_name`, `courier_account_number`) will be ignored.",
                "nullable": true
              },
              "courier_umbrella": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The umbrella name of the courier service (e.g., \"FedEx\"). This field is optional; however, if provided, `courier_service_name` and `courier_account_number` must also be included."
              },
              "courier_service_name": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The official name of the courier service (e.g., \"FedEx International Priority®\"). This field is optional; however, if provided, `courier_umbrella` and `courier_account_number` must also be included."
              },
              "courier_account_number": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The account number of the courier account. This field is optional; however, if provided, `courier_umbrella` and `courier_service_name` must also be included."
              },
              "allow_fallback": {
                "type": "boolean",
                "default": false,
                "description": "If `courier_service_id` is provided but the courier can’t be selected, allow the shipment to be created and the next best rate to be selected. Default: `false`. When false and rates for the `courier_service_id` can't be found, an error will be raised and the shipment won’t be created."
              },
              "apply_shipping_rules": {
                "type": "boolean",
                "default": true,
                "description": "Apply any [shipping rules](https://support.easyship.com/hc/en-us/articles/115003580152-Automate-Shipping-Process-Shipping-Rules) created on the Easyship dashboard (Default: `true`)"
              },
              "list_unavailable_services": {
                "type": "boolean",
                "description": "Setting this option will return detailed information with reasons for each courier in the response."
              }
            }
          },
          "shipping_settings": {
            "type": "object",
            "properties": {
              "additional_services": {
                "type": "object",
                "description": "Configuration for additional services",
                "additionalProperties": false,
                "properties": {
                  "delivery_confirmation": {
                    "description": "Currently officially supported only for selected customers. **Subject to change.**",
                    "type": "string",
                    "enum": [
                      "ups_delivery_confirmation_adult_signature_required",
                      "ups_delivery_confirmation_signature_required",
                      "dpd_uk_signature_required",
                      "dpd_uk_proof_of_identity",
                      "dpd_uk_proof_of_age",
                      "dpd_uk_pin_required"
                    ]
                  },
                  "qr_code": {
                    "type": "string",
                    "description": "Generate QR code when generating label. If a courier does not support it, label will be generated without the QR code. Currently officially supported only for USPS courier. When set to `qr_code`, both the QR code and the original label are returned. `qr_code_with_label` is deprecated and no longer supported; if provided, it silently falls back to `qr_code`. Label customization is not available for USPS. **Subject to change.**",
                    "default": "none",
                    "enum": [
                      "qr_code",
                      "qr_code_with_label",
                      "none"
                    ]
                  }
                }
              },
              "units": {
                "$ref": "#/components/schemas/Units"
              },
              "buy_label": {
                "type": "boolean",
                "default": false,
                "description": "Create a shipment and buy the label in a single API call instead of two. Default: `false`."
              },
              "buy_label_synchronous": {
                "type": "boolean",
                "default": false,
                "description": "Generate a label synchronously. Returns a label in the response. Default: `false`."
              },
              "b13a_filing": {
                "$ref": "#/components/schemas/Shipment/properties/shipping_settings/properties/b13a_filing"
              },
              "printing_options": {
                "type": "object",
                "description": "Specify the format and page sizes of the shipping documents. This will only be taken into account if buy_label_synchronous is `true`.",
                "properties": {
                  "format": {
                    "type": "string",
                    "description": "Options: `png`, `pdf`, `url`, `zpl` (Default: `png`)",
                    "default": "png",
                    "enum": [
                      "png",
                      "pdf",
                      "url",
                      "zpl"
                    ]
                  },
                  "label": {
                    "type": "string",
                    "description": "Label page size. Options: `4x6` / `A4` / `A5` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "A5"
                    ]
                  },
                  "commercial_invoice": {
                    "type": "string",
                    "description": "Commercial invoice page size. Options: `4x6` / `A4` (Default: `A4`)",
                    "default": "A4",
                    "enum": [
                      "4x6",
                      "A4"
                    ]
                  },
                  "packing_slip": {
                    "type": "string",
                    "description": "Packing slip page size. Options: `4x6` / `A4` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "none"
                    ]
                  },
                  "remarks": {
                    "type": "string",
                    "maxLength": 70,
                    "description": "Customized commercial invoice remarks for current shipment. It has higher priority than remarks from company settings."
                  }
                }
              },
              "label_customization_fields": {
                "description": "Label customization fields for the shipment. This is only applicable for specific couriers. For detailed explanation, please refer to [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "required": [
                    "value"
                  ],
                  "properties": {
                    "code": {
                      "description": "Courier accepted code, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                      "type": "string"
                    },
                    "value": {
                      "type": "string",
                      "description": "Content to display on the label, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    },
                    "convert_to_barcode": {
                      "description": "Identifying for converting value to barcode, specific application logic applies. See [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    }
                  }
                }
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/ParcelCreate"
            }
          }
        }
      },
      "RateRequest": {
        "type": "object",
        "description": "Rates request body",
        "additionalProperties": false,
        "required": [
          "origin_address",
          "destination_address",
          "parcels"
        ],
        "properties": {
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin Address",
                "required": [
                  "state",
                  "city",
                  "postal_code"
                ]
              }
            ]
          },
          "destination_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DestinationAddress"
              },
              {
                "description": "Destination Address",
                "required": [
                  "line_1",
                  "state",
                  "city",
                  "postal_code",
                  "country_alpha2"
                ]
              }
            ]
          },
          "set_as_residential": {
            "$ref": "#/components/schemas/ShipmentCreate/properties/set_as_residential"
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "insurance": {
            "$ref": "#/components/schemas/Shipment/properties/insurance"
          },
          "return": {
            "$ref": "#/components/schemas/ShipmentCreate/properties/return"
          },
          "courier_settings": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "show_courier_logo_url": {
                "type": "boolean",
                "default": false,
                "description": "Return courier logo URL"
              },
              "apply_shipping_rules": {
                "type": "boolean",
                "default": true,
                "description": "Apply any [shipping rules](https://support.easyship.com/hc/en-us/articles/115003580152-Automate-Shipping-Process-Shipping-Rules) created on the Easyship dashboard (Default: `true`)"
              }
            }
          },
          "shipping_settings": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "units": {
                "$ref": "#/components/schemas/Units"
              },
              "output_currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "Output currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). Default: Origin Country Currency."
                  }
                ]
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ParcelRateCreate"
            }
          },
          "calculate_tax_and_duties": {
            "type": "boolean",
            "default": true,
            "description": "Whether to calculate taxes and duties for international shipments. Must be true when using DDP Incoterms. When set to `true`, the response will include estimated import tax and duty charges. When set to `false`, tax and duty calculations will be skipped."
          },
          "filter_options": {
            "type": "object",
            "description": "Filter response by keywords",
            "properties": {
              "courier_service_name": {
                "type": "string",
                "description": "Filter by courier service name"
              },
              "courier_service_ids": {
                "type": "array",
                "items": {
                  "type": "string",
                  "format": "uuid"
                },
                "description": "Filter by courier service IDs"
              }
            }
          }
        }
      },
      "ParcelItemCreate": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "required": [
          "description",
          "declared_currency",
          "declared_customs_value"
        ],
        "properties": {
          "description": {
            "type": "string",
            "description": "Description of the item",
            "maximum": 200
          },
          "category": {
            "type": "string",
            "nullable": true,
            "description": "Item category name or slug. Required if hs_code is not provided. Use the [Item Categories API](https://developers.easyship.com/reference/item_categories_index) to retrieve a list of available item categories.",
            "maximum": 200
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item. Required if category is not provided."
          },
          "sku": {
            "type": "string",
            "description": "Item Stock Keeping Unit (SKU) as listed in your store.",
            "maximum": 100
          },
          "platform_product_id": {
            "$ref": "#/components/schemas/ParcelItem/properties/platform_product_id"
          },
          "manufacturer_part_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/manufacturer_part_number"
          },
          "global_trade_item_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/global_trade_item_number"
          },
          "contains_battery_pi966": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi966"
          },
          "contains_battery_pi967": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi967"
          },
          "contains_liquids": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_liquids"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2Nullable"
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          },
          "dimensions": {
            "type": "object",
            "description": "Dimensions of the item",
            "additionalProperties": false,
            "properties": {
              "length": {
                "type": "number",
                "description": "Item length; Optional if the Box dimensions are provided."
              },
              "width": {
                "type": "number",
                "description": "Item width; Optional if the Box dimensions are provided."
              },
              "height": {
                "type": "number",
                "description": "Item height; Optional if the Box dimensions are provided."
              }
            }
          },
          "actual_weight": {
            "type": "number",
            "description": "Item actual weight in `kg`. Must be greater than 0.\nOptional when `total_actual_weight` is provided.\n**Required when the shipping rule action `split_parcels_by_sku` is enabled, regardless of the existence of `total_actual_weight`**\n"
          },
          "declared_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Item currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "declared_customs_value": {
            "type": "number",
            "description": "Item customs value, must be greater than 0 unless category is `documents`. Please note that this value refers to the unit rather than the total."
          }
        }
      },
      "ParcelRateCreate": {
        "type": "object",
        "description": "Parcel for rate calculation",
        "additionalProperties": false,
        "properties": {
          "total_actual_weight": {
            "type": "number",
            "description": "Total weight of the shipment, including the box weight. If you provide the total weight of the shipment, then the weight for items can be optional."
          },
          "box": {
            "type": "object",
            "nullable": true,
            "description": "The box dimensions for the shipment. If the box dimensions are provided, then dimensions for items are optional.",
            "additionalProperties": false,
            "properties": {
              "slug": {
                "type": "string",
                "nullable": true,
                "description": "Courier or Custom Box Slug. Use the [Boxes API](https://developers.easyship.com/reference/boxes_index) to retrieve a list of available boxes."
              },
              "length": {
                "type": "number",
                "description": "Length of the box"
              },
              "width": {
                "type": "number",
                "description": "Width of the box"
              },
              "height": {
                "type": "number",
                "description": "Height of the box"
              }
            }
          },
          "items": {
            "type": "array",
            "description": "Array of all shipment items",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/ParcelItemRateCreate"
                },
                {
                  "$ref": "#/components/schemas/ParcelProductItemCreate"
                },
                {
                  "$ref": "#/components/schemas/ParcelReturnItemCreate"
                }
              ]
            },
            "minItems": 1,
            "maxItems": 200
          }
        }
      },
      "ParcelItemRateCreate": {
        "type": "object",
        "description": "A line item for rate calculation; may be multiple physical objects.",
        "additionalProperties": false,
        "required": [
          "declared_currency",
          "declared_customs_value"
        ],
        "properties": {
          "description": {
            "type": "string",
            "description": "Description of the item.",
            "maximum": 200
          },
          "category": {
            "type": "string",
            "nullable": true,
            "description": "Item category name or slug. Required if hs_code is not provided. Use the [Item Categories API](https://developers.easyship.com/reference/item_categories_index) to retrieve a list of available item categories.",
            "maximum": 200
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item. Required if category is not provided."
          },
          "sku": {
            "type": "string",
            "description": "Item Stock Keeping Unit (SKU) as listed in your store.",
            "maximum": 100
          },
          "platform_product_id": {
            "$ref": "#/components/schemas/ParcelItem/properties/platform_product_id"
          },
          "manufacturer_part_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/manufacturer_part_number"
          },
          "global_trade_item_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/global_trade_item_number"
          },
          "contains_battery_pi966": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi966"
          },
          "contains_battery_pi967": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi967"
          },
          "contains_liquids": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_liquids"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2Nullable"
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          },
          "dimensions": {
            "type": "object",
            "description": "Dimensions of the item",
            "additionalProperties": false,
            "properties": {
              "length": {
                "type": "number",
                "description": "Item length; Optional if the Box dimensions are provided."
              },
              "width": {
                "type": "number",
                "description": "Item width; Optional if the Box dimensions are provided."
              },
              "height": {
                "type": "number",
                "description": "Item height; Optional if the Box dimensions are provided."
              }
            }
          },
          "actual_weight": {
            "type": "number",
            "description": "Item actual weight in `kg`. Must be greater than 0.\nOptional when `total_actual_weight` is provided.\n**Required when the shipping rule action `split_parcels_by_sku` is enabled, regardless of the existence of `total_actual_weight`**\n"
          },
          "declared_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Item currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "declared_customs_value": {
            "type": "number",
            "description": "Item customs value, must be greater than 0 unless category is `documents`. Please note that this value refers to the unit rather than the total."
          }
        }
      },
      "ParcelProductItemCreate": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "properties": {
          "product": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "description": "Product ID. Required if the `sku` is not provided."
              },
              "sku": {
                "type": "string",
                "description": "Product SKU. Required if the `id` is not provided."
              }
            }
          },
          "quantity": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/quantity"
          },
          "declared_currency": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_currency"
          },
          "declared_customs_value": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_customs_value"
          }
        }
      },
      "Units": {
        "type": "object",
        "description": "Units",
        "additionalProperties": false,
        "properties": {
          "weight": {
            "type": "string",
            "description": "Unit of weight values provided. Options: `kg` / `g` / `lb` / `oz` (Default: `kg`). Unit of values in the response will be in `kg`.",
            "default": "kg",
            "enum": [
              "kg",
              "g",
              "lb",
              "oz"
            ]
          },
          "dimensions": {
            "type": "string",
            "description": "Unit of dimension values provided. Options: `cm` / `in` (Default: `cm`) Unit of values in the response will be in `cm`.",
            "default": "cm",
            "enum": [
              "cm",
              "in"
            ]
          }
        }
      },
      "ImportDutyAdditionalRate": {
        "type": "object",
        "description": "An additional duty surcharge applied on top of the base duty rate.",
        "additionalProperties": false,
        "properties": {
          "description": {
            "type": "string",
            "nullable": true,
            "description": "Description of the additional duty surcharge."
          },
          "rate": {
            "type": "number",
            "nullable": true,
            "description": "Additional duty rate as a decimal (e.g. `0.025` = 2.5%)."
          },
          "amount": {
            "type": "number",
            "nullable": true,
            "description": "Computed additional duty amount for this surcharge in the response currency."
          }
        }
      },
      "ImportDutyDetails": {
        "type": "object",
        "description": "Duty calculation details for a line item, including HS code fallback and rate breakdown.",
        "additionalProperties": false,
        "properties": {
          "hs_code_provided": {
            "type": "string",
            "nullable": true,
            "description": "Raw HS code as provided in the request, before normalisation or fallback.",
            "example": "42029100"
          },
          "hs_code_applied": {
            "type": "string",
            "nullable": true,
            "description": "HS code used to determine the duty rate after normalising to 10 digits and applying fallback, if any.",
            "example": "4202910010"
          },
          "subheading": {
            "type": "boolean",
            "nullable": true,
            "description": "True if a shorter parent subheading was used to determine the duty rate because no record existed for the full code."
          },
          "duty_origin_country_id_provided": {
            "type": "integer",
            "nullable": true,
            "description": "Country of origin ID explicitly provided on the item. Null when COO was not provided and fell back to the shipment origin."
          },
          "duty_origin_country_id_applied": {
            "type": "integer",
            "nullable": true,
            "description": "Country of origin ID actually used to determine the duty rate (either provided or the shipment origin fallback)."
          },
          "duty_calculation_method": {
            "type": "string",
            "nullable": true,
            "description": "Customs valuation method used for this destination.",
            "enum": [
              "CIF",
              "FOB"
            ]
          },
          "line_item_shipment_value": {
            "type": "number",
            "nullable": true,
            "description": "Shipment value used for duty calculation (customs value × quantity, plus allocated shipping and insurance for CIF destinations). Returned in the response currency."
          },
          "applied_rate_type": {
            "type": "string",
            "nullable": true,
            "description": "Whether the FTA preferential rate or the general rate was applied.",
            "enum": [
              "fta",
              "general"
            ]
          },
          "additional_rates": {
            "type": "array",
            "nullable": true,
            "description": "Additional duty surcharges applied on top of the base duty rate (e.g. anti-dumping duties, section tariffs).",
            "items": {
              "$ref": "#/components/schemas/ImportDutyAdditionalRate"
            }
          },
          "base_duty_rate": {
            "type": "number",
            "nullable": true,
            "description": "Base duty rate as a decimal (e.g. `0.12` = 12%)."
          },
          "base_duty_amount": {
            "type": "number",
            "nullable": true,
            "description": "Computed base duty amount for the line item in the response currency."
          },
          "line_item_total_duty": {
            "type": "number",
            "nullable": true,
            "description": "Total duty for the line item including base and all additional surcharges, in the response currency."
          }
        }
      }
    }
  }
}
```