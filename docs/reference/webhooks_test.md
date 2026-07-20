# Test a Webhook

Test a single webhook in your account.

Required authorization scope: `public.Webhook`


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
      "name": "Webhooks"
    }
  ],
  "paths": {
    "/2024-09/webhooks/{webhook_id}/test": {
      "post": {
        "summary": "Test a Webhook",
        "tags": [
          "Webhooks"
        ],
        "operationId": "webhooks_test",
        "description": "Test a single webhook in your account.\n\nRequired authorization scope: `public.Webhook`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "webhook_id",
            "in": "path",
            "required": true,
            "description": "Webhook ID",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "webhook successfully tested",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "success": {
                        "message": "Webhook test succeeded"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "webhook successfully tested"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Success"
                }
              }
            }
          },
          "400": {
            "description": "failed to test webhook",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "api_error",
                        "details": [
                          "Webhook test failed. A 2xx status code is expected. (Response Code: 502)"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Test a Webhook",
                            "url": "https://developers.easyship.com/reference/webhooks_test"
                          }
                        ],
                        "message": "Internal or 3rd party API error.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "api_error"
                      }
                    },
                    "summary": "failed to test webhook"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "422": {
            "description": "event_type is invalid",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "\"Unknown_event_type\" isn't part of the enum in #/components/schemas/WebhookTestCreate2024_09/properties/event_type"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "event_type is invalid"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "429": {
            "description": "too many requests",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "too_many_requests",
                        "details": [
                          "Webhook test failed. Test webhook rate limit exceeded (2 per second)"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Rate limit",
                            "url": "https://developers.easyship.com/reference/rate-limit"
                          },
                          {
                            "kind": "documentation",
                            "name": "Test a Webhook",
                            "url": "https://developers.easyship.com/reference/webhooks_test"
                          }
                        ],
                        "message": "Rate Limit Exceeded. You have reached the maximum number of requests. Please try again later.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "too many requests"
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
                "$ref": "#/components/schemas/WebhookTestCreate"
              },
              "examples": {
                "webhook_successfully_tested": {
                  "summary": "webhook successfully tested",
                  "value": {
                    "version": "2024-09",
                    "event_type": "courier_state_changed"
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
      },
      "Webhook2023_01": {
        "type": "object",
        "description": "v2023_01 Webhook",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/WebhookBase/properties/id"
          },
          "endpoint": {
            "$ref": "#/components/schemas/WebhookBase/properties/endpoint"
          },
          "configuration": {
            "$ref": "#/components/schemas/WebhookConfiguration"
          },
          "event_types": {
            "type": "array",
            "minItems": 1,
            "maxItems": 13,
            "items": {
              "type": "string",
              "enum": [
                "shipment_label_created",
                "shipment_tracking_checkpoints_created",
                "shipment_tracking_status_changed",
                "shipment_cancelled",
                "shipment_label_failed",
                "shipment_warehouse_state_updated",
                "batch_started",
                "batch_finished",
                "batch_item_finished",
                "credit_balance_low",
                "courier_account_state_changed",
                "external_shipment_insured",
                "oauth_authorization_revoked"
              ],
              "description": "Allowed event types"
            }
          },
          "version": {
            "type": "string",
            "description": "Webhook payload version. Refer to documentation for information regarding payload versioning.",
            "default": "2023-01",
            "enum": [
              "2023-01"
            ]
          },
          "state": {
            "$ref": "#/components/schemas/WebhookBase/properties/state"
          },
          "secret_token": {
            "$ref": "#/components/schemas/WebhookBase/properties/secret_token"
          },
          "updated_at": {
            "$ref": "#/components/schemas/WebhookBase/properties/updated_at"
          },
          "created_at": {
            "$ref": "#/components/schemas/WebhookBase/properties/created_at"
          }
        }
      },
      "Webhook2024_09": {
        "type": "object",
        "description": "v2024_09 Webhook",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/WebhookBase/properties/id"
          },
          "endpoint": {
            "$ref": "#/components/schemas/WebhookBase/properties/endpoint"
          },
          "configuration": {
            "$ref": "#/components/schemas/WebhookConfiguration"
          },
          "event_types": {
            "type": "array",
            "minItems": 1,
            "maxItems": 13,
            "items": {
              "type": "string",
              "enum": [
                "shipment_label_created",
                "shipment_tracking_checkpoints_created",
                "shipment_tracking_status_changed",
                "shipment_cancelled",
                "shipment_label_failed",
                "shipment_warehouse_state_updated",
                "batch_started",
                "batch_finished",
                "batch_item_finished",
                "credit_balance_low",
                "courier_state_changed",
                "external_shipment_insured",
                "oauth_authorization_revoked"
              ],
              "description": "Allowed event types"
            }
          },
          "version": {
            "type": "string",
            "description": "Webhook payload version. Refer to documentation for information regarding payload versioning.",
            "default": "2024-09",
            "enum": [
              "2024-09"
            ]
          },
          "state": {
            "$ref": "#/components/schemas/WebhookBase/properties/state"
          },
          "secret_token": {
            "$ref": "#/components/schemas/WebhookBase/properties/secret_token"
          },
          "updated_at": {
            "$ref": "#/components/schemas/WebhookBase/properties/updated_at"
          },
          "created_at": {
            "$ref": "#/components/schemas/WebhookBase/properties/created_at"
          }
        }
      },
      "WebhookTestCreate2023_01": {
        "type": "object",
        "description": "Test v2023_01 Webhook",
        "additionalProperties": false,
        "required": [
          "event_type"
        ],
        "properties": {
          "event_type": {
            "type": "string",
            "enum": [
              "shipment_label_created",
              "shipment_tracking_checkpoints_created",
              "shipment_tracking_status_changed",
              "shipment_cancelled",
              "shipment_label_failed",
              "shipment_warehouse_state_updated",
              "batch_started",
              "batch_finished",
              "batch_item_finished",
              "credit_balance_low",
              "courier_account_state_changed",
              "external_shipment_insured",
              "oauth_authorization_revoked"
            ],
            "description": "Webhook event type"
          },
          "version": {
            "$ref": "#/components/schemas/Webhook2023_01/properties/version"
          }
        }
      },
      "WebhookTestCreate2024_09": {
        "type": "object",
        "description": "Test v2024_09 Webhook",
        "additionalProperties": false,
        "required": [
          "event_type"
        ],
        "properties": {
          "event_type": {
            "type": "string",
            "enum": [
              "shipment_label_created",
              "shipment_tracking_checkpoints_created",
              "shipment_tracking_status_changed",
              "shipment_cancelled",
              "shipment_label_failed",
              "shipment_warehouse_state_updated",
              "batch_started",
              "batch_finished",
              "batch_item_finished",
              "credit_balance_low",
              "courier_state_changed",
              "external_shipment_insured",
              "oauth_authorization_revoked"
            ],
            "description": "Webhook event type"
          },
          "version": {
            "$ref": "#/components/schemas/Webhook2024_09/properties/version"
          }
        }
      },
      "WebhookTestCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/WebhookTestCreate2023_01"
          },
          {
            "$ref": "#/components/schemas/WebhookTestCreate2024_09"
          }
        ],
        "discriminator": {
          "propertyName": "version",
          "mapping": {
            "2023-01": "#/components/schemas/WebhookTestCreate2023_01",
            "2024-09": "#/components/schemas/WebhookTestCreate2024_09"
          }
        }
      }
    }
  }
}
```