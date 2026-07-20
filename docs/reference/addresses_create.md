# Create an Address

Create a new address.

Required authorization scope: `public.address:write`


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
      "name": "Addresses"
    }
  ],
  "paths": {
    "/2024-09/addresses": {
      "post": {
        "summary": "Create an Address",
        "tags": [
          "Addresses"
        ],
        "operationId": "addresses_create",
        "description": "Create a new address.\n\nRequired authorization scope: `public.address:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "address successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "address": {
                        "city": "Bandung",
                        "company_name": "Individual Resident",
                        "contact_email": "urang@bandung.com",
                        "contact_name": "Rina Sundari",
                        "contact_phone": "+622232133123",
                        "country_alpha2": "ID",
                        "default_for": {
                          "pickup": false,
                          "billing": false,
                          "sender": false,
                          "return": false
                        },
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "line_1": "Jalan Jawa",
                        "line_2": null,
                        "postal_code": "412321",
                        "state": "West Java",
                        "status": "active"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "address successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/address_single"
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
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/AddressCreate missing required parameters: city, company_name, contact_email, contact_name, contact_phone, country_alpha2"
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
                "$ref": "#/components/schemas/AddressCreate"
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
      "address_single": {
        "type": "object",
        "description": "Address details",
        "additionalProperties": false,
        "properties": {
          "address": {
            "$ref": "#/components/schemas/AddressFull"
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
      "AddressCreate": {
        "type": "object",
        "required": [
          "city",
          "company_name",
          "contact_email",
          "contact_name",
          "contact_phone",
          "country_alpha2",
          "line_1"
        ],
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
          "company_name": {
            "type": "string",
            "description": "The company or organization at the address",
            "maximum": 27
          },
          "contact_name": {
            "$ref": "#/components/schemas/Address/properties/contact_name"
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20
          },
          "contact_email": {
            "$ref": "#/components/schemas/Address/properties/contact_email"
          },
          "default_for": {
            "type": "object",
            "additionalProperties": false,
            "description": "Each element indicates if the address is set as default value for pickup, billing, sender, and return address.",
            "properties": {
              "pickup": {
                "type": "boolean",
                "enum": [
                  true
                ]
              },
              "billing": {
                "type": "boolean",
                "enum": [
                  true
                ]
              },
              "sender": {
                "type": "boolean",
                "enum": [
                  true
                ]
              },
              "return": {
                "type": "boolean",
                "enum": [
                  true
                ]
              }
            }
          }
        }
      },
      "AddressFull": {
        "type": "object",
        "description": "Address object for Addresses API",
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Address ID"
          },
          "status": {
            "type": "string",
            "enum": [
              "active",
              "inactive"
            ],
            "description": "Status of the address"
          },
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
          "company_name": {
            "$ref": "#/components/schemas/Address/properties/company_name"
          },
          "contact_name": {
            "$ref": "#/components/schemas/Address/properties/contact_name"
          },
          "contact_phone": {
            "$ref": "#/components/schemas/Address/properties/contact_phone"
          },
          "contact_email": {
            "$ref": "#/components/schemas/Address/properties/contact_email"
          },
          "default_for": {
            "type": "object",
            "additionalProperties": false,
            "description": "Each element indicates if the address is set as default value for pickup, billing, sender, and return address.",
            "properties": {
              "billing": {
                "type": "boolean",
                "description": "Whether this is the default billing address"
              },
              "sender": {
                "type": "boolean",
                "description": "Whether this is the default sender address"
              },
              "pickup": {
                "type": "boolean",
                "description": "Whether this is the default pickup address"
              },
              "return": {
                "type": "boolean",
                "description": "Whether this is the default return address"
              }
            }
          },
          "hk_district": {
            "type": "object",
            "nullable": true,
            "additionalProperties": false,
            "description": "Details of the district for an address in Hong Kong. Display only applicable for addresses in Hong Kong.",
            "properties": {
              "id": {
                "type": "integer"
              },
              "area": {
                "type": "string"
              },
              "district": {
                "type": "string"
              },
              "zone": {
                "type": "string"
              }
            }
          },
          "validation": {
            "type": "object",
            "additionalProperties": false,
            "description": "Available only when the Address Validation is active for your account and the address was created by Address Validation",
            "properties": {
              "status": {
                "type": "string",
                "description": "Status of the address validation. Refers to the validation output (not the input)."
              },
              "detail": {
                "type": "string",
                "nullable": true,
                "description": "The relative level to which the post-processed address is verifiable while also considering its closeness to the input data."
              },
              "comparison": {
                "type": "object",
                "additionalProperties": false,
                "nullable": true,
                "description": "A descriptive comparison of the pre/post validated address. Similar to `detail` with more fidelity.",
                "properties": {
                  "pre": {
                    "type": "string",
                    "enum": [
                      "delivery_point",
                      "premise",
                      "street",
                      "city",
                      "state",
                      "none"
                    ],
                    "description": "The verification level of the address before validation."
                  },
                  "post": {
                    "type": "string",
                    "enum": [
                      "delivery_point",
                      "premise",
                      "street",
                      "city",
                      "state",
                      "none"
                    ],
                    "description": "The verification level of the address after validation."
                  },
                  "changes": {
                    "type": "string",
                    "enum": [
                      "none",
                      "minor",
                      "moderate",
                      "major",
                      "drastic"
                    ],
                    "description": "The extent of changes made to the address during validation. * `none` - No changes * `minor` - Minor changes like capitalization or a single character * `moderate` - Moderate changes worth reviewing * `major` - Larger changes worth reviewing * `drastic` - Drastic changes worth reviewing\n"
                  }
                }
              },
              "address": {
                "type": "object",
                "description": "The validated address as sourced from validation service",
                "properties": {
                  "line_1": {
                    "type": "string",
                    "description": "First line of the street address"
                  },
                  "line_2": {
                    "type": "string",
                    "nullable": true,
                    "description": "Second line of the street address"
                  },
                  "line_3": {
                    "type": "string",
                    "nullable": true,
                    "description": "Third line of the street address",
                    "maximum": 35
                  },
                  "state": {
                    "type": "string",
                    "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names."
                  },
                  "city": {
                    "type": "string",
                    "description": "City or Suburb"
                  },
                  "postal_code": {
                    "type": "string",
                    "description": "Postal code."
                  },
                  "country_alpha2": {
                    "$ref": "#/components/schemas/CountryAlpha2"
                  },
                  "company_name": {
                    "type": "string",
                    "nullable": true,
                    "description": "The company or organization at the address"
                  },
                  "contact_name": {
                    "type": "string",
                    "description": "The full name of a person at the address"
                  }
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