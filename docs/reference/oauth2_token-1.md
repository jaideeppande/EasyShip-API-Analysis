# Create an Access Token

Retrieve an OAuth 2 Access Token.

The endpoint is part of [OAuth 2.0 Authorization Code](https://developers.easyship.com/docs/how-to-authorize-easyship-user) flow.

Refresh tokens are for one-time use only. A new refresh token is always issued with a new access token.


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
    "/oauth2/token": {
      "post": {
        "summary": "Create an Access Token",
        "tags": [
          "Authorization"
        ],
        "operationId": "oauth2_token",
        "description": "Retrieve an OAuth 2 Access Token.\n\nThe endpoint is part of [OAuth 2.0 Authorization Code](https://developers.easyship.com/docs/how-to-authorize-easyship-user) flow.\n\nRefresh tokens are for one-time use only. A new refresh token is always issued with a new access token.\n",
        "parameters": [],
        "responses": {
          "200": {
            "description": "Access Token (Refresh Token)",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "access_token": "test_3m0V3q5MDgxNIR5Cglw/ONL8ZMPNy91f1Kolt+BOWG8=",
                      "token_type": "Bearer",
                      "expires_in": 1645539660,
                      "refresh_token": "UhLaQeeduKhGPLoEnQ29aLGuV077VSNEp7LPij_P6Tg",
                      "scope": "rate shipment label track company pickup location store product",
                      "created_at": 1645532460
                    },
                    "summary": "Access Token (Refresh Token)"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2TokenResponse"
                }
              }
            }
          },
          "401": {
            "description": "Unsupported Client Credentials grant type",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": "unauthorized_client",
                      "error_description": "The client is not authorized to perform this request using this method."
                    },
                    "summary": "Unsupported Client Credentials grant type"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/OAuth2ErrorResponse"
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
                "access_token_code": {
                  "summary": "authorization_code",
                  "value": {
                    "client_id": "ixaj5e4L25axd_d6b4K2wG479_9c3itEN8eexE_67Qk",
                    "client_secret": "M9z6YbwW-e19ffQ6w4YuQIU0SGE2wNhOzBlWslNF4mY",
                    "code": "zm_0fp6O7yBRasUlB-ZKax0JHPY-3HArw6Y9u66XjIM",
                    "grant_type": "authorization_code",
                    "redirect_uri": "https://domain.com/callback"
                  }
                },
                "access_token_refresh_token": {
                  "summary": "refresh_token",
                  "value": {
                    "client_id": "ixaj5e4L25axd_d6b4K2wG479_9c3itEN8eexE_67Qk",
                    "client_secret": "M9z6YbwW-e19ffQ6w4YuQIU0SGE2wNhOzBlWslNF4mY",
                    "refresh_token": "UhLaQeeduKhGPLoEnQ29aLGuV077VSNEp7LPij_P6Tg",
                    "grant_type": "refresh_token",
                    "scope": "rate shipment label track company pickup location store product"
                  }
                },
                "unsupported_client_credentials_grant_type": {
                  "summary": "client_credentials",
                  "value": {
                    "grant_type": "client_credentials",
                    "client_id": "ixaj5e4L25axd_d6b4K2wG479_9c3itEN8eexE_67Qk",
                    "client_secret": "M9z6YbwW-e19ffQ6w4YuQIU0SGE2wNhOzBlWslNF4mY",
                    "scope": "address"
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
      "url": "https://api.easyship.com",
      "description": "Production"
    }
  ],
  "components": {
    "schemas": {
      "OAuth2TokenRequest": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/OAuth2ClientCredentialsRequest"
          },
          {
            "$ref": "#/components/schemas/OAuth2AuthorizationCodeRequest"
          },
          {
            "$ref": "#/components/schemas/OAuth2RefreshTokenRequest"
          }
        ],
        "discriminator": {
          "propertyName": "grant_type",
          "mapping": {
            "client_credentials": "#/components/schemas/OAuth2ClientCredentialsRequest",
            "authorization_code": "#/components/schemas/OAuth2AuthorizationCodeRequest",
            "refresh_token": "#/components/schemas/OAuth2RefreshTokenRequest"
          }
        }
      },
      "OAuth2AuthorizationCodeRequest": {
        "type": "object",
        "description": "OAuth 2 Authorization Code Request",
        "additionalProperties": false,
        "required": [
          "grant_type",
          "client_id",
          "client_secret",
          "code",
          "redirect_uri"
        ],
        "properties": {
          "grant_type": {
            "type": "string",
            "description": "OAuth 2 Grant Type",
            "enum": [
              "authorization_code"
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
          "redirect_uri": {
            "type": "string",
            "format": "uri",
            "description": "OAuth 2 Redirect URI"
          },
          "code": {
            "type": "string",
            "description": "OAuth 2 Authorization Code provided by authenticated user in the callback to `redirect_uri`."
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
            "description": "OAuth 2 Scopes separated by space. All Public API scopes are supported, but they must be allowed on the Partner Application on the Dashboard.\n\n> 🚧 Warning\n> \n> With the release of Public API 2024-09, we introduced new [enhanced scopes](https://developers.easyship.com/reference/scopes).\n> We support only 1 type of API scopes per OAuth 2 application. It is impossible to mix old and new scopes on a single application.\n\n|Scope|Description|\n|---|---|\n|address|Addresses API (2023-01 and older)|\n|address_validation|Address Validations API (2023-01 and older)|\n|analytics|Analytics API (2023-01 and older)|\n|asset|Assets API (2023-01 and older)|\n|batch|Batches API (2023-01 and older)|\n|billing_document|Billing Documents API (2023-01 and older)|\n|box|Boxes API (2023-01 and older)|\n|courier|Couriers API (2023-01 and older)|\n|courier_account|Courier Accounts API (2023-01 and older)|\n|credit|Credits API (2023-01 and older)|\n|custom_markup_rate|Custom Markup Rates API (2023-01 and older)|\n|efulfillment|E-Fulfillment API (2023-01 and older)|\n|hs_code|Hs Codes API (2023-01 and older)|\n|label|Labels API (2023-01 and older)|\n|location|Locations API (2023-01 and older)|\n|manifest|Manifests API (2023-01 and older)|\n|payment|Payments API (2023-01 and older)|\n|payment_source|Payment Sources API (2023-01 and older)|\n|pickup|Pickups API (2023-01 and older)|\n|product|Products API (2023-01 and older)|\n|rate|Rates API (2023-01 and older)|\n|reference|References API (2023-01 and older)|\n|settings|Settings API (2023-01 and older)|\n|shipment|Shipments API (2023-01 and older)|\n|shipment_document|Shipment Documents API (2023-01 and older)|\n|shipping_rule|Shipping Rules API (2023-01 and older)|\n|store|Stores API (2023-01 and older)|\n|tag|Tags API (2023-01 and older)|\n|tax_and_duty|Tax And Duties API (2023-01 and older)|\n|track|Tracks API (2023-01 and older)|\n|track_3p|Track 3ps API (2023-01 and older)|\n|transaction_record|Transaction Records API (2023-01 and older)|\n|webhook|Webhooks API (2023-01 and older)|\n|public.address:read|Addresses (read only) Public API (2024-09 and newer)|\n|public.address:write|Addresses (write only) Public API (2024-09 and newer)|\n|public.address_validation:write|Address Validations (write only) Public API (2024-09 and newer)|\n|public.analytics:read|Analytics (read only) Public API (2024-09 and newer)|\n|public.app_access:write|App Accesses (write only) Public API (2024-09 and newer)|\n|public.asset:read|Assets (read only) Public API (2024-09 and newer)|\n|public.asset:write|Assets (write only) Public API (2024-09 and newer)|\n|public.batch:read|Batches (read only) Public API (2024-09 and newer)|\n|public.batch:write|Batches (write only) Public API (2024-09 and newer)|\n|public.billing_document:read|Billing Documents (read only) Public API (2024-09 and newer)|\n|public.billing_document:write|Billing Documents (write only) Public API (2024-09 and newer)|\n|public.box:read|Boxes (read only) Public API (2024-09 and newer)|\n|public.box:write|Boxes (write only) Public API (2024-09 and newer)|\n|public.courier:read|Couriers (read only) Public API (2024-09 and newer)|\n|public.courier:write|Couriers (write only) Public API (2024-09 and newer)|\n|public.courier_service:read|Courier Services (read only) Public API (2024-09 and newer)|\n|public.credit:read|Credits (read only) Public API (2024-09 and newer)|\n|public.efulfillment:write|E-Fulfillment (write only) Public API (2024-09 and newer)|\n|public.hs_code:read|Hs Codes (read only) Public API (2024-09 and newer)|\n|public.label:write|Labels (write only) Public API (2024-09 and newer)|\n|public.location:read|Locations (read only) Public API (2024-09 and newer)|\n|public.manifest:read|Manifests (read only) Public API (2024-09 and newer)|\n|public.manifest:write|Manifests (write only) Public API (2024-09 and newer)|\n|public.payment:write|Payments (write only) Public API (2024-09 and newer)|\n|public.payment_source:read|Payment Sources (read only) Public API (2024-09 and newer)|\n|public.payment_source:write|Payment Sources (write only) Public API (2024-09 and newer)|\n|public.pickup:read|Pickups (read only) Public API (2024-09 and newer)|\n|public.pickup:write|Pickups (write only) Public API (2024-09 and newer)|\n|public.product:read|Products (read only) Public API (2024-09 and newer)|\n|public.product:write|Products (write only) Public API (2024-09 and newer)|\n|public.rate:read|Rates (read only) Public API (2024-09 and newer)|\n|public.redirect:write|Redirects (write only) Public API (2024-09 and newer)|\n|public.reference:read|References (read only) Public API (2024-09 and newer)|\n|public.setting:read|Settings (read only) Public API (2024-09 and newer)|\n|public.setting:write|Settings (write only) Public API (2024-09 and newer)|\n|public.shipment:read|Shipments (read only) Public API (2024-09 and newer)|\n|public.shipment:write|Shipments (write only) Public API (2024-09 and newer)|\n|public.shipment_document:read|Shipment Documents (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:read|Shipping Rules (read only) Public API (2024-09 and newer)|\n|public.shipping_rule:write|Shipping Rules (write only) Public API (2024-09 and newer)|\n|public.store:read|Stores (read only) Public API (2024-09 and newer)|\n|public.tag:read|Tags (read only) Public API (2024-09 and newer)|\n|public.tag:write|Tags (write only) Public API (2024-09 and newer)|\n|public.tax_and_duty:read|Tax And Duties (read only) Public API (2024-09 and newer)|\n|public.track:read|Tracks (read only) Public API (2024-09 and newer)|\n|public.track_3p:read|Track 3ps (read only) Public API (2024-09 and newer)|\n|public.track_3p:write|Track 3ps (write only) Public API (2024-09 and newer)|\n|public.transaction_record:read|Transaction Records (read only) Public API (2024-09 and newer)|\n|public.webhook:read|Webhooks (read only) Public API (2024-09 and newer)|\n|public.webhook:write|Webhooks (write only) Public API (2024-09 and newer)|\n"
          }
        }
      },
      "OAuth2ErrorResponse": {
        "type": "object",
        "description": "OAuth 2 Error Response",
        "additionalProperties": false,
        "properties": {
          "error": {
            "type": "string",
            "description": "OAuth 2 Error Code"
          },
          "error_description": {
            "type": "string",
            "description": "OAuth 2 Error Description"
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
      }
    }
  },
  "x-readme": {}
}
```