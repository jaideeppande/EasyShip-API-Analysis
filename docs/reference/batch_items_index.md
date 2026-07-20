# List all Batch Items

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
    "/2024-09/batches/{batch_id}/items": {
      "get": {
        "summary": "List all Batch Items",
        "tags": [
          "Batches"
        ],
        "operationId": "batch_items_index",
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
            "name": "batch_id",
            "in": "path",
            "required": true,
            "description": "Batch ID",
            "schema": {
              "type": "string"
            }
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
                      "batch_items": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                          "created_at": "2022-02-22T12:21:00Z",
                          "finished_at": null,
                          "processing_errors": [],
                          "record_id": null,
                          "record_type": null,
                          "reference_id": "1",
                          "state": "created",
                          "type": "shipment_batch_item"
                        },
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0004",
                          "created_at": "2022-02-22T12:21:00Z",
                          "finished_at": "2022-02-22T12:20:00Z",
                          "processing_errors": [],
                          "record_id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "record_type": "Shipment",
                          "reference_id": "1",
                          "state": "processed",
                          "type": "shipment_batch_item"
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
                    "summary": "list of batches"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/batch_item_list"
                }
              }
            }
          },
          "404": {
            "description": "record not found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Batch was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List all Batch Items",
                            "url": "https://developers.easyship.com/reference/batch_items_index"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "record not found"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
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
      "batch_item_list": {
        "type": "object",
        "description": "List of Batches",
        "additionalProperties": false,
        "properties": {
          "batch_items": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/BatchItem"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
      "BatchItem": {
        "type": "object",
        "description": "Batch Item",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Batch Item ID"
          },
          "type": {
            "type": "string",
            "description": "Batch Item type",
            "enum": [
              "address_batch_item",
              "shipment_batch_item",
              "label_batch_item"
            ]
          },
          "reference_id": {
            "type": "string",
            "nullable": true
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
          "record_type": {
            "type": "string",
            "nullable": true
          },
          "record_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true
          },
          "processing_errors": {
            "type": "array",
            "items": {
              "type": "string"
            }
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