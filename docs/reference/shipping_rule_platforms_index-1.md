# List all Platform Names

Retrieve a list of available platform names for shipping rules.

Required authorization scope: `enterprise.shipping_rule:read`


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
      "name": "Shipping Rules",
      "description": "Shipping Rules API"
    }
  ],
  "paths": {
    "/2024-11/shipping_rules/platforms": {
      "get": {
        "summary": "List all Platform Names",
        "tags": [
          "Shipping Rules"
        ],
        "operationId": "shipping_rule_platforms_index",
        "description": "Retrieve a list of available platform names for shipping rules.\n\nRequired authorization scope: `enterprise.shipping_rule:read`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.shipping_rule"
            ]
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
            "description": "list of platform names",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "platforms": [
                        {
                          "name": "SellerCenter"
                        },
                        {
                          "name": "eBay"
                        },
                        {
                          "name": "Amazon"
                        },
                        {
                          "name": "Shopify"
                        },
                        {
                          "name": "EtsyGroup"
                        },
                        {
                          "name": "WooCommerceGroup"
                        },
                        {
                          "name": "Shopmatic"
                        },
                        {
                          "name": "API"
                        },
                        {
                          "name": "AlloyAutomation"
                        },
                        {
                          "name": "Builderall"
                        },
                        {
                          "name": "Make"
                        },
                        {
                          "name": "Odoo"
                        },
                        {
                          "name": "Omnyfy"
                        },
                        {
                          "name": "Zapier"
                        },
                        {
                          "name": "BackerKit"
                        },
                        {
                          "name": "Netsuite"
                        },
                        {
                          "name": "Celigo"
                        },
                        {
                          "name": "SkuVault"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": 2,
                          "count": 48
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of platform names"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_platform_list"
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
      "shipping_rule_platform_list": {
        "type": "object",
        "description": "List of plaforms for Shipping Rules",
        "additionalProperties": false,
        "properties": {
          "platforms": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShippingRulePlatform"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
      "ShippingRulePlatform": {
        "type": "object",
        "description": "Platform",
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "Platform name for shipping rules."
          }
        }
      }
    }
  }
}
```