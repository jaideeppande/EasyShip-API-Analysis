# Create a Webhook

Create a single webhook for specific organization.

Required authorization scope: `enterprise.webhook:write`


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Easyship Enterprise API",
    "version": "2024-11",
    "description": "Easyship Enterprise API",
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
      "name": "Webhooks",
      "description": "Webhooks API"
    }
  ],
  "paths": {
    "/2024-11/organizations/{organization_id}/webhooks": {
      "post": {
        "summary": "Create a Webhook",
        "tags": [
          "Webhooks"
        ],
        "operationId": "organizations_webhooks_create",
        "description": "Create a single webhook for specific organization.\n\nRequired authorization scope: `enterprise.webhook:write`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.webhook"
            ]
          }
        ],
        "parameters": [
          {
            "name": "organization_id",
            "in": "path",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true,
            "description": "Organization ID provided when creating an organization"
          }
        ],
        "responses": {
          "201": {
            "description": "webhook successfully created",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/webhook_single"
                }
              }
            }
          },
          "422": {
            "description": "failed validations",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Endpoint can't be blank",
                          "Endpoint is not a valid URL",
                          "Event types not supported event: [\"unsupported_event\"]"
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "failed validations"
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
              }
            }
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://enterprise-api.easyship.com",
      "description": "Production"
    }
  ],
  "components": {
    "securitySchemes": {
      "OAuth2": {
        "type": "oauth2",
        "flows": {
          "clientCredentials": {
            "tokenUrl": "https://enterprise-api.easyship.com/oauth2/token",
            "scopes": {
              "address": "Addresses API (2023-01 and older)",
              "address_validation": "Address Validations API (2023-01 and older)",
              "analytics": "Analytics API (2023-01 and older)",
              "asset": "Assets API (2023-01 and older)",
              "batch": "Batches API (2023-01 and older)",
              "billing_document": "Billing Documents API (2023-01 and older)",
              "box": "Boxes API (2023-01 and older)",
              "courier": "Couriers API (2023-01 and older)",
              "courier_account": "Courier Accounts API (2023-01 and older)",
              "credit": "Credits API (2023-01 and older)",
              "efulfillment": "E-Fulfillment API (2023-01 and older)",
              "hs_code": "Hs Codes API (2023-01 and older)",
              "label": "Labels API (2023-01 and older)",
              "location": "Locations API (2023-01 and older)",
              "payment": "Payments API (2023-01 and older)",
              "payment_source": "Payment Sources API (2023-01 and older)",
              "pickup": "Pickups API (2023-01 and older)",
              "product": "Products API (2023-01 and older)",
              "rate": "Rates API (2023-01 and older)",
              "reference": "References API (2023-01 and older)",
              "settings": "Settings API (2023-01 and older)",
              "shipment": "Shipments API (2023-01 and older)",
              "shipment_document": "Shipment Documents API (2023-01 and older)",
              "shipping_rule": "Shipping Rules API (2023-01 and older)",
              "store": "Stores API (2023-01 and older)",
              "tag": "Tags API (2023-01 and older)",
              "tax_and_duty": "Tax And Duties API (2023-01 and older)",
              "track": "Tracks API (2023-01 and older)",
              "track_3p": "Track 3ps API (2023-01 and older)",
              "transaction_record": "Transaction Records API (2023-01 and older)",
              "webhook": "Webhooks API (2023-01 and older)",
              "enterprise.child_companies_access": "Child Companies Accesses API (2023-09 and older)",
              "enterprise.company": "Companies API (2023-09 and older)",
              "enterprise.organization": "Organizations API (2023-09 and older)",
              "enterprise.shipping_rule": "Shipping Rules API (2023-09 and older)",
              "enterprise.webhook": "Webhooks API (2023-09 and older)",
              "enterprise.child_company:access": "Child Companies (access only) Enterprise API (2024-11 and newer)",
              "enterprise.company:read": "Companies (read only) Enterprise API (2024-11 and newer)",
              "enterprise.company:write": "Companies (write only) Enterprise API (2024-11 and newer)",
              "enterprise.organization:read": "Organizations (read only) Enterprise API (2024-11 and newer)",
              "enterprise.organization:write": "Organizations (write only) Enterprise API (2024-11 and newer)",
              "enterprise.shipping_rule:read": "Shipping Rules (read only) Enterprise API (2024-11 and newer)",
              "enterprise.shipping_rule:write": "Shipping Rules (write only) Enterprise API (2024-11 and newer)",
              "enterprise.webhook:read": "Webhooks (read only) Enterprise API (2024-11 and newer)",
              "enterprise.webhook:write": "Webhooks (write only) Enterprise API (2024-11 and newer)",
              "public.address:read": "Addresses (read only) Public API (2024-09 and newer)",
              "public.address:write": "Addresses (write only) Public API (2024-09 and newer)",
              "public.address_validation:write": "Address Validations (write only) Public API (2024-09 and newer)",
              "public.analytics:read": "Analytics (read only) Public API (2024-09 and newer)",
              "public.app_access:write": "App Accesses (write only) Public API (2024-09 and newer)",
              "public.asset:read": "Assets (read only) Public API (2024-09 and newer)",
              "public.asset:write": "Assets (write only) Public API (2024-09 and newer)",
              "public.batch:read": "Batches (read only) Public API (2024-09 and newer)",
              "public.batch:write": "Batches (write only) Public API (2024-09 and newer)",
              "public.billing_document:read": "Billing Documents (read only) Public API (2024-09 and newer)",
              "public.billing_document:write": "Billing Documents (write only) Public API (2024-09 and newer)",
              "public.box:read": "Boxes (read only) Public API (2024-09 and newer)",
              "public.box:write": "Boxes (write only) Public API (2024-09 and newer)",
              "public.courier:read": "Couriers (read only) Public API (2024-09 and newer)",
              "public.courier:write": "Couriers (write only) Public API (2024-09 and newer)",
              "public.courier_service:read": "Courier Services (read only) Public API (2024-09 and newer)",
              "public.credit:read": "Credits (read only) Public API (2024-09 and newer)",
              "public.efulfillment:write": "E-Fulfillment (write only) Public API (2024-09 and newer)",
              "public.hs_code:read": "Hs Codes (read only) Public API (2024-09 and newer)",
              "public.insurance_policy:read": "Insurance Policies (read only) Public API (2024-09 and newer)",
              "public.insurance_policy:write": "Insurance Policies (write only) Public API (2024-09 and newer)",
              "public.insurance_policy_3p:write": "Insurance Policy 3ps (write only) Public API (2024-09 and newer)",
              "public.label:write": "Labels (write only) Public API (2024-09 and newer)",
              "public.location:read": "Locations (read only) Public API (2024-09 and newer)",
              "public.manifest:read": "Manifests (read only) Public API (2024-09 and newer)",
              "public.manifest:write": "Manifests (write only) Public API (2024-09 and newer)",
              "public.payment:write": "Payments (write only) Public API (2024-09 and newer)",
              "public.payment_source:read": "Payment Sources (read only) Public API (2024-09 and newer)",
              "public.payment_source:write": "Payment Sources (write only) Public API (2024-09 and newer)",
              "public.pickup:read": "Pickups (read only) Public API (2024-09 and newer)",
              "public.pickup:write": "Pickups (write only) Public API (2024-09 and newer)",
              "public.product:read": "Products (read only) Public API (2024-09 and newer)",
              "public.product:write": "Products (write only) Public API (2024-09 and newer)",
              "public.rate:read": "Rates (read only) Public API (2024-09 and newer)",
              "public.redirect:write": "Redirects (write only) Public API (2024-09 and newer)",
              "public.reference:read": "References (read only) Public API (2024-09 and newer)",
              "public.setting:read": "Settings (read only) Public API (2024-09 and newer)",
              "public.setting:write": "Settings (write only) Public API (2024-09 and newer)",
              "public.shipment:read": "Shipments (read only) Public API (2024-09 and newer)",
              "public.shipment:write": "Shipments (write only) Public API (2024-09 and newer)",
              "public.shipment_document:read": "Shipment Documents (read only) Public API (2024-09 and newer)",
              "public.shipping_rule:read": "Shipping Rules (read only) Public API (2024-09 and newer)",
              "public.shipping_rule:write": "Shipping Rules (write only) Public API (2024-09 and newer)",
              "public.store:read": "Stores (read only) Public API (2024-09 and newer)",
              "public.tag:read": "Tags (read only) Public API (2024-09 and newer)",
              "public.tag:write": "Tags (write only) Public API (2024-09 and newer)",
              "public.tax_and_duty:read": "Tax And Duties (read only) Public API (2024-09 and newer)",
              "public.track:read": "Tracks (read only) Public API (2024-09 and newer)",
              "public.track_3p:read": "Track 3ps (read only) Public API (2024-09 and newer)",
              "public.track_3p:write": "Track 3ps (write only) Public API (2024-09 and newer)",
              "public.transaction_record:read": "Transaction Records (read only) Public API (2024-09 and newer)",
              "public.webhook:read": "Webhooks (read only) Public API (2024-09 and newer)",
              "public.webhook:write": "Webhooks (write only) Public API (2024-09 and newer)"
            }
          }
        }
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
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
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
            "maxItems": 15,
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
                "enterprise_company_creation",
                "enterprise_company_deletion",
                "courier_account_state_changed",
                "external_shipment_insured",
                "oauth_authorization_revoked",
                "easyship_account_verification_changed"
              ],
              "description": "Allowed event types"
            }
          },
          "version": {
            "type": "string",
            "description": "Webhook payload version. Refer to documentation for information regarding payload versioning.",
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
            "maxItems": 15,
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
                "enterprise_company_creation",
                "enterprise_company_deletion",
                "courier_state_changed",
                "external_shipment_insured",
                "oauth_authorization_revoked",
                "easyship_account_verification_changed"
              ],
              "description": "Allowed event types"
            }
          },
          "version": {
            "type": "string",
            "description": "Webhook payload version. Refer to documentation for information regarding payload versioning.",
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