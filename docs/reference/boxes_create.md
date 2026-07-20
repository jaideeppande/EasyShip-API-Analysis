# Create a Box

Create a box.

Required authorization scope: `public.box:write` 


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
      "name": "Boxes"
    }
  ],
  "paths": {
    "/2024-09/boxes": {
      "post": {
        "summary": "Create a Box",
        "tags": [
          "Boxes"
        ],
        "operationId": "boxes_create",
        "description": "Create a box.\n\nRequired authorization scope: `public.box:write` \n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "box successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "box": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                        "name": "Wood Box",
                        "outer_dimensions": {
                          "length": 35.56,
                          "width": 30.48,
                          "height": 30.48
                        },
                        "slug": "wood-box",
                        "type": "box",
                        "weight": 0.90718474
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "box successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/box_single"
                }
              }
            }
          },
          "422": {
            "description": "failed validations",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Name can't be blank",
                          "Outer length can't be blank",
                          "Outer length is not a number",
                          "Outer width can't be blank",
                          "Outer width is not a number",
                          "Outer height can't be blank",
                          "Outer height is not a number",
                          "Inner length can't be blank",
                          "Inner length is not a number",
                          "Inner width can't be blank",
                          "Inner width is not a number",
                          "Inner height can't be blank",
                          "Inner height is not a number"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Box",
                            "url": "https://developers.easyship.com/reference/boxes_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "failed validations"
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
                "$ref": "#/components/schemas/BoxCreate"
              },
              "examples": {
                "box_successfully_created": {
                  "summary": "box successfully created",
                  "value": {
                    "name": "Wood Box",
                    "outer_length": 14,
                    "outer_width": 12,
                    "outer_height": 12,
                    "weight": 2
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
      "box_single": {
        "type": "object",
        "description": "Box details",
        "additionalProperties": false,
        "properties": {
          "box": {
            "$ref": "#/components/schemas/Box"
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
      "Box": {
        "type": "object",
        "description": "User-defined details of a box used for shipments",
        "externalDocs": {
          "description": "Saving Shipping Boxes Dimensions - Easyship Support",
          "url": "https://support.easyship.com/hc/en-us/articles/360025430011-Saving-Shipping-Boxes-Dimensions"
        },
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "ID"
          },
          "courier": {
            "type": "object",
            "nullable": true,
            "additionalProperties": false,
            "properties": {
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service, when applicable."
              },
              "country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              }
            }
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Name"
          },
          "slug": {
            "type": "string",
            "nullable": true,
            "description": "Slug"
          },
          "outer_dimensions": {
            "type": "object",
            "additionalProperties": false,
            "description": "A measure of the space taken by the box itself, in cm.",
            "properties": {
              "length": {
                "type": "number"
              },
              "width": {
                "type": "number"
              },
              "height": {
                "type": "number"
              }
            }
          },
          "weight": {
            "type": "number",
            "description": "The weight of the box's packaging materials (excluding items inside), in kg."
          },
          "type": {
            "type": "string",
            "description": "Box type."
          }
        }
      },
      "BoxCreate": {
        "type": "object",
        "description": "User-defined details of a box used for shipments",
        "externalDocs": {
          "description": "Saving Shipping Boxes Dimensions - Easyship Support",
          "url": "https://support.easyship.com/hc/en-us/articles/360025430011-Saving-Shipping-Boxes-Dimensions"
        },
        "additionalProperties": false,
        "properties": {
          "name": {
            "type": "string",
            "description": "Name"
          },
          "outer_length": {
            "description": "Box length in centimeters. Metric system by default. Enable imperial system via dashboard for inches.",
            "type": "number"
          },
          "outer_width": {
            "description": "Box width in centimeters. Metric system by default. Enable imperial system via dashboard for inches.",
            "type": "number"
          },
          "outer_height": {
            "description": "Box height in centimeters. Metric system by default. Enable imperial system via dashboard for inches.",
            "type": "number"
          },
          "weight": {
            "type": "number",
            "description": "The weight of the box (excluding items inside) in kilograms. Metric system by default. Enable imperial system via dashboard for pounds."
          }
        }
      },
      "CountryAlpha2": {
        "type": "string",
        "description": "Country Code in Alpha-2 format (ISO 3166-1)",
        "enum": [
          "AD",
          "AE",
          "AF",
          "AG",
          "AI",
          "AL",
          "AM",
          "AN",
          "AO",
          "AQ",
          "AR",
          "AS",
          "AT",
          "AU",
          "AW",
          "AX",
          "AZ",
          "BA",
          "BB",
          "BD",
          "BE",
          "BF",
          "BG",
          "BH",
          "BI",
          "BJ",
          "BL",
          "BM",
          "BN",
          "BO",
          "BQ",
          "BR",
          "BS",
          "BT",
          "BV",
          "BW",
          "BY",
          "BZ",
          "CA",
          "CC",
          "CD",
          "CF",
          "CG",
          "CH",
          "CI",
          "CK",
          "CL",
          "CM",
          "CN",
          "CO",
          "CR",
          "CU",
          "CV",
          "CW",
          "CX",
          "CY",
          "CZ",
          "DE",
          "DJ",
          "DK",
          "DM",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "EH",
          "ER",
          "ES",
          "ET",
          "FI",
          "FJ",
          "FK",
          "FM",
          "FO",
          "FR",
          "GA",
          "GB",
          "GD",
          "GE",
          "GF",
          "GG",
          "GH",
          "GI",
          "GL",
          "GM",
          "GN",
          "GP",
          "GQ",
          "GR",
          "GS",
          "GT",
          "GU",
          "GW",
          "GY",
          "HK",
          "HM",
          "HN",
          "HR",
          "HT",
          "HU",
          "ID",
          "IE",
          "IL",
          "IM",
          "IN",
          "IO",
          "IQ",
          "IR",
          "IS",
          "IT",
          "JE",
          "JM",
          "JO",
          "JP",
          "KE",
          "KG",
          "KH",
          "KI",
          "KM",
          "KN",
          "KP",
          "KR",
          "KW",
          "KY",
          "KZ",
          "LA",
          "LB",
          "LC",
          "LI",
          "LK",
          "LR",
          "LS",
          "LT",
          "LU",
          "LV",
          "LY",
          "MA",
          "MC",
          "MD",
          "ME",
          "MF",
          "MG",
          "MH",
          "MK",
          "ML",
          "MM",
          "MN",
          "MO",
          "MP",
          "MQ",
          "MR",
          "MS",
          "MT",
          "MU",
          "MV",
          "MW",
          "MX",
          "MY",
          "MZ",
          "NA",
          "NC",
          "NE",
          "NF",
          "NG",
          "NI",
          "NL",
          "NO",
          "NP",
          "NR",
          "NU",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PF",
          "PG",
          "PH",
          "PK",
          "PL",
          "PM",
          "PN",
          "PR",
          "PS",
          "PT",
          "PW",
          "PY",
          "QA",
          "RE",
          "RO",
          "RS",
          "RU",
          "RW",
          "SA",
          "SB",
          "SC",
          "SD",
          "SE",
          "SG",
          "SH",
          "SI",
          "SJ",
          "SK",
          "SL",
          "SM",
          "SN",
          "SO",
          "SR",
          "SS",
          "ST",
          "SV",
          "SX",
          "SY",
          "SZ",
          "TC",
          "TD",
          "TF",
          "TG",
          "TH",
          "TJ",
          "TK",
          "TL",
          "TM",
          "TN",
          "TO",
          "TR",
          "TT",
          "TV",
          "TW",
          "TZ",
          "UA",
          "UG",
          "UM",
          "US",
          "UY",
          "UZ",
          "VA",
          "VC",
          "VE",
          "VG",
          "VI",
          "VN",
          "VU",
          "WF",
          "WS",
          "YE",
          "YT",
          "ZA",
          "ZM",
          "ZW"
        ]
      }
    }
  }
}
```