# Confirm Payment Source

Easyship integrate with Stripe Setup Intent to collect credit card and bank account information.
Ref: https://docs.stripe.com/payments/save-and-reuse-cards-only

Here's a example of how you can process 3DS for card setup intent on the client side. Once the validation is completed, you can use the `setup_intent.id` to finalize the payment source in Easyship.

<details>
  <summary>Confirm 3DS Example</summary>

  ```html
    <html>
      <body>
        <form id="form">
          <label>
            <span>Intent Secret</span>
            <input id="secret" class="field" placeholder="" />
          </label>
          <div class="button-row">
            <button>Submit</button>
          </div>
        </form>

        <script src="https://js.stripe.com/v3/"></script>
        <script>
          // Retrieve Easyship stripe publishable api key through `GET /2024-01/account/stripe`
          var stripe = Stripe('Easyship_stripe_publishable_api_key');

          // Handle form submission and trigger 3DS
          var form = document.getElementById('form');
          form.addEventListener('submit', function (event) {
            event.preventDefault();

            var secret = document.getElementById('secret').value;
            console.log(secret)

            stripe.confirmCardSetup(secret).then(function (result) {
              if (result.error) {
                // error handling
              } else {
                // You would receive the `setup intent id` with prefix `seti_`.
                // `POST /2024-01/payment_sources/confirm` here to finalize the payment source in Easyship
              }
            });
          });
        </script>
      </body>
    </html>
  ```

</details>

Should the setup intent not have undergone 3D Secure, you'll receive a status code 202, indicating the need to process 3D Secure.

If the setup intent is for us bank account. You'll receive a status code 202, indicating the need to do micro deposit verification. The verification url will be provided in the response and the verification code will be sent to the email address attached to the bank account.

Reference: https://docs.stripe.com/payments/ach-debit/set-up-payment?platform=web&payment-ui=direct-api#optional:-send-custom-email-notifications

Once the verification is completed, stripe webhook would mark your bank account payment source activated.

Required authorization scope: `public.payment_source:write`


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
      "name": "Payment Sources"
    }
  ],
  "paths": {
    "/2024-09/payment_sources/confirm": {
      "post": {
        "summary": "Confirm Payment Source",
        "tags": [
          "Payment Sources"
        ],
        "operationId": "payment_sources_confrim_3ds_create",
        "description": "Easyship integrate with Stripe Setup Intent to collect credit card and bank account information.\nRef: https://docs.stripe.com/payments/save-and-reuse-cards-only\n\nHere's a example of how you can process 3DS for card setup intent on the client side. Once the validation is completed, you can use the `setup_intent.id` to finalize the payment source in Easyship.\n\n<details>\n  <summary>Confirm 3DS Example</summary>\n\n  ```html\n    <html>\n      <body>\n        <form id=\"form\">\n          <label>\n            <span>Intent Secret</span>\n            <input id=\"secret\" class=\"field\" placeholder=\"\" />\n          </label>\n          <div class=\"button-row\">\n            <button>Submit</button>\n          </div>\n        </form>\n\n        <script src=\"https://js.stripe.com/v3/\"></script>\n        <script>\n          // Retrieve Easyship stripe publishable api key through `GET /2024-01/account/stripe`\n          var stripe = Stripe('Easyship_stripe_publishable_api_key');\n\n          // Handle form submission and trigger 3DS\n          var form = document.getElementById('form');\n          form.addEventListener('submit', function (event) {\n            event.preventDefault();\n\n            var secret = document.getElementById('secret').value;\n            console.log(secret)\n\n            stripe.confirmCardSetup(secret).then(function (result) {\n              if (result.error) {\n                // error handling\n              } else {\n                // You would receive the `setup intent id` with prefix `seti_`.\n                // `POST /2024-01/payment_sources/confirm` here to finalize the payment source in Easyship\n              }\n            });\n          });\n        </script>\n      </body>\n    </html>\n  ```\n\n</details>\n\nShould the setup intent not have undergone 3D Secure, you'll receive a status code 202, indicating the need to process 3D Secure.\n\nIf the setup intent is for us bank account. You'll receive a status code 202, indicating the need to do micro deposit verification. The verification url will be provided in the response and the verification code will be sent to the email address attached to the bank account.\n\nReference: https://docs.stripe.com/payments/ach-debit/set-up-payment?platform=web&payment-ui=direct-api#optional:-send-custom-email-notifications\n\nOnce the verification is completed, stripe webhook would mark your bank account payment source activated.\n\nRequired authorization scope: `public.payment_source:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "setup intent successfully confirmed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "payment_source": {
                        "card": {
                          "brand": "visa",
                          "expiration_month": "9",
                          "expiration_year": "2025",
                          "holder_name": null,
                          "last_four_digits": "4242"
                        },
                        "id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "payment_method_type": "card"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "setup intent successfully confirmed"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/payment_source_single"
                }
              }
            }
          },
          "202": {
            "description": "action required",
            "content": {
              "application/json": {
                "examples": {
                  "3d_validation": {
                    "value": {
                      "action_required": {
                        "code": "require_3ds_validation",
                        "data": {
                          "client_secret": "seti_1PuVYCKqoWrxoPJuwVAIIMhy_secret_Qm3fS25Q689Z5xxKqN2vgVD76fqJISA",
                          "intent_id": "seti_1PuVYCKqoWrxoPJuwVAIIMhy"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "3D validation"
                  },
                  "require_bank_account_verification": {
                    "value": {
                      "action_required": {
                        "code": "require_micro_deposit_verification",
                        "data": {
                          "client_secret": "seti_1PuVrIJBnUpvN50zezHd7zjM_secret_Qm3zk9X1GlVNewkfMeI3TLCHS2ZNnD3",
                          "intent_id": "seti_1PuVrIJBnUpvN50zezHd7zjM",
                          "verification_url": "https://payments.stripe.com/microdeposit/sacs_test_YWNjdF8xN25Oc3pKQm5VcHZONTB6LHNhX25vbmNlX1FtNDFFVW55S1FzRnJoV3cwV253eDg2SGpPOVBHN000000wC5N1dar"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "require_bank_account_verification"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/require_action_single"
                }
              }
            }
          },
          "422": {
            "description": "payment source already existed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Payment source already exists"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Confirm Payment Source",
                            "url": "https://developers.easyship.com/reference/payment_sources_confrim_3ds_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "payment source already existed"
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
                "$ref": "#/components/schemas/PaymentSourceConfirm"
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
      "payment_source_single": {
        "type": "object",
        "description": "Payment source details",
        "additionalProperties": false,
        "properties": {
          "payment_source": {
            "$ref": "#/components/schemas/PaymentSource"
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
      "PaymentSource": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Payment source id in Easyship"
          },
          "third_party_source_id": {
            "type": "string",
            "description": "Third party payment source id"
          },
          "payment_method_type": {
            "type": "string",
            "enum": [
              "card",
              "bank_account"
            ]
          },
          "bank_account": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "bank_name": {
                "type": "string",
                "description": "Bank name"
              },
              "holder_name": {
                "type": "string",
                "description": "Account holder name"
              },
              "last_four_digits": {
                "type": "string",
                "description": "Last four digits of bank account number"
              },
              "routing_number": {
                "type": "string",
                "description": "Routing number"
              },
              "is_verified": {
                "type": "boolean",
                "description": "Whether the bank account is verified by Stripe"
              }
            }
          },
          "card": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "brand": {
                "type": "string",
                "description": "Credit card brand",
                "example": "visa"
              },
              "expiration_year": {
                "type": "string",
                "description": "The expiration year of the card",
                "example": "2023"
              },
              "expiration_month": {
                "type": "string",
                "description": "The expiration month of the card",
                "example": "01"
              },
              "last_four_digits": {
                "type": "string",
                "description": "Last four digits of credit card"
              },
              "holder_name": {
                "type": "string",
                "description": "Card holder name",
                "nullable": true
              }
            }
          }
        }
      },
      "PaymentSourceConfirm": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "intent_id"
        ],
        "properties": {
          "intent_id": {
            "type": "string",
            "description": "Reference ID to confirm the payment source. It could be found in the response of `POST /2024-09/payment_sources`."
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