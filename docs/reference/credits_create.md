# Add credit

Top up your credit.

In case your payment source (credit card) requires 3D validation use the Stripe SDK.

To detect any fraudulent activities and initiate Radar and 3D Secure, integrate `handleCardAction` from Stripe.js.
Reference: https://stripe.com/docs/js/payment_intents/handle_card_action

Example:
```html
<script src="https://js.stripe.com/v3/"></script>
<script>
   // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`
   var stripe = Stripe('stripe_publishable_api_key');

   // When `POST /2024-09/account/credit` returns status code 202, retrieve the secret in the response.
   var secret = response.action.client_secret

   // 3D validation
   stripe.handleCardAction(secret).then(function (result) {
     if (result.error) {
       // error handling
     } else {
       // You would receive stripe payment_intent object
       // `POST /2024-09/account/credit/confirm_3ds` with payment_intent.id to confirm credit top-up
     }
   });
 </script>
```

> If you are using an authorized bank account as your payment method, the transaction might take around 1 to 3 days to complete.

Required authorization scope: `public.payment:write`


# OpenAPI definition

````json
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
    "/2024-09/account/credit": {
      "post": {
        "summary": "Add credit",
        "tags": [
          "Credit"
        ],
        "operationId": "credits_create",
        "description": "Top up your credit.\n\nIn case your payment source (credit card) requires 3D validation use the Stripe SDK.\n\nTo detect any fraudulent activities and initiate Radar and 3D Secure, integrate `handleCardAction` from Stripe.js.\nReference: https://stripe.com/docs/js/payment_intents/handle_card_action\n\nExample:\n```html\n<script src=\"https://js.stripe.com/v3/\"></script>\n<script>\n   // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`\n   var stripe = Stripe('stripe_publishable_api_key');\n\n   // When `POST /2024-09/account/credit` returns status code 202, retrieve the secret in the response.\n   var secret = response.action.client_secret\n\n   // 3D validation\n   stripe.handleCardAction(secret).then(function (result) {\n     if (result.error) {\n       // error handling\n     } else {\n       // You would receive stripe payment_intent object\n       // `POST /2024-09/account/credit/confirm_3ds` with payment_intent.id to confirm credit top-up\n     }\n   });\n </script>\n```\n\n> If you are using an authorized bank account as your payment method, the transaction might take around 1 to 3 days to complete.\n\nRequired authorization scope: `public.payment:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "credit successfully added",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "credit": {
                        "available_balance": 10,
                        "balance": 0,
                        "currency": "HKD"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "credit successfully added"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/credit_single"
                }
              }
            }
          },
          "202": {
            "description": "3D validation",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "action_required": {
                        "code": "require_3ds_validation",
                        "data": {
                          "client_secret": "pi_3PuTZXKqoWrxoPJu1ilKTpuz_secret_Can5GoWe8uiy1ynVzmSypjzvd",
                          "intent_id": "pi_3PuTZXKqoWrxoPJu1ilKTpuz"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "3D validation"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/require_action_single"
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
                          "The Payment Source was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Add Credit",
                            "url": "https://developers.easyship.com/reference/credits_create"
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
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/CreditCreate"
              },
              "examples": {
                "credit_successfully_added": {
                  "summary": "credit successfully added",
                  "value": {
                    "payment_source_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                    "amount": 10
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
      "CreditCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "payment_source_id",
          "amount"
        ],
        "properties": {
          "payment_source_id": {
            "type": "string",
            "description": "Source ID based on Payment Source API. Your payment source should have the `card` accept type. Use default card if this property is not provided."
          },
          "amount": {
            "type": "number",
            "description": "Amount of credits to be added to a current account."
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
````