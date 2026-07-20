# Create a Product

Create a single product in your account.

Required authorization scope: `public.product:write`


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
      "name": "Products"
    }
  ],
  "paths": {
    "/2024-09/products": {
      "post": {
        "summary": "Create a Product",
        "tags": [
          "Products"
        ],
        "operationId": "products_create",
        "description": "Create a single product in your account.\n\nRequired authorization scope: `public.product:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "product successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "product": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                        "comments": "comments",
                        "contains_battery_pi966": null,
                        "contains_battery_pi967": true,
                        "contains_liquids": null,
                        "cost_price": null,
                        "cost_price_currency": null,
                        "created_at": "2022-02-22T12:21:00Z",
                        "height": 0.79,
                        "hs_code": "150810",
                        "identifier": "SKU-00000001",
                        "image_url": null,
                        "input_type": "api",
                        "item_category": {
                          "id": 1,
                          "name": "Mobile Phones"
                        },
                        "length": 14.75,
                        "name": "iPhone 14 Pro",
                        "origin_country_alpha2": "ID",
                        "pick_location": "Apple Store",
                        "platform_product_id": "SHOPIFY-VAR-12345",
                        "manufacturer_part_number": "MFR-98234",
                        "global_trade_item_number": "5901234123457",
                        "selling_price": null,
                        "selling_price_currency": null,
                        "store_id": null,
                        "updated_at": "2022-02-22T12:21:00Z",
                        "weight": 0.21,
                        "width": 7.15
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "product successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/product_single"
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
                          "Identifier can't be blank"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Product",
                            "url": "https://developers.easyship.com/reference/products_create"
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
                "$ref": "#/components/schemas/ProductCreate"
              },
              "examples": {
                "product_successfully_created": {
                  "summary": "product successfully created",
                  "value": {
                    "item_category_id": 1,
                    "name": "iPhone 14 Pro",
                    "length": 14.75,
                    "width": 7.15,
                    "height": 0.785,
                    "weight": 0.206,
                    "identifier": "SKU-00000001",
                    "input_type": "api",
                    "comments": "comments",
                    "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                    "hs_code": "150810",
                    "pick_location": "Apple Store",
                    "contains_battery_pi967": true,
                    "origin_country_alpha2": "ID"
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
      "product_single": {
        "type": "object",
        "description": "Product detail",
        "additionalProperties": false,
        "properties": {
          "product": {
            "$ref": "#/components/schemas/Product"
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
      "CountryAlpha2Nullable": {
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
          "ZW",
          null
        ],
        "nullable": true
      },
      "CurrencyNullable": {
        "type": "string",
        "nullable": true,
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
          "ZWR",
          null
        ],
        "example": "USD",
        "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)"
      },
      "Product": {
        "type": "object",
        "description": "Product",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Product ID"
          },
          "store_id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "Store ID"
          },
          "name": {
            "type": "string",
            "description": "Human-readable name of the product."
          },
          "item_category": {
            "type": "object",
            "additionalProperties": false,
            "nullable": true,
            "properties": {
              "id": {
                "type": "integer",
                "description": "Item Category ID"
              },
              "name": {
                "type": "string",
                "description": "Item Category Name"
              }
            }
          },
          "comments": {
            "type": "string",
            "nullable": true
          },
          "input_type": {
            "type": "string",
            "enum": [
              "manual_input",
              "product_sync",
              "api",
              "api_upload",
              "csv_upload"
            ]
          },
          "identifier": {
            "type": "string",
            "description": "Stock Keeping Unit (SKU). Your internal product identifier, typically unique within your store for inventory management and tracking."
          },
          "length": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Product length in cm (centimeters)."
          },
          "width": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Product width in cm (centimeters)."
          },
          "height": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Product height in cm (centimeters)."
          },
          "weight": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Product weight in kg (kilograms)."
          },
          "platform_product_id": {
            "type": "string",
            "nullable": true,
            "description": "Platform Product ID (PPID). Unique identifier from your store platform (e.g. Shopify variant ID, WooCommerce product ID). Used to link shipment items to product catalog entries for auto-population of product attributes."
          },
          "manufacturer_part_number": {
            "type": "string",
            "nullable": true,
            "description": "Manufacturer Part Number (MPN). The manufacturer's internal code or part number for the product. Useful for wholesale and B2B operations to identify products by their source."
          },
          "global_trade_item_number": {
            "type": "string",
            "nullable": true,
            "description": "Global Trade Item Number (GTIN). Internationally recognized unique identifier for trade items, including UPC (US/Canada), EAN (Europe), JAN (Japan), and ISBN (books). Used by retailers and carriers for product identification and inventory tracking."
          },
          "cost_price": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "cost_price_currency": {
            "$ref": "#/components/schemas/CurrencyNullable"
          },
          "selling_price": {
            "type": "number",
            "format": "double",
            "nullable": true
          },
          "selling_price_currency": {
            "$ref": "#/components/schemas/CurrencyNullable"
          },
          "image_url": {
            "type": "string",
            "nullable": true
          },
          "pick_location": {
            "type": "string",
            "nullable": true
          },
          "origin_country_alpha2": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CountryAlpha2Nullable"
              },
              {
                "description": "Country where the product is manufactured. Country Code in Alpha-2 format (ISO 3166-1)"
              }
            ]
          },
          "hs_code": {
            "type": "string",
            "nullable": true
          },
          "contains_liquids": {
            "type": "boolean",
            "nullable": true
          },
          "contains_battery_pi966": {
            "type": "boolean",
            "nullable": true
          },
          "contains_battery_pi967": {
            "type": "boolean",
            "nullable": true
          },
          "created_at": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          }
        }
      },
      "ProductCreate": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/Product/properties/id"
          },
          "store_id": {
            "$ref": "#/components/schemas/Product/properties/store_id"
          },
          "name": {
            "type": "string",
            "description": "Human-readable name of the product.",
            "maxLength": 500
          },
          "comments": {
            "$ref": "#/components/schemas/Product/properties/comments"
          },
          "input_type": {
            "$ref": "#/components/schemas/Product/properties/input_type"
          },
          "identifier": {
            "type": "string",
            "description": "SKU for the product. This should be unique per one store. Identifier is required when store_id or platform_product_id is empty."
          },
          "length": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Length of the product in cm (centimeters).",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "width": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Width of the product in cm (centimeters).",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "height": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Height of the product in cm (centimeters).",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "weight": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Weight of the product in kg (kilograms).",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "item_category_id": {
            "type": "integer",
            "description": "Item Category ID"
          },
          "platform_product_id": {
            "$ref": "#/components/schemas/Product/properties/platform_product_id"
          },
          "manufacturer_part_number": {
            "$ref": "#/components/schemas/Product/properties/manufacturer_part_number"
          },
          "global_trade_item_number": {
            "$ref": "#/components/schemas/Product/properties/global_trade_item_number"
          },
          "cost_price": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Cost of the product.",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "cost_price_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyNullable"
              },
              {
                "description": "Product cost currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "selling_price": {
            "type": "number",
            "format": "double",
            "nullable": true,
            "description": "Product selling price.",
            "minimum": 0,
            "exclusiveMinimum": true
          },
          "selling_price_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CurrencyNullable"
              },
              {
                "description": "Currency of the product selling price. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "image_url": {
            "type": "string",
            "nullable": true,
            "description": "Image URL of the product."
          },
          "pick_location": {
            "type": "string",
            "nullable": true,
            "description": "Pickup location for the product.",
            "maximum": 80
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/Product/properties/origin_country_alpha2"
          },
          "hs_code": {
            "$ref": "#/components/schemas/Product/properties/hs_code"
          },
          "contains_liquids": {
            "type": "boolean",
            "nullable": true,
            "description": "Check if the product contains liquid."
          },
          "contains_battery_pi966": {
            "type": "boolean",
            "nullable": true,
            "description": "Check if the product should apply packing instruction 966."
          },
          "contains_battery_pi967": {
            "type": "boolean",
            "nullable": true,
            "description": "Check if the product should apply packing instruction 967."
          },
          "created_at": {
            "type": "string"
          },
          "updated_at": {
            "type": "string"
          }
        }
      }
    }
  }
}
```