# List USPS Locations

Retrieve USPS locations.

This endpoint routes requests to the USPS Locations API. For further information, kindly look into the UPS API documentation available at https://developers.usps.com/locationsv3.

Required authorization scope: `public.location:read`


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
      "name": "Locations"
    }
  ],
  "paths": {
    "/2024-09/locations/usps": {
      "get": {
        "summary": "List USPS Locations",
        "tags": [
          "Locations"
        ],
        "operationId": "locations_usps_index",
        "description": "Retrieve USPS locations.\n\nThis endpoint routes requests to the USPS Locations API. For further information, kindly look into the UPS API documentation available at https://developers.usps.com/locationsv3.\n\nRequired authorization scope: `public.location:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1
            },
            "required": false,
            "description": "Page number to fetch, default: `1`",
            "example": 1
          },
          {
            "name": "per_page",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 100
            },
            "required": false,
            "description": "Number of records per page to fetch, default: `20`",
            "example": 10
          },
          {
            "name": "country_alpha2",
            "in": "query",
            "required": true,
            "description": "Country code: Alpha-2 format (ISO 3166-1).",
            "example": "US",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "postal_code",
            "in": "query",
            "required": false,
            "description": "A unique location code used by postal services to sort and deliver mail.",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "get courier service points",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "locations": [
                        {
                          "address": {
                            "line_1": "29 JAY ST",
                            "line_2": null,
                            "state": "NY",
                            "city": "SCHENECTADY",
                            "postal_code": "12305",
                            "country_alpha2": "US"
                          },
                          "name": "SCHENECTADY",
                          "opening_hours": [
                            {
                              "day": "MONDAY",
                              "open_time": "05:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "TUESDAY",
                              "open_time": "05:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "WEDNESDAY",
                              "open_time": "05:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "THURSDAY",
                              "open_time": "05:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "FRIDAY",
                              "open_time": "05:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "SATURDAY",
                              "open_time": "07:00",
                              "close_time": "17:00"
                            }
                          ],
                          "phone_number": "5183883118",
                          "service_types": [
                            "bound_printed_matter",
                            "library_mail",
                            "media_mail",
                            "bound_printed_matter",
                            "library_mail",
                            "media_mail",
                            "bound_printed_matter",
                            "library_mail",
                            "media_mail",
                            "parcel_select",
                            "usps_connect_local",
                            "usps_connect_mail",
                            "parcel_select",
                            "usps_connect_local",
                            "usps_connect_mail"
                          ]
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 4,
                          "next": null,
                          "count": 4
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "get courier service points"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/location_usps_list"
                }
              }
            }
          },
          "422": {
            "description": "location service not found for provided courier",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "We do not support locations for USPS in Andorra."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List USPS Locations",
                            "url": "https://developers.easyship.com/reference/locations_usps_index"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "location service not found for provided courier"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "500": {
            "description": "forward request failed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "internal_server_error",
                        "details": [
                          "400 - OASValidation OpenAPI-Spec-Validation-Locations with resource oas://locations-v3.yaml: failed with reason: [ERROR - ECMA 262 regex d{5} does not match input string 01: []]"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List USPS Locations",
                            "url": "https://developers.easyship.com/reference/locations_usps_index"
                          }
                        ],
                        "message": "Unexpected internal error.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "api_error"
                      }
                    },
                    "summary": "forward request failed"
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
      "location_usps_list": {
        "type": "object",
        "description": "List of USPS locations",
        "additionalProperties": false,
        "properties": {
          "locations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LocationUsps"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
            "maximum": 200
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "nullable": true,
            "description": "Postal code. Leave it null or 0 if the country does not have postal codes. Mandatory for these countries: AD, AF, AI, AL, AM, AQ, AR, AS, AT, AU, AX, AZ, BA, BB, BD, BE, BG, BL, BM, BN, BQ, BR, BT, BV, BY, CA, CC, CH, CL, CN, CO, CR, CU, CV, CX, CY, CZ, DE, DK, DO, DZ, EC, EE, EG, EH, ES, ET, FI, FK, FM, FO, FR, GA, GB, GE, GF, GG, GI, GL, GP, GR, GS, GT, GU, GW, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JO, JP, KG, KH, KR, KW, KY, KZ, LA, LB, LI, LK, LR, LS, LT, LU, LV, MA, MC, MD, ME, MF, MG, MH, MK, MM, MN, MP, MQ, MT, MV, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NZ, OM, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, RE, RO, RS, RU, SD, SE, SG, SH, SI, SJ, SK, SM, SN, SS, SV, SX, SZ, TC, TD, TH, TJ, TM, TN, TR, TW, UA, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, WF, WS, YT, ZA, ZM."
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 27
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 22
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20,
            "nullable": true
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name\"",
            "maximum": 50
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
      },
      "Location": {
        "description": "Location",
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the location"
          },
          "phone_number": {
            "type": "string",
            "description": "The phone number associated with the location",
            "nullable": true
          },
          "address": {
            "type": "object",
            "additionalProperties": false,
            "description": "The address of the location",
            "properties": {
              "line_1": {
                "$ref": "#/components/schemas/Address/properties/line_1"
              },
              "line_2": {
                "$ref": "#/components/schemas/Address/properties/line_2"
              },
              "state": {
                "$ref": "#/components/schemas/Address/properties/state"
              },
              "city": {
                "$ref": "#/components/schemas/Address/properties/city"
              },
              "postal_code": {
                "$ref": "#/components/schemas/Address/properties/postal_code"
              },
              "country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "longitude": {
                "description": "The longitude of the location",
                "type": "string",
                "nullable": true
              },
              "latitude": {
                "description": "The latitude of the location",
                "type": "string",
                "nullable": true
              }
            }
          },
          "opening_hours": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "day": {
                  "type": "string",
                  "description": "The day of the week"
                },
                "open_time": {
                  "type": "string",
                  "description": "The opening time for the specified day",
                  "nullable": true
                },
                "close_time": {
                  "type": "string",
                  "description": "The closing time for the specified day",
                  "nullable": true
                }
              }
            }
          }
        }
      },
      "LocationUsps": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Location"
          },
          {
            "description": "USPS Location",
            "type": "object",
            "properties": {
              "service_types": {
                "type": "array",
                "description": "Supported types for the location",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "enum": [
                    "parcel_select",
                    "parcel_select_lightweight",
                    "usps_connect_local",
                    "usps_connect_mail",
                    "usps_connect_regional",
                    "library_mail",
                    "media_mail",
                    "bound_printed_matter"
                  ]
                }
              }
            }
          }
        ]
      }
    }
  }
}
```