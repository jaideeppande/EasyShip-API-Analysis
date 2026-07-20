# List all Payment Sources

Retrieve a list of payment sources.

Required authorization scope: `public.payment_source:read`


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
    "/2024-09/payment_sources": {
      "get": {
        "summary": "List all Payment Sources",
        "tags": [
          "Payment Sources"
        ],
        "operationId": "payment_sources_index",
        "description": "Retrieve a list of payment sources.\n\nRequired authorization scope: `public.payment_source:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1
            },
            "required": false,
            "description": "Page number to fetch, default: `1`",
            "example": 1
          },
          {
            "name": "per_page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "required": false,
            "description": "Number of records per page to fetch, default: `20`",
            "example": 10
          }
        ],
        "responses": {
          "200": {
            "description": "list of payment sources",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "payment_sources": [
                        {
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
                        {
                          "bank_account": {
                            "bank_name": "test",
                            "holder_name": "Test",
                            "is_verified": false,
                            "last_four_digits": "1111",
                            "routing_number": "1100000"
                          },
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "payment_method_type": "bank_account"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 2
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of payment sources"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/payment_source_list"
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
      "payment_source_list": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "payment_sources": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PaymentSource"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
          }
        }
      },
      "Pagination": {
        "type": "object",
        "description": "Pagination",
        "additionalProperties": false,
        "properties": {
          "next": {
            "type": "integer",
            "nullable": true
          },
          "count": {
            "type": "integer",
            "description": "The total number of items. The `null` value is used with countless pagination (used for faster response on large datasets, like shipments).",
            "nullable": true
          },
          "page": {
            "type": "integer",
            "description": "Current page"
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
      "MetaWithPagination": {
        "allOf": [
          {
            "type": "object",
            "properties": {
              "pagination": {
                "$ref": "#/components/schemas/Pagination"
              }
            }
          },
          {
            "$ref": "#/components/schemas/Meta"
          }
        ]
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
      }
    }
  }
}
```