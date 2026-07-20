# Retrieve an Access Token

Retrieve an OAuth 2 Access Token.

There are two ways of accessing the child companies:

1. **Client Credentials Grant** with a `enterprise.child_company::access` scope and a custom header `X_EASYSHIP_COMPANY_ID` in each request to our Public API.
2. A custom **Delegated Account Grant**, that will generate access and refresh tokens associated with a specific child company defined in the `easyship_company_id`.


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
    "/oauth2/token": {
      "post": {
        "summary": "Retrieve an Access Token",
        "tags": [
          "Authorization"
        ],
        "operationId": "oauth2_token",
        "description": "Retrieve an OAuth 2 Access Token.\n\nThere are two ways of accessing the child companies:\n\n1. **Client Credentials Grant** with a `enterprise.child_company::access` scope and a custom header `X_EASYSHIP_COMPANY_ID` in each request to our Public API.\n2. A custom **Delegated Account Grant**, that will generate access and refresh tokens associated with a specific child company defined in the `easyship_company_id`.\n",
        "parameters": [],
        "responses": {
          "200": {
            "description": "Access and Refresh Tokens from Delegated Account grant",
            "content": {
              "application/json": {
                "examples": {
                  "client_credentials": {
                    "value": {
                      "access_token": "test_3m0V3q5MDgxNIR5Cglw/ONL8ZMPNy91f1Kolt+BOWG8=",
                      "token_type": "Bearer",
                      "expires_in": 7200,
                      "scope": "enterprise.organization:write",
                      "created_at": 1645532460
                    },
                    "summary": "Access Token from Client Credentials grant"
                  },
                  "delegated_account": {
                    "value": {
                      "access_token": "test_3m0V3q5MDgxNIR5Cglw/ONL8ZMPNy91f1Kolt+BOWG8=",
                      "token_type": "Bearer",
                      "expires_in": 7200,
                      "refresh_token": "hiwZBEsfFV71suH_EbCvRdQUtEVK2dv61msrJ1DptEM",
                      "scope": "rate",
                      "created_at": 1645532460
                    },
                    "summary": "Access and Refresh Tokens from Delegated Account grant"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2TokenResponse"
                }
              }
            }
          },
          "400": {
            "description": "Invalid Company for Delegated Account",
            "content": {
              "application/json": {
                "examples": {
                  "delegated_account_invalid_company": {
                    "value": {
                      "error": "invalid_account",
                      "error_description": "The authorization server encountered an unexpected condition which prevented it from fulfilling the request."
                    },
                    "summary": "Invalid Company for Delegated Account"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2Error"
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/OAuth2TokenRequest"
              },
              "examples": {
                "access_token_from_client_credentials_grant": {
                  "summary": "Access Token from Client Credentials grant",
                  "value": {
                    "grant_type": "client_credentials",
                    "client_id": "28P8K2PSAsVyugLBKIY1neZXYulpHElHVAAmOrJ9Pds",
                    "client_secret": "M9z6YbwW-e19ffQ6w4YuQIU0SGE2wNhOzBlWslNF4mY",
                    "scope": "enterprise.organization:write"
                  }
                },
                "access_and_refresh_tokens_from_delegated_account_grant": {
                  "summary": "Access and Refresh Tokens from Delegated Account grant",
                  "value": {
                    "grant_type": "delegated_account",
                    "client_id": "28P8K2PSAsVyugLBKIY1neZXYulpHElHVAAmOrJ9Pds",
                    "client_secret": "M9z6YbwW-e19ffQ6w4YuQIU0SGE2wNhOzBlWslNF4mY",
                    "easyship_company_id": "CGB00001",
                    "scope": "rate"
                  }
                },
                "invalid_company_for_delegated_account": {
                  "summary": "Invalid Company",
                  "value": {
                    "grant_type": "delegated_account",
                    "client_id": "28P8K2PSAsVyugLBKIY1neZXYulpHElHVAAmOrJ9Pds",
                    "client_secret": "KJIzFE1qCyJ2ZkJjb4WtTsD67kXiKliJSAShCSPRRco",
                    "easyship_company_id": "CGB00001",
                    "scope": "rate"
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
      "OAuth2DelegatedAccountRequest": {
        "type": "object",
        "description": "OAuth 2 Delegated Account Request",
        "additionalProperties": false,
        "required": [
          "grant_type",
          "client_id",
          "client_secret",
          "easyship_company_id",
          "scope"
        ],
        "properties": {
          "grant_type": {
            "type": "string",
            "description": "OAuth 2 Grant Type",
            "enum": [
              "delegated_account"
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
          "easyship_company_id": {
            "type": "string",
            "description": "Easyship Company ID of the child company"
          },
          "scope": {
            "type": "string",
            "description": "OAuth 2 Scopes separated by space. All Enterprise and Public API scopes are supported, but they must be allowed on the Enterprise API Client Application on the Dashboard.\n\n|Scope|Description|\n|---|---|\n|address|Addresses API (2023-01 and older)|\n|asset|Assets API (2023-01 and older)|\n|billing_document|Billing Documents API (2023-01 and older)|\n|box|Boxes API (2023-01 and older)|\n|courier|Couriers API (2023-01 and older)|\n|courier_account|Courier Accounts API (2023-01 and older)|\n|credit|Credits API (2023-01 and older)|\n|hs_code|Hs Codes API (2023-01 and older)|\n|label|Labels API (2023-01 and older)|\n|pickup|Pickups API (2023-01 and older)|\n|product|Products API (2023-01 and older)|\n|rate|Rates API (2023-01 and older)|\n|reference|References API (2023-01 and older)|\n|settings|Settings API (2023-01 and older)|\n|shipment|Shipments API (2023-01 and older)|\n|shipment_document|Shipment Documents API (2023-01 and older)|\n|store|Stores API (2023-01 and older)|\n|tag|Tags API (2023-01 and older)|\n|tax_and_duty|Tax And Duties API (2023-01 and older)|\n|track|Tracks API (2023-01 and older)|\n|transaction_record|Transaction Records API (2023-01 and older)|\n|webhook|Webhooks API (2023-01 and older)|\n|public.address:read|Addresses (read only) Public API (2024-09 and newer)|\n|public.address:write|Addresses (write only) Public API (2024-09 and newer)|\n|public.analytics:read|Analytics (read only) Public API (2024-09 and newer)|\n|public.app_access:write|App Accesses (write only) Public API (2024-09 and newer)|\n|public.asset:read|Assets (read only) Public API (2024-09 and newer)|\n|public.asset:write|Assets (write only) Public API (2024-09 and newer)|\n|public.batch:read|Batches (read only) Public API (2024-09 and newer)|\n|public.batch:write|Batches (write only) Public API (2024-09 and newer)|\n|public.billing_document:read|Billing Documents (read only) Public API (2024-09 and newer)|\n|public.billing_document:write|Billing Documents (write only) Public API (2024-09 and newer)|\n|public.box:read|Boxes (read only) Public API (2024-09 and newer)|\n|public.box:write|Boxes (write only) Public API (2024-09 and newer)|\n|public.courier:read|Couriers (read only) Public API (2024-09 and newer)|\n|public.courier:write|Couriers (write only) Public API (2024-09 and newer)|\n|public.courier_service:read|Courier Services (read only) Public API (2024-09 and newer)|\n|public.credit:read|Credits (read only) Public API (2024-09 and newer)|\n|public.hs_code:read|Hs Codes (read only) Public API (2024-09 and newer)|\n|public.label:write|Labels (write only) Public API (2024-09 and newer)|\n|public.location:read|Locations (read only) Public API (2024-09 and newer)|\n|public.manifest:read|Manifests (read only) Public API (2024-09 and newer)|\n|public.manifest:write|Manifests (write only) Public API (2024-09 and newer)|\n|public.payment:write|Payments (write only) Public API (2024-09 and newer)|\n|public.payment_source:read|Payment Sources (read only) Public API (2024-09 and newer)|\n|public.payment_source:write|Payment Sources (write only) Public API (2024-09 and newer)|\n|public.pickup:read|Pickups (read only) Public API (2024-09 and newer)|\n|public.pickup:write|Pickups (write only) Public API (2024-09 and newer)|\n|public.product:read|Products (read only) Public API (2024-09 and newer)|\n|public.product:write|Products (write only) Public API (2024-09 and newer)|\n|public.rate:read|Rates (read only) Public API (2024-09 and newer)|\n|public.redirect:write|Redirects (write only) Public API (2024-09 and newer)|\n|public.reference:read|References (read only) Public API (2024-09 and newer)|\n|public.setting:read|Settings (read only) Public API (2024-09 and newer)|\n|public.setting:write|Settings (write only) Public API (2024-09 and newer)|\n|public.shipment:read|Shipments (read only) Public API (2024-09 and newer)|\n|public.shipment:write|Shipments (write only) Public API (2024-09 and newer)|\n|public.shipment_document:read|Shipment Documents (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:read|Shipping Rules (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:write|Shipping Rules (write only) Public API (2024-09 and newer)|\n|public.store:read|Stores (read only) Public API (2024-09 and newer)|\n|public.tag:read|Tags (read only) Public API (2024-09 and newer)|\n|public.tag:write|Tags (write only) Public API (2024-09 and newer)|\n|public.tax_and_duty:read|Tax And Duties (read only) Public API (2024-09 and newer)|\n|public.track:read|Tracks (read only) Public API (2024-09 and newer)|\n|public.transaction_record:read|Transaction Records (read only) Public API (2024-09 and newer)|\n|public.webhook:read|Webhooks (read only) Public API (2024-09 and newer)|\n|public.webhook:write|Webhooks (write only) Public API (2024-09 and newer)|\n"
          }
        }
      },
      "OAuth2RefreshTokenRequest": {
        "type": "object",
        "description": "OAuth 2 Refresh Token Request",
        "additionalProperties": false,
        "required": [
          "grant_type",
          "client_id",
          "client_secret",
          "refresh_token"
        ],
        "properties": {
          "grant_type": {
            "type": "string",
            "description": "OAuth 2 Grant Type",
            "enum": [
              "refresh_token"
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
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest/properties/scope"
          },
          "refresh_token": {
            "type": "string",
            "description": "OAuth 2 Refresh Token"
          }
        }
      },
      "OAuth2TokenRequest": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest"
          },
          {
            "$ref": "#/components/schemas/OAuth2DelegatedAccountRequest"
          },
          {
            "$ref": "#/components/schemas/OAuth2RefreshTokenRequest"
          }
        ],
        "discriminator": {
          "propertyName": "grant_type",
          "mapping": {
            "client_credentials": "#/components/schemas/OAuth2ClientCredentialsRequest",
            "delegated_account": "#/components/schemas/OAuth2DelegatedAccountRequest",
            "refresh_token": "#/components/schemas/OAuth2RefreshTokenRequest"
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
      "OAuth2Error": {
        "type": "object",
        "description": "OAuth 2 Error",
        "additionalProperties": false,
        "required": [
          "error",
          "error_description"
        ],
        "properties": {
          "error": {
            "type": "string"
          },
          "error_description": {
            "type": "string"
          }
        }
      }
    }
  }
}
```