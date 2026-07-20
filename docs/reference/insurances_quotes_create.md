# Create an Insurance Quote

> **Regional availability**: This endpoint is currently only available for US entities. Support for additional regions will be available in a future release.

Create an insurance quote for products to be shipped.
Returns a quote with fee calculations per product and an overall total.
The quote is valid for 48 hours and can be converted to a policy using the
[Create Insurance Policy from Quote](#operation/insurances_policies_from_quote_create) endpoint.

Required authorization scope: `public.insurance_quote:write`


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
  "paths": {
    "/2024-09/insurances/quotes": {
      "post": {
        "summary": "Create an Insurance Quote",
        "tags": [
          "Insurance"
        ],
        "operationId": "insurances_quotes_create",
        "description": "> **Regional availability**: This endpoint is currently only available for US entities. Support for additional regions will be available in a future release.\n\nCreate an insurance quote for products to be shipped.\nReturns a quote with fee calculations per product and an overall total.\nThe quote is valid for 48 hours and can be converted to a policy using the\n[Create Insurance Policy from Quote](#operation/insurances_policies_from_quote_create) endpoint.\n\nRequired authorization scope: `public.insurance_quote:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "Insurance quote successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "created": {
                    "value": {
                      "insurance_quote": {
                        "insurance_fee_currency": "USD",
                        "products": [
                          {
                            "easyship_product_id": null,
                            "insured_currency": "USD",
                            "insured_eligibility": true,
                            "insured_eligibility_failure_reason": null,
                            "insured_fee": 3,
                            "platform_product_id": null,
                            "manufacturer_part_number": null,
                            "global_trade_item_number": null
                          }
                        ],
                        "quote_id": "4df6ef29-067e-48e7-aafb-1a6bdc551582",
                        "total_insurance_fee": 3,
                        "total_insurance_fee_raw": 3,
                        "valid_until": "2025-01-22T12:21:00Z"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Insurance quote successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/insurance_quote_single"
                }
              }
            }
          },
          "422": {
            "description": "validation error",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/InsuranceQuoteCreate/properties/quote missing required parameters: insured_value, origin_country, destination_country, products"
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
                    "summary": "validation error"
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
                "$ref": "#/components/schemas/InsuranceQuoteCreate"
              },
              "examples": {
                "insurance_quote_successfully_created": {
                  "summary": "Insurance quote successfully created",
                  "value": {
                    "quote": {
                      "insured_value": 200,
                      "currency": "USD",
                      "origin_country": "US",
                      "destination_country": "GB",
                      "products": [
                        {
                          "platform_product_id": null,
                          "manufacturer_part_number": null,
                          "global_trade_item_number": null,
                          "category": "Fashion",
                          "price": 100,
                          "quantity": 2,
                          "description": "T-shirt"
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
      "InsuranceQuote": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "quote_id": {
            "type": "string",
            "format": "uuid",
            "description": "Unique identifier for this insurance quote"
          },
          "total_insurance_fee": {
            "type": "number",
            "description": "Total insurance fee (rounded to currency precision)"
          },
          "total_insurance_fee_raw": {
            "type": "number",
            "description": "Raw total insurance fee before rounding"
          },
          "insurance_fee_currency": {
            "$ref": "#/components/schemas/Currency",
            "description": "Currency of the insurance fee"
          },
          "valid_until": {
            "type": "string",
            "format": "date-time",
            "description": "Quote expiry timestamp (ISO 8601)"
          },
          "products": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "easyship_product_id": {
                  "type": "integer",
                  "nullable": true
                },
                "insured_eligibility": {
                  "type": "boolean",
                  "description": "Whether this product is eligible for insurance"
                },
                "insured_eligibility_failure_reason": {
                  "type": "string",
                  "nullable": true,
                  "description": "Reason ineligible, or null if eligible"
                },
                "insured_fee": {
                  "type": "number",
                  "description": "Insurance fee for this product"
                },
                "insured_currency": {
                  "$ref": "#/components/schemas/Currency"
                },
                "platform_product_id": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          }
        }
      },
      "InsuranceQuoteCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "quote"
        ],
        "properties": {
          "quote": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "insured_value",
              "currency",
              "origin_country",
              "destination_country",
              "products"
            ],
            "properties": {
              "insured_value": {
                "type": "number",
                "description": "Total declared value to insure"
              },
              "currency": {
                "$ref": "#/components/schemas/Currency"
              },
              "origin_country": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "destination_country": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "products": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": [
                    "category",
                    "price"
                  ],
                  "properties": {
                    "platform_product_id": {
                      "type": "string",
                      "nullable": true,
                      "description": "Your platform's product identifier"
                    },
                    "category": {
                      "type": "string",
                      "description": "Product category"
                    },
                    "price": {
                      "type": "number",
                      "description": "Unit price"
                    },
                    "currency": {
                      "$ref": "#/components/schemas/Currency",
                      "description": "Currency of the product price. Defaults to the quote-level currency if not provided"
                    },
                    "quantity": {
                      "type": "integer",
                      "minimum": 1,
                      "description": "Number of units. Defaults to 1 if not provided"
                    },
                    "description": {
                      "type": "string"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "insurance_quote_single": {
        "type": "object",
        "description": "Insurance quote details",
        "additionalProperties": false,
        "properties": {
          "insurance_quote": {
            "$ref": "#/components/schemas/InsuranceQuote"
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
          }
        }
      }
    }
  }
}
```