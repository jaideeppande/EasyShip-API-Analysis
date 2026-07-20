# Introspect an Access Token

Introspect an OAuth 2 Access Token using another Access Token.


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
      "name": "Authorization",
      "description": "OAuth 2 API"
    }
  ],
  "paths": {
    "/oauth2/introspect": {
      "post": {
        "summary": "Introspect an Access Token",
        "tags": [
          "Authorization"
        ],
        "operationId": "oauth2_token_introspect",
        "description": "Introspect an OAuth 2 Access Token using another Access Token.\n",
        "security": [
          {
            "OAuth2": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "Access Token Introspect",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "active": true,
                      "scope": "enterprise.organization:write rate",
                      "client_id": "28P8K2PSAsVyugLBKIY1neZXYulpHElHVAAmOrJ9Pds",
                      "token_type": "Bearer",
                      "exp": 3291072120,
                      "iat": 1645532460,
                      "easyship_company_id": "CHK000001"
                    },
                    "summary": "Access Token Introspect"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2IntrospectResponse"
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OAuth2IntrospectRequest"
              },
              "examples": {
                "access_token_introspect": {
                  "summary": "Access Token Introspect",
                  "value": {
                    "token": "test_0RQXwH8Bmf5UkRxB/plFd7f3/R46ffRfbtiwvSZi9Ao="
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
      "OAuth2ClientCredentialsRequest": {
        "type": "object",
        "description": "OAuth 2 Client Credentials Request",
        "additionalProperties": false,
        "required": [
          "grant_type",
          "client_id",
          "client_secret",
          "scope"
        ],
        "properties": {
          "grant_type": {
            "type": "string",
            "description": "OAuth 2 Grant Type",
            "enum": [
              "client_credentials"
            ]
          },
          "client_id": {
            "type": "string",
            "description": "OAuth 2 Client ID"
          },
          "client_secret": {
            "type": "string",
            "description": "OAuth 2 Client Secret"
          },
          "scope": {
            "type": "string",
            "description": "OAuth 2 Scopes separated by space. All Enterprise and Public API scopes are supported, but they must be allowed on the Enterprise API Client Application on the Dashboard.\n\n|Scope|Description|\n|---|---|\n|address|Addresses API (2023-01 and older)|\n|asset|Assets API (2023-01 and older)|\n|billing_document|Billing Documents API (2023-01 and older)|\n|box|Boxes API (2023-01 and older)|\n|courier|Couriers API (2023-01 and older)|\n|courier_account|Courier Accounts API (2023-01 and older)|\n|credit|Credits API (2023-01 and older)|\n|hs_code|Hs Codes API (2023-01 and older)|\n|label|Labels API (2023-01 and older)|\n|pickup|Pickups API (2023-01 and older)|\n|product|Products API (2023-01 and older)|\n|rate|Rates API (2023-01 and older)|\n|reference|References API (2023-01 and older)|\n|settings|Settings API (2023-01 and older)|\n|shipment|Shipments API (2023-01 and older)|\n|shipment_document|Shipment Documents API (2023-01 and older)|\n|store|Stores API (2023-01 and older)|\n|tag|Tags API (2023-01 and older)|\n|tax_and_duty|Tax And Duties API (2023-01 and older)|\n|track|Tracks API (2023-01 and older)|\n|transaction_record|Transaction Records API (2023-01 and older)|\n|webhook|Webhooks API (2023-01 and older)|\n|public.address:read|Addresses (read only) Public API (2024-09 and newer)|\n|public.address:write|Addresses (write only) Public API (2024-09 and newer)|\n|public.analytics:read|Analytics (read only) Public API (2024-09 and newer)|\n|public.app_access:write|App Accesses (write only) Public API (2024-09 and newer)|\n|public.asset:read|Assets (read only) Public API (2024-09 and newer)|\n|public.asset:write|Assets (write only) Public API (2024-09 and newer)|\n|public.batch:read|Batches (read only) Public API (2024-09 and newer)|\n|public.batch:write|Batches (write only) Public API (2024-09 and newer)|\n|public.billing_document:read|Billing Documents (read only) Public API (2024-09 and newer)|\n|public.billing_document:write|Billing Documents (write only) Public API (2024-09 and newer)|\n|public.box:read|Boxes (read only) Public API (2024-09 and newer)|\n|public.box:write|Boxes (write only) Public API (2024-09 and newer)|\n|public.courier:read|Couriers (read only) Public API (2024-09 and newer)|\n|public.courier:write|Couriers (write only) Public API (2024-09 and newer)|\n|public.courier_service:read|Courier Services (read only) Public API (2024-09 and newer)|\n|public.credit:read|Credits (read only) Public API (2024-09 and newer)|\n|public.hs_code:read|Hs Codes (read only) Public API (2024-09 and newer)|\n|public.label:write|Labels (write only) Public API (2024-09 and newer)|\n|public.location:read|Locations (read only) Public API (2024-09 and newer)|\n|public.manifest:read|Manifests (read only) Public API (2024-09 and newer)|\n|public.manifest:write|Manifests (write only) Public API (2024-09 and newer)|\n|public.payment:write|Payments (write only) Public API (2024-09 and newer)|\n|public.payment_source:read|Payment Sources (read only) Public API (2024-09 and newer)|\n|public.payment_source:write|Payment Sources (write only) Public API (2024-09 and newer)|\n|public.pickup:read|Pickups (read only) Public API (2024-09 and newer)|\n|public.pickup:write|Pickups (write only) Public API (2024-09 and newer)|\n|public.product:read|Products (read only) Public API (2024-09 and newer)|\n|public.product:write|Products (write only) Public API (2024-09 and newer)|\n|public.rate:read|Rates (read only) Public API (2024-09 and newer)|\n|public.redirect:write|Redirects (write only) Public API (2024-09 and newer)|\n|public.reference:read|References (read only) Public API (2024-09 and newer)|\n|public.setting:read|Settings (read only) Public API (2024-09 and newer)|\n|public.setting:write|Settings (write only) Public API (2024-09 and newer)|\n|public.shipment:read|Shipments (read only) Public API (2024-09 and newer)|\n|public.shipment:write|Shipments (write only) Public API (2024-09 and newer)|\n|public.shipment_document:read|Shipment Documents (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:read|Shipping Rules (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:write|Shipping Rules (write only) Public API (2024-09 and newer)|\n|public.store:read|Stores (read only) Public API (2024-09 and newer)|\n|public.tag:read|Tags (read only) Public API (2024-09 and newer)|\n|public.tag:write|Tags (write only) Public API (2024-09 and newer)|\n|public.tax_and_duty:read|Tax And Duties (read only) Public API (2024-09 and newer)|\n|public.track:read|Tracks (read only) Public API (2024-09 and newer)|\n|public.transaction_record:read|Transaction Records (read only) Public API (2024-09 and newer)|\n|public.webhook:read|Webhooks (read only) Public API (2024-09 and newer)|\n|public.webhook:write|Webhooks (write only) Public API (2024-09 and newer)|\n"
          }
        }
      },
      "OAuth2TokenResponse": {
        "type": "object",
        "description": "OAuth 2 Token Response",
        "additionalProperties": false,
        "properties": {
          "access_token": {
            "type": "string",
            "description": "OAuth 2 Access Token"
          },
          "token_type": {
            "type": "string",
            "description": "OAuth 2 Token Type",
            "enum": [
              "Bearer"
            ]
          },
          "expires_in": {
            "type": "integer",
            "description": "OAuth 2 Access Token Expiration Time in Seconds"
          },
          "scope": {
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest/properties/scope"
          },
          "created_at": {
            "type": "integer",
            "description": "OAuth 2 Access Token Creation Time"
          },
          "refresh_token": {
            "type": "string",
            "description": "OAuth 2 Refresh Token. Available only for Authorization Code Grant Type.",
            "nullable": true
          }
        }
      },
      "OAuth2IntrospectRequest": {
        "type": "object",
        "description": "OAuth 2 Introspect Request",
        "additionalProperties": false,
        "properties": {
          "token": {
            "type": "string",
            "description": "OAuth 2 Access Token"
          }
        }
      },
      "OAuth2IntrospectResponse": {
        "type": "object",
        "description": "OAuth 2 Introspect Response",
        "additionalProperties": false,
        "properties": {
          "active": {
            "type": "boolean"
          },
          "scope": {
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest/properties/scope"
          },
          "client_id": {
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest/properties/client_id"
          },
          "token_type": {
            "$ref": "#/components/schemas/OAuth2TokenResponse/properties/token_type"
          },
          "iat": {
            "type": "integer"
          },
          "exp": {
            "type": "integer"
          },
          "easyship_company_id": {
            "type": "string",
            "description": "Easyship Company ID"
          }
        }
      }
    }
  }
}
```