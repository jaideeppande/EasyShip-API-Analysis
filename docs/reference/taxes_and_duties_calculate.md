# Calculate Tax and Duty

Retrieve tax and duty costs information.

Use either of the two schemas `WITH COUNTRY IDS` OR `WITH COUNTRY ALPHA2` to provide country specific details.

Required authorization scope: `public.tax_and_duty:read`

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
      "name": "Taxes and Duties"
    }
  ],
  "paths": {
    "/2024-09/taxes_and_duties": {
      "post": {
        "summary": "Calculate Tax and Duty",
        "tags": [
          "Taxes and Duties"
        ],
        "operationId": "taxes_and_duties_calculate",
        "description": "Retrieve tax and duty costs information.\n\nUse either of the two schemas `WITH COUNTRY IDS` OR `WITH COUNTRY ALPHA2` to provide country specific details.\n\nRequired authorization scope: `public.tax_and_duty:read`\n\n> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).\n\nCalls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "get tax and duty",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "tax_and_duty": {
                        "currency": "USD",
                        "duty": 100.21,
                        "import_duty_details": null,
                        "tax": 20.21
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "get tax and duty"
                  },
                  "with_duty_breakdown": {
                    "value": {
                      "tax_and_duty": {
                        "currency": "USD",
                        "duty": 7.5,
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
                        "tax": 10
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "get tax and duty"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/tax_and_duty_single"
                }
              }
            }
          },
          "402": {
            "description": "when insufficient subscription tier for specific feature",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "insufficient_subscription",
                        "details": [
                          "The TAXES AND DUTIES feature is not available for free subscription plan, please contact Easyship"
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
                            "name": "Calculate Tax and Duty",
                            "url": "https://developers.easyship.com/reference/taxes_and_duties_calculate"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Calculate Taxes and Duties",
                            "url": "https://developers.easyship.com/docs/how-to-calculate-taxes-and-duties"
                          }
                        ],
                        "message": "You don't have access to this feature. Please upgrade your plan",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "when insufficient subscription tier for specific feature"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "422": {
            "description": "could not calculate tax and duty",
            "content": {
              "application/json": {
                "examples": {
                  "invalid_content": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "shipment_charge is not a number",
                          "items[2]: hs_code is not an eight-digit number"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Calculate Tax and Duty",
                            "url": "https://developers.easyship.com/reference/taxes_and_duties_calculate"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Calculate Taxes and Duties",
                            "url": "https://developers.easyship.com/docs/how-to-calculate-taxes-and-duties"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "could not calculate tax and duty"
                  },
                  "could_not_calculate_tax_and_duty": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "No import tax record was found for the specified origin and destination"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Calculate Tax and Duty",
                            "url": "https://developers.easyship.com/reference/taxes_and_duties_calculate"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Calculate Taxes and Duties",
                            "url": "https://developers.easyship.com/docs/how-to-calculate-taxes-and-duties"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "could not calculate tax and duty"
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
                "$ref": "#/components/schemas/TaxAndDutyCreate"
              },
              "examples": {
                "with_country_ids": {
                  "summary": "with country IDs",
                  "value": {
                    "destination_country_id": 96,
                    "origin_country_id": 234,
                    "insurance_fee": 0,
                    "shipment_charge": 120.1,
                    "items": [
                      {
                        "duty_origin_country_id": 234,
                        "hs_code": "17029010",
                        "customs_value": 100
                      },
                      {
                        "duty_origin_country_id": 158,
                        "hs_code": "17029090",
                        "customs_value": 20.1
                      }
                    ]
                  }
                },
                "with_country_alpha2": {
                  "summary": "with country alpha2 codes",
                  "value": {
                    "origin_country_alpha2": "US",
                    "destination_country_alpha2": "CA",
                    "insurance_fee": 0,
                    "shipment_charge": 120.1,
                    "items": [
                      {
                        "duty_origin_country_alpha2": "US",
                        "hs_code": "17029010",
                        "customs_value": 100
                      },
                      {
                        "duty_origin_country_alpha2": "US",
                        "hs_code": "17029090",
                        "customs_value": 20.1
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
      "tax_and_duty_single": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "tax_and_duty": {
            "$ref": "#/components/schemas/TaxAndDuty"
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
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
      },
      "CountryID": {
        "type": "integer",
        "description": "Country ID based on Countries API",
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70,
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78,
          79,
          80,
          81,
          82,
          83,
          84,
          85,
          86,
          87,
          88,
          89,
          90,
          91,
          92,
          93,
          94,
          95,
          96,
          97,
          98,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          109,
          110,
          111,
          112,
          113,
          114,
          115,
          116,
          117,
          118,
          119,
          120,
          121,
          122,
          123,
          124,
          125,
          126,
          127,
          128,
          129,
          130,
          131,
          132,
          133,
          134,
          135,
          136,
          137,
          138,
          139,
          140,
          141,
          142,
          143,
          144,
          145,
          146,
          147,
          148,
          149,
          150,
          151,
          152,
          153,
          154,
          155,
          156,
          157,
          158,
          159,
          160,
          161,
          162,
          163,
          164,
          165,
          166,
          167,
          168,
          169,
          170,
          171,
          172,
          173,
          174,
          175,
          176,
          177,
          178,
          179,
          180,
          181,
          182,
          183,
          184,
          185,
          186,
          187,
          188,
          189,
          190,
          191,
          192,
          193,
          194,
          195,
          196,
          197,
          198,
          199,
          200,
          201,
          202,
          203,
          204,
          205,
          206,
          207,
          208,
          209,
          210,
          211,
          212,
          213,
          214,
          215,
          216,
          217,
          218,
          219,
          220,
          221,
          222,
          223,
          224,
          225,
          226,
          227,
          228,
          229,
          230,
          231,
          232,
          233,
          234,
          235,
          236,
          237,
          238,
          239,
          240,
          241,
          242,
          243,
          244,
          245,
          246,
          247,
          248,
          249,
          250
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
      },
      "TaxAndDuty": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "tax",
          "duty",
          "currency"
        ],
        "properties": {
          "tax": {
            "type": "number",
            "description": "Taxes or other fees that are applied to the item being purchased."
          },
          "duty": {
            "type": "number",
            "description": "Tariffs or fees applied to an imported or exported item."
          },
          "currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). Based on currency or origin_country_id in request body."
              }
            ]
          },
          "import_duty_details": {
            "type": "array",
            "nullable": true,
            "description": "Per line-item duty calculation breakdown in the response `currency`. Present when a duty calculation was performed, including when the duty amount is zero (e.g. FTA preferential rate). Amounts align with the top-level `duty` field. Null when no duty calculation was performed.",
            "items": {
              "$ref": "#/components/schemas/ImportDutyDetails"
            }
          }
        }
      },
      "TaxAndDutyCreate": {
        "oneOf": [
          {
            "type": "object",
            "title": "WITH COUNTRY IDS",
            "description": "Tax and duty calculation request with Country IDs (based on Countries API)",
            "additionalProperties": false,
            "required": [
              "destination_country_id",
              "origin_country_id",
              "insurance_fee",
              "shipment_charge",
              "items"
            ],
            "properties": {
              "destination_country_id": {
                "$ref": "#/components/schemas/CountryID"
              },
              "origin_country_id": {
                "$ref": "#/components/schemas/CountryID"
              },
              "insurance_fee": {
                "type": "number",
                "description": "Insurance fee of a shipment"
              },
              "shipment_charge": {
                "type": "number",
                "description": "Delivery fee of a shipment"
              },
              "currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). If not provided, the default currency will be based on origin_country_id."
                  }
                ]
              },
              "items": {
                "type": "array",
                "description": "Every element represents a collection of items grouped by HS code",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": [
                    "duty_origin_country_id",
                    "hs_code",
                    "customs_value"
                  ],
                  "properties": {
                    "duty_origin_country_id": {
                      "allOf": [
                        {
                          "$ref": "#/components/schemas/CountryID"
                        },
                        {
                          "description": "Country of origin for the item. This field is used to calculate import tariffs. Country ID can be found in our Country API."
                        }
                      ]
                    },
                    "hs_code": {
                      "type": "string",
                      "description": "Eight-digit HS code with last two digits as `00` (e.g. `42029100`), or a ten-digit regional HS code (e.g. `4202910010`).",
                      "pattern": "^\\d{8}(\\d{2})?$"
                    },
                    "customs_value": {
                      "type": "number",
                      "description": "Total value of this HS code group"
                    }
                  }
                }
              }
            }
          },
          {
            "type": "object",
            "title": "WITH COUNTRY ALPHA2",
            "description": "Tax and duty calculation request with country alpha2 codes",
            "additionalProperties": false,
            "required": [
              "destination_country_alpha2",
              "origin_country_alpha2",
              "insurance_fee",
              "shipment_charge",
              "items"
            ],
            "properties": {
              "destination_country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "origin_country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "insurance_fee": {
                "type": "number",
                "description": "Insurance fee of a shipment"
              },
              "shipment_charge": {
                "type": "number",
                "description": "Delivery fee of a shipment"
              },
              "currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). If not provided, the default currency will be based on origin_country_id."
                  }
                ]
              },
              "items": {
                "type": "array",
                "description": "Every element represents a collection of items grouped by HS code",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "required": [
                    "duty_origin_country_alpha2",
                    "hs_code",
                    "customs_value"
                  ],
                  "properties": {
                    "duty_origin_country_alpha2": {
                      "$ref": "#/components/schemas/CountryAlpha2"
                    },
                    "hs_code": {
                      "type": "string",
                      "description": "Eight-digit HS code with last two digits as `00` (e.g. `42029100`), or a ten-digit regional HS code (e.g. `4202910010`).",
                      "pattern": "^\\d{8}(\\d{2})?$"
                    },
                    "customs_value": {
                      "type": "number",
                      "description": "Total value of this HS code group"
                    }
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
```