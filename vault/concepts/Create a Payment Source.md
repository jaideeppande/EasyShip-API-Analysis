---
type: concept
---
# Create a Payment Source

Create a payment sources.

Easyship won't hold the details of your credit card. We use `stripe token` to attach the credit card to your easyship account on Stripe.
Please upload your credit card to stripe via Stripe Token JS.

Example:
<details>
  <summary>Stripe Token JS Example</summary>

  ```html
  <script src="https://js.stripe.com/v3/"></script>
  <script>
    // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`
    var stripe = Stripe('stripe_publishable_api_key');

    // Create an instance of Elements.
    // https://stripe.com/docs/js/elements_object/create_element?type=card
    var elements = stripe.elements();

    // Create a CardElement
    var card = elements.create('card')

    // Create your token from the CardElement data
    // https://stripe.com/docs/js/tokens/create_token?type=cardElement
    stripe.createToken(card).then(function (result) {
      if (result.error) {
        // error handling
      } else {
        // You would receive the `stripe token` with prefix `tok_`.
        // `POST /2024-09/payment_sources` here to attach your card to Easyship
        var token = result.token;
      }
    });
  </script>
  ```

</details>

When the credit card needs 3DS (with response status code 202), proceed with the next step found in `POST /2024-09/payment_sources/confirm`.

If the payment source type is bank account, you'll receive a status code 202, indicating the need to submit the bank account information.
Easyship won't hold the details of your bank account. We use `setup intent` to attach the bank account to your easyship account on Stripe.

Note: A bank account payment source is only available for US companies.

Example:
<details>
  <summary>Stripe Bank Account JS Example</summary>

  ```html
    <script>
      // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`
      const stripe = Stripe('stripe_publishable_api_key');

      // Use the form that already exists on the web page.
      const paymentMethodForm = document.getElementById('payment-method-form');

      paymentMethodForm.addEventListener('submit', (ev) => {
        ev.preventDefault();
        const accountHolderNameField = document.getElementById('account-holder-name');
        const emailField = document.getElementById('email-field');

        // Retrieve the client secret from POST /2024-09/payment_sources.
        const clientSecretField = document.getElementById('client-secret-field');

        // Calling this method will open the dialog to submit bank account information.
        stripe.collectBankAccountForSetup({
          clientSecret: clientSecretField.value,
          params: {
            payment_method_type: 'us_bank_account',
            payment_method_data: {
              billing_details: {
                name: accountHolderNameField.value,
                email: emailField.value,
              },
            },
          }
        })
        .then(({setupIntent, error}) => {
          if (error) {
            console.error(error.message);
          } else {
            // POST /2024-09/payment_sources/confirm to finalize the bank account payment source at Easyship
          }
        });
      });
    </script>
  ```

</details>

Once the bank account information has been submitted successfully, proceed with the next step found in `POST /2024-09/payment_sources/confirm`.


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
    "/2024-09/payment_sources": {
      "post": {
        "summary": "Create a Payment Source",
        "tags": [
          "Payment Sources"
        ],
        "operationId": "payment_sources_create",
        "description": "Create a payment sources.\n\nEasyship won't hold the details of your credit card. We use `stripe token` to attach the credit card to your easyship account on Stripe.\nPlease upload your credit card to stripe via Stripe Token JS.\n\nExample:\n<details>\n  <summary>Stripe Token JS Example</summary>\n\n  ```html\n  <script src=\"https://js.stripe.com/v3/\"></script>\n  <script>\n    // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`\n    var stripe = Stripe('stripe_publishable_api_key');\n\n    // Create an instance of Elements.\n    // https://stripe.com/docs/js/elements_object/create_element?type=card\n    var elements = stripe.elements();\n\n    // Create a CardElement\n    var card = elements.create('card')\n\n    // Create your token from the CardElement data\n    // https://stripe.com/docs/js/tokens/create_token?type=cardElement\n    stripe.createToken(card).then(function (result) {\n      if (result.error) {\n        // error handling\n      } else {\n        // You would receive the `stripe token` with prefix `tok_`.\n        // `POST /2024-09/payment_sources` here to attach your card to Easyship\n        var token = result.token;\n      }\n    });\n  </script>\n  ```\n\n</details>\n\nWhen the credit card needs 3DS (with response status code 202), proceed with the next step found in `POST /2024-09/payment_sources/confirm`.\n\nIf the payment source type is bank account, you'll receive a status code 202, indicating the need to submit the bank account information.\nEasyship won't hold the details of your bank account. We use `setup intent` to attach the bank account to your easyship account on Stripe.\n\nNote: A bank account payment source is only available for US companies.\n\nExample:\n<details>\n  <summary>Stripe Bank Account JS Example</summary>\n\n  ```html\n    <script>\n      // Retrieve Easyship stripe publishable api key through `GET /2024-09/account/stripe`\n      const stripe = Stripe('stripe_publishable_api_key');\n\n      // Use the form that already exists on the web page.\n      const paymentMethodForm = document.getElementById('payment-method-form');\n\n      paymentMethodForm.addEventListener('submit', (ev) => {\n        ev.preventDefault();\n        const accountHolderNameField = document.getElementById('account-holder-name');\n        const emailField = document.getElementById('email-field');\n\n        // Retrieve the client secret from POST /2024-09/payment_sources.\n        const clientSecretField = document.getElementById('client-secret-field');\n\n        // Calling this method will open the dialog to submit bank account information.\n        stripe.collectBankAccountForSetup({\n          clientSecret: clientSecretField.value,\n          params: {\n            payment_method_type: 'us_bank_account',\n            payment_method_data: {\n              billing_details: {\n                name: accountHolderNameField.value,\n                email: emailField.value,\n              },\n            },\n          }\n        })\n        .then(({setupIntent, error}) => {\n          if (error) {\n            console.error(error.message);\n          } else {\n            // POST /2024-09/payment_sources/confirm to finalize the bank account payment source at Easyship\n          }\n        });\n      });\n    </script>\n  ```\n\n</details>\n\nOnce the bank account information has been submitted successfully, proceed with the next step found in `POST /2024-09/payment_sources/confirm`.\n\n\nRequired authorization scope: `public.payment_source:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "payment source successfully created",
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
                          "holder_name": "local test",
                          "last_four_digits": "4242"
                        },
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "payment_method_type": "card"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "payment source successfully created"
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
                          "client_secret": "seti_1PuTddKqoWrxoPJuvusXcxHn_secret_Qm1huwxwRpNSebdWFuWjxTDPeifjlWj",
                          "intent_id": "seti_1PuTddKqoWrxoPJuvusXcxHn"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "3D validation"
                  },
                  "require_bank_account_information": {
                    "value": {
                      "action_required": {
                        "code": "require_bank_account_info",
                        "data": {
                          "client_secret": "seti_1PuTdeJBnUpvN50zsEmGG7OT_secret_Qm1higMjeUThnurP5gQPvazo5VsjGbG",
                          "intent_id": "seti_1PuTdeJBnUpvN50zsEmGG7OT"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "require_bank_account_information"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/require_action_single"
                }
              }
            }
          },
          "422": {
            "description": "credit card has expired",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Your card has expired."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Payment Source",
                            "url": "https://developers.easyship.com/reference/payment_sources_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "credit card has expired"
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
                "$ref": "#/components/schemas/PaymentSourceCreate"
              },
              "examples": {
                "payment_source_successfully_created": {
                  "summary": "payment source successfully created",
                  "value": {
                    "type": "card",
                    "stripe_token": "tok_visa",
                    "holder": {
                      "name": "local test"
                    }
                  }
                },
                "action_required": {
                  "summary": "action required",
                  "value": {
                    "type": "bank_account"
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
      "PaymentSourceCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/PaymentSourceCreateCard"
          },
          {
            "$ref": "#/components/schemas/PaymentSourceCreateBankAccount"
          }
        ],
        "discriminator": {
          "propertyName": "type",
          "mapping": {
            "card": "#/components/schemas/PaymentSourceCreateCard",
            "bank_account": "#/components/schemas/PaymentSourceCreateBankAccount"
          }
        }
      },
      "PaymentSourceCreateBankAccount": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "type"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of the payment source",
            "enum": [
              "bank_account"
            ]
          }
        }
      },
      "PaymentSourceCreateCard": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "stripe_token",
          "type"
        ],
        "properties": {
          "type": {
            "type": "string",
            "description": "Type of the payment source",
            "enum": [
              "card"
            ]
          },
          "verify_3ds": {
            "type": "boolean",
            "description": "Force 3DS validation. If 3DS is required, a Stripe Client Secret will be provided for confirmation. The confirmation must be handled with [Stripe JS](https://docs.stripe.com/js/setup_intents/handle_next_action). This behavior will be enforced in the upcoming API version.",
            "default": false
          },
          "stripe_token": {
            "type": "string",
            "description": "Token generated via stripe js."
          },
          "holder": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "name": {
                "type": "string",
                "description": "Card holder's name. This will only be applicable if the name was not assigned during token generation.",
                "maxLength": 24
              }
            }
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
