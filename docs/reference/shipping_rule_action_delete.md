# Delete Action of a Shipping Rule

Delete shipping rule action.

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
      "name": "Shipping Rule's Actions"
    }
  ],
  "paths": {
    "/2024-09/shipping_rules/{shipping_rule_id}/actions/{action_id}": {
      "delete": {
        "summary": "Delete Action of a Shipping Rule",
        "tags": [
          "Shipping Rule's Actions"
        ],
        "operationId": "shipping_rule_action_delete",
        "description": "Delete shipping rule action.\n\nRequired authorization scope: `public.shipping_rule:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "shipping_rule_id",
            "in": "path",
            "required": true,
            "description": "Shipping Rule ID provided when creating",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "action_id",
            "in": "path",
            "required": true,
            "description": "Action ID provided when creating",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "action successfully deleted",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "success": {
                        "message": "Action successfully deleted"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "action successfully deleted"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Success"
                }
              }
            }
          },
          "403": {
            "description": "unauthorized",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "forbidden",
                        "details": [],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Scopes",
                            "url": "https://developers.easyship.com/reference/scopes"
                          },
                          {
                            "kind": "documentation",
                            "name": "Delete Action of a Shipping Rule",
                            "url": "https://developers.easyship.com/reference/shipping_rule_action_delete"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Automate your Shipments",
                            "url": "https://developers.easyship.com/docs/how-to-automate-your-shipments"
                          }
                        ],
                        "message": "You do not have permission to access this resource. Please contact our support team or your account manager if you believe you should have access.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "unauthorized"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
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
                          "The Action was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Delete Action of a Shipping Rule",
                            "url": "https://developers.easyship.com/reference/shipping_rule_action_delete"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Automate your Shipments",
                            "url": "https://developers.easyship.com/docs/how-to-automate-your-shipments"
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