# List Shipment Analytics within a Date Range

Retrieve data on whether the company has made any shipments within specified period.

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
    "/2024-09/analytics/shipments_shipped": {
      "get": {
        "summary": "List Shipment Analytics within a Date Range",
        "tags": [
          "Analytics"
        ],
        "operationId": "analytics_shipment_shipped_index",
        "description": "Retrieve data on whether the company has made any shipments within specified period.\n\nRequired authorization scope: `public.analytics:read`\n",
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
            "description": "list of shipments has ever shipped",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "analytics_shipments_shipped": {
                        "currency": "USD",
                        "from_date": "2021-10-01T00:00:00Z",
                        "has_ever_shipped": false,
                        "to_date": "2021-10-02T23:59:59Z"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of shipments has ever shipped"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/analytics_shipments_shipped_data"
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
                            "name": "List Shipment Analytics within a Date Range",
                            "url": "https://developers.easyship.com/reference/analytics_shipment_shipped_index"
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
      "analytics_shipments_shipped_data": {
        "type": "object",
        "description": "Summary Analytics Shipment Has Ever Shipped Data",
        "additionalProperties": false,
        "properties": {
          "analytics_shipments_shipped": {
            "$ref": "#/components/schemas/AnalyticsShipmentsHasEverShipped"
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
      "AnalyticsShipmentsHasEverShipped": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "from_date",
          "to_date"
        ],
        "properties": {
          "from_date": {
            "$ref": "#/components/schemas/AnalyticsShipment/properties/from_date"
          },
          "to_date": {
            "$ref": "#/components/schemas/AnalyticsShipment/properties/to_date"
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "has_ever_shipped": {
            "type": "boolean",
            "description": "Whether the company has ever shipped"
          }
        }
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
      }
    }
  }
}
```