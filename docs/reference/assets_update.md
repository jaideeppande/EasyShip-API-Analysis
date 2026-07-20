# Update an Asset

Update an asset.

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
    "/2024-09/account/assets/{id}": {
      "patch": {
        "summary": "Update an Asset",
        "tags": [
          "Settings"
        ],
        "operationId": "assets_update",
        "description": "Update an asset.\n\nRequired authorization scope: `public.asset:write`\n",
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
            "description": "asset successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "asset": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "name": "Asset name",
                        "type": "tracking_email_ad",
                        "url": "https://s3.amazonaws.com/test/assets/01563646-58c1-4607-8fe0-cae3e33c0001/tracking_email_ad/01563646-58c1-4607-8fe0-cae3e33c0001/main.png?1645532460"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "asset successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/asset_single"
                }
              }
            }
          },
          "404": {
            "description": "no record found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Asset was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Update an Asset",
                            "url": "https://developers.easyship.com/reference/assets_update"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "no record found"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/AssetUpdate"
              },
              "examples": {
                "asset_successfully_updated": {
                  "summary": "asset successfully updated",
                  "value": {
                    "name": "Asset name"
                  }
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
      "asset_single": {
        "type": "object",
        "description": "Asset details",
        "additionalProperties": false,
        "properties": {
          "asset": {
            "$ref": "#/components/schemas/Asset"
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
      },
      "AssetUpdate": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "Asset name",
            "maxLength": 50,
            "nullable": true
          }
        }
      }
    }
  }
}
```