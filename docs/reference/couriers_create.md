# Create a Courier

Creates a new courier.
- `201` status when created successfully.
- `202` status when created but requiring additional verification.

Required authorization scope: `public.courier:write`


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
      "name": "Couriers"
    }
  ],
  "paths": {
    "/2024-09/couriers": {
      "post": {
        "summary": "Create a Courier",
        "tags": [
          "Couriers"
        ],
        "operationId": "couriers_create",
        "description": "Creates a new courier.\n- `201` status when created successfully.\n- `202` status when created but requiring additional verification.\n\nRequired authorization scope: `public.courier:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "courier successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "australia_post_eparcel": {
                    "value": {
                      "courier": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                        "account_number": "4392843289284",
                        "auth": {
                          "errors": [],
                          "state": "verified"
                        },
                        "created_at": "2022-02-22T12:21:00Z",
                        "ddp_handling_fee": 10,
                        "easyship_courier": false,
                        "filtered_account_details": {
                          "account_number": "*********9284",
                          "api_key": "***_KEY"
                        },
                        "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/dhl.png",
                        "nickname": "AU Post Dev",
                        "origin_country_alpha2": "AU",
                        "pickup_fee": 20,
                        "state": "active",
                        "umbrella_name": "Australia Post eParcel"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Australia Post eParcel"
                  },
                  "dhl": {
                    "value": {
                      "courier": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                        "account_number": "123456789",
                        "auth": {
                          "errors": [],
                          "state": "verified"
                        },
                        "created_at": "2022-02-22T12:21:00Z",
                        "ddp_handling_fee": 10,
                        "easyship_courier": false,
                        "filtered_account_details": {
                          "account_number": "*****6789",
                          "api_key": "***_KEY"
                        },
                        "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/dhl.png",
                        "nickname": "Dev DHL",
                        "origin_country_alpha2": "US",
                        "pickup_fee": 20,
                        "state": "active",
                        "umbrella_name": "DHL"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "DHL"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/courier_single"
                }
              }
            }
          },
          "202": {
            "description": "courier successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "royal_mail": {
                    "value": {
                      "courier": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0003",
                        "account_number": "test number",
                        "auth": {
                          "errors": [],
                          "state": "partially_verified"
                        },
                        "created_at": "2022-02-22T12:21:00Z",
                        "ddp_handling_fee": 10,
                        "easyship_courier": false,
                        "filtered_account_details": {
                          "account_number": "test number",
                          "address_line_1": "12 Privet Drive",
                          "city": "London",
                          "contact_email": "test@email.com",
                          "contact_phone": "07311111928",
                          "customer_name": "test name",
                          "oba_email_address": "test@email.com",
                          "postal_code": "BA53HZ",
                          "posting_location": "9876543210",
                          "receiving_hub": "002631"
                        },
                        "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/dhl.png",
                        "nickname": "My Royal Mail",
                        "origin_country_alpha2": "HK",
                        "pickup_fee": 20,
                        "state": "pending",
                        "umbrella_name": "Royal Mail"
                      },
                      "meta": {
                        "messages": [
                          "Before you can start generating labels with your Royal Mail account, we'll need to verify your Royal Mail Online Business Account (OBA) details. This process takes up to 2 - 3 business days."
                        ],
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "Royal Mail"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/courier_single"
                }
              }
            }
          },
          "402": {
            "description": "over limit",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "over_limit",
                        "details": [],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Subscriptions",
                            "url": "https://developers.easyship.com/reference/subscription"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Courier",
                            "url": "https://developers.easyship.com/reference/courier_accounts_create"
                          }
                        ],
                        "message": "You have reached your plan limit. Please upgrade your subscription plan.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "over limit"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
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
                          "Nickname must be between 3 to 15 characters."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Courier",
                            "url": "https://developers.easyship.com/reference/courier_accounts_create"
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
                "$ref": "#/components/schemas/CourierCreate"
              },
              "examples": {
                "australia_post_eparcel": {
                  "summary": "with Australia Post courier",
                  "value": {
                    "courier_umbrella_name": "Australia Post eParcel",
                    "nickname": "AU Post Dev",
                    "customer_reference_id": "reference id",
                    "origin_country_alpha2": "AU",
                    "account_details": {
                      "account_number": "4392843289284",
                      "api_key": "API_KEY",
                      "password": "PASSWORD"
                    },
                    "ddp_handling_fee": 10,
                    "pickup_fee": 20
                  }
                },
                "dhl": {
                  "summary": "with DHL courier",
                  "value": {
                    "courier_umbrella_name": "DHL",
                    "nickname": "Dev DHL",
                    "customer_reference_id": "reference id",
                    "origin_country_alpha2": "US",
                    "account_details": {
                      "account_number": "123456789",
                      "api_key": "API_KEY",
                      "api_secret": "API_SECRET"
                    },
                    "ddp_handling_fee": 10,
                    "pickup_fee": 20
                  }
                },
                "royal_mail": {
                  "summary": "with Royal Mail courier",
                  "value": {
                    "courier_umbrella_name": "Royal Mail",
                    "nickname": "My Royal Mail",
                    "customer_reference_id": "reference id",
                    "account_details": {
                      "account_number": "test number",
                      "customer_name": "test name",
                      "oba_email_address": "test@email.com",
                      "posting_location": "9876543210",
                      "address_line_1": "12 Privet Drive",
                      "city": "London",
                      "postal_code": "BA53HZ",
                      "contact_phone": "07311111928",
                      "contact_email": "test@email.com"
                    },
                    "ddp_handling_fee": 10,
                    "pickup_fee": 20
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
      "courier_single": {
        "type": "object",
        "description": "Single courier with all its details",
        "additionalProperties": false,
        "properties": {
          "courier": {
            "$ref": "#/components/schemas/Courier"
          },
          "meta": {
            "$ref": "#/components/schemas/CourierMeta"
          }
        }
      },
      "CourierAuth": {
        "type": "object",
        "description": "Courier authentication state for LYOC accounts.",
        "additionalProperties": false,
        "properties": {
          "state": {
            "type": "string",
            "description": "Authentication State for LYOC only. For Royal Mail, a newly-created account will be set to `partially_verified` until the account details have been `verified`. If there are issues with the account details, this will be set to `failed`.",
            "enum": [
              "unverified",
              "partially_verified",
              "verified",
              "failed"
            ]
          },
          "errors": {
            "type": "array",
            "description": "Authentication errors for LYOC only. If the authentication state of the account is `failed`, this will contain a list of error messages concerning the failure.",
            "items": {
              "type": "string"
            }
          }
        }
      },
      "CourierBase": {
        "type": "object",
        "description": "Courier",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid"
          },
          "customer_reference_id": {
            "type": "string",
            "nullable": true,
            "description": "An identifier for the customer who owns the account. Available only for selected customers."
          },
          "easyship_courier": {
            "type": "boolean",
            "description": "Whether the courier belongs to Easyship or not."
          },
          "nickname": {
            "type": "string",
            "description": "For LYOC. Unique nickname used to identify the linked account.",
            "minimum": 3,
            "maximum": 15
          },
          "umbrella_name": {
            "type": "string",
            "description": "Umbrella Name of the courier"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "state": {
            "type": "string",
            "description": "Courier State for LYOC only. For Royal Mail, a newly-created account will be set to `pending` until the account details are verified. Once verified, the account will be set to `active` and the associated courier services will available for Rates and Labels.",
            "enum": [
              "pending",
              "active",
              "inactive"
            ]
          },
          "auth": {
            "$ref": "#/components/schemas/CourierAuth"
          },
          "ddp_handling_fee": {
            "type": "number",
            "description": "For LYOC only. DDP handling fee applied by the courier when DDP is requested."
          },
          "pickup_fee": {
            "type": "number",
            "description": "For LYOC only. Additional pickup fee to apply to all shipments. This fee will be added to your quoted rates."
          },
          "account_number": {
            "type": "string",
            "nullable": true,
            "description": "For LYOC only. The account number associated with the linked courier account."
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "For LYOC only. The date and time the courier account was created in ISO 8601 format."
          }
        }
      },
      "CourierRoyalMail": {
        "type": "object",
        "description": "Royal Mail Courier",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/CourierBase/properties/id"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "easyship_courier": {
            "$ref": "#/components/schemas/CourierBase/properties/easyship_courier"
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "umbrella_name": {
            "type": "string",
            "description": "Umbrella Name of the courier",
            "enum": [
              "Royal Mail"
            ]
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "state": {
            "$ref": "#/components/schemas/CourierBase/properties/state"
          },
          "auth": {
            "$ref": "#/components/schemas/CourierAuth"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "account_number": {
            "$ref": "#/components/schemas/CourierBase/properties/account_number"
          },
          "created_at": {
            "$ref": "#/components/schemas/CourierBase/properties/created_at"
          },
          "filtered_account_details": {
            "type": "object",
            "description": "For LYOC only. Account details. For security reasons, if credentials are provided in the initial creation request, these will not returned.",
            "additionalProperties": false,
            "properties": {
              "account_number": {
                "type": "string",
                "description": "(deprecated) Royal Mail account number",
                "nullable": true
              },
              "customer_name": {
                "type": "string",
                "description": "Customer Name associated with the customer's Royal Mail Online Business Account (OBA). Prior to linking an account, the user will need to register for an OBA with Royal Mail. More details about this process can be found [here](https://support.easyship.com/hc/en-us/articles/360046578311-Link-Your-Royal-Mail-Account)."
              },
              "oba_email_address": {
                "type": "string",
                "format": "email",
                "description": "Email address associated with the customer's OBA"
              },
              "posting_location": {
                "type": "string",
                "description": "Posting Location (Must be 10 digits, starting with 9)",
                "nullable": true
              },
              "address_line_1": {
                "$ref": "#/components/schemas/Address/properties/line_1"
              },
              "city": {
                "$ref": "#/components/schemas/Address/properties/city"
              },
              "postal_code": {
                "type": "string",
                "description": "Postal Code. This will be used to determine the customer's receiving hub."
              },
              "contact_phone": {
                "$ref": "#/components/schemas/Address/properties/contact_phone"
              },
              "contact_email": {
                "$ref": "#/components/schemas/Address/properties/contact_email"
              },
              "receiving_hub": {
                "type": "string",
                "description": "Receiving hub"
              }
            }
          }
        }
      },
      "Courier": {
        "type": "object",
        "description": "Courier",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/CourierBase/properties/id"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "easyship_courier": {
            "$ref": "#/components/schemas/CourierBase/properties/easyship_courier"
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "state": {
            "$ref": "#/components/schemas/CourierBase/properties/state"
          },
          "auth": {
            "$ref": "#/components/schemas/CourierAuth"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "account_number": {
            "$ref": "#/components/schemas/CourierBase/properties/account_number"
          },
          "created_at": {
            "$ref": "#/components/schemas/CourierBase/properties/created_at"
          },
          "umbrella_name": {
            "type": "string",
            "description": "Umbrella Name of the Courier"
          },
          "filtered_account_details": {
            "type": "object",
            "description": "Account details are available only for LYOC couriers. The content is different per courier.",
            "additionalProperties": true
          },
          "logo_url": {
            "type": "string",
            "description": "URL of the Courier logo."
          }
        }
      },
      "CourierCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/CourierAustraliaPostEParcelCreate"
          },
          {
            "$ref": "#/components/schemas/CourierDHLCreate"
          },
          {
            "$ref": "#/components/schemas/CourierRoyalMailCreate"
          }
        ],
        "discriminator": {
          "propertyName": "courier_umbrella_name",
          "mapping": {
            "Australia Post eParcel": "#/components/schemas/CourierAustraliaPostEParcelCreate",
            "DHL": "#/components/schemas/CourierDHLCreate",
            "Royal Mail": "#/components/schemas/CourierRoyalMailCreate"
          }
        }
      },
      "CourierAustraliaPostEParcelCreate": {
        "type": "object",
        "additionalProperties": false,
        "description": "Create Australia Post eParcel Courier",
        "required": [
          "origin_country_alpha2",
          "courier_umbrella_name",
          "nickname",
          "account_details"
        ],
        "properties": {
          "courier_umbrella_name": {
            "type": "string",
            "enum": [
              "Australia Post eParcel",
              "Australia Post"
            ],
            "description": "- `Australia Post eParcel`: Australia Post eParcel\n- `Australia Post`: Deprecated. Umbrella name will be converted automatically to Australia Post eParcel when it is provided.\n"
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "origin_country_alpha2": {
            "allOf": [
              {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              {
                "enum": [
                  "AU"
                ]
              }
            ]
          },
          "account_details": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "account_number",
              "password",
              "api_key"
            ],
            "properties": {
              "account_number": {
                "type": "string",
                "description": "Australia Post eParcel account number"
              },
              "password": {
                "type": "string",
                "description": "Australia Post eParcel password"
              },
              "api_key": {
                "type": "string",
                "description": "Australia Post eParcel API key"
              }
            }
          }
        }
      },
      "CourierDHLCreate": {
        "type": "object",
        "additionalProperties": false,
        "description": "Create DHL Courier",
        "required": [
          "courier_umbrella_name",
          "nickname",
          "account_details"
        ],
        "properties": {
          "courier_umbrella_name": {
            "type": "string",
            "enum": [
              "DHL"
            ]
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "account_details": {
            "type": "object",
            "additionalProperties": false,
            "required": [
              "account_number",
              "api_key",
              "api_secret"
            ],
            "properties": {
              "account_number": {
                "type": "string",
                "description": "DHL account number"
              },
              "api_key": {
                "type": "string",
                "description": "DHL API key"
              },
              "api_secret": {
                "type": "string",
                "description": "DHL API secret"
              }
            }
          }
        }
      },
      "CourierRoyalMailCreate": {
        "type": "object",
        "additionalProperties": false,
        "description": "Create Royal Mail Courier",
        "properties": {
          "courier_umbrella_name": {
            "type": "string",
            "enum": [
              "Royal Mail"
            ]
          },
          "nickname": {
            "$ref": "#/components/schemas/CourierBase/properties/nickname"
          },
          "customer_reference_id": {
            "$ref": "#/components/schemas/CourierBase/properties/customer_reference_id"
          },
          "ddp_handling_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/ddp_handling_fee"
          },
          "pickup_fee": {
            "$ref": "#/components/schemas/CourierBase/properties/pickup_fee"
          },
          "account_details": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "account_number": {
                "type": "string",
                "description": "Royal Mail account number"
              },
              "customer_name": {
                "$ref": "#/components/schemas/CourierRoyalMail/properties/filtered_account_details/properties/customer_name"
              },
              "oba_email_address": {
                "$ref": "#/components/schemas/CourierRoyalMail/properties/filtered_account_details/properties/oba_email_address"
              },
              "posting_location": {
                "$ref": "#/components/schemas/CourierRoyalMail/properties/filtered_account_details/properties/posting_location"
              },
              "address_line_1": {
                "$ref": "#/components/schemas/Address/properties/line_1"
              },
              "city": {
                "$ref": "#/components/schemas/Address/properties/city"
              },
              "postal_code": {
                "$ref": "#/components/schemas/CourierRoyalMail/properties/filtered_account_details/properties/postal_code"
              },
              "contact_phone": {
                "$ref": "#/components/schemas/Address/properties/contact_phone"
              },
              "contact_email": {
                "$ref": "#/components/schemas/Address/properties/contact_email"
              }
            },
            "required": [
              "account_number",
              "customer_name",
              "oba_email_address",
              "posting_location",
              "address_line_1",
              "city",
              "postal_code",
              "contact_phone",
              "contact_email"
            ]
          }
        },
        "required": [
          "courier_umbrella_name",
          "nickname",
          "account_details"
        ]
      },
      "CourierMeta": {
        "type": "object",
        "description": "Courier Metadata",
        "additionalProperties": false,
        "properties": {
          "messages": {
            "type": "array",
            "description": "Messages from courier service when the Courier creation is a partial success (status code `202`).",
            "items": {
              "type": "string"
            }
          },
          "request_id": {
            "$ref": "#/components/schemas/Meta/properties/request_id"
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