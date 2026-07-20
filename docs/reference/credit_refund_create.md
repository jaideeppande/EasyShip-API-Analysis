# Refund a Credit

Refund your credit.

Required authorization scope: `public.payment:write`


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
      "name": "Credit"
    }
  ],
  "paths": {
    "/2024-09/account/credit/refund": {
      "post": {
        "summary": "Refund a Credit",
        "tags": [
          "Credit"
        ],
        "operationId": "credit_refund_create",
        "description": "Refund your credit.\n\nRequired authorization scope: `public.payment:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "specified credit amount successfully refunded",
            "content": {
              "application/json": {
                "examples": {
                  "refund_balance": {
                    "value": {
                      "refunds": [
                        {
                          "amount": 10,
                          "currency": "HKD",
                          "payment_source_id": "01563646-58c1-4607-8fe0-cae3e33c0001"
                        }
                      ],
                      "meta": {
                        "total_refunded": 10,
                        "total_non_refunded": 0,
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "entire credit balance successfully refunded"
                  },
                  "refund_specified_amount": {
                    "value": {
                      "refunds": [
                        {
                          "amount": 5,
                          "currency": "HKD",
                          "payment_source_id": "01563646-58c1-4607-8fe0-cae3e33c0001"
                        }
                      ],
                      "meta": {
                        "total_refunded": 5,
                        "total_non_refunded": 0,
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "specified credit amount successfully refunded"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/credit_refund_list"
                }
              }
            }
          },
          "422": {
            "description": "insufficient balance",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Refund amount must be less than or equal to company balance"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Refund a Credit",
                            "url": "https://developers.easyship.com/reference/credit_refund_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "insufficient balance"
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
                "$ref": "#/components/schemas/CreditRefundCreate"
              },
              "examples": {
                "entire_credit_balance_successfully_refunded": {
                  "summary": "Refund balance",
                  "value": {}
                },
                "specified_credit_amount_successfully_refunded": {
                  "summary": "Refund specified amount",
                  "value": {
                    "amount": 5
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
      "credit_refund_list": {
        "type": "object",
        "description": "List of credit refunds",
        "additionalProperties": false,
        "properties": {
          "refunds": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/CreditRefund"
            }
          },
          "meta": {
            "allOf": [
              {
                "type": "object",
                "properties": {
                  "total_refunded": {
                    "type": "number",
                    "description": "Amount of credit successfully refunded"
                  },
                  "total_non_refunded": {
                    "type": "number",
                    "description": "Amount of credit unsuccessfully refunded"
                  }
                }
              },
              {
                "$ref": "#/components/schemas/Meta"
              }
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
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
          }
        }
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
      "CreditRefund": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "payment_source_id": {
            "type": "string",
            "format": "uuid",
            "description": "Payment Source ID for refunded payment"
          },
          "amount": {
            "type": "number",
            "description": "Total amount refunded"
          },
          "currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Currency code for the account. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          }
        }
      },
      "CreditRefundCreate": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "amount": {
            "type": "number",
            "nullable": true,
            "description": "Amount of credits to be refunded from a current account. **Refunds your entire balance if this value is not provided.**"
          }
        }
      }
    }
  }
}
```