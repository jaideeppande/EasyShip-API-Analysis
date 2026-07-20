# Create a Shipping Rule

Create a shipping rule for a specific organization.

Required authorization scope: `enterprise.shipping_rule:write`


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
    "/2024-11/organizations/{organization_id}/shipping_rules": {
      "post": {
        "summary": "Create a Shipping Rule",
        "tags": [
          "Shipping Rules"
        ],
        "operationId": "organizations_shipping_rules_create",
        "description": "Create a shipping rule for a specific organization.\n\nRequired authorization scope: `enterprise.shipping_rule:write`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.shipping_rule"
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
            "description": "shipping rule successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "shipping_rule": {
                        "accessible": true,
                        "actions": [
                          {
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0004",
                            "options": {
                              "never_courier_service_ids": [
                                "01563646-58c1-4607-8fe0-cae3e33c0001",
                                "01563646-58c1-4607-8fe0-cae3e33c0002"
                              ]
                            },
                            "type": "add_never_courier_service"
                          }
                        ],
                        "active": true,
                        "checkout_restrictive": true,
                        "conditions": [
                          {
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                            "options": {
                              "country_ids": [
                                234,
                                235
                              ]
                            },
                            "type": "match_country"
                          },
                          {
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                            "options": {
                              "shipment_items_count": 2,
                              "operator": "equal_to"
                            },
                            "type": "match_items_count"
                          }
                        ],
                        "created_at": "2022-02-22T12:21:00Z",
                        "description": "Description of the Shipping Rule",
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "name": "Example Shipping Rule",
                        "priority": 10,
                        "updated_at": "2022-02-22T12:21:00Z"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "shipping rule successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_single"
                }
              }
            }
          },
          "422": {
            "description": "invalid content",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Name can't be blank",
                          "Description can't be blank"
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "invalid content"
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
                "$ref": "#/components/schemas/ShippingRuleCreate"
              },
              "examples": {
                "shipping_rule_successfully_created": {
                  "summary": "shipping rule successfully created",
                  "value": {
                    "name": "Example Shipping Rule",
                    "description": "Description of the Shipping Rule",
                    "recalculate_shipments": true,
                    "priority": 10,
                    "conditions": [
                      {
                        "type": "match_country",
                        "options": {
                          "country_ids": [
                            234,
                            235
                          ]
                        }
                      },
                      {
                        "type": "match_items_count",
                        "options": {
                          "operator": "equal_to",
                          "shipment_items_count": 2
                        }
                      }
                    ],
                    "actions": [
                      {
                        "type": "add_never_courier_service",
                        "options": {
                          "never_courier_service_ids": [
                            "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "01563646-58c1-4607-8fe0-cae3e33c0002"
                          ]
                        }
                      }
                    ]
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
      "shipping_rule_single": {
        "type": "object",
        "description": "Shipping Rule detail",
        "additionalProperties": false,
        "properties": {
          "shipping_rule": {
            "$ref": "#/components/schemas/ShippingRule"
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
      "ActionAddNeverCourier": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionAddNeverCourierCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionAddPreferredCourier": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionAddPreferredCourierCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceIncoterms": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceIncotermsCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceSortBy": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceSortByCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceInsurance": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceInsuranceCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceTrackingRating": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceTrackingRatingCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "string"
              }
            }
          }
        ]
      },
      "ActionForcePackage": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForcePackageCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionRejectPackages": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionRejectPackagesCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceResidentialSurcharge": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceResidentialSurchargeCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceShipFrom": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceShipFromCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionForceAutomatedReturnRequested": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionForceAutomatedReturnRequestedCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionAddForcedDeliveryTime": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ActionAddForcedDeliveryTimeCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ActionAddNeverCourierCreate": {
        "type": "object",
        "description": "Never add specific courier services",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "add_never_courier_service"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "never_courier_service_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "never_courier_service_ids": {
                "type": "array",
                "description": "List of courier service IDs based on Courier Service API",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "format": "uuid"
                }
              }
            }
          }
        }
      },
      "ActionAddPreferredCourierCreate": {
        "type": "object",
        "description": "Use preferred courier services",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "add_preferred_courier_service"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "preferred_courier_service_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "preferred_courier_service_ids": {
                "type": "array",
                "description": "List of courier service IDs based on Courier Service API",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "format": "uuid"
                }
              }
            }
          }
        }
      },
      "ActionForceIncotermsCreate": {
        "type": "object",
        "description": "Taxes & duties",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_incoterms"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "incoterms"
            ],
            "additionalProperties": false,
            "properties": {
              "incoterms": {
                "type": "string",
                "description": "\"DDP\": \"Pre-paid (included in shipping cost)\"<br>\n\"DDU\": \"Post-paid (not included in shipping cost)\"<br>\n\"DDU_and_Best_DDP\": \"Offer 3 post-paid and 1 pre-paid shipping options (for checkout only)\"<br>\n\"DDP_and_Best_DDU\": \"Offer 1 post-paid and 3 pre-paid shipping options\n",
                "enum": [
                  "DDP",
                  "DDU",
                  "DDU_and_Best_DDP",
                  "DDP_and_Best_DDU"
                ]
              }
            }
          }
        }
      },
      "ActionForceSortByCreate": {
        "type": "object",
        "description": "Sort couriers by total_charge, delivery_time_rank or value_for_money_rank",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_sort_by"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "sort_by"
            ],
            "additionalProperties": false,
            "properties": {
              "sort_by": {
                "type": "string",
                "description": "total_charge: Cheapest\ndelivery_time_rank: Fastest\nvalue_for_money_rank: Best value for money\n",
                "enum": [
                  "total_charge",
                  "delivery_time_rank",
                  "value_for_money_rank"
                ]
              }
            }
          }
        }
      },
      "ActionForceInsuranceCreate": {
        "type": "object",
        "description": "Force applying insurance",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_insurance"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "insured"
            ],
            "additionalProperties": false,
            "properties": {
              "insured": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "ActionForceTrackingRatingCreate": {
        "type": "object",
        "description": "Filter couriers by tracking quality\n\n**Note:** this option is very restrictive and you may not see rates. Please make sure to verify the items selected.\n",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_tracking_rating"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "force_tracking_rating"
            ],
            "additionalProperties": false,
            "properties": {
              "force_tracking_rating": {
                "type": "array",
                "description": "List of tracking ratings to use\n\nFor example: to filter out couriers with `limited` or `basic` tracking you'd set `force_tracking_rating` to `[2, 3]`\n",
                "minItems": 1,
                "items": {
                  "type": "integer",
                  "description": "0: limited \n1: basic \n2: regular \n3: excellent\n",
                  "enum": [
                    0,
                    1,
                    2,
                    3
                  ]
                }
              }
            }
          }
        }
      },
      "ActionForcePackageCreate": {
        "type": "object",
        "description": "Use package",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_package"
            ]
          },
          "options": {
            "oneOf": [
              {
                "type": "object",
                "properties": {
                  "force_box_id": {
                    "type": "string",
                    "format": "uuid",
                    "description": "Box ID based on Box API. Box type is 'box'."
                  }
                }
              },
              {
                "type": "object",
                "properties": {
                  "force_flat_rate_box_id": {
                    "type": "string",
                    "format": "uuid",
                    "description": "Box ID based on Box API. Box type is 'flat_rate_box'."
                  }
                }
              }
            ]
          }
        }
      },
      "ActionRejectPackagesCreate": {
        "type": "object",
        "description": "Exclude specified boxes",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "reject_packages"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "never_package_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "never_package_ids": {
                "type": "array",
                "description": "Box IDs based on Box API.",
                "minItems": 1,
                "items": {
                  "format": "uuid",
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "ActionForceResidentialSurchargeCreate": {
        "type": "object",
        "description": "Declare destination address as residential.",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_residential_surcharge"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "set_as_residential"
            ],
            "additionalProperties": false,
            "properties": {
              "set_as_residential": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "ActionForceShipFromCreate": {
        "type": "object",
        "description": "Ship From",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_ship_from"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "origin_address_id"
            ],
            "additionalProperties": false,
            "properties": {
              "origin_address_id": {
                "type": "string",
                "format": "uuid",
                "description": "Address ID based on Address API."
              }
            }
          }
        }
      },
      "ActionForceAutomatedReturnRequestedCreate": {
        "type": "object",
        "description": "Return labels for domestic shipments",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "force_automated_return_requested"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "automated_return_requested"
            ],
            "additionalProperties": false,
            "properties": {
              "force_automated_return_requested": {
                "type": "boolean"
              }
            }
          }
        }
      },
      "ActionAddForcedDeliveryTimeCreate": {
        "type": "object",
        "description": "Restrict courier services based on delivery time",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "add_forced_delivery_time"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "value"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "Operators for comparison include less than (<), less than or equal to (<=), greater than or equal to (>=), and greater than (>)",
                "enum": [
                  "less_than",
                  "less_than_or_equal_to",
                  "greater_than_or_equal_to",
                  "greater_than"
                ]
              },
              "value": {
                "type": "integer",
                "description": "How many days"
              }
            }
          }
        }
      },
      "ConditionMatchAll": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchAllCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchCountry": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchCountryCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchCategory": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchCategoryCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchState": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchStateCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchZipcode": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchZipcodeCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchSku": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchSkuCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchPlatformName": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchPlatformNameCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchStore": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchStoreCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchBuyerSelectedCourierName": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchBuyerSelectedCourierNameCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchItemsCount": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchItemsCountCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchSellingPrice": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchSellingPriceCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchWeight": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchWeightCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionIncludeOrderTagName": {
        "allOf": [
          {
            "$ref": "#/components/schemas/ConditionIncludeOrderTagNameCreate"
          },
          {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              }
            }
          }
        ]
      },
      "ConditionMatchAllCreate": {
        "type": "object",
        "description": "Condition that matches all orders",
        "required": [
          "type"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_all"
            ]
          }
        }
      },
      "ConditionMatchCountryCreate": {
        "type": "object",
        "description": "Condition that matches the destination country of the orders",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_country"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "country_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "country_ids": {
                "type": "array",
                "minItems": 1,
                "items": {
                  "$ref": "#/components/schemas/CountryID"
                }
              }
            }
          }
        }
      },
      "ConditionMatchCategoryCreate": {
        "type": "object",
        "description": "Condition that matches orders containing specific categories",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_category"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "category_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "category_ids": {
                "type": "array",
                "description": "List of category IDs based on Category API",
                "minItems": 1,
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "ConditionMatchStateCreate": {
        "type": "object",
        "description": "Condition that matches the destination state of the orders",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_state"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "states"
            ],
            "additionalProperties": false,
            "properties": {
              "states": {
                "type": "array",
                "description": "List of country ID + state abbr based on State API",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "example": "39-AB"
                }
              }
            }
          }
        }
      },
      "ConditionMatchZipcodeCreate": {
        "type": "object",
        "description": "Condition that matches the destination zipcode of the orders",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_zipcode"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "zipcodes"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "enum": [
                  "is_any_of",
                  "is_none_of",
                  "starts_with"
                ]
              },
              "zipcodes": {
                "type": "array",
                "description": "List of zipcodes",
                "minItems": 1,
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "ConditionMatchSkuCreate": {
        "type": "object",
        "description": "Condition that matches items SKU",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_sku"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "shipment_items_sku"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "Operator for comparing items SKU",
                "enum": [
                  "contains",
                  "does_not_contain",
                  "is_exactly"
                ]
              },
              "shipment_items_sku": {
                "type": "string"
              }
            }
          }
        }
      },
      "ConditionMatchPlatformNameCreate": {
        "type": "object",
        "description": "Condition that matches platform",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_platform_name"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "platform_names"
            ],
            "additionalProperties": false,
            "properties": {
              "platform_names": {
                "type": "array",
                "description": "List of platform name base on Shipping Rule Platform API.",
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "ConditionMatchStoreCreate": {
        "type": "object",
        "description": "Condition that matches store",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_store"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "store_ids"
            ],
            "additionalProperties": false,
            "properties": {
              "store_ids": {
                "type": "array",
                "description": "List of store IDs base on Store API.",
                "items": {
                  "type": "string",
                  "format": "uuid"
                }
              }
            }
          }
        }
      },
      "ConditionMatchBuyerSelectedCourierNameCreate": {
        "type": "object",
        "description": "Condition that matches input courier name. This text is compared to the shipping solution options offered to buyers by your e-commerce store. This condition will not apply if you have setup our Checkout plugin in your store.",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_buyer_selected_courier_name"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "buyer_selected_courier_name"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "operator for filtering couriers",
                "enum": [
                  "contains",
                  "does_not_contain",
                  "is_exactly"
                ]
              },
              "buyer_selected_courier_name": {
                "description": "The courier name is determined and set in your e-commerce store before syncing the order to EasyShip.",
                "type": "string"
              }
            }
          }
        }
      },
      "ConditionMatchItemsCountCreate": {
        "type": "object",
        "description": "Condition that matches order items count",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_items_count"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "shipment_items_count"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "Operator for comparing items count",
                "enum": [
                  "greater_than",
                  "greater_than_or_equal_to",
                  "less_than",
                  "less_than_or_equal_to",
                  "equal_to"
                ]
              },
              "shipment_items_count": {
                "type": "integer",
                "description": "Items count",
                "minimum": 0
              }
            }
          }
        }
      },
      "ConditionMatchSellingPriceCreate": {
        "type": "object",
        "description": "Condition that matches order's selling price",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_selling_price"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "value",
              "currency"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "Operator for comparing order's selling price",
                "enum": [
                  "greater_than",
                  "greater_than_or_equal_to",
                  "less_than",
                  "less_than_or_equal_to",
                  "equal_to"
                ]
              },
              "value": {
                "type": "number",
                "description": "Selling price"
              },
              "currency": {
                "$ref": "#/components/schemas/Currency"
              }
            }
          }
        }
      },
      "ConditionMatchWeightCreate": {
        "type": "object",
        "description": "Condition that matches order weight",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "match_weight"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "operator",
              "total_actual_weight"
            ],
            "additionalProperties": false,
            "properties": {
              "operator": {
                "type": "string",
                "description": "Operator for comparing order weight",
                "enum": [
                  "greater_than",
                  "greater_than_or_equal_to",
                  "less_than",
                  "less_than_or_equal_to",
                  "equal_to"
                ]
              },
              "total_actual_weight": {
                "type": "number",
                "description": "LB or KG based on country setting."
              }
            }
          }
        }
      },
      "ConditionIncludeOrderTagNameCreate": {
        "type": "object",
        "description": "Condition that matches order tags",
        "required": [
          "type",
          "options"
        ],
        "properties": {
          "type": {
            "type": "string",
            "enum": [
              "include_order_tag_name"
            ]
          },
          "options": {
            "type": "object",
            "required": [
              "order_tag_list"
            ],
            "additionalProperties": false,
            "properties": {
              "order_tag_list": {
                "type": "array",
                "description": "Tag names based on Tag API",
                "minItems": 1,
                "items": {
                  "type": "string"
                }
              }
            }
          }
        }
      },
      "CountryID": {
        "type": "integer",
        "description": "Country ID based on Countries API",
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70,
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78,
          79,
          80,
          81,
          82,
          83,
          84,
          85,
          86,
          87,
          88,
          89,
          90,
          91,
          92,
          93,
          94,
          95,
          96,
          97,
          98,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          109,
          110,
          111,
          112,
          113,
          114,
          115,
          116,
          117,
          118,
          119,
          120,
          121,
          122,
          123,
          124,
          125,
          126,
          127,
          128,
          129,
          130,
          131,
          132,
          133,
          134,
          135,
          136,
          137,
          138,
          139,
          140,
          141,
          142,
          143,
          144,
          145,
          146,
          147,
          148,
          149,
          150,
          151,
          152,
          153,
          154,
          155,
          156,
          157,
          158,
          159,
          160,
          161,
          162,
          163,
          164,
          165,
          166,
          167,
          168,
          169,
          170,
          171,
          172,
          173,
          174,
          175,
          176,
          177,
          178,
          179,
          180,
          181,
          182,
          183,
          184,
          185,
          186,
          187,
          188,
          189,
          190,
          191,
          192,
          193,
          194,
          195,
          196,
          197,
          198,
          199,
          200,
          201,
          202,
          203,
          204,
          205,
          206,
          207,
          208,
          209,
          210,
          211,
          212,
          213,
          214,
          215,
          216,
          217,
          218,
          219,
          220,
          221,
          222,
          223,
          224,
          225,
          226,
          227,
          228,
          229,
          230,
          231,
          232,
          233,
          234,
          235,
          236,
          237,
          238,
          239,
          240,
          241,
          242,
          243,
          244,
          245,
          246,
          247,
          248,
          249,
          250
        ]
      },
      "Currency": {
        "type": "string",
        "nullable": false,
        "enum": [
          "AED",
          "AFN",
          "ALL",
          "AMD",
          "ANG",
          "AOA",
          "ARS",
          "AUD",
          "AWG",
          "AZN",
          "BAM",
          "BBD",
          "BDT",
          "BGN",
          "BHD",
          "BIF",
          "BMD",
          "BND",
          "BOB",
          "BRL",
          "BSD",
          "BTN",
          "BWP",
          "BYR",
          "BZD",
          "CAD",
          "CDF",
          "CHF",
          "CLF",
          "CLP",
          "CNY",
          "COP",
          "CRC",
          "CUC",
          "CUP",
          "CVE",
          "CZK",
          "DJF",
          "DKK",
          "DOP",
          "DZD",
          "EGP",
          "ERN",
          "ETB",
          "EUR",
          "FJD",
          "FKP",
          "GBP",
          "GEL",
          "GHS",
          "GIP",
          "GMD",
          "GNF",
          "GTQ",
          "GYD",
          "HKD",
          "HNL",
          "HRK",
          "HTG",
          "HUF",
          "IDR",
          "ILS",
          "INR",
          "IQD",
          "IRR",
          "ISK",
          "JMD",
          "JOD",
          "JPY",
          "KES",
          "KGS",
          "KHR",
          "KMF",
          "KPW",
          "KRW",
          "KWD",
          "KYD",
          "KZT",
          "LAK",
          "LBP",
          "LKR",
          "LRD",
          "LSL",
          "LTL",
          "LVL",
          "LYD",
          "MAD",
          "MDL",
          "MGA",
          "MKD",
          "MMK",
          "MNT",
          "MOP",
          "MRO",
          "MUR",
          "MVR",
          "MWK",
          "MXN",
          "MYR",
          "MZN",
          "NAD",
          "NGN",
          "NIO",
          "NOK",
          "NPR",
          "NZD",
          "OMR",
          "PAB",
          "PEN",
          "PGK",
          "PHP",
          "PKR",
          "PLN",
          "PYG",
          "QAR",
          "RON",
          "RSD",
          "RUB",
          "RWF",
          "SAR",
          "SBD",
          "SCR",
          "SDG",
          "SEK",
          "SGD",
          "SHP",
          "SKK",
          "SLL",
          "SOS",
          "SRD",
          "SSP",
          "STD",
          "SVC",
          "SYP",
          "SZL",
          "THB",
          "TJS",
          "TMT",
          "TND",
          "TOP",
          "TRY",
          "TTD",
          "TWD",
          "TZS",
          "UAH",
          "UGX",
          "USD",
          "UYU",
          "UZS",
          "VES",
          "VND",
          "VUV",
          "WST",
          "XAF",
          "XAG",
          "XAU",
          "XCD",
          "XDR",
          "XOF",
          "XPF",
          "YER",
          "ZAR",
          "ZMW",
          "BTC",
          "JEP",
          "EEK",
          "GHC",
          "MTL",
          "TMM",
          "YEN",
          "ZWD",
          "ZWL",
          "ZWN",
          "ZWR"
        ],
        "example": "USD",
        "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)"
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
      "ShippingRule": {
        "type": "object",
        "description": "Shipping Rules",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "name": {
            "type": "string",
            "description": "Shipping Rule name"
          },
          "description": {
            "type": "string",
            "description": "Shipping Rule description"
          },
          "priority": {
            "type": "integer",
            "description": "The smaller value represent the higher priority. High priority shipping rule would be execute first."
          },
          "active": {
            "type": "boolean",
            "description": "Turn on or turn off this shipping rule"
          },
          "accessible": {
            "type": "boolean",
            "description": "Based on current subscription plan. Return false if current subscription do not own shipping rule features."
          },
          "checkout_restrictive": {
            "type": "boolean"
          },
          "conditions": {
            "type": "array",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ShippingRuleCondition"
            }
          },
          "actions": {
            "type": "array",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ShippingRuleAction"
            }
          },
          "created_at": {
            "type": "string",
            "format": "date-time"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time"
          }
        }
      },
      "ShippingRuleCondition": {
        "discriminator": {
          "propertyName": "type",
          "mapping": {
            "match_country": "#/components/schemas/ConditionMatchCountry",
            "match_all": "#/components/schemas/ConditionMatchAll",
            "match_category": "#/components/schemas/ConditionMatchCategory",
            "match_state": "#/components/schemas/ConditionMatchState",
            "match_zipcode": "#/components/schemas/ConditionMatchZipcode",
            "match_sku": "#/components/schemas/ConditionMatchSku",
            "match_platform_name": "#/components/schemas/ConditionMatchPlatformName",
            "match_store": "#/components/schemas/ConditionMatchStore",
            "match_buyer_selected_courier_name": "#/components/schemas/ConditionMatchBuyerSelectedCourierName",
            "match_items_count": "#/components/schemas/ConditionMatchItemsCount",
            "match_selling_price": "#/components/schemas/ConditionMatchSellingPrice",
            "match_weight": "#/components/schemas/ConditionMatchWeight",
            "include_order_tag_name": "#/components/schemas/ConditionIncludeOrderTagName"
          }
        },
        "oneOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchCountry"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchAll"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchCategory"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchState"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchZipcode"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchSku"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchPlatformName"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchStore"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchBuyerSelectedCourierName"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchItemsCount"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchSellingPrice"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchWeight"
          },
          {
            "$ref": "#/components/schemas/ConditionIncludeOrderTagName"
          }
        ]
      },
      "ShippingRuleConditionCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/ConditionMatchCountryCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchAllCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchCategoryCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchStateCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchZipcodeCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchSkuCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchPlatformNameCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchStoreCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchBuyerSelectedCourierNameCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchItemsCountCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchSellingPriceCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionMatchWeightCreate"
          },
          {
            "$ref": "#/components/schemas/ConditionIncludeOrderTagNameCreate"
          }
        ],
        "discriminator": {
          "propertyName": "type",
          "mapping": {
            "match_country": "#/components/schemas/ConditionMatchCountryCreate",
            "match_all": "#/components/schemas/ConditionMatchAllCreate",
            "match_category": "#/components/schemas/ConditionMatchCategoryCreate",
            "match_state": "#/components/schemas/ConditionMatchStateCreate",
            "match_zipcode": "#/components/schemas/ConditionMatchZipcodeCreate",
            "match_sku": "#/components/schemas/ConditionMatchSkuCreate",
            "match_platform_name": "#/components/schemas/ConditionMatchPlatformNameCreate",
            "match_store": "#/components/schemas/ConditionMatchStoreCreate",
            "match_buyer_selected_courier_name": "#/components/schemas/ConditionMatchBuyerSelectedCourierNameCreate",
            "match_items_count": "#/components/schemas/ConditionMatchItemsCountCreate",
            "match_selling_price": "#/components/schemas/ConditionMatchSellingPriceCreate",
            "match_weight": "#/components/schemas/ConditionMatchWeightCreate",
            "include_order_tag_name": "#/components/schemas/ConditionIncludeOrderTagNameCreate"
          }
        }
      },
      "ShippingRuleAction": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/ActionAddNeverCourier"
          },
          {
            "$ref": "#/components/schemas/ActionAddPreferredCourier"
          },
          {
            "$ref": "#/components/schemas/ActionForceIncoterms"
          },
          {
            "$ref": "#/components/schemas/ActionForceSortBy"
          },
          {
            "$ref": "#/components/schemas/ActionForceInsurance"
          },
          {
            "$ref": "#/components/schemas/ActionForceTrackingRating"
          },
          {
            "$ref": "#/components/schemas/ActionForcePackage"
          },
          {
            "$ref": "#/components/schemas/ActionRejectPackages"
          },
          {
            "$ref": "#/components/schemas/ActionForceResidentialSurcharge"
          },
          {
            "$ref": "#/components/schemas/ActionForceShipFrom"
          },
          {
            "$ref": "#/components/schemas/ActionForceAutomatedReturnRequested"
          },
          {
            "$ref": "#/components/schemas/ActionAddForcedDeliveryTime"
          }
        ],
        "discriminator": {
          "propertyName": "type",
          "mapping": {
            "add_never_courier_service": "#/components/schemas/ActionAddNeverCourier",
            "add_preferred_courier_service": "#/components/schemas/ActionAddPreferredCourier",
            "force_incoterms": "#/components/schemas/ActionForceIncoterms",
            "force_sort_by": "#/components/schemas/ActionForceSortBy",
            "force_insurance": "#/components/schemas/ActionForceInsurance",
            "force_tracking_rating": "#/components/schemas/ActionForceTrackingRating",
            "force_package": "#/components/schemas/ActionForcePackage",
            "reject_packages": "#/components/schemas/ActionRejectPackages",
            "force_residential_surcharge": "#/components/schemas/ActionForceResidentialSurcharge",
            "force_ship_from": "#/components/schemas/ActionForceShipFrom",
            "force_automated_return_requested": "#/components/schemas/ActionForceAutomatedReturnRequested",
            "add_forced_delivery_time": "#/components/schemas/ActionAddForcedDeliveryTime"
          }
        }
      },
      "ShippingRuleActionCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/ActionAddNeverCourierCreate"
          },
          {
            "$ref": "#/components/schemas/ActionAddPreferredCourierCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceIncotermsCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceSortByCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceInsuranceCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceTrackingRatingCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForcePackageCreate"
          },
          {
            "$ref": "#/components/schemas/ActionRejectPackagesCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceResidentialSurchargeCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceShipFromCreate"
          },
          {
            "$ref": "#/components/schemas/ActionForceAutomatedReturnRequestedCreate"
          },
          {
            "$ref": "#/components/schemas/ActionAddForcedDeliveryTimeCreate"
          }
        ],
        "discriminator": {
          "propertyName": "type",
          "mapping": {
            "add_never_courier_service": "#/components/schemas/ActionAddNeverCourierCreate",
            "add_preferred_courier_service": "#/components/schemas/ActionAddPreferredCourierCreate",
            "force_incoterms": "#/components/schemas/ActionForceIncotermsCreate",
            "force_sort_by": "#/components/schemas/ActionForceSortByCreate",
            "force_insurance": "#/components/schemas/ActionForceInsuranceCreate",
            "force_tracking_rating": "#/components/schemas/ActionForceTrackingRatingCreate",
            "force_package": "#/components/schemas/ActionForcePackageCreate",
            "reject_packages": "#/components/schemas/ActionRejectPackagesCreate",
            "force_residential_surcharge": "#/components/schemas/ActionForceResidentialSurchargeCreate",
            "force_ship_from": "#/components/schemas/ActionForceShipFromCreate",
            "force_automated_return_requested": "#/components/schemas/ActionForceAutomatedReturnRequestedCreate",
            "add_forced_delivery_time": "#/components/schemas/ActionAddForcedDeliveryTimeCreate"
          }
        }
      },
      "ShippingRuleCreate": {
        "type": "object",
        "description": "Shipping Rule Create Params",
        "additionalProperties": false,
        "required": [
          "name",
          "description",
          "conditions",
          "actions"
        ],
        "properties": {
          "name": {
            "type": "string",
            "description": "Shipping Rule name"
          },
          "description": {
            "type": "string",
            "description": "Shipping Rule description"
          },
          "recalculate_shipments": {
            "type": "boolean",
            "description": "Recalculate all shipments affected by this shipping rule"
          },
          "priority": {
            "type": "integer",
            "description": "The smaller value represent the higher priority. High priority shipping rule would be execute first."
          },
          "conditions": {
            "type": "array",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ShippingRuleConditionCreate"
            }
          },
          "actions": {
            "type": "array",
            "minItems": 1,
            "items": {
              "$ref": "#/components/schemas/ShippingRuleActionCreate"
            }
          }
        }
      }
    }
  }
}
```