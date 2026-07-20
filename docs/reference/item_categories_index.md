# List all Item Categories

Retrieve a list of item categories.

Required authorization scope: `public.reference:read`


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
      "name": "Item Categories"
    }
  ],
  "paths": {
    "/2024-09/item_categories": {
      "get": {
        "summary": "List all Item Categories",
        "tags": [
          "Item Categories"
        ],
        "operationId": "item_categories_index",
        "description": "Retrieve a list of item categories.\n\nRequired authorization scope: `public.reference:read`\n",
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
            "description": "list of item categories",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "item_categories": [
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": true,
                          "contains_liquids": false,
                          "hs_code": "85171300",
                          "id": 1,
                          "includes_battery": true,
                          "name": "Mobile Phones",
                          "slug": "mobile_phones"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": true,
                          "contains_liquids": false,
                          "hs_code": "84713000",
                          "id": 2,
                          "includes_battery": true,
                          "name": "Tablets",
                          "slug": "tablets"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": true,
                          "contains_liquids": false,
                          "hs_code": "84713000",
                          "id": 3,
                          "includes_battery": true,
                          "name": "Computers & Laptops",
                          "slug": "computers_laptops"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": true,
                          "contains_liquids": false,
                          "hs_code": "85258900",
                          "id": 4,
                          "includes_battery": true,
                          "name": "Cameras",
                          "slug": "cameras"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "85171400",
                          "id": 5,
                          "includes_battery": false,
                          "name": "Accessory (no-battery)",
                          "slug": "accessory_no_battery"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": true,
                          "contains_liquids": false,
                          "hs_code": "85171400",
                          "id": 6,
                          "includes_battery": true,
                          "name": "Accessory (with battery)",
                          "slug": "accessory_with_battery"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": true,
                          "hs_code": "33040000",
                          "id": 7,
                          "includes_battery": false,
                          "name": "Health & Beauty",
                          "slug": "health_beauty"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "62032900",
                          "id": 8,
                          "includes_battery": false,
                          "name": "Fashion",
                          "slug": "fashion"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "91021900",
                          "id": 9,
                          "includes_battery": false,
                          "name": "Watches",
                          "slug": "watches"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "85098000",
                          "id": 10,
                          "includes_battery": false,
                          "name": "Home Appliances",
                          "slug": "home_appliances"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "94038990",
                          "id": 11,
                          "includes_battery": false,
                          "name": "Home Decor",
                          "slug": "home_decor"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "95030099",
                          "id": 12,
                          "includes_battery": false,
                          "name": "Toys",
                          "slug": "toys"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "9506910000",
                          "id": 13,
                          "includes_battery": false,
                          "name": "Sport & Leisure",
                          "slug": "sport_leisure"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "42029210",
                          "id": 14,
                          "includes_battery": false,
                          "name": "Bags & Luggages",
                          "slug": "bags_luggages"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "85198160",
                          "id": 15,
                          "includes_battery": false,
                          "name": "Audio Video",
                          "slug": "audio_video"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "49011000",
                          "id": 16,
                          "includes_battery": false,
                          "name": "Documents",
                          "slug": "documents"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "71022900",
                          "id": 17,
                          "includes_battery": false,
                          "name": "Jewelry",
                          "slug": "jewelry"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "17049000",
                          "id": 18,
                          "includes_battery": false,
                          "name": "Dry Food & Supplements",
                          "slug": "dry_food_supplements"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "49019900",
                          "id": 19,
                          "includes_battery": false,
                          "name": "Books & Collectibles",
                          "slug": "books_collectibles"
                        },
                        {
                          "active": true,
                          "contains_battery_pi966": false,
                          "contains_battery_pi967": false,
                          "contains_liquids": false,
                          "hs_code": "42010000",
                          "id": 20,
                          "includes_battery": false,
                          "name": "Pet Accessory",
                          "slug": "pet_accessory"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": 2,
                          "count": 25
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of item categories"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/item_category_list"
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
      "item_category_list": {
        "type": "object",
        "description": "List of item categories",
        "additionalProperties": false,
        "properties": {
          "item_categories": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemCategory"
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
      "ItemCategory": {
        "type": "object",
        "description": "Item Category",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "integer",
            "description": "Item Category ID"
          },
          "name": {
            "type": "string"
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item"
          },
          "slug": {
            "type": "string"
          },
          "active": {
            "type": "boolean",
            "description": "Item Category state"
          },
          "includes_battery": {
            "type": "boolean",
            "description": "Whether the item includes batteries."
          },
          "contains_liquids": {
            "type": "boolean",
            "description": "Whether the item contains liquids."
          },
          "contains_battery_pi966": {
            "type": "boolean",
            "description": "Whether the item contains a PI966 battery."
          },
          "contains_battery_pi967": {
            "type": "boolean",
            "description": "Whether the item contains a PI967 battery."
          }
        }
      }
    }
  }
}
```