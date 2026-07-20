# Information about the Account

Retrieve information about current account

Properties below would display only when the access token includes the corresponding scopes.

| Property | Required API Scope |
| -------- | ------------------ |
| `billing_address` | `public.address:read` |
| `credit` | `public.credit:read` |
| `payment_sources` | `public.payment_source:read` |


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
      "name": "Account"
    }
  ],
  "paths": {
    "/2024-09/account": {
      "get": {
        "summary": "Information about the Account",
        "tags": [
          "Account"
        ],
        "operationId": "account_show",
        "description": "Retrieve information about current account\n\nProperties below would display only when the access token includes the corresponding scopes.\n\n| Property | Required API Scope |\n| -------- | ------------------ |\n| `billing_address` | `public.address:read` |\n| `credit` | `public.credit:read` |\n| `payment_sources` | `public.payment_source:read` |\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "information of current account",
            "content": {
              "application/json": {
                "examples": {
                  "scopes_of_access_token_contains_supported_scopes": {
                    "value": {
                      "account": {
                        "billing_address": {
                          "city": "York",
                          "company_name": "Test Plc.",
                          "contact_email": "gb@testgbemail.com",
                          "contact_name": "Foo Bar",
                          "contact_phone": "+44 7784 024023",
                          "country_alpha2": "GB",
                          "default_for": {
                            "pickup": false,
                            "billing": true,
                            "sender": false,
                            "return": false
                          },
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "line_1": "58 Goodramgate",
                          "line_2": null,
                          "postal_code": "YO1 7LF",
                          "state": "Yorkshire",
                          "status": "active"
                        },
                        "credit": {
                          "available_balance": 100,
                          "balance": 100,
                          "currency": "HKD"
                        },
                        "easyship_company_id": "CHK000001",
                        "name": "The Shopify Limited",
                        "payment_sources": [
                          {
                            "card": {
                              "brand": "Visa",
                              "expiration_month": "12",
                              "expiration_year": "2099",
                              "holder_name": null,
                              "last_four_digits": "1111"
                            },
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "payment_method_type": "card"
                          }
                        ]
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "scopes of access token contains supported scopes"
                  },
                  "scopes_of_access_token_doesn_t_contain_supported_scopes": {
                    "value": {
                      "account": {
                        "easyship_company_id": "CHK000001",
                        "name": "The Shopify Limited"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "scopes of access token doesn't contains supported scopes"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/account_single"
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
      "account_single": {
        "type": "object",
        "description": "Account details",
        "additionalProperties": false,
        "properties": {
          "account": {
            "$ref": "#/components/schemas/Account"
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
      "Account": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "billing_address": {
            "$ref": "#/components/schemas/AddressFull"
          },
          "name": {
            "type": "string",
            "description": "Company name of current account"
          },
          "easyship_company_id": {
            "type": "string",
            "description": "Easyship company ID"
          },
          "credit": {
            "$ref": "#/components/schemas/Credit"
          },
          "payment_sources": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PaymentSource"
            }
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
      "Credit": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "balance": {
            "type": "number",
            "description": "Total amount in the account without considering holds or pending transactions."
          },
          "available_balance": {
            "type": "number",
            "description": "Funds accessible for use, accounting for holds and pending transactions."
          },
          "currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Currency code for the account. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          }
        }
      },
      "PaymentSource": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Payment source id in Easyship"
          },
          "third_party_source_id": {
            "type": "string",
            "description": "Third party payment source id"
          },
          "payment_method_type": {
            "type": "string",
            "enum": [
              "card",
              "bank_account"
            ]
          },
          "bank_account": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "bank_name": {
                "type": "string",
                "description": "Bank name"
              },
              "holder_name": {
                "type": "string",
                "description": "Account holder name"
              },
              "last_four_digits": {
                "type": "string",
                "description": "Last four digits of bank account number"
              },
              "routing_number": {
                "type": "string",
                "description": "Routing number"
              },
              "is_verified": {
                "type": "boolean",
                "description": "Whether the bank account is verified by Stripe"
              }
            }
          },
          "card": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "brand": {
                "type": "string",
                "description": "Credit card brand",
                "example": "visa"
              },
              "expiration_year": {
                "type": "string",
                "description": "The expiration year of the card",
                "example": "2023"
              },
              "expiration_month": {
                "type": "string",
                "description": "The expiration month of the card",
                "example": "01"
              },
              "last_four_digits": {
                "type": "string",
                "description": "Last four digits of credit card"
              },
              "holder_name": {
                "type": "string",
                "description": "Card holder name",
                "nullable": true
              }
            }
          }
        }
      }
    }
  }
}
```