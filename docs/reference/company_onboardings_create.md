# Create a Company Onboarding

Create a Company Onboarding.

Required authorization scope: `enterprise.company:write`


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
      "name": "Companies",
      "description": "Companies API"
    }
  ],
  "paths": {
    "/2024-11/company_onboardings": {
      "post": {
        "summary": "Create a Company Onboarding",
        "tags": [
          "Companies"
        ],
        "operationId": "company_onboardings_create",
        "description": "Create a Company Onboarding.\n\nRequired authorization scope: `enterprise.company:write`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.company"
            ]
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "Company onboarding created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "company_onboarding": {
                        "app_access": {
                          "expires_at": "2022-02-22T12:21:10Z",
                          "url": "https://onboarding.easyship.com?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..S3mXgIgk-0kT78FG"
                        },
                        "completed_at": null,
                        "created_at": "2022-02-22T12:21:00Z",
                        "easyship_company_id": null,
                        "external_id": "my-company-123"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Company onboarding created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/company_onboarding_single"
                }
              }
            }
          },
          "422": {
            "description": "Company Onboarding already exists",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "a Company Onboarding with external_id 'my-company-123' already exists"
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "Company Onboarding already exists"
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
                "$ref": "#/components/schemas/CompanyOnboardingCreate"
              },
              "examples": {
                "company_onboarding_created": {
                  "summary": "Company onboarding created",
                  "value": {
                    "external_id": "my-company-123",
                    "country_alpha2": "US",
                    "name": "My Company",
                    "owner": {
                      "email": "test@test.com",
                      "first_name": "Test",
                      "last_name": "User"
                    },
                    "address": {
                      "line_1": "123 Main St",
                      "line_2": "Apt 1",
                      "city": "Anytown",
                      "state": "CA",
                      "postal_code": "12345",
                      "contact_phone": "+1234567890"
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
      "company_onboarding_single": {
        "type": "object",
        "description": "Company Onboarding Detail",
        "additionalProperties": false,
        "properties": {
          "company_onboarding": {
            "$ref": "#/components/schemas/CompanyOnboarding"
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
      "Address": {
        "type": "object",
        "properties": {
          "line_1": {
            "type": "string",
            "description": "First line of the street address",
            "maximum": 35
          },
          "line_2": {
            "type": "string",
            "nullable": true,
            "description": "Second line of the street address",
            "maximum": 35
          },
          "state": {
            "type": "string",
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names.",
            "maximum": 200,
            "nullable": true
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "description": "Postal code. Leave it null or 0 if the country does not have postal codes. Mandatory for these countries: AD, AF, AI, AL, AM, AQ, AR, AS, AT, AU, AX, AZ, BA, BB, BD, BE, BG, BL, BM, BN, BQ, BR, BT, BV, BY, CA, CC, CH, CL, CN, CO, CR, CU, CV, CX, CY, CZ, DE, DK, DO, DZ, EC, EE, EG, EH, ES, ET, FI, FK, FM, FO, FR, GA, GB, GE, GF, GG, GI, GL, GP, GR, GS, GT, GU, GW, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JO, JP, KG, KH, KR, KW, KY, KZ, LA, LB, LI, LK, LR, LS, LT, LU, LV, MA, MC, MD, ME, MF, MG, MH, MK, MM, MN, MP, MQ, MT, MV, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NZ, OM, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, RE, RO, RS, RU, SD, SE, SG, SH, SI, SJ, SK, SM, SN, SS, SV, SX, SZ, TC, TD, TH, TJ, TM, TN, TR, TW, UA, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, WF, WS, YT, ZA, ZM."
          },
          "contact_name": {
            "type": "string",
            "nullable": true,
            "description": "The full name of a person at the address. Owner name will be used if not provided.",
            "maximum": 22
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready).",
            "maximum": 20
          }
        }
      },
      "AppAccess": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "url": {
            "type": "string",
            "format": "uri",
            "description": "App Access redirect URL with one time token"
          },
          "expires_at": {
            "type": "string",
            "format": "datetime",
            "description": "Expiry time for URI"
          }
        }
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
      "CompanyOnboarding": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "app_access",
          "completed_at",
          "created_at",
          "easyship_company_id",
          "external_id"
        ],
        "properties": {
          "app_access": {
            "$ref": "#/components/schemas/AppAccess"
          },
          "completed_at": {
            "type": "string",
            "format": "date-time",
            "nullable": true,
            "description": "When the onboarding was completed"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the Company Onboarding was created"
          },
          "easyship_company_id": {
            "type": "string",
            "nullable": true,
            "description": "Easyship Company ID of the onboarded Company. Only present after the Company Onboarding is completed."
          },
          "external_id": {
            "type": "string",
            "nullable": false,
            "description": "External identifier of the Company to onboard."
          }
        }
      },
      "CompanyOnboardingCreate": {
        "type": "object",
        "required": [
          "external_id",
          "country_alpha2"
        ],
        "properties": {
          "external_id": {
            "type": "string",
            "nullable": false,
            "allOf": [
              {
                "$ref": "#/components/schemas/Company/properties/external_id"
              }
            ]
          },
          "country_alpha2": {
            "type": "string",
            "nullable": false,
            "description": "Country Code in Alpha-2 format (ISO 3166-1).",
            "allOf": [
              {
                "$ref": "#/components/schemas/Company/properties/country_alpha2"
              }
            ]
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Company name. Optional field that can be used to pre-fill the company name in the onboarding form."
          },
          "owner": {
            "type": "object",
            "nullable": true,
            "description": "Company owner information. Optional field that will be used to pre-fill the company owner in the onboarding form.",
            "properties": {
              "email": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/CompanyOwner/properties/email"
                  }
                ]
              },
              "first_name": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/CompanyOwner/properties/first_name"
                  }
                ]
              },
              "last_name": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/CompanyOwner/properties/last_name"
                  }
                ]
              }
            }
          },
          "address": {
            "type": "object",
            "nullable": true,
            "description": "Company address information. Optional field that will be used to pre-fill the company address in the onboarding form.",
            "properties": {
              "line_1": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/line_1"
                  }
                ]
              },
              "line_2": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/line_2"
                  }
                ]
              },
              "city": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/city"
                  }
                ]
              },
              "state": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/state"
                  }
                ]
              },
              "postal_code": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/postal_code"
                  }
                ]
              },
              "contact_phone": {
                "type": "string",
                "nullable": true,
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Address/properties/contact_phone"
                  }
                ]
              }
            }
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
      }
    }
  }
}
```