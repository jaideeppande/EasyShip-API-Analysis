# List all Manifests

Retrieve a list of [manifests](https://support.easyship.com/hc/en-us/articles/4414489808525-What-Is-a-Manifest-in-Shipping).

Required authorization scope: `public.manifest:read`


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
      "name": "Manifests"
    }
  ],
  "paths": {
    "/2024-09/manifests": {
      "get": {
        "summary": "List all Manifests",
        "tags": [
          "Manifests"
        ],
        "operationId": "manifests_index",
        "description": "Retrieve a list of [manifests](https://support.easyship.com/hc/en-us/articles/4414489808525-What-Is-a-Manifest-in-Shipping).\n\nRequired authorization scope: `public.manifest:read`\n",
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
          },
          {
            "name": "courier_umbrella_name",
            "in": "query",
            "required": false,
            "description": "Filter by courier umbrella name",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "courier_id",
            "in": "query",
            "required": false,
            "description": "Filter by courier id",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "ref_number",
            "in": "query",
            "schema": {
              "type": "array",
              "items": {
                "type": "string"
              }
            },
            "explode": false,
            "required": false,
            "description": "Filter by reference number provided when creating the manifest."
          },
          {
            "name": "created_at_from",
            "in": "query",
            "required": false,
            "description": "Display only manifests created after this date (ISO8601 date format)",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "created_at_to",
            "in": "query",
            "required": false,
            "description": "Display only manifests created before this date (ISO8601 date format)",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "list of manifests",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "manifests": [
                        {
                          "courier": {
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "umbrella_name": "USPS"
                          },
                          "created_at": "2022-02-22T12:21:00Z",
                          "document": {
                            "format": "url",
                            "url": "http://document.url"
                          },
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "ref_number": "ABC123",
                          "shipments_count": 1
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
                    "summary": "list of manifests"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/manifest_list"
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
      "manifest_list": {
        "type": "object",
        "description": "List of manifests",
        "additionalProperties": false,
        "properties": {
          "manifests": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Manifest"
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
      "Manifest": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Manifest ID"
          },
          "courier": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "description": "Courier ID"
              },
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service."
              }
            }
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Manifest creation date"
          },
          "ref_number": {
            "type": "string",
            "description": "Manifest reference number"
          },
          "shipments_count": {
            "type": "number",
            "description": "Number of shipments in manifest"
          },
          "document": {
            "type": "object",
            "description": "Manifest document",
            "additionalProperties": false,
            "properties": {
              "format": {
                "type": "string",
                "description": "Manifest document format",
                "enum": [
                  "url"
                ]
              },
              "url": {
                "type": "string",
                "description": "Manifest document URL"
              }
            }
          }
        }
      }
    }
  }
}
```