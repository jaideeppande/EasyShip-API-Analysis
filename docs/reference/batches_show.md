# Get a Batch

Retrieve a batch by its ID.

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
    "/2024-09/batches/{batch_id}": {
      "get": {
        "summary": "Get a Batch",
        "tags": [
          "Batches"
        ],
        "operationId": "batches_show",
        "description": "Retrieve a batch by its ID.\n\nRequired authorization scope: `public.batch:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
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
            "description": "batch",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "batch": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "created_at": "2022-02-22T12:21:00Z",
                        "created_count": 1,
                        "failed_count": 1,
                        "finished_at": null,
                        "processed_count": 0,
                        "processing_count": 0,
                        "started_at": null,
                        "state": "created",
                        "total_count": 2,
                        "type": "shipment_batch"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "batch"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/batch_single"
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
                            "name": "Get a Batch",
                            "url": "https://developers.easyship.com/reference/batches_show"
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
      "batch_single": {
        "type": "object",
        "description": "Batch",
        "additionalProperties": false,
        "properties": {
          "batch": {
            "$ref": "#/components/schemas/BatchSingle"
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
      },
      "BatchSingle": {
        "type": "object",
        "description": "Batch Detail",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/Batch/properties/id"
          },
          "state": {
            "$ref": "#/components/schemas/Batch/properties/state"
          },
          "type": {
            "$ref": "#/components/schemas/Batch/properties/type"
          },
          "started_at": {
            "$ref": "#/components/schemas/Batch/properties/started_at"
          },
          "finished_at": {
            "$ref": "#/components/schemas/Batch/properties/finished_at"
          },
          "created_at": {
            "$ref": "#/components/schemas/Batch/properties/created_at"
          },
          "updated_at": {
            "$ref": "#/components/schemas/Batch/properties/updated_at"
          },
          "total_count": {
            "type": "integer",
            "description": "Batch Items total count"
          },
          "failed_count": {
            "type": "integer",
            "description": "Batch Items failed count"
          },
          "processed_count": {
            "type": "integer",
            "description": "Batch Items processed count"
          },
          "processing_count": {
            "type": "integer",
            "description": "Batch Items processing count"
          },
          "created_count": {
            "type": "integer",
            "description": "Batch Items created count"
          }
        }
      }
    }
  }
}
```