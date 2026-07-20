# Create Action for a Shipping Rule

Create an action for a shipping rule.

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
      "name": "Shipping Rule's Actions",
      "description": "Shipping Rule's Actions API"
    }
  ],
  "paths": {
    "/2024-11/shipping_rules/{shipping_rule_id}/actions": {
      "post": {
        "summary": "Create Action for a Shipping Rule",
        "tags": [
          "Shipping Rule's Actions"
        ],
        "operationId": "shipping_rule_action_create",
        "description": "Create an action for a shipping rule.\n\nRequired authorization scope: `enterprise.shipping_rule:write`\n",
        "security": [
          {
            "OAuth2": [
              "enterprise.shipping_rule"
            ]
          }
        ],
        "parameters": [
          {
            "name": "shipping_rule_id",
            "in": "path",
            "schema": {
              "type": "string",
              "format": "uuid"
            },
            "required": true,
            "description": "Shipping Rule ID provided when creating"
          }
        ],
        "responses": {
          "201": {
            "description": "action successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "action": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "options": {
                          "insured": true
                        },
                        "type": "force_insurance"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "action successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_action_single"
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
                          "Automation action can't be blank",
                          "Automation action  is not a valid action",
                          "Options can't be blank"
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
                "$ref": "#/components/schemas/ShippingRuleActionCreate"
              },
              "examples": {
                "action_successfully_created": {
                  "summary": "action successfully created",
                  "value": {
                    "type": "force_insurance",
                    "options": {
                      "insured": true
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
      "shipping_rule_action_single": {
        "type": "object",
        "description": "Shipping Rule Action detail",
        "additionalProperties": false,
        "properties": {
          "action": {
            "$ref": "#/components/schemas/ShippingRuleAction"
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
      }
    }
  }
}
```