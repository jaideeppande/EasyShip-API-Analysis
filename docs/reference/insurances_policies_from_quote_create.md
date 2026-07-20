# Create an Insurance Policy from Quote

> **Regional availability**: This endpoint is currently only available for US entities. Support for additional regions will be available in a future release.

Create an insurance policy from an existing quote.
The quote must be active and not expired.

Easyship relies on the tracking number and courier service name to register the shipment with the insurance provider.

Required authorization scope: `public.insurance_policy_3p:write`

> This API requires an updated contract with Easyship. Get in touch with your account manager or Easyship Support Team.


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
    "/2024-09/insurances/policies-from-quote": {
      "post": {
        "summary": "Create an Insurance Policy from Quote",
        "description": "> **Regional availability**: This endpoint is currently only available for US entities. Support for additional regions will be available in a future release.\n\nCreate an insurance policy from an existing quote.\nThe quote must be active and not expired.\n\nEasyship relies on the tracking number and courier service name to register the shipment with the insurance provider.\n\nRequired authorization scope: `public.insurance_policy_3p:write`\n\n> This API requires an updated contract with Easyship. Get in touch with your account manager or Easyship Support Team.\n",
        "operationId": "insurances_policies_from_quote_create",
        "tags": [
          "Insurance"
        ],
        "parameters": [],
        "security": [
          {
            "Bearer": []
          }
        ],
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/InsurancePolicyFromQuoteCreate"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "Insurance policy successfully created from quote",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/insurance_policy_from_quote_single"
                }
              }
            }
          },
          "422": {
            "description": "validation error",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/Error"
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
      "InsurancePolicyFromQuote": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "policy_id": {
            "type": "string",
            "description": "Unique identifier for this insurance policy"
          },
          "status": {
            "type": "string",
            "description": "Policy creation status"
          },
          "insured_value": {
            "type": "number",
            "description": "Total declared value insured"
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "insurance_fee": {
            "type": "number",
            "description": "Fee charged for the insurance policy"
          },
          "tracking_number": {
            "type": "string",
            "description": "Shipment tracking number"
          },
          "insurance_valid_from": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When insurance coverage begins (ISO 8601)"
          },
          "claim_window_opens": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When the claim window opens (ISO 8601)"
          },
          "claim_window_closes": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When the claim window closes (ISO 8601)"
          }
        }
      },
      "InsurancePolicyFromQuoteCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "policy"
        ],
        "properties": {
          "policy": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "quote_id",
              "tracking_number",
              "courier_service_name",
              "email_address",
              "first_name",
              "last_name"
            ],
            "properties": {
              "quote_id": {
                "type": "string",
                "format": "uuid",
                "description": "ID of the insurance quote to convert to a policy"
              },
              "tracking_number": {
                "type": "string",
                "description": "Shipment tracking number"
              },
              "courier_service_name": {
                "type": "string",
                "description": "Name of the courier service"
              },
              "email_address": {
                "type": "string",
                "format": "email",
                "description": "Email address for policy notifications"
              },
              "policy_holder_type": {
                "type": "string",
                "enum": [
                  "buyer",
                  "merchant"
                ],
                "description": "Who holds the insurance policy. Defaults to \"merchant\" if not provided"
              },
              "order_number": {
                "type": "string",
                "nullable": true,
                "description": "Your platform's order reference"
              },
              "first_name": {
                "type": "string",
                "description": "Policy holder first name"
              },
              "last_name": {
                "type": "string",
                "description": "Policy holder last name"
              },
              "order_date": {
                "type": "string",
                "format": "date",
                "description": "Date the order was placed"
              },
              "ship_date": {
                "type": "string",
                "format": "date",
                "description": "Date the shipment was dispatched"
              },
              "phone": {
                "type": "string",
                "description": "Policy holder phone number"
              },
              "send_email": {
                "type": "boolean",
                "description": "Whether to send a policy confirmation email"
              },
              "shipping_address1": {
                "type": "string",
                "description": "Shipping address line 1"
              },
              "shipping_address2": {
                "type": "string",
                "description": "Shipping address line 2"
              },
              "shipping_city": {
                "type": "string",
                "description": "Shipping city"
              },
              "shipping_state": {
                "type": "string",
                "description": "Shipping state or province"
              },
              "shipping_zip": {
                "type": "string",
                "description": "Shipping postal code"
              },
              "shipping_country": {
                "type": "string",
                "description": "Shipping country code (ISO 3166-1 alpha-2)"
              },
              "billing_address1": {
                "type": "string",
                "description": "Billing address line 1"
              },
              "billing_address2": {
                "type": "string",
                "description": "Billing address line 2"
              },
              "billing_city": {
                "type": "string",
                "description": "Billing city"
              },
              "billing_state": {
                "type": "string",
                "description": "Billing state or province"
              },
              "billing_zip": {
                "type": "string",
                "description": "Billing postal code"
              },
              "billing_country": {
                "type": "string",
                "description": "Billing country code (ISO 3166-1 alpha-2)"
              }
            }
          }
        }
      },
      "insurance_policy_from_quote_single": {
        "type": "object",
        "description": "Insurance policy created from quote",
        "additionalProperties": false,
        "properties": {
          "insurance_policy": {
            "$ref": "#/components/schemas/InsurancePolicyFromQuote"
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