# Get a Manifest

Retrieve details of a specific manifest.

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
    "/2024-09/manifests/{manifest_id}": {
      "get": {
        "summary": "Get a Manifest",
        "tags": [
          "Manifests"
        ],
        "operationId": "manifests_show",
        "description": "Retrieve details of a specific manifest.\n\nRequired authorization scope: `public.manifest:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "manifest_id",
            "in": "path",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true,
            "description": "Manifest ID"
          }
        ],
        "responses": {
          "200": {
            "description": "manifest",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "manifest": {
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
                        "shipments_count": 0
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "manifest"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/manifest_single"
                }
              }
            }
          },
          "404": {
            "description": "manifest was not found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Manifest was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Get a Manifest",
                            "url": "https://developers.easyship.com/reference/manifests_show"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "manifest was not found"
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
      "manifest_single": {
        "type": "object",
        "description": "Manifest details",
        "additionalProperties": false,
        "properties": {
          "manifest": {
            "$ref": "#/components/schemas/Manifest"
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