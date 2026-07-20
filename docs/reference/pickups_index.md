# List all Pickups

Retrieve a list of pickups.

Required authorization scope: `public.pickup:read`


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
      "name": "Pickups"
    }
  ],
  "paths": {
    "/2024-09/pickups": {
      "get": {
        "summary": "List all Pickups",
        "tags": [
          "Pickups"
        ],
        "operationId": "pickups_index",
        "description": "Retrieve a list of pickups.\n\nRequired authorization scope: `public.pickup:read`\n",
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
            "name": "pickup_date",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "date"
            },
            "example": "2023-02-28",
            "required": false,
            "description": "Selected pickup date. Only accept `YYYY-MM-DD` format."
          },
          {
            "name": "courier",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "USPS",
                "Australia Post eParcel",
                "StarTrack",
                "Royal Mail",
                "DHL eCommerce",
                "Canada Post",
                "Quantium"
              ]
            },
            "required": false,
            "description": "Courier name",
            "example": "DHL"
          },
          {
            "name": "pickup_state",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "cancelled",
                "completed",
                "partially-completed",
                "pending-confirmation",
                "pending-delayed-api-request",
                "pending-drop-off",
                "pending-handover",
                "request-failed",
                "request-pickup-window-failed",
                "request-technical-failed",
                "requested"
              ]
            },
            "required": false,
            "description": "Pickup state",
            "example": "request-failed"
          },
          {
            "name": "shipment_id",
            "in": "query",
            "required": false,
            "description": "Shipment ID",
            "example": "ESHK1234567",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "list of pickups",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "pickups": [
                        {
                          "address": {
                            "city": "City",
                            "company_name": "Test Plc.",
                            "contact_email": "asd@asd.com",
                            "contact_name": "Foo Bar",
                            "contact_phone": "+852-1234-5678",
                            "country_alpha2": "HK",
                            "default_for": {
                              "pickup": true,
                              "billing": false,
                              "sender": true,
                              "return": true
                            },
                            "hk_district": {
                              "id": 1,
                              "area": "Admiralty",
                              "district": "Central and Western",
                              "zone": "Hong Kong Island"
                            },
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0005",
                            "line_1": "123 Test Street",
                            "line_2": "Block 3",
                            "postal_code": "ABC123",
                            "state": "State",
                            "status": "active"
                          },
                          "courier_service": {
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "easyship_courier_service": true,
                            "name": "USPS - Priority Mail",
                            "umbrella_name": "USPS"
                          },
                          "easyship_pickup_id": "PHK10000001",
                          "pickup_fee": 0,
                          "pickup_reference_number": null,
                          "pickup_state": "requested",
                          "provider_name": "Standard Pickup",
                          "selected_from_time": "2022-02-28T20:21",
                          "selected_to_time": "2015-01-01T09:00",
                          "shipments_count": 0,
                          "total_actual_weight": 0
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
                    "summary": "list of pickups"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/pickup_list"
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
      "pickup_list": {
        "type": "object",
        "description": "List of Pickups",
        "additionalProperties": false,
        "properties": {
          "pickups": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Pickup"
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
      "AddressFull": {
        "type": "object",
        "description": "Address object for Addresses API",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Address ID"
          },
          "status": {
            "type": "string",
            "enum": [
              "active",
              "inactive"
            ],
            "description": "Status of the address"
          },
          "line_1": {
            "$ref": "#/components/schemas/Address/properties/line_1"
          },
          "line_2": {
            "$ref": "#/components/schemas/Address/properties/line_2"
          },
          "state": {
            "$ref": "#/components/schemas/Address/properties/state"
          },
          "city": {
            "$ref": "#/components/schemas/Address/properties/city"
          },
          "postal_code": {
            "$ref": "#/components/schemas/Address/properties/postal_code"
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "$ref": "#/components/schemas/Address/properties/company_name"
          },
          "contact_name": {
            "$ref": "#/components/schemas/Address/properties/contact_name"
          },
          "contact_phone": {
            "$ref": "#/components/schemas/Address/properties/contact_phone"
          },
          "contact_email": {
            "$ref": "#/components/schemas/Address/properties/contact_email"
          },
          "default_for": {
            "type": "object",
            "additionalProperties": false,
            "description": "Each element indicates if the address is set as default value for pickup, billing, sender, and return address.",
            "properties": {
              "billing": {
                "type": "boolean",
                "description": "Whether this is the default billing address"
              },
              "sender": {
                "type": "boolean",
                "description": "Whether this is the default sender address"
              },
              "pickup": {
                "type": "boolean",
                "description": "Whether this is the default pickup address"
              },
              "return": {
                "type": "boolean",
                "description": "Whether this is the default return address"
              }
            }
          },
          "hk_district": {
            "type": "object",
            "nullable": true,
            "additionalProperties": false,
            "description": "Details of the district for an address in Hong Kong. Display only applicable for addresses in Hong Kong.",
            "properties": {
              "id": {
                "type": "integer"
              },
              "area": {
                "type": "string"
              },
              "district": {
                "type": "string"
              },
              "zone": {
                "type": "string"
              }
            }
          },
          "validation": {
            "type": "object",
            "additionalProperties": false,
            "description": "Available only when the Address Validation is active for your account and the address was created by Address Validation",
            "properties": {
              "status": {
                "type": "string",
                "description": "Status of the address validation. Refers to the validation output (not the input)."
              },
              "detail": {
                "type": "string",
                "nullable": true,
                "description": "The relative level to which the post-processed address is verifiable while also considering its closeness to the input data."
              },
              "comparison": {
                "type": "object",
                "additionalProperties": false,
                "nullable": true,
                "description": "A descriptive comparison of the pre/post validated address. Similar to `detail` with more fidelity.",
                "properties": {
                  "pre": {
                    "type": "string",
                    "enum": [
                      "delivery_point",
                      "premise",
                      "street",
                      "city",
                      "state",
                      "none"
                    ],
                    "description": "The verification level of the address before validation."
                  },
                  "post": {
                    "type": "string",
                    "enum": [
                      "delivery_point",
                      "premise",
                      "street",
                      "city",
                      "state",
                      "none"
                    ],
                    "description": "The verification level of the address after validation."
                  },
                  "changes": {
                    "type": "string",
                    "enum": [
                      "none",
                      "minor",
                      "moderate",
                      "major",
                      "drastic"
                    ],
                    "description": "The extent of changes made to the address during validation. * `none` - No changes * `minor` - Minor changes like capitalization or a single character * `moderate` - Moderate changes worth reviewing * `major` - Larger changes worth reviewing * `drastic` - Drastic changes worth reviewing\n"
                  }
                }
              },
              "address": {
                "type": "object",
                "description": "The validated address as sourced from validation service",
                "properties": {
                  "line_1": {
                    "type": "string",
                    "description": "First line of the street address"
                  },
                  "line_2": {
                    "type": "string",
                    "nullable": true,
                    "description": "Second line of the street address"
                  },
                  "line_3": {
                    "type": "string",
                    "nullable": true,
                    "description": "Third line of the street address",
                    "maximum": 35
                  },
                  "state": {
                    "type": "string",
                    "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names."
                  },
                  "city": {
                    "type": "string",
                    "description": "City or Suburb"
                  },
                  "postal_code": {
                    "type": "string",
                    "description": "Postal code."
                  },
                  "country_alpha2": {
                    "$ref": "#/components/schemas/CountryAlpha2"
                  },
                  "company_name": {
                    "type": "string",
                    "nullable": true,
                    "description": "The company or organization at the address"
                  },
                  "contact_name": {
                    "type": "string",
                    "description": "The full name of a person at the address"
                  }
                }
              }
            }
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
      "Pickup": {
        "type": "object",
        "description": "Pickup",
        "additionalProperties": false,
        "properties": {
          "easyship_pickup_id": {
            "type": "string",
            "description": "Pickup ID"
          },
          "selected_from_time": {
            "type": "string"
          },
          "selected_to_time": {
            "type": "string"
          },
          "pickup_reference_number": {
            "type": "string",
            "nullable": true
          },
          "pickup_fee": {
            "type": "number",
            "format": "double"
          },
          "provider_name": {
            "type": "string"
          },
          "shipments_count": {
            "type": "number",
            "format": "integer"
          },
          "total_actual_weight": {
            "type": "number",
            "format": "double"
          },
          "pickup_state": {
            "type": "string"
          },
          "courier_service": {
            "$ref": "#/components/schemas/Shipment/properties/courier_service"
          },
          "address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/AddressFull"
              },
              {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "string",
                    "format": "uuid",
                    "description": "Company ID"
                  },
                  "hk_district": {
                    "type": "object",
                    "nullable": true,
                    "additionalProperties": false,
                    "properties": {
                      "id": {
                        "type": "integer"
                      },
                      "area": {
                        "type": "string"
                      },
                      "district": {
                        "type": "string"
                      },
                      "zone": {
                        "type": "string"
                      }
                    }
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```