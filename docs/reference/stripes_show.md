# Get a Stripe Public Key

Retrieve a stripe public key according to your registration country.

Required authorization scope: `public.payment_sources:read` 


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
    "/2024-09/account/stripe": {
      "get": {
        "summary": "Get a Stripe Public Key",
        "tags": [
          "Payment Sources"
        ],
        "operationId": "stripes_show",
        "description": "Retrieve a stripe public key according to your registration country.\n\nRequired authorization scope: `public.payment_sources:read` \n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "stripe public key",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "stripe": {
                        "public_key": "pk_test_12345"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "stripe public key"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/stripe_single"
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
      "stripe_single": {
        "type": "object",
        "description": "Stripe public api key",
        "additionalProperties": false,
        "properties": {
          "stripe": {
            "$ref": "#/components/schemas/Stripe"
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
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
      "Stripe": {
        "type": "object",
        "description": "Easyship Stripe public information",
        "additionalProperties": false,
        "properties": {
          "public_key": {
            "type": "string"
          }
        }
      }
    }
  }
}
```