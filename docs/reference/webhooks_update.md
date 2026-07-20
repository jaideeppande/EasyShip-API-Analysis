# Update a Webhook

Update a single webhook in your account.

Required authorization scope: `public.webhook:write` 


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
    "/2024-09/webhooks/{webhook_id}": {
      "patch": {
        "summary": "Update a Webhook",
        "tags": [
          "Webhooks"
        ],
        "operationId": "webhooks_update",
        "description": "Update a single webhook in your account.\n\nRequired authorization scope: `public.webhook:write` \n",
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
            "description": "webhook successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "webhook": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "configuration": {
                          "credit_balance_low": {
                            "credit_balance_limit": 100
                          }
                        },
                        "created_at": "2022-02-22T12:21:00Z",
                        "endpoint": "https://example.com/new_tests",
                        "event_types": [
                          "batch_finished"
                        ],
                        "secret_token": "webh_497146d1efccb6071d53f8010fe99b8d",
                        "state": "active",
                        "updated_at": "2022-02-22T12:21:00Z",
                        "version": "2024-09"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "webhook successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/webhook_single"
                }
              }
            }
          },
          "422": {
            "description": "failed event_types validations",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "\"unsupported_event\" isn't part of the enum in #/components/schemas/Webhook2024_09/properties/event_types/items"
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
                    "summary": "failed event_types validations"
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
                "$ref": "#/components/schemas/WebhookCreate"
              },
              "examples": {
                "webhook_successfully_updated": {
                  "summary": "webhook successfully updated",
                  "value": {
                    "version": "2024-09",
                    "endpoint": "https://example.com/new_tests",
                    "event_types": [
                      "batch_finished"
                    ],
                    "configuration": {
                      "credit_balance_low": {
                        "credit_balance_limit": 100
                      }
                    }
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
      "webhook_single": {
        "type": "object",
        "description": "Webhook details",
        "additionalProperties": false,
        "properties": {
          "webhook": {
            "$ref": "#/components/schemas/Webhook"
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
      "Webhook": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/Webhook2023_01"
          },
          {
            "$ref": "#/components/schemas/Webhook2024_09"
          }
        ],
        "discriminator": {
          "propertyName": "version",
          "mapping": {
            "2023-01": "#/components/schemas/Webhook2023_01",
            "2024-09": "#/components/schemas/Webhook2024_09"
          }
        }
      },
      "WebhookBase": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Webhook ID"
          },
          "endpoint": {
            "type": "string",
            "format": "URI"
          },
          "configuration": {
            "$ref": "#/components/schemas/WebhookConfiguration"
          },
          "version": {
            "type": "string",
            "description": "Webhook payload version. Refer to documentation for information regarding payload versioning.",
            "enum": [
              "2023-01",
              "2024-09"
            ]
          },
          "state": {
            "type": "string",
            "description": "Webhook state either active, inactive or failed",
            "enum": [
              "active",
              "inactive",
              "failed"
            ]
          },
          "secret_token": {
            "type": "string",
            "description": "Incoming webhook events are signed with `X-EASYSHIP-SIGNATURE` in their headers and contain this token as the value."
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the webhook was most recently modified"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the webhook was created in the Easyship system recently"
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
      "WebhookConfiguration": {
        "type": "object",
        "additionalProperties": false,
        "nullable": true,
        "properties": {
          "credit_balance_low": {
            "type": "object",
            "additionalProperties": false,
            "nullable": true,
            "properties": {
              "credit_balance_limit": {
                "type": "number",
                "nullable": true,
                "description": "Required only when event_types include `credit_balance_low`. The webhook would be triggered if the credit balance is lower than this limit. Please note that the webhook will only be triggered once a day and it will reset at 00:00 UTC."
              }
            }
          }
        }
      },
      "WebhookCreate2023_01": {
        "type": "object",
        "description": "Create v2023_01 Webhook",
        "additionalProperties": false,
        "required": [
          "endpoint",
          "event_types"
        ],
        "properties": {
          "configuration": {
            "$ref": "#/components/schemas/WebhookConfiguration"
          },
          "endpoint": {
            "$ref": "#/components/schemas/WebhookBase/properties/endpoint"
          },
          "event_types": {
            "$ref": "#/components/schemas/Webhook2023_01/properties/event_types"
          },
          "version": {
            "$ref": "#/components/schemas/Webhook2023_01/properties/version"
          }
        }
      },
      "WebhookCreate2024_09": {
        "type": "object",
        "description": "Create v2024_09 Webhook",
        "additionalProperties": false,
        "required": [
          "endpoint",
          "event_types"
        ],
        "properties": {
          "configuration": {
            "$ref": "#/components/schemas/WebhookConfiguration"
          },
          "endpoint": {
            "$ref": "#/components/schemas/WebhookBase/properties/endpoint"
          },
          "event_types": {
            "$ref": "#/components/schemas/Webhook2024_09/properties/event_types"
          },
          "version": {
            "$ref": "#/components/schemas/Webhook2024_09/properties/version"
          }
        }
      },
      "WebhookCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/WebhookCreate2023_01"
          },
          {
            "$ref": "#/components/schemas/WebhookCreate2024_09"
          }
        ],
        "discriminator": {
          "propertyName": "version",
          "mapping": {
            "2023-01": "#/components/schemas/WebhookCreate2023_01",
            "2024-09": "#/components/schemas/WebhookCreate2024_09"
          }
        }
      }
    }
  }
}
```