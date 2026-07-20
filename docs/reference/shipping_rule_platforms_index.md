# List all Platform Names

Retrieve a list of available platform names for shipping rules.

Required authorization scope: `public.shipping_rule:write`  


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
      "name": "Shipping Rules"
    }
  ],
  "paths": {
    "/2024-09/shipping_rules/platforms": {
      "get": {
        "summary": "List all Platform Names",
        "tags": [
          "Shipping Rules"
        ],
        "operationId": "shipping_rule_platforms_index",
        "description": "Retrieve a list of available platform names for shipping rules.\n\nRequired authorization scope: `public.shipping_rule:write`  \n",
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
            "description": "list of platform names",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "platforms": [
                        {
                          "name": "SellerCenter"
                        },
                        {
                          "name": "eBay"
                        },
                        {
                          "name": "Amazon"
                        },
                        {
                          "name": "Shopify"
                        },
                        {
                          "name": "EtsyGroup"
                        },
                        {
                          "name": "WooCommerceGroup"
                        },
                        {
                          "name": "Shopmatic"
                        },
                        {
                          "name": "API"
                        },
                        {
                          "name": "AlloyAutomation"
                        },
                        {
                          "name": "Builderall"
                        },
                        {
                          "name": "Make"
                        },
                        {
                          "name": "Odoo"
                        },
                        {
                          "name": "Omnyfy"
                        },
                        {
                          "name": "Zapier"
                        },
                        {
                          "name": "BackerKit"
                        },
                        {
                          "name": "Netsuite"
                        },
                        {
                          "name": "Celigo"
                        },
                        {
                          "name": "SkuVault"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": 2,
                          "count": 49
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of platform names"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_platform_list"
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
      "shipping_rule_platform_list": {
        "type": "object",
        "description": "List of plaforms for Shipping Rules",
        "additionalProperties": false,
        "properties": {
          "platforms": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShippingRulePlatform"
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
      "ShippingRulePlatform": {
        "type": "object",
        "description": "Platform",
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "Platform name for shipping rules."
          }
        }
      }
    }
  }
}
```