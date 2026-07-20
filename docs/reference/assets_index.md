# List all Assets

Retrieve a list of assets.

Required authorization scope: `public.asset:read`


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
    "/2024-09/account/assets": {
      "get": {
        "summary": "List all Assets",
        "tags": [
          "Settings"
        ],
        "operationId": "assets_index",
        "description": "Retrieve a list of assets.\n\nRequired authorization scope: `public.asset:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "sort_by",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "type",
                "created_at"
              ]
            },
            "required": false,
            "description": "Sort records by listed columns. Default: `created_at`",
            "example": "created_at"
          },
          {
            "name": "sort_direction",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "ASC",
                "DESC"
              ]
            },
            "required": false,
            "description": "Set the sort direction. Default: `DESC`",
            "example": "ASC"
          },
          {
            "name": "type",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "logo",
                "tracking_email_ad",
                "tracking_page_ad"
              ]
            },
            "required": false,
            "description": "Filter records by asset type",
            "example": "logo"
          }
        ],
        "responses": {
          "200": {
            "description": "list of assets",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "assets": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "name": null,
                          "type": "tracking_email_ad",
                          "url": "https://s3.amazonaws.com/test/assets/01563646-58c1-4607-8fe0-cae3e33c0001/tracking_email_ad/01563646-58c1-4607-8fe0-cae3e33c0001/main.png?1645532460"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of assets"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/asset_list"
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
      "asset_list": {
        "type": "object",
        "description": "List all assets",
        "additionalProperties": false,
        "properties": {
          "assets": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Asset"
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
      "Asset": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "type": {
            "type": "string",
            "enum": [
              "logo",
              "tracking_page_ad",
              "tracking_email_ad"
            ],
            "description": "Asset type"
          },
          "name": {
            "type": "string",
            "description": "Asset name",
            "nullable": true
          },
          "url": {
            "type": "string",
            "format": "uri",
            "description": "Asset link",
            "example": "https://s3.amazonaws.com/test/assets/0001/logo/6c8e/main.png?1645532460"
          }
        }
      }
    }
  }
}
```