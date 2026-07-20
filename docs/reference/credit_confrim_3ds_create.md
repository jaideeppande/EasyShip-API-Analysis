# Confirm Credit Top-up

Easyship integrate with Stripe Payment Intent to collect credit card payments.
Ref: https://stripe.com/docs/payments/payment-intents

The confirmation process includes the collection of payment and creation of a transaction record (credit) in your account.

Should the payment intent not have undergone 3D Secure, you'll receive a status code 202, indicating the need to process 3D Secure.

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
    "/2024-09/account/credit/confirm_3ds": {
      "post": {
        "summary": "Confirm Credit Top-up",
        "tags": [
          "Credit"
        ],
        "operationId": "credit_confrim_3ds_create",
        "description": "Easyship integrate with Stripe Payment Intent to collect credit card payments.\nRef: https://stripe.com/docs/payments/payment-intents\n\nThe confirmation process includes the collection of payment and creation of a transaction record (credit) in your account.\n\nShould the payment intent not have undergone 3D Secure, you'll receive a status code 202, indicating the need to process 3D Secure.\n\nRequired authorization scope: `public.payment:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "payment intent successfully confirmed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "credit": {
                        "available_balance": 200,
                        "balance": 0,
                        "currency": "HKD"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "payment intent successfully confirmed"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/credit_single"
                }
              }
            }
          },
          "202": {
            "description": "required 3D validation",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "action_required": {
                        "code": "require_3ds_validation",
                        "data": {
                          "client_secret": "pi_3PuTOWKqoWrxoPJu1NVmtJcA_secret_mAZ8WXoOGYc31zLAW26spgFDv",
                          "intent_id": "pi_3PuTOWKqoWrxoPJu1NVmtJcA"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "required 3D validation"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/require_action_single"
                }
              }
            }
          },
          "422": {
            "description": "payment intent has been confirmed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "You cannot confirm this PaymentIntent because it has already succeeded after being previously confirmed."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Confirm Credit Top-up",
                            "url": "https://developers.easyship.com/reference/credit_confrim_3ds_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "payment intent has been confirmed"
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
                "$ref": "#/components/schemas/CreditConfirm"
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
      "require_action_single": {
        "type": "object",
        "description": "Require action",
        "additionalProperties": false,
        "properties": {
          "action_required": {
            "$ref": "#/components/schemas/RequireAction"
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
          }
        }
      },
      "credit_single": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "credit": {
            "$ref": "#/components/schemas/Credit"
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
      "3DSValidation": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "code": {
            "type": "string",
            "description": "Action code",
            "enum": [
              "require_3ds_validation"
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "intent_id": {
                "type": "string",
                "description": "Reference ID to confirm intent after 3DS validation"
              },
              "client_secret": {
                "type": "string",
                "description": "Client secret for the 3DS validation flow"
              }
            }
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
      "Credit": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "balance": {
            "type": "number",
            "description": "Total amount in the account without considering holds or pending transactions."
          },
          "available_balance": {
            "type": "number",
            "description": "Funds accessible for use, accounting for holds and pending transactions."
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
      "CreditConfirm": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "intent_id"
        ],
        "properties": {
          "intent_id": {
            "type": "string",
            "description": "Reference ID to confirm the credit. If your credit card requires 3DS validation, it could be found in the response of `POST /2023-01/account/credit`."
          }
        }
      },
      "RequireAction": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/3DSValidation"
          },
          {
            "$ref": "#/components/schemas/RequireMicroDepositVerification"
          },
          {
            "$ref": "#/components/schemas/RequireBankAccountInfo"
          }
        ],
        "discriminator": {
          "propertyName": "code",
          "mapping": {
            "require_3ds_validation": "#/components/schemas/3DSValidation",
            "require_micro_deposit_verification": "#/components/schemas/RequireMicroDepositVerification",
            "require_bank_account_info": "#/components/schemas/RequireBankAccountInfo"
          }
        }
      },
      "RequireBankAccountInfo": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "code": {
            "type": "string",
            "description": "Action code",
            "enum": [
              "require_bank_account_info"
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "intent_id": {
                "type": "string",
                "description": "Reference ID to confirm intent after collecting bank account information"
              },
              "client_secret": {
                "type": "string",
                "description": "Client secret for collection bank account information"
              }
            }
          }
        }
      },
      "RequireMicroDepositVerification": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "code": {
            "type": "string",
            "description": "Action code",
            "enum": [
              "require_micro_deposit_verification"
            ]
          },
          "data": {
            "type": "object",
            "properties": {
              "intent_id": {
                "type": "string",
                "description": "Reference ID of the bank account setup intent"
              },
              "verification_url": {
                "type": "string",
                "nullable": true,
                "description": "Link to Stripe micro deposit verification page"
              },
              "client_secret": {
                "type": "string",
                "description": "Client secret for customizing verification page"
              }
            }
          }
        }
      }
    }
  }
}
```