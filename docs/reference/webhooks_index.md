# List all Webhooks

Retrieve a list of webhooks available within your account.

Required authorization scope: `public.webhook:read`


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
    "/2024-09/webhooks": {
      "get": {
        "summary": "List all Webhooks",
        "tags": [
          "Webhooks"
        ],
        "operationId": "webhooks_index",
        "description": "Retrieve a list of webhooks available within your account.\n\nRequired authorization scope: `public.webhook:read`\n",
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
            "description": "list of webhooks within account",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "webhooks": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "configuration": {
                            "credit_balance_low": {
                              "credit_balance_limit": 1
                            }
                          },
                          "created_at": "2022-02-22T12:21:00Z",
                          "endpoint": "https://example.com/webhook/callback/endpoint",
                          "event_types": [
                            "batch_started",
                            "batch_finished",
                            "credit_balance_low",
                            "courier_state_changed"
                          ],
                          "secret_token": "webh_497146d1efccb6071d53f8010fe99b8d",
                          "state": "active",
                          "updated_at": "2022-02-22T12:21:00Z",
                          "version": "2024-09"
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
                    "summary": "list of webhooks within account"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/webhook_list"
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
      "webhook_list": {
        "type": "object",
        "description": "List of Webhooks",
        "additionalProperties": false,
        "properties": {
          "webhooks": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Webhook"
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
      }
    }
  }
}
```