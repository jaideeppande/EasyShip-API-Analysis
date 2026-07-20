# Validate a single domestic (US) address

Create a domestic address validation for US addresses.

This endpoint is specifically for US addresses.
The `country_alpha2` parameter is optional and will be ignored if provided.

Required authorization scope: `public.address_validation_domestic:write`

> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).

> **Note:** Calls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.


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
    "/2024-09/addresses/validations_domestic": {
      "post": {
        "summary": "Validate a single domestic (US) address",
        "tags": [
          "Addresses"
        ],
        "operationId": "addresses_validation_domestic",
        "description": "Create a domestic address validation for US addresses.\n\nThis endpoint is specifically for US addresses.\nThe `country_alpha2` parameter is optional and will be ignored if provided.\n\nRequired authorization scope: `public.address_validation_domestic:write`\n\n> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).\n\n> **Note:** Calls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "success with validated address",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "address": {
                        "city": "Washington",
                        "company_name": "Easyship Inc",
                        "country_alpha2": "US",
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "line_1": "1600 Pennsylvania Avenue NW",
                        "line_2": null,
                        "postal_code": "20500",
                        "state": "DC",
                        "validation": {
                          "address": {
                            "city": "Washington",
                            "company_name": "The White House",
                            "country_alpha2": "US",
                            "line_1": "1600 Pennsylvania Avenue NW",
                            "line_2": null,
                            "line_3": null,
                            "postal_code": "20500",
                            "state": "DC"
                          },
                          "comparison": {
                            "changes": "none",
                            "post": "premise",
                            "pre": "premise"
                          },
                          "detail": "premise",
                          "status": "verified"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "success with validated address"
                  },
                  "replace_with_validation_result": {
                    "value": {
                      "address": {
                        "city": "Washington",
                        "company_name": "The White House",
                        "country_alpha2": "US",
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "line_1": "1600 Pennsylvania Avenue NW",
                        "line_2": null,
                        "postal_code": "20500",
                        "state": "DC",
                        "validation": {
                          "address": {
                            "city": "Washington",
                            "company_name": "The White House",
                            "country_alpha2": "US",
                            "line_1": "1600 Pennsylvania Avenue NW",
                            "line_2": null,
                            "line_3": null,
                            "postal_code": "20500",
                            "state": "DC"
                          },
                          "comparison": {
                            "changes": "none",
                            "post": "premise",
                            "pre": "premise"
                          },
                          "detail": "premise",
                          "status": "verified"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Replace with validation result"
                  },
                  "without_country": {
                    "value": {
                      "address": {
                        "city": "Washington",
                        "company_name": "Easyship Inc",
                        "country_alpha2": "US",
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                        "line_1": "1600 Pennsylvania Avenue NW",
                        "line_2": null,
                        "postal_code": "20500",
                        "state": "DC",
                        "validation": {
                          "address": {
                            "city": "Washington",
                            "company_name": "The White House",
                            "country_alpha2": "US",
                            "line_1": "1600 Pennsylvania Avenue NW",
                            "line_2": null,
                            "line_3": null,
                            "postal_code": "20500",
                            "state": "DC"
                          },
                          "comparison": {
                            "changes": "none",
                            "post": "premise",
                            "pre": "premise"
                          },
                          "detail": "premise",
                          "status": "verified"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Country automatically set to US"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/address_validation_single"
                }
              }
            }
          },
          "422": {
            "description": "invalid request",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/AddressValidationDomesticCreate missing required parameters: line_1, city"
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
                    "summary": "invalid request"
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
                "$ref": "#/components/schemas/AddressValidationDomesticCreate"
              },
              "examples": {
                "success_with_validated_address": {
                  "summary": "success with validated address",
                  "value": {
                    "company_name": "Easyship Inc",
                    "line_1": "1600 Pennsylvania Avenue NW",
                    "city": "Washington",
                    "state": "DC",
                    "postal_code": "20500",
                    "replace_with_validation_result": true
                  }
                },
                "invalid_request": {
                  "summary": "invalid request",
                  "value": {
                    "company_name": "Easyship Inc",
                    "postal_code": "20500"
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
      "address_validation_single": {
        "type": "object",
        "description": "Address validation details",
        "additionalProperties": false,
        "properties": {
          "address": {
            "$ref": "#/components/schemas/AddressValidation"
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
      "AddressValidation": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "company_name": {
            "$ref": "#/components/schemas/Address/properties/company_name"
          },
          "line_1": {
            "$ref": "#/components/schemas/Address/properties/line_1"
          },
          "line_2": {
            "$ref": "#/components/schemas/Address/properties/line_2"
          },
          "state": {
            "type": "string",
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names.",
            "maximum": 200,
            "nullable": true
          },
          "city": {
            "$ref": "#/components/schemas/Address/properties/city"
          },
          "postal_code": {
            "type": "string",
            "nullable": true,
            "description": "Postal code."
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "validation": {
            "$ref": "#/components/schemas/AddressFull/properties/validation"
          }
        }
      },
      "AddressValidationDomesticCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "line_1",
          "city"
        ],
        "properties": {
          "company_name": {
            "$ref": "#/components/schemas/Address/properties/company_name"
          },
          "line_1": {
            "$ref": "#/components/schemas/Address/properties/line_1"
          },
          "line_2": {
            "$ref": "#/components/schemas/Address/properties/line_2"
          },
          "state": {
            "$ref": "#/components/schemas/AddressValidation/properties/state"
          },
          "city": {
            "$ref": "#/components/schemas/Address/properties/city"
          },
          "postal_code": {
            "$ref": "#/components/schemas/AddressValidation/properties/postal_code"
          },
          "replace_with_validation_result": {
            "$ref": "#/components/schemas/BatchAddressesCreate/properties/defaults/properties/replace_with_validation_result"
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
      "BatchAddressesCreate": {
        "type": "object",
        "description": "Batch Addresses Create",
        "additionalProperties": false,
        "required": [
          "addresses"
        ],
        "properties": {
          "defaults": {
            "type": "object",
            "description": "Default settings for each address (can be override on the individual address)",
            "additionalProperties": false,
            "properties": {
              "country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2Nullable"
              },
              "validate": {
                "type": "boolean",
                "default": false,
                "description": "Whether the company validates the address they want to create"
              },
              "replace_with_validation_result": {
                "type": "boolean",
                "default": false,
                "description": "Override user's address with the address validation results"
              }
            }
          },
          "addresses": {
            "type": "array",
            "minItems": 1,
            "maxItems": 1000,
            "items": {
              "type": "object",
              "description": "Address",
              "additionalProperties": false,
              "required": [
                "city",
                "contact_name",
                "contact_phone",
                "line_1",
                "postal_code",
                "state"
              ],
              "properties": {
                "city": {
                  "$ref": "#/components/schemas/Address/properties/city"
                },
                "company_name": {
                  "$ref": "#/components/schemas/Address/properties/company_name"
                },
                "contact_email": {
                  "$ref": "#/components/schemas/Address/properties/contact_email"
                },
                "contact_name": {
                  "$ref": "#/components/schemas/Address/properties/contact_name"
                },
                "contact_phone": {
                  "$ref": "#/components/schemas/Address/properties/contact_phone"
                },
                "country_alpha2": {
                  "$ref": "#/components/schemas/CountryAlpha2"
                },
                "line_1": {
                  "$ref": "#/components/schemas/Address/properties/line_1"
                },
                "line_2": {
                  "$ref": "#/components/schemas/Address/properties/line_2"
                },
                "postal_code": {
                  "$ref": "#/components/schemas/Address/properties/postal_code"
                },
                "reference_id": {
                  "type": "string",
                  "description": "Reference ID",
                  "maximum": 36,
                  "nullable": true
                },
                "state": {
                  "$ref": "#/components/schemas/Address/properties/state"
                },
                "validate": {
                  "type": "boolean",
                  "nullable": true,
                  "description": "Whether the company validates the address they want to create"
                },
                "replace_with_validation_result": {
                  "$ref": "#/components/schemas/BatchAddressesCreate/properties/defaults/properties/replace_with_validation_result"
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