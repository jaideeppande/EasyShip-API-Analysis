# List all Trackings

Retrieve the most recent status for a shipment and a history of all previous checkpoints.

Required authorization scope: `public.track:read`


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
      "name": "Shipments"
    }
  ],
  "paths": {
    "/2024-09/shipments/trackings": {
      "get": {
        "summary": "List all Trackings",
        "tags": [
          "Shipments"
        ],
        "operationId": "shipments_trackings_index",
        "description": "Retrieve the most recent status for a shipment and a history of all previous checkpoints.\n\nRequired authorization scope: `public.track:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1
            },
            "required": false,
            "description": "Page number to fetch, default: `1`",
            "example": 1
          },
          {
            "name": "per_page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "required": false,
            "description": "Number of records per page to fetch, default: `20`",
            "example": 10
          },
          {
            "name": "easyship_shipment_id",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "explode": false,
            "required": false,
            "description": "Easyship Shipment ID provided when creating the shipment."
          },
          {
            "name": "platform_order_number",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "explode": false,
            "required": false,
            "description": "Order number on the sales platform. You can choose to use either `easyship_shipment_id` or `platform_order_number`."
          },
          {
            "name": "include_checkpoints",
            "in": "query",
            "description": "Include checkpoints in the response.",
            "example": true,
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "list of shipment trackings with checkpoints",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "shipments": [
                        {
                          "easyship_shipment_id": "ESSG10006001",
                          "checkpoints": [
                            {
                              "checkpoint_time": "2022-02-22T12:21:00Z",
                              "city": "Hong Kong",
                              "country_iso3": "HKG",
                              "country_name": "Hong Kong SAR",
                              "handler": "aramex",
                              "location": null,
                              "message": "Info Received At Origin Center",
                              "order_number": null,
                              "postal_code": null,
                              "primary_status": "Awaiting Pickup at Seller",
                              "state": null
                            }
                          ],
                          "destination_country_alpha2": "SG",
                          "eta_date": null,
                          "origin_country_alpha2": "HK",
                          "platform_order_number": null,
                          "status": "Awaiting Pickup at Seller",
                          "tracking_page_url": "http://api.easyship.com:9003/shipment-tracking/ESSG10006001",
                          "trackings": [
                            {
                              "alternate_tracking_number": null,
                              "handler": "aramex",
                              "leg_number": 1,
                              "local_tracking_number": null,
                              "tracking_number": "TEST123",
                              "tracking_state": "active"
                            }
                          ]
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
                    "summary": "list of shipment trackings with checkpoints"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipment_tracking_list"
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
      "shipment_tracking_list": {
        "type": "object",
        "description": "List of Shipments with tracking info",
        "additionalProperties": false,
        "properties": {
          "shipments": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShipmentTrackingList"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
      "ShipmentTracking": {
        "type": "object",
        "description": "A source of tracking data for the shipment's journey",
        "additionalProperties": false,
        "properties": {
          "tracking_number": {
            "type": "string",
            "description": "Reference provided by the courier for this leg"
          },
          "local_tracking_number": {
            "type": "string",
            "nullable": true,
            "description": "Local tracking number provided by DHL eCommerce"
          },
          "alternate_tracking_number": {
            "type": "string",
            "nullable": true,
            "description": "Alternate tracking number provided by DHL eCommerce"
          },
          "leg_number": {
            "type": "integer",
            "minimum": 1,
            "description": "Sequential index of the different portions of the shipment's journey. If a shipment is passed to a new courier, it begins a new leg."
          },
          "handler": {
            "type": "string",
            "description": "The service that is handling the tracking process"
          },
          "tracking_state": {
            "type": "string",
            "description": "The current state of the tracking",
            "enum": [
              "created",
              "active",
              "pending",
              "completed",
              "overwritten_by_admin"
            ]
          }
        }
      },
      "ShipmentTrackingList": {
        "type": "object",
        "description": "A source of tracking data for the shipment's journey",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "platform_order_number": {
            "$ref": "#/components/schemas/Shipment/properties/order_data/properties/platform_order_number"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "destination_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "status": {
            "type": "string",
            "description": "The latest event status",
            "enum": [
              "Created",
              "Cancelled by Company",
              "Cancelled by Easyship",
              "Awaiting Pickup at Seller",
              "Assigned Pickup",
              "Picked Up at Seller",
              "Received at Fulfillment Center",
              "Verified",
              "Packed",
              "Shipped",
              "Incomplete",
              "Lost by Courier",
              "Returned To Sender",
              "Archived",
              "Draft",
              "Cancelled",
              "Label Pending",
              "Label Ready",
              "Label Printed",
              "Pickup Scheduled",
              "Pickup Complete",
              "Cancelled (No Stock)",
              "Handed Over to Courier",
              "Label Rejected",
              "Drop-off Complete",
              "Dispatched from Sorting Hub",
              "Received at Local Fulfilment Center",
              "Awaiting Pickup Confirmation by Courier",
              "Pickup Request Failed",
              "Uncancelled",
              "Discarded Draft",
              "Processing at Consolidation Center",
              "Exception",
              "To be returned",
              "Liquidated",
              "Awaiting Confirmation by Warehouse",
              "Order Failed to Create at Warehouse",
              "Order Received by Warehouse",
              "Order Packed",
              "Order Collected",
              "Backorder (No Stock)",
              "Awaiting Dispatch by Warehouse",
              "Cancellation Requested",
              "Cancellation Request Failed"
            ],
            "nullable": true
          },
          "tracking_page_url": {
            "type": "string",
            "format": "uri"
          },
          "eta_date": {
            "type": "string",
            "format": "date-time",
            "nullable": true
          },
          "trackings": {
            "type": "array",
            "description": "Sources of tracking data for this shipment",
            "items": {
              "$ref": "#/components/schemas/ShipmentTracking"
            }
          },
          "checkpoints": {
            "type": "array",
            "nullable": true,
            "items": {
              "$ref": "#/components/schemas/ShipmentTrackingCheckpoint"
            }
          }
        }
      },
      "ShipmentTrackingCheckpoint": {
        "type": "object",
        "description": "This represents a checkpoint in the shipment's journey to its destination. This information includes various attributes that provide details about the current state and location of a shipment as recorded by the handler.\nEasyship provides a webhook event that will be triggered when a new tracking checkpoint is created. For a detailed overview, please refer to the [Webhook Guide](https://developers.easyship.com/reference/webhooks-guide#/) and shipment.tracking.checkpointscreated [event](https://developers.easyship.com/reference/shipmenttrackingcheckpointscreated).\n",
        "additionalProperties": false,
        "properties": {
          "order_number": {
            "type": "integer",
            "nullable": true,
            "description": "A number used for chronological sorting of tracking events. Numbers may not be sequential but maintain proper chronological ordering across the entire shipment journey. Range\tOrder Number Purpose\n  * 100-199\tFirst leg of journey (e.g., origin country to hub)\n  * 200-299\tSecond leg of journey (e.g., international transit)\n  * 300-399\tThird leg of journey (e.g., destination country processing)\n  * 801\tCommon shipment status events\n  * 901\tLater stage events\n",
            "example": 101
          },
          "handler": {
            "type": "string",
            "description": "The name of the shipping carrier or handler responsible for this checkpoint.",
            "example": "USPS"
          },
          "message": {
            "type": "string",
            "description": "A brief message describing the event at this checkpoint.",
            "example": "Arrived at Regional Facility"
          },
          "location": {
            "type": "string",
            "nullable": true,
            "description": "A string containing the location details of this checkpoint, often including city, state, and postal code.",
            "example": "East Bridgewater, MA, US, United States"
          },
          "city": {
            "type": "string",
            "description": "The city where this checkpoint occurred."
          },
          "country_name": {
            "type": "string",
            "description": "The full name of the country where this checkpoint occurred.",
            "example": "United States"
          },
          "country_iso3": {
            "type": "string",
            "description": "The ISO 3166-1 alpha-3 code for the country.",
            "example": "USA"
          },
          "state": {
            "type": "string",
            "nullable": true,
            "description": "The state or province where this checkpoint occurred."
          },
          "postal_code": {
            "type": "string",
            "nullable": true,
            "description": "The postal or zip code of the location."
          },
          "checkpoint_time": {
            "type": "string",
            "format": "date-time",
            "description": "The timestamp indicating when this checkpoint event occurred, in ISO 8601 format (UTC).",
            "example": "2025-01-01T10:00:00.000Z"
          },
          "primary_status": {
            "type": "string",
            "description": "A high-level status category for this specific checkpoint.",
            "example": "In Transit to Customer",
            "enum": [
              "Awaiting Pickup at Seller",
              "Tracking Info Received",
              "In Transit to Customer",
              "Out For Delivery",
              "Failed Delivery Attempt",
              "Delivered",
              "Exception"
            ]
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
      }
    }
  }
}
```