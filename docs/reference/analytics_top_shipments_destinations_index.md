# List Analytics Top Shipments Destinations

Retrieve a company top shipments destinations country.

Required authorization scope: `public.analytics:read`


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
      "name": "Analytics"
    }
  ],
  "paths": {
    "/2024-09/analytics/top_shipments_destinations": {
      "get": {
        "summary": "List Analytics Top Shipments Destinations",
        "tags": [
          "Analytics"
        ],
        "operationId": "analytics_top_shipments_destinations_index",
        "description": "Retrieve a company top shipments destinations country.\n\nRequired authorization scope: `public.analytics:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "from_date",
            "in": "query",
            "example": "2023-01-01",
            "required": true,
            "description": "Beginning of date. Only accept `YYYY-MM-DD` format.",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "to_date",
            "in": "query",
            "example": "2023-02-28",
            "required": true,
            "description": "End of date. Only accept `YYYY-MM-DD` format.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "successfully returns top destinations data",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "analytics_top_shipments_destinations": {
                        "from_date": "2023-01-01T00:00:00Z",
                        "shipments_count_by_country": [],
                        "shipments_count_by_zone": [
                          {
                            "name": "Europe",
                            "shipments_count": 1
                          },
                          {
                            "name": "Asia",
                            "shipments_count": 0
                          },
                          {
                            "name": "North America",
                            "shipments_count": 0
                          },
                          {
                            "name": "Africa",
                            "shipments_count": 0
                          },
                          {
                            "name": "Others",
                            "shipments_count": 0
                          },
                          {
                            "name": "South America",
                            "shipments_count": 0
                          },
                          {
                            "name": "Oceania",
                            "shipments_count": 0
                          }
                        ],
                        "to_date": "2023-02-28T23:59:59Z",
                        "total_shipments_count": 1
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "successfully returns top destinations data"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/analytics_top_shipments_destinations_data"
                }
              }
            }
          },
          "400": {
            "description": "failed validations",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "api_error",
                        "details": [
                          "Invalid request: provide `from_date` and `to_date` fields in the `YYYY-MM-DD` format (`2023-01-31`)."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List Analytics Top Shipments Destinations",
                            "url": "https://developers.easyship.com/reference/analytics_top_shipments_destinations_index"
                          }
                        ],
                        "message": "Internal or 3rd party API error.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "api_error"
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
      "analytics_top_shipments_destinations_data": {
        "type": "object",
        "description": "Summary Analytics Shipments Top Destinations",
        "additionalProperties": false,
        "properties": {
          "analytics_top_shipments_destinations": {
            "$ref": "#/components/schemas/AnalyticsTopShipmentsDestination"
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
      "AnalyticsShipment": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from_date",
          "to_date"
        ],
        "properties": {
          "from_date": {
            "type": "string",
            "description": "Start date of the report period",
            "format": "date-time",
            "example": "2023-01-01T00:00:00.000Z"
          },
          "to_date": {
            "type": "string",
            "description": "End date of the report period",
            "format": "date-time",
            "example": "2023-02-28T23:59:59.999Z"
          },
          "total_shipments_count": {
            "type": "integer",
            "nullable": true
          },
          "shipments_count_by_date": {
            "type": "object",
            "additionalProperties": false,
            "nullable": true,
            "properties": {
              "max": {
                "type": "integer",
                "minimum": 1,
                "maximum": 99999
              },
              "data": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "key": {
                    "type": "string"
                  },
                  "values": {
                    "type": "array",
                    "items": {
                      "type": "object",
                      "additionalProperties": false,
                      "properties": {
                        "series": {
                          "type": "integer"
                        },
                        "datetime_int": {
                          "type": "integer",
                          "description": "Time in epoch format"
                        },
                        "total": {
                          "type": "integer"
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
      "AnalyticsTopShipmentsDestination": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "from_date": {
            "$ref": "#/components/schemas/AnalyticsShipment/properties/from_date"
          },
          "to_date": {
            "$ref": "#/components/schemas/AnalyticsShipment/properties/to_date"
          },
          "total_shipments_count": {
            "$ref": "#/components/schemas/AnalyticsShipment/properties/total_shipments_count"
          },
          "shipments_count_by_zone": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Zone name"
                },
                "shipments_count": {
                  "type": "integer",
                  "description": "Shipments count"
                }
              }
            }
          },
          "shipments_count_by_country": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Country name"
                },
                "country_alpha2": {
                  "$ref": "#/components/schemas/CountryAlpha2"
                },
                "shipments_count": {
                  "type": "integer",
                  "description": "Shipments count"
                },
                "percentage": {
                  "type": "number",
                  "nullable": true
                }
              }
            }
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