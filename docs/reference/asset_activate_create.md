# Activate Assets

Activate specific uploaded asset and define other assets of the same type as inactive.

Required authorization scope: `public.asset:write`


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
      "name": "Settings"
    }
  ],
  "paths": {
    "/2024-09/account/assets/{id}/activate": {
      "post": {
        "summary": "Activate Assets",
        "tags": [
          "Settings"
        ],
        "operationId": "asset_activate_create",
        "description": "Activate specific uploaded asset and define other assets of the same type as inactive.\n\nRequired authorization scope: `public.asset:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "id",
            "in": "path",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true,
            "description": "Asset ID",
            "example": "01563646-58c1-4607-8fe0-cae3e33c0001"
          }
        ],
        "responses": {
          "200": {
            "description": "asset successfully activated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "success": {
                        "message": "Asset successfully activated"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "asset successfully activated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Success"
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
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
          }
        }
      },
      "Success": {
        "type": "object",
        "description": "General success response",
        "additionalProperties": false,
        "properties": {
          "success": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "message": {
                "type": "string"
              }
            }
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