# List all Courier Services

Retrieve a list of active courier services available with your account.

Required authorization scope: `public.courier_service:read`


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
      "name": "Courier Services"
    }
  ],
  "paths": {
    "/2024-09/courier_services": {
      "get": {
        "summary": "List all Courier Services",
        "tags": [
          "Courier Services"
        ],
        "operationId": "courier_services_index",
        "description": "Retrieve a list of active courier services available with your account.\n\nRequired authorization scope: `public.courier_service:read`\n",
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
            "name": "sort_by",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "origin_country_id",
                "courier_name",
                "created_at"
              ]
            },
            "required": false,
            "description": "Sort records by listed columns. Default: `created_at`",
            "example": "created_at"
          },
          {
            "name": "sort_direction",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "ASC",
                "DESC"
              ]
            },
            "required": false,
            "description": "Set the sort direction. Default: `DESC`",
            "example": "ASC"
          },
          {
            "name": "country_alpha2",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
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
              }
            },
            "explode": false,
            "required": false,
            "description": "Filter records by country code: Alpha-2 format (ISO 3166-1).",
            "example": [
              "US",
              "HK"
            ]
          },
          {
            "name": "umbrella_name",
            "in": "query",
            "required": false,
            "description": "Filter records by courier umbrella name",
            "example": "DHL",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "customer_reference_id",
            "in": "query",
            "required": false,
            "description": "An identifier for a customer (available only for selected customers)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "accepts",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "outbounds",
                  "prepaid_returns",
                  "pay_on_scan_returns",
                  "pi965_batteries",
                  "pi966_batteries",
                  "pi967_batteries",
                  "liquids",
                  "documents",
                  "parcels",
                  "specific_dangerous_goods"
                ]
              }
            },
            "example": [
              "pi965_batteries",
              "parcels"
            ],
            "explode": false,
            "required": false,
            "description": "Filter records by acceptance criteria"
          },
          {
            "name": "supported_incoterms",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "DDU",
                  "DDP"
                ]
              }
            },
            "example": [
              "DDU"
            ],
            "explode": false,
            "required": false,
            "description": "Filter records if the courier supports DDUs, DDPs or both"
          },
          {
            "name": "international",
            "in": "query",
            "required": false,
            "description": "Filter records if the courier is an international service",
            "schema": {
              "type": "boolean"
            }
          },
          {
            "name": "domestic",
            "in": "query",
            "required": false,
            "description": "Filter records if the courier is an domestic service",
            "schema": {
              "type": "boolean"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "list of courier services",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "courier_services": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "accepts": {
                            "documents": false,
                            "liquids": false,
                            "outbounds": true,
                            "parcels": false,
                            "pay_on_scan_returns": false,
                            "pi965_batteries": false,
                            "pi966_batteries": false,
                            "pi967_batteries": false,
                            "prepaid_returns": false,
                            "specific_dangerous_goods": false
                          },
                          "accepts_outbounds": true,
                          "accepts_pay_on_scan_returns": false,
                          "accepts_prepaid_returns": false,
                          "active": true,
                          "available_handover_options": [
                            "dropoff",
                            "free_pickup",
                            "paid_pickup"
                          ],
                          "country_alpha2": "GB",
                          "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0006",
                          "courier_logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/aramex.png",
                          "domestic": true,
                          "easyship_courier_service": true,
                          "international": true,
                          "ioss_support": null,
                          "logo_url": "aramex",
                          "name": "Aramex",
                          "nickname": null,
                          "official_name": "Aramex",
                          "restricted_to_destination_states": null,
                          "restricted_to_origin_states": null,
                          "service_name": "Parcel",
                          "supported_incoterms": [
                            "DDU",
                            "DDP"
                          ],
                          "tracking_rating": 2,
                          "umbrella_name": "DHL"
                        },
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "accepts": {
                            "documents": false,
                            "liquids": false,
                            "outbounds": true,
                            "parcels": false,
                            "pay_on_scan_returns": false,
                            "pi965_batteries": false,
                            "pi966_batteries": false,
                            "pi967_batteries": false,
                            "prepaid_returns": false,
                            "specific_dangerous_goods": false
                          },
                          "accepts_outbounds": true,
                          "accepts_pay_on_scan_returns": false,
                          "accepts_prepaid_returns": false,
                          "active": true,
                          "available_handover_options": [
                            "dropoff",
                            "free_pickup",
                            "paid_pickup"
                          ],
                          "country_alpha2": "CA",
                          "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0006",
                          "courier_logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/aramex.png",
                          "domestic": true,
                          "easyship_courier_service": true,
                          "international": true,
                          "ioss_support": null,
                          "logo_url": "aramex",
                          "name": "Aramex",
                          "nickname": null,
                          "official_name": "Aramex",
                          "restricted_to_destination_states": null,
                          "restricted_to_origin_states": null,
                          "service_name": "Parcel",
                          "supported_incoterms": [
                            "DDU",
                            "DDP"
                          ],
                          "tracking_rating": 2,
                          "umbrella_name": "Aramex"
                        },
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                          "accepts": {
                            "documents": false,
                            "liquids": false,
                            "outbounds": true,
                            "parcels": false,
                            "pay_on_scan_returns": false,
                            "pi965_batteries": false,
                            "pi966_batteries": false,
                            "pi967_batteries": false,
                            "prepaid_returns": false,
                            "specific_dangerous_goods": false
                          },
                          "accepts_outbounds": true,
                          "accepts_pay_on_scan_returns": false,
                          "accepts_prepaid_returns": false,
                          "active": true,
                          "available_handover_options": [
                            "dropoff",
                            "free_pickup",
                            "paid_pickup"
                          ],
                          "country_alpha2": "HK",
                          "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0006",
                          "courier_logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/aramex.png",
                          "domestic": true,
                          "easyship_courier_service": false,
                          "international": true,
                          "ioss_support": null,
                          "logo_url": "aramex",
                          "name": "LYOC - Aramex",
                          "nickname": "LYOC",
                          "official_name": "Aramex",
                          "restricted_to_destination_states": null,
                          "restricted_to_origin_states": null,
                          "service_name": "Parcel",
                          "supported_incoterms": [
                            "DDU",
                            "DDP"
                          ],
                          "tracking_rating": 2,
                          "umbrella_name": "DHL"
                        },
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0005",
                          "accepts": {
                            "documents": false,
                            "liquids": false,
                            "outbounds": true,
                            "parcels": false,
                            "pay_on_scan_returns": false,
                            "pi965_batteries": false,
                            "pi966_batteries": false,
                            "pi967_batteries": false,
                            "prepaid_returns": false,
                            "specific_dangerous_goods": false
                          },
                          "accepts_outbounds": true,
                          "accepts_pay_on_scan_returns": false,
                          "accepts_prepaid_returns": false,
                          "active": true,
                          "available_handover_options": [
                            "dropoff",
                            "free_pickup",
                            "paid_pickup"
                          ],
                          "country_alpha2": "US",
                          "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0006",
                          "courier_logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/aramex.png",
                          "customer_reference_id": "customer_reference_id",
                          "domestic": true,
                          "easyship_courier_service": false,
                          "international": true,
                          "ioss_support": null,
                          "logo_url": "aramex",
                          "name": "Subordinate Nickname - Aramex",
                          "nickname": "Subordinate Nickname",
                          "official_name": "Aramex",
                          "restricted_to_destination_states": null,
                          "restricted_to_origin_states": null,
                          "service_name": "Parcel",
                          "supported_incoterms": [
                            "DDU",
                            "DDP"
                          ],
                          "tracking_rating": 2,
                          "umbrella_name": "DHL"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 4
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of courier services"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/courier_service_list"
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
      "courier_service_list": {
        "type": "object",
        "description": "List of couriers service",
        "additionalProperties": false,
        "properties": {
          "courier_services": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CourierService"
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
      }
    }
  }
}
```