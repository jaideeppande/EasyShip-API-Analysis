# List all Batches

Retrieve a list of all batches ordered by date of creation.

Required authorization scope: `public.batch:read`


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
      "name": "Batches"
    }
  ],
  "paths": {
    "/2024-09/batches": {
      "get": {
        "summary": "List all Batches",
        "tags": [
          "Batches"
        ],
        "operationId": "batches_index",
        "description": "Retrieve a list of all batches ordered by date of creation.\n\nRequired authorization scope: `public.batch:read`\n",
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
            "name": "state",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "created",
                "processing",
                "processed",
                "failed"
              ]
            },
            "required": false,
            "description": "Filter records by state.",
            "example": "created"
          },
          {
            "name": "type",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "shipment_batch",
                "address_batch",
                "label_batch"
              ]
            },
            "required": false,
            "description": "Filter records by batch type.",
            "example": "shipment"
          }
        ],
        "responses": {
          "200": {
            "description": "list of batches",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "batches": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "created_at": "2022-02-22T12:21:00Z",
                          "finished_at": null,
                          "started_at": null,
                          "state": "created",
                          "type": "shipment_batch"
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
                    "summary": "list of batches"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/batch_list"
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
      "batch_list": {
        "type": "object",
        "description": "List of Batches",
        "additionalProperties": false,
        "properties": {
          "batches": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Batch"
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
      "Batch": {
        "type": "object",
        "description": "Batch",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Batch ID"
          },
          "state": {
            "type": "string",
            "description": "Batch state",
            "enum": [
              "created",
              "processing",
              "processed",
              "failed"
            ]
          },
          "type": {
            "type": "string",
            "description": "Batch type",
            "enum": [
              "shipment_batch",
              "address_batch",
              "label_batch"
            ]
          },
          "started_at": {
            "type": "string",
            "format": "datetime",
            "nullable": true
          },
          "finished_at": {
            "type": "string",
            "format": "datetime",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "datetime"
          },
          "updated_at": {
            "type": "string",
            "format": "datetime"
          }
        }
      }
    }
  }
}
```