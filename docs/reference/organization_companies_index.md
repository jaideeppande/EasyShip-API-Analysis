# List all Companies of the Organization

Retrieve a list of companies from a specific organization.

Required authorization scope: `enterprise.company:read`


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
      "name": "Organizations",
      "description": "Organizations API"
    }
  ],
  "paths": {
    "/2024-11/organizations/{organization_id}/companies": {
      "get": {
        "summary": "List all Companies of the Organization",
        "tags": [
          "Organizations"
        ],
        "operationId": "organization_companies_index",
        "description": "Retrieve a list of companies from a specific organization.\n\nRequired authorization scope: `enterprise.company:read`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.company"
            ]
          }
        ],
        "parameters": [
          {
            "name": "sort_by",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "company_name",
                "created_at"
              ]
            },
            "required": false,
            "description": "Sort records by listed columns. Default: `created_at`",
            "example": "created_at"
          },
          {
            "name": "sort_direction",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "ASC",
                "DESC"
              ]
            },
            "required": false,
            "description": "Set the sort direction. Default: `DESC`",
            "example": "ASC"
          },
          {
            "name": "organization_id",
            "in": "path",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true,
            "description": "Organization ID provided when creating the organization"
          },
          {
            "name": "company_name",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "required": false,
            "description": "Filter by company name"
          },
          {
            "name": "easyship_company_id",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "required": false,
            "description": "Filter by Easyship company ID"
          },
          {
            "name": "owner_email",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "required": false,
            "description": "Filter by company owner's email"
          }
        ],
        "responses": {
          "200": {
            "description": "company list",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "companies": [
                        {
                          "country_alpha2": "HK",
                          "created_at": "2022-02-22T12:21:00Z",
                          "easyship_company_id": "CHK100001",
                          "external_id": null,
                          "name": "Test company 1",
                          "organization": {
                            "created_at": "2022-02-22T12:21:00Z",
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "name": "test organization",
                            "updated_at": "2022-02-22T12:21:00Z"
                          },
                          "owner": {
                            "email": "test@test.com",
                            "first_name": "Foo",
                            "last_name": "Bar",
                            "mobile_phone": "+852-1234-5678"
                          },
                          "updated_at": "2022-02-22T12:21:00Z"
                        },
                        {
                          "country_alpha2": "HK",
                          "created_at": "2022-02-22T12:20:00Z",
                          "easyship_company_id": "CHK100002",
                          "external_id": null,
                          "name": "Test company 2",
                          "organization": {
                            "created_at": "2022-02-22T12:21:00Z",
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "name": "test organization",
                            "updated_at": "2022-02-22T12:21:00Z"
                          },
                          "owner": {
                            "email": "test@test.com",
                            "first_name": "Foo",
                            "last_name": "Bar",
                            "mobile_phone": "+852-1234-5678"
                          },
                          "updated_at": "2022-02-22T12:21:00Z"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 2
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "company list"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/company_list"
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
      "company_list": {
        "type": "object",
        "description": "List of Companies",
        "additionalProperties": false,
        "properties": {
          "companies": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Company"
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
      "Company": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "Company name"
          },
          "country_alpha2": {
            "type": "string",
            "description": "Country Code in Alpha-2 format (ISO 3166-1)",
            "enum": [
              "AE",
              "AL",
              "AT",
              "AU",
              "BA",
              "BE",
              "BG",
              "CA",
              "CH",
              "CN",
              "CY",
              "CZ",
              "DE",
              "DK",
              "EE",
              "ES",
              "FI",
              "FR",
              "GB",
              "GR",
              "HK",
              "HR",
              "HU",
              "ID",
              "IE",
              "IL",
              "IN",
              "IS",
              "IT",
              "JP",
              "KR",
              "LT",
              "LU",
              "LV",
              "MT",
              "MX",
              "MY",
              "NL",
              "NO",
              "NZ",
              "PH",
              "PL",
              "PT",
              "RO",
              "RS",
              "SE",
              "SG",
              "SI",
              "SK",
              "TH",
              "TR",
              "TW",
              "UA",
              "US",
              "VN"
            ]
          },
          "easyship_company_id": {
            "type": "string",
            "description": "Easyship Company ID"
          },
          "external_id": {
            "type": "string",
            "nullable": true,
            "description": "An ID to distinguish different child company under same organization"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "Date and time when the company was created"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "Date and time when the company was last updated"
          },
          "owner": {
            "$ref": "#/components/schemas/CompanyOwner"
          },
          "organization": {
            "$ref": "#/components/schemas/Organization"
          }
        }
      },
      "CompanyOwner": {
        "type": "object",
        "description": "Company Owner",
        "additionalProperties": false,
        "properties": {
          "email": {
            "type": "string",
            "description": "Email address",
            "format": "(?i-mx:\\A(?:[a-z0-9!#$%&'*+\\/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+\\/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])\\z)"
          },
          "first_name": {
            "type": "string",
            "description": "First name of the company owner",
            "maxLength": 140,
            "minLength": 1
          },
          "last_name": {
            "type": "string",
            "description": "Last name of the company owner",
            "maxLength": 140,
            "minLength": 1
          },
          "mobile_phone": {
            "type": "string",
            "nullable": true,
            "description": "Optional phone number of the company owner."
          }
        }
      },
      "Organization": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Organization ID"
          },
          "name": {
            "type": "string",
            "description": "Organization name"
          },
          "updated_at": {
            "type": "string",
            "format": "datetime"
          },
          "created_at": {
            "type": "string",
            "format": "datetime"
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
      }
    }
  }
}
```