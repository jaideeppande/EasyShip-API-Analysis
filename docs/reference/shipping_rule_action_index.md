# List all Actions for a Shipping Rule

List actions for a shipping rule.

Required authorization scope: `public.shipping_rule:read`


# OpenAPI definition

```json
{
  "openapi": "3.0.3",
  "info": {
    "title": "Easyship Public API",
    "version": "v2024-09",
    "description": "## Powerful Shipping API for Ecommerce\nEasyship provides a powerful shipping API for you to add hassle free worldwide shipping options to your website and end to end shipping functionality to your warehouse, ERP or platform.\n\n### Craft an amazing checkout experience\nProvide instant access to heavily discounted shipping with a single integration. Let end customers choose their preferred shipping method and cost, all within your own UI. Once they've selected and paid, confirm the shipment and all costs are guaranteed by us.\n\n### Write less code, have more options\nYou don’t need to be a shipping expert. We continuously add new shipping solutions to our platform to provide better pricing and service to our users. You don’t need to open direct accounts or write multiple integrations, once we’ve added them, they’re available to you instantly.\n\n### Streamline your processes\nInteract with the Easyship platform from any interface. Whether it’s your ecommerce platform, warehouse/wms, ERP or order management system, you can get rates, create shipments, download labels and track deliveries, without leaving your main business system.",
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
      "name": "Shipping Rule's Actions"
    }
  ],
  "paths": {
    "/2024-09/shipping_rules/{shipping_rule_id}/actions": {
      "get": {
        "summary": "List all Actions for a Shipping Rule",
        "tags": [
          "Shipping Rule's Actions"
        ],
        "operationId": "shipping_rule_action_index",
        "description": "List actions for a shipping rule.\n\nRequired authorization scope: `public.shipping_rule:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "shipping_rule_id",
            "in": "path",
            "required": true,
            "description": "Shipping Rule ID provided when creating",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "actions",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "actions": [
                        {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "options": {
                            "insured": false
                          },
                          "type": "force_insurance"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "actions"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_action_list"
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
      "url": "https://public-api.easyship.com",
      "description": "Production"
    }
  ],
  "components": {
    "securitySchemes": {
      "Bearer": {
        "description": "Bearer Token necessary to use API",
        "type": "http",
        "scheme": "bearer",
        "bearerFormat": "token"
      }
    },
    "schemas": {
      "shipping_rule_action_list": {
        "type": "object",
        "description": "List of shipping rule actions",
        "additionalProperties": false,
        "properties": {
          "actions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShippingRuleAction"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
                  "description": "-1: No tracking number\n0: limited \n1: basic \n2: regular \n3: excellent\n",
                  "enum": [
                    -1,
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
                "required": [
                  "force_box_id"
                ],
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
                "required": [
                  "force_flat_rate_box_id"
                ],
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
              "force_automated_return_requested"
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
      }
    }
  }
}
```