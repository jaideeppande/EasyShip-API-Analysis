# Update a Courier

Updates a courier.

Required authorization scope: `public.courier:write`


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
      "name": "Couriers"
    }
  ],
  "paths": {
    "/2024-09/couriers/{courier_id}": {
      "patch": {
        "summary": "Update a Courier",
        "tags": [
          "Couriers"
        ],
        "operationId": "couriers_update",
        "description": "Updates a courier.\n\nRequired authorization scope: `public.courier:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "courier_id",
            "in": "path",
            "required": true,
            "description": "The Courier ID",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "courier successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "courier": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "account_number": "123456789",
                        "auth": {
                          "errors": [],
                          "state": "verified"
                        },
                        "created_at": "2022-02-22T12:11:00Z",
                        "customer_reference_id": "reference id",
                        "ddp_handling_fee": 2.5,
                        "easyship_courier": false,
                        "filtered_account_details": {
                          "account_number": "123456789",
                          "address_line_1": "",
                          "city": "",
                          "contact_email": "",
                          "contact_phone": "",
                          "customer_name": "",
                          "oba_email_address": "",
                          "postal_code": "",
                          "posting_location": null,
                          "receiving_hub": ""
                        },
                        "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/dhl.png",
                        "nickname": "My Royal Mail",
                        "origin_country_alpha2": "HK",
                        "pickup_fee": 1.5,
                        "state": "pending",
                        "umbrella_name": "Royal Mail"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "courier successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/courier_single"
                }
              }
            }
          },
          "403": {
            "description": "unauthorized",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "forbidden",
                        "details": [],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Scopes",
                            "url": "https://developers.easyship.com/reference/scopes"
                          },
                          {
                            "kind": "documentation",
                            "name": "Update a Courier",
                            "url": "https://developers.easyship.com/reference/courier_accounts_update"
                          }
                        ],
                        "message": "You do not have permission to access this resource. Please contact our support team or your account manager if you believe you should have access.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "unauthorized"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "404": {
            "description": "record not found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Courier was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Update a Courier",
                            "url": "https://developers.easyship.com/reference/courier_accounts_update"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "record not found"
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
                          "#/components/schemas/CourierBase/properties/nickname does not allow null values"
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
                "$ref": "#/components/schemas/CourierUpdate"
              },
              "examples": {
                "courier_successfully_updated": {
                  "summary": "courier successfully updated",
                  "value": {
                    "nickname": "My Royal Mail",
                    "ddp_handling_fee": 2.5,
                    "pickup_fee": 1.5
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
      "courier_single": {
        "type": "object",
        "description": "Single courier with all its details",
        "additionalProperties": false,
        "properties": {
          "courier": {
            "$ref": "#/components/schemas/Courier"
          },
          "meta": {
            "$ref": "#/components/schemas/CourierMeta"
          }
        }
      },
      "CourierAuth": {
        "type": "object",
        "description": "Courier authentication state for LYOC accounts.",
        "additionalProperties": false,
        "properties": {
          "state": {
            "type": "string",
            "description": "Authentication State for LYOC only. For Royal Mail, a newly-created account will be set to `partially_verified` until the account details have been `verified`. If there are issues with the account details, this will be set to `failed`.",
            "enum": [
              "unverified",
              "partially_verified",
              "verified",
              "failed"
            ]
          },
          "errors": {
            "type": "array",
            "description": "Authentication errors for LYOC only. If the authentication state of the account is `failed`, this will contain a list of error messages concerning the failure.",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "CourierBase": {
        "type": "object",
        "description": "Courier",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "customer_reference_id": {
            "type": "string",
            "nullable": true,
            "description": "An identifier for the customer who owns the account. Available only for selected customers."
          },
          "easyship_courier": {
            "type": "boolean",
            "description": "Whether the courier belongs to Easyship or not."
          },
          "nickname": {
            "type": "string",
            "description": "For LYOC. Unique nickname used to identify the linked account.",
            "minimum": 3,
            "maximum": 15
          },
          "umbrella_name": {
            "type": "string",
            "description": "Umbrella Name of the courier"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "state": {
            "type": "string",
            "description": "Courier State for LYOC only. For Royal Mail, a newly-created account will be set to `pending` until the account details are verified. Once verified, the account will be set to `active` and the associated courier services will available for Rates and Labels.",
            "enum": [
              "pending",
              "active",
              "inactive"
            ]
          },
          "auth": {
            "$ref": "#/components/schemas/CourierAuth"
          },
          "ddp_handling_fee": {
            "type": "number",
            "description": "For LYOC only. DDP handling fee applied by the courier when DDP is requested."
          },
          "pickup_fee": {
            "type": "number",
            "description": "For LYOC only. Additional pickup fee to apply to all shipments. This fee will be added to your quoted rates."
          },
          "account_number": {
            "type": "string",
            "nullable": true,
            "description": "For LYOC only. The account number associated with the linked courier account."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "For LYOC only. The date and time the courier account was created in ISO 8601 format."
          }
        }
      },
      "Courier": {
        "type": "object",
        "description": "Courier",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/CourierBase/properties/id"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "easyship_courier": {
            "$ref": "#/components/schemas/CourierBase/properties/easyship_courier"
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "state": {
            "$ref": "#/components/schemas/CourierBase/properties/state"
          },
          "auth": {
            "$ref": "#/components/schemas/CourierAuth"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "account_number": {
            "$ref": "#/components/schemas/CourierBase/properties/account_number"
          },
          "created_at": {
            "$ref": "#/components/schemas/CourierBase/properties/created_at"
          },
          "umbrella_name": {
            "type": "string",
            "description": "Umbrella Name of the Courier"
          },
          "filtered_account_details": {
            "type": "object",
            "description": "Account details are available only for LYOC couriers. The content is different per courier.",
            "additionalProperties": true
          },
          "logo_url": {
            "type": "string",
            "description": "URL of the Courier logo."
          }
        }
      },
      "CourierUpdate": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          }
        }
      },
      "CourierMeta": {
        "type": "object",
        "description": "Courier Metadata",
        "additionalProperties": false,
        "properties": {
          "messages": {
            "type": "array",
            "description": "Messages from courier service when the Courier creation is a partial success (status code `202`).",
            "items": {
              "type": "string"
            }
          },
          "request_id": {
            "$ref": "#/components/schemas/Meta/properties/request_id"
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
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
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
      }
    }
  }
}
```