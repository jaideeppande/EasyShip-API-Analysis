# Update a Payment Source

Update a card payment source.

Required authorization scope: `public.payment_source:write`


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
      "name": "Payment Sources"
    }
  ],
  "paths": {
    "/2024-09/payment_sources/{payment_source_id}": {
      "parameters": [
        {
          "name": "payment_source_id",
          "in": "path",
          "required": true,
          "description": "Payment source ID provided when creating",
          "schema": {
            "type": "string"
          }
        }
      ],
      "patch": {
        "summary": "Update a Payment Source",
        "tags": [
          "Payment Sources"
        ],
        "operationId": "payment_sources_update",
        "description": "Update a card payment source.\n\nRequired authorization scope: `public.payment_source:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "payment source successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "payment_source": {
                        "card": {
                          "brand": "Visa",
                          "expiration_month": "12",
                          "expiration_year": "2099",
                          "holder_name": "Test",
                          "last_four_digits": "1111"
                        },
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "payment_method_type": "card"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "payment source successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/payment_source_single"
                }
              }
            }
          },
          "404": {
            "description": "No record found",
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
                            "name": "Update a Payment Source",
                            "url": "https://developers.easyship.com/reference/payment_sources_update"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "No record found"
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
                "$ref": "#/components/schemas/PaymentSourceUpdate"
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
      "PaymentSourceUpdate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "set_default_for"
        ],
        "properties": {
          "set_default_for": {
            "type": "string",
            "description": "Set current payment source as the default for selected property",
            "enum": [
              "shipment"
            ]
          }
        }
      }
    }
  }
}
```