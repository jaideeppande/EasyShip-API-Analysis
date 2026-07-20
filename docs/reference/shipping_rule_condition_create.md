# Create Condition for a Shipping Rule

Create condition for a shipping rule.

Required authorization scope: `public.shipping_rule:write`


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
      "name": "Shipping Rule's Conditions"
    }
  ],
  "paths": {
    "/2024-09/shipping_rules/{shipping_rule_id}/conditions": {
      "post": {
        "summary": "Create Condition for a Shipping Rule",
        "tags": [
          "Shipping Rule's Conditions"
        ],
        "operationId": "shipping_rule_condition_create",
        "description": "Create condition for a shipping rule.\n\nRequired authorization scope: `public.shipping_rule:write`\n",
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
          "201": {
            "description": "condition successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "condition": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "options": {
                          "store_ids": [
                            "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "01563646-58c1-4607-8fe0-cae3e33c0002"
                          ]
                        },
                        "type": "match_store"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "condition successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_rule_condition_single"
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
                          "The request does not comply with the OpenAPI Specification.",
                          "discriminator propertyName type does not exist in value {} in #/components/schemas/ShippingRuleConditionCreate/discriminator"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          }
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
                "$ref": "#/components/schemas/ShippingRuleConditionCreate"
              },
              "examples": {
                "condition_successfully_created": {
                  "summary": "condition successfully created",
                  "value": {
                    "type": "match_store",
                    "options": {
                      "store_ids": [
                        "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "01563646-58c1-4607-8fe0-cae3e33c0002"
                      ]
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
      "shipping_rule_condition_single": {
        "type": "object",
        "description": "Shipping Rrule Condition detail",
        "additionalProperties": false,
        "properties": {
          "condition": {
            "$ref": "#/components/schemas/ShippingRuleCondition"
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
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
      "Meta": {
        "type": "object",
        "properties": {
          "request_id": {
            "type": "string",
            "description": "An unique ID represent the request."
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
      }
    }
  }
}
```