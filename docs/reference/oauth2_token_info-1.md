# Retrieve info for the Access Token

Retrieve an OAuth 2 Access Token information.


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Easyship Partner App Authentication",
    "version": "2024-02-21",
    "description": "Easyship Oauth 2 API",
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
    "/oauth2/token/info": {
      "get": {
        "summary": "Retrieve info for the Access Token",
        "tags": [
          "Authorization"
        ],
        "operationId": "oauth2_token_info",
        "description": "Retrieve an OAuth 2 Access Token information.\n",
        "security": [
          {
            "OAuth2": []
          }
        ],
        "responses": {
          "200": {
            "description": "Access Token Info",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "resource_owner_id": "CHK000001",
                      "scope": [
                        "rate",
                        "shipment",
                        "label",
                        "track",
                        "company",
                        "pickup",
                        "location",
                        "store",
                        "product"
                      ],
                      "expires_in": 1645539660,
                      "application": {
                        "uid": "ixaj5e4L25axd_d6b4K2wG479_9c3itEN8eexE_67Qk"
                      },
                      "created_at": 1645532460,
                      "resource_owner_type": "Company"
                    },
                    "summary": "Access Token Info"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2TokenInfo"
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
      "url": "https://api.easyship.com",
      "description": "Production"
    }
  ],
  "components": {
    "securitySchemes": {
      "OAuth2": {
        "type": "oauth2",
        "flows": {
          "clientCredentials": {
            "tokenUrl": "https://api.easyship.com/oauth2/token",
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
              "custom_markup_rate": "Custom Markup Rates API (2023-01 and older)",
              "efulfillment": "E-Fulfillment API (2023-01 and older)",
              "hs_code": "Hs Codes API (2023-01 and older)",
              "label": "Labels API (2023-01 and older)",
              "location": "Locations API (2023-01 and older)",
              "manifest": "Manifests API (2023-01 and older)",
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
      "OAuth2TokenInfo": {
        "type": "object",
        "description": "OAuth 2 Token Info",
        "additionalProperties": false,
        "properties": {
          "resource_owner_id": {
            "type": "string",
            "nullable": true,
            "description": "OAuth 2 Resource Owner ID. Always `null` when using `client_credentials` grant type."
          },
          "resource_owner_type": {
            "type": "string",
            "nullable": true,
            "description": "OAuth 2 Resource Owner Type. Always `null` when using `client_credentials` grant type."
          },
          "scope": {
            "description": "OAuth 2 Scopes",
            "type": "array",
            "items": {
              "type": "string",
              "description": "OAuth 2 Scope name"
            }
          },
          "expires_in": {
            "$ref": "#/components/schemas/OAuth2TokenResponse/properties/expires_in"
          },
          "created_at": {
            "$ref": "#/components/schemas/OAuth2TokenResponse/properties/created_at"
          },
          "application": {
            "type": "object",
            "description": "OAuth 2 Client Application",
            "additionalProperties": false,
            "properties": {
              "uid": {
                "type": "string",
                "description": "OAuth 2 Client Application UID"
              }
            }
          }
        }
      }
    }
  },
  "x-readme": {}
}
```