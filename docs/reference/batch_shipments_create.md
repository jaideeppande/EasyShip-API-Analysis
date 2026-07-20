# Create a Batch of Shipments

Create a batch of shipments and schedule it for processing.

Required authorization scopes: `public.batch:write`, `public.shipment:write` and `public.label:write` if a label(s) will be created during the batch processing.


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
      "name": "Batches"
    }
  ],
  "paths": {
    "/2024-09/batches/shipments": {
      "post": {
        "summary": "Create a Batch of Shipments",
        "tags": [
          "Batches"
        ],
        "operationId": "batch_shipments_create",
        "description": "Create a batch of shipments and schedule it for processing.\n\nRequired authorization scopes: `public.batch:write`, `public.shipment:write` and `public.label:write` if a label(s) will be created during the batch processing.\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "202": {
            "description": "batch successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "batch": {
                        "id": "01563646-58c1-4607-8fe0-cae3e33c0004",
                        "created_at": "2022-02-22T12:21:00Z",
                        "finished_at": null,
                        "started_at": null,
                        "state": "created",
                        "type": "shipment_batch"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "batch successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/batch_single"
                }
              }
            }
          },
          "422": {
            "description": "invalid params",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/BatchShipmentsCreate/properties/defaults/properties/origin_address_id does not allow null values"
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
                    "summary": "invalid params"
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
                "$ref": "#/components/schemas/BatchShipmentsCreate"
              },
              "examples": {
                "batch_successfully_created": {
                  "summary": "batch successfully created",
                  "value": {
                    "defaults": {
                      "origin_address_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                      "sender_address_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                      "return_address_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                      "incoterms": "DDP",
                      "regulatory_identifiers": {
                        "eori": "d_123456789",
                        "ioss": "d_123456789",
                        "vat_number": "d_123456789"
                      },
                      "shipping_settings": {
                        "buy_label": false,
                        "units": {
                          "weight": "lb",
                          "dimensions": "in"
                        },
                        "printing_options": {
                          "format": "url",
                          "label": "A4",
                          "commercial_invoice": "A4",
                          "packing_slip": "A4"
                        }
                      },
                      "courier_settings": {
                        "allow_fallback": true,
                        "apply_shipping_rules": false,
                        "courier_service_id": null
                      }
                    },
                    "shipments": [
                      {
                        "origin_address_id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "sender_address_id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "return_address_id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                        "consignee_tax_id": "123456789",
                        "eei_reference": "123456789",
                        "incoterms": "DDU",
                        "set_as_residential": true,
                        "metadata": {
                          "key": "value"
                        },
                        "regulatory_identifiers": {
                          "eori": "123456789",
                          "ioss": "123456789",
                          "vat_number": "123456789"
                        },
                        "insurance": {
                          "is_insured": true,
                          "insured_amount": 10,
                          "insured_currency": "USD"
                        },
                        "order_data": {
                          "platform_name": "Shopy",
                          "platform_order_number": "123456789",
                          "order_tag_list": [
                            "tag1",
                            "tag2"
                          ],
                          "seller_notes": "Seller notes",
                          "buyer_notes": "Buyer notes"
                        },
                        "shipping_settings": {
                          "buy_label": false,
                          "units": {
                            "weight": "kg",
                            "dimensions": "cm"
                          },
                          "printing_options": {
                            "format": "png",
                            "label": "4x6",
                            "commercial_invoice": "4x6",
                            "packing_slip": "4x6"
                          }
                        },
                        "destination_address": {
                          "company_name": "Test Plc.",
                          "contact_name": "Foo Bar",
                          "contact_email": "us@testusemail.com",
                          "contact_phone": "917-275-6975",
                          "line_1": "73 CHESTER RD",
                          "line_2": null,
                          "postal_code": "02478",
                          "city": "Belmont",
                          "state": "Massachusetts",
                          "country_alpha2": "US"
                        },
                        "parcels": [
                          {
                            "total_actual_weight": 1,
                            "box": {
                              "slug": "custom",
                              "length": 10,
                              "width": 10,
                              "height": 1
                            },
                            "items": [
                              {
                                "product": {
                                  "id": "01563646-58c1-4607-8fe0-cae3e33c0003"
                                },
                                "quantity": 1,
                                "declared_currency": "USD",
                                "declared_customs_value": 10
                              }
                            ]
                          }
                        ],
                        "courier_settings": {
                          "allow_fallback": false,
                          "apply_shipping_rules": true,
                          "courier_service_id": null
                        }
                      }
                    ]
                  }
                },
                "invalid_params": {
                  "summary": "invalid params",
                  "value": {
                    "defaults": {
                      "origin_address_id": null,
                      "sender_address_id": null,
                      "return_address_id": null
                    },
                    "shipments": [
                      {
                        "destination_address": {
                          "company_name": "Test Plc.",
                          "contact_name": "Foo Bar",
                          "contact_email": "us@testusemail.com",
                          "contact_phone": "917-275-6975",
                          "line_1": "73 CHESTER RD",
                          "line_2": null,
                          "postal_code": "02478",
                          "city": "Belmont",
                          "state": "Massachusetts",
                          "country_alpha2": "US"
                        },
                        "parcels": [
                          {
                            "total_actual_weight": 1,
                            "items": [
                              {
                                "product": {
                                  "id": "01563646-58c1-4607-8fe0-cae3e33c0003"
                                },
                                "quantity": 1,
                                "declared_currency": "USD",
                                "declared_customs_value": 10
                              }
                            ]
                          }
                        ]
                      }
                    ]
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
      "batch_single": {
        "type": "object",
        "description": "Batch",
        "additionalProperties": false,
        "properties": {
          "batch": {
            "$ref": "#/components/schemas/BatchSingle"
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
      "DestinationAddress": {
        "type": "object",
        "additionalProperties": false,
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
            "nullable": true,
            "maximum": 200,
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names."
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "description": "Postal code. Mandatory for most countries (if not applicable, for example Hong Kong, leave null or 0)"
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 50
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 50
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name`",
            "maximum": 50
          },
          "delivery_instructions": {
            "type": "string",
            "description": "Delivery instructions for the address, see [Delivery Instructions](https://developers.easyship.com/page/delivery-instructions).",
            "maximum": 200,
            "nullable": true
          }
        }
      },
      "Batch": {
        "type": "object",
        "description": "Batch",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "Batch ID"
          },
          "state": {
            "type": "string",
            "description": "Batch state",
            "enum": [
              "created",
              "processing",
              "processed",
              "failed"
            ]
          },
          "type": {
            "type": "string",
            "description": "Batch type",
            "enum": [
              "shipment_batch",
              "address_batch",
              "label_batch"
            ]
          },
          "started_at": {
            "type": "string",
            "format": "datetime",
            "nullable": true
          },
          "finished_at": {
            "type": "string",
            "format": "datetime",
            "nullable": true
          },
          "created_at": {
            "type": "string",
            "format": "datetime"
          },
          "updated_at": {
            "type": "string",
            "format": "datetime"
          }
        }
      },
      "BatchSingle": {
        "type": "object",
        "description": "Batch Detail",
        "additionalProperties": false,
        "properties": {
          "id": {
            "$ref": "#/components/schemas/Batch/properties/id"
          },
          "state": {
            "$ref": "#/components/schemas/Batch/properties/state"
          },
          "type": {
            "$ref": "#/components/schemas/Batch/properties/type"
          },
          "started_at": {
            "$ref": "#/components/schemas/Batch/properties/started_at"
          },
          "finished_at": {
            "$ref": "#/components/schemas/Batch/properties/finished_at"
          },
          "created_at": {
            "$ref": "#/components/schemas/Batch/properties/created_at"
          },
          "updated_at": {
            "$ref": "#/components/schemas/Batch/properties/updated_at"
          },
          "total_count": {
            "type": "integer",
            "description": "Batch Items total count"
          },
          "failed_count": {
            "type": "integer",
            "description": "Batch Items failed count"
          },
          "processed_count": {
            "type": "integer",
            "description": "Batch Items processed count"
          },
          "processing_count": {
            "type": "integer",
            "description": "Batch Items processing count"
          },
          "created_count": {
            "type": "integer",
            "description": "Batch Items created count"
          }
        }
      },
      "BatchShipmentsCreate": {
        "type": "object",
        "description": "Batch Shipments Create",
        "additionalProperties": false,
        "properties": {
          "defaults": {
            "type": "object",
            "description": "Default settings for each shipment (can be override on the individual shipment)",
            "additionalProperties": false,
            "required": [
              "origin_address_id",
              "sender_address_id",
              "return_address_id"
            ],
            "properties": {
              "origin_address_id": {
                "type": "string",
                "format": "uuid"
              },
              "sender_address_id": {
                "type": "string",
                "format": "uuid"
              },
              "return_address_id": {
                "type": "string",
                "format": "uuid"
              },
              "incoterms": {
                "$ref": "#/components/schemas/Shipment/properties/incoterms"
              },
              "regulatory_identifiers": {
                "$ref": "#/components/schemas/Shipment/properties/regulatory_identifiers"
              },
              "buyer_regulatory_identifiers": {
                "$ref": "#/components/schemas/Shipment/properties/buyer_regulatory_identifiers"
              },
              "courier_settings": {
                "$ref": "#/components/schemas/ShipmentCreate/properties/courier_settings"
              },
              "shipping_settings": {
                "type": "object",
                "properties": {
                  "additional_services": {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/additional_services"
                  },
                  "units": {
                    "$ref": "#/components/schemas/Units"
                  },
                  "buy_label": {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/buy_label"
                  },
                  "b13a_filing": {
                    "$ref": "#/components/schemas/Shipment/properties/shipping_settings/properties/b13a_filing"
                  },
                  "printing_options": {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/printing_options"
                  }
                }
              }
            }
          },
          "shipments": {
            "type": "array",
            "minItems": 1,
            "maxItems": 1000,
            "items": {
              "type": "object",
              "description": "Shipment",
              "additionalProperties": false,
              "required": [
                "destination_address",
                "parcels"
              ],
              "properties": {
                "origin_address_id": {
                  "type": "string",
                  "format": "uuid"
                },
                "sender_address_id": {
                  "type": "string",
                  "format": "uuid"
                },
                "return_address_id": {
                  "type": "string",
                  "format": "uuid"
                },
                "destination_address": {
                  "allOf": [
                    {
                      "$ref": "#/components/schemas/DestinationAddress"
                    }
                  ],
                  "required": [
                    "line_1",
                    "state",
                    "city",
                    "postal_code",
                    "contact_name",
                    "contact_email"
                  ]
                },
                "metadata": {
                  "$ref": "#/components/schemas/Shipment/properties/metadata"
                },
                "set_as_residential": {
                  "$ref": "#/components/schemas/ShipmentCreate/properties/set_as_residential"
                },
                "consignee_tax_id": {
                  "$ref": "#/components/schemas/ShipmentCreate/properties/consignee_tax_id"
                },
                "eei_reference": {
                  "$ref": "#/components/schemas/ShipmentCreate/properties/eei_reference"
                },
                "regulatory_identifiers": {
                  "$ref": "#/components/schemas/Shipment/properties/regulatory_identifiers"
                },
                "buyer_regulatory_identifiers": {
                  "$ref": "#/components/schemas/Shipment/properties/buyer_regulatory_identifiers"
                },
                "incoterms": {
                  "$ref": "#/components/schemas/Shipment/properties/incoterms"
                },
                "insurance": {
                  "$ref": "#/components/schemas/Shipment/properties/insurance"
                },
                "order_data": {
                  "$ref": "#/components/schemas/Shipment/properties/order_data"
                },
                "courier_settings": {
                  "$ref": "#/components/schemas/ShipmentCreate/properties/courier_settings"
                },
                "shipping_settings": {
                  "type": "object",
                  "properties": {
                    "additional_services": {
                      "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/additional_services"
                    },
                    "units": {
                      "$ref": "#/components/schemas/Units"
                    },
                    "buy_label": {
                      "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/buy_label"
                    },
                    "b13a_filing": {
                      "$ref": "#/components/schemas/Shipment/properties/shipping_settings/properties/b13a_filing"
                    },
                    "printing_options": {
                      "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/printing_options"
                    }
                  }
                },
                "parcels": {
                  "type": "array",
                  "minItems": 1,
                  "items": {
                    "type": "object",
                    "description": "Parcel",
                    "additionalProperties": false,
                    "properties": {
                      "total_actual_weight": {
                        "$ref": "#/components/schemas/ParcelCreate/properties/total_actual_weight"
                      },
                      "box": {
                        "$ref": "#/components/schemas/ParcelCreate/properties/box"
                      },
                      "items": {
                        "type": "array",
                        "minItems": 1,
                        "maxItems": 200,
                        "description": "Array of all shipment items",
                        "items": {
                          "type": "object",
                          "description": "Shipment Item based on Product",
                          "additionalProperties": false,
                          "required": [
                            "product"
                          ],
                          "properties": {
                            "product": {
                              "$ref": "#/components/schemas/ParcelProductItemCreate/properties/product"
                            },
                            "description": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/description"
                            },
                            "hs_code": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/hs_code"
                            },
                            "category": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/category"
                            },
                            "quantity": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/quantity"
                            },
                            "declared_currency": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_currency"
                            },
                            "declared_customs_value": {
                              "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_customs_value"
                            }
                          }
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
      "Shipment": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "type": "string",
            "pattern": "^ES\\w{2}\\d{7,}$",
            "description": "Readable identifier prefixed with ES (Easyship) and destination country code"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was created in the Easyship system"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was most recently modified"
          },
          "label_paid_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When Easyship was paid for the shipment"
          },
          "label_generated_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When label was generated"
          },
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin address"
              }
            ]
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender address"
              }
            ]
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return address"
              }
            ]
          },
          "destination_address": {
            "$ref": "#/components/schemas/DestinationAddress"
          },
          "order_data": {
            "type": "object",
            "description": "Free-form data related to the eCommerce platform",
            "additionalProperties": false,
            "properties": {
              "platform_name": {
                "type": "string",
                "nullable": true,
                "description": "A display-ready sales channel or platform name",
                "maximum": 200
              },
              "platform_order_number": {
                "type": "string",
                "nullable": true,
                "description": "Order number that was either copied from an order synced from an ecommerce platform or manually edited in Easyship's order from",
                "maximum": 200
              },
              "order_created_at": {
                "type": "string",
                "nullable": true,
                "format": "date-time",
                "description": "When the order was created (e.g. in an online store connected to Easyship)"
              },
              "order_tag_list": {
                "type": "array",
                "description": "Tags that have been assigned to this shipment, either as an order on its e-commerce store or within the Easyship app",
                "items": {
                  "type": "string"
                },
                "maxItems": 500
              },
              "seller_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the merchant. Will not be shown to the receiver."
              },
              "buyer_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the buyer during order checkout. Will be displayed on the packing slip."
              },
              "buyer_selected_courier_name": {
                "type": "string",
                "nullable": true,
                "description": "Courier name for shipping rule condition `match_buyer_selected_courier_name`. If the name matches, actions of this shipping rule would apply to the current shipment."
              }
            }
          },
          "last_failure_http_response_messages": {
            "type": "array",
            "description": "This attribute stores the HTTP response of the most recent unsuccessful attempt to interact with an external service, such as a failed label creation.",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "code": {
                  "type": "string",
                  "nullable": true
                },
                "content": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          },
          "metadata": {
            "type": "object",
            "description": "Set of key-value pairs that you can attach to a shipment. This can be useful for storing additional information about the object in a structured format"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "Indicates whether or not the user believes the receiver address qualifies for a residential surcharge."
          },
          "consignee_tax_id": {
            "type": "string",
            "nullable": true,
            "description": "Tax ID for the receiver. Maybe helpful or required for customs clearance, depending on the destination country."
          },
          "eei_reference": {
            "type": "string",
            "nullable": true,
            "description": "References data (Electronic Export Information) filed through one of the systems for goods shipped from the U.S.\nto a foreign country. Currently only used for FedEx shipments. The following possibilities may or may not qualify:\n  * An Automated Export System (AES) citation\n  * A Foreign Trade Regulations (FTR) exemption number\n  * An International Traffic in Arms Reduction (ITAR) exemption code\n  * A US Department of Commerce export license number"
          },
          "regulatory_identifiers": {
            "type": "object",
            "description": "Seller's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "eori": {
                "type": "string",
                "nullable": true,
                "description": "Economic Operators Registration and Identification (EORI) number."
              },
              "ioss": {
                "type": "string",
                "nullable": true,
                "description": "Import One Stop Shop (IOSS) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              }
            }
          },
          "buyer_regulatory_identifiers": {
            "type": "object",
            "description": "Buyer's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "ein": {
                "type": "string",
                "nullable": true,
                "description": "Employer Identification Number (EIN) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              },
              "ssn": {
                "type": "string",
                "nullable": true,
                "description": "Social Security Number (SSN) number."
              }
            }
          },
          "return": {
            "type": "boolean",
            "description": "Whether the shipment is a return shipment or not"
          },
          "incoterms": {
            "description": "Terms of Sale\nDDP: Seller pays all import duties/taxes.\nDDU: Buyer pays all import duties/taxes.\nnull: No incoterm specified; defaults to DDU.\n",
            "type": "string",
            "enum": [
              "DDU",
              "DDP",
              null
            ],
            "default": "DDU",
            "nullable": true
          },
          "insurance": {
            "type": "object",
            "description": "Insurance",
            "nullable": true,
            "additionalProperties": false,
            "properties": {
              "is_insured": {
                "type": "boolean",
                "description": "Indicates if premium insurance has been purchased for this shipment (either by the merchant or buyer).\nBasic, courier-supplied coverage is not applicable.",
                "default": false
              },
              "insured_amount": {
                "type": "number",
                "description": "Amount to insure with Easyship's insurance provider. If not specified, we'll use the sum of customs values and shipping cost."
              },
              "insured_currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "Insurance currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). If not specified, we will use the currency of the account country."
                  }
                ]
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/Parcel"
            }
          },
          "total_customs_value": {
            "type": "number",
            "minimum": 0,
            "description": "Sum of the value assigned to all shipment line items"
          },
          "total_actual_weight": {
            "type": "number",
            "description": "Sum of the specified weights of all *parcels* in the shipment (`parcel.actual_weight`), as measured on a scale in units specified by `company.weight_unit`."
          },
          "shipment_state": {
            "type": "string",
            "description": "The state of the shipment record within the Easyship system",
            "default": "created",
            "nullable": false,
            "enum": [
              "created",
              "draft",
              "calculating",
              "cancelling",
              "cancelled",
              "discarded",
              "deleted"
            ]
          },
          "pickup_state": {
            "type": "string",
            "default": "not_requested",
            "nullable": false,
            "description": "The state of the hand-over from shipper to courier. `pending_handover` applies only to eFulfillment companies."
          },
          "delivery_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the hand-over from courier to receiver.",
            "enum": [
              "not_created",
              "pending",
              "info_received",
              "in_transit_to_customer",
              "out_for_delivery",
              "delivered",
              "failed_attempt",
              "exception",
              "expired",
              "lost_by_courier",
              "returned_to_shipper"
            ]
          },
          "label_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the label(s) meant to be printed and attached to this shipment's parcels",
            "enum": [
              "not_created",
              "pending",
              "generating",
              "generated",
              "printed",
              "failed",
              "technical_failed",
              "reported",
              "voided",
              "void_failed"
            ]
          },
          "warehouse_state": {
            "type": "string",
            "default": "none",
            "nullable": false,
            "description": "The state of the fulfillment process within the warehouse",
            "enum": [
              "none",
              "pending",
              "created",
              "failed",
              "packed",
              "cancelled",
              "cancelled_no_stock",
              "backorder_no_stock",
              "shipped",
              "returned",
              "awaiting_dispatch"
            ]
          },
          "warehouse_code": {
            "type": "string",
            "description": "Warehouse code (warehouse/eFulfilment only)"
          },
          "original_easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "trackings": {
            "type": "array",
            "description": "Sources of tracking data for this shipment",
            "items": {
              "$ref": "#/components/schemas/ShipmentTracking"
            }
          },
          "tracking_page_url": {
            "type": "string",
            "description": "Tracking page URL"
          },
          "shipping_documents": {
            "type": "array",
            "description": "Shipping documents",
            "items": {
              "$ref": "#/components/schemas/ShipmentDocument"
            }
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "courier_service": {
            "type": "object",
            "nullable": true,
            "description": "Selected courier service for this shipment. May be null if no service has been selected yet, or if the shipment was created without selecting a service.\nMore information about the [courier service](https://developers.easyship.com/reference/courier_services_index)",
            "additionalProperties": false,
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              },
              "name": {
                "type": "string"
              },
              "courier_id": {
                "type": "string",
                "format": "uuid",
                "description": "The courier ID that the current courier service is associated with"
              },
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service."
              },
              "easyship_courier_service": {
                "$ref": "#/components/schemas/CourierService/properties/easyship_courier_service"
              }
            }
          },
          "rates": {
            "type": "array",
            "description": "Array of available courier services for this shipment, along with the rates charged. Courier services are excluded if the shipment's contents or destination do not meet each service's eligibility requirements.",
            "items": {
              "$ref": "#/components/schemas/Rate"
            }
          },
          "shipping_settings": {
            "type": "object",
            "description": "Shipping settings",
            "additionalProperties": false,
            "properties": {
              "b13a_filing": {
                "type": "object",
                "description": "B13A filing (currently available only for FedEx)",
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                  "option": {
                    "type": "string",
                    "enum": [
                      "not_required",
                      "fedex_to_stamp",
                      "filed_electronically",
                      "manually_attached",
                      "summary_reporting"
                    ]
                  },
                  "option_export_compliance_statement": {
                    "type": "string",
                    "nullable": true,
                    "description": "Export compliance statement"
                  },
                  "permit_number": {
                    "type": "string",
                    "nullable": true,
                    "description": "Permit number"
                  }
                }
              },
              "label_customization_fields": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/label_customization_fields"
                  },
                  {
                    "type": "array",
                    "minItems": 0
                  }
                ]
              }
            }
          }
        }
      },
      "ShipmentCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "parcels"
        ],
        "properties": {
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin Address",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "origin_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of origin address. Required if the `origin_address` object is not provided. If provided, the origin address will be ignored."
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender Address. Only applies if the courier allows a different address to be displayed on the label. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "sender_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of sender address. Required if the `sender_address` object is not provided."
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return Address. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "return_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of return address. Required if the `return_address` object is not provided."
          },
          "destination_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DestinationAddress"
              },
              {
                "required": [
                  "line_1",
                  "city",
                  "contact_name",
                  "contact_email",
                  "contact_phone"
                ]
              }
            ]
          },
          "return": {
            "type": "boolean",
            "description": "Set the shipment as a return shipment"
          },
          "metadata": {
            "$ref": "#/components/schemas/Shipment/properties/metadata"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "US addresses will be automatically validated when not specified. If specified, the validation will be bypassed."
          },
          "consignee_tax_id": {
            "type": "string",
            "description": "The consignee's tax identification number or EIN. This is required for customs clearance when shipping to certain countries, such as China and Brazil."
          },
          "eei_reference": {
            "type": "string",
            "description": "The Electronic Export Identifier (EEI). This is required when shipping goods over USD2500 in value (Applies to US-outbound shipments only)."
          },
          "regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/regulatory_identifiers"
          },
          "buyer_regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/buyer_regulatory_identifiers"
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "insurance": {
            "$ref": "#/components/schemas/Shipment/properties/insurance"
          },
          "order_data": {
            "$ref": "#/components/schemas/Shipment/properties/order_data"
          },
          "courier_settings": {
            "type": "object",
            "properties": {
              "courier_service_id": {
                "type": "string",
                "description": "Select a specific courier service to create the shipment with, only the rate for this courier service will be returned. If provided, all other courier service lookup parameters (`courier_umbrella`, `courier_service_name`, `courier_account_number`) will be ignored.",
                "nullable": true
              },
              "courier_umbrella": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The umbrella name of the courier service (e.g., \"FedEx\"). This field is optional; however, if provided, `courier_service_name` and `courier_account_number` must also be included."
              },
              "courier_service_name": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The official name of the courier service (e.g., \"FedEx International Priority®\"). This field is optional; however, if provided, `courier_umbrella` and `courier_account_number` must also be included."
              },
              "courier_account_number": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The account number of the courier account. This field is optional; however, if provided, `courier_umbrella` and `courier_service_name` must also be included."
              },
              "allow_fallback": {
                "type": "boolean",
                "default": false,
                "description": "If `courier_service_id` is provided but the courier can’t be selected, allow the shipment to be created and the next best rate to be selected. Default: `false`. When false and rates for the `courier_service_id` can't be found, an error will be raised and the shipment won’t be created."
              },
              "apply_shipping_rules": {
                "type": "boolean",
                "default": true,
                "description": "Apply any [shipping rules](https://support.easyship.com/hc/en-us/articles/115003580152-Automate-Shipping-Process-Shipping-Rules) created on the Easyship dashboard (Default: `true`)"
              },
              "list_unavailable_services": {
                "type": "boolean",
                "description": "Setting this option will return detailed information with reasons for each courier in the response."
              }
            }
          },
          "shipping_settings": {
            "type": "object",
            "properties": {
              "additional_services": {
                "type": "object",
                "description": "Configuration for additional services",
                "additionalProperties": false,
                "properties": {
                  "delivery_confirmation": {
                    "description": "Currently officially supported only for selected customers. **Subject to change.**",
                    "type": "string",
                    "enum": [
                      "ups_delivery_confirmation_adult_signature_required",
                      "ups_delivery_confirmation_signature_required",
                      "dpd_uk_signature_required",
                      "dpd_uk_proof_of_identity",
                      "dpd_uk_proof_of_age",
                      "dpd_uk_pin_required"
                    ]
                  },
                  "qr_code": {
                    "type": "string",
                    "description": "Generate QR code when generating label. If a courier does not support it, label will be generated without the QR code. Currently officially supported only for USPS courier. When set to `qr_code`, both the QR code and the original label are returned. `qr_code_with_label` is deprecated and no longer supported; if provided, it silently falls back to `qr_code`. Label customization is not available for USPS. **Subject to change.**",
                    "default": "none",
                    "enum": [
                      "qr_code",
                      "qr_code_with_label",
                      "none"
                    ]
                  }
                }
              },
              "units": {
                "$ref": "#/components/schemas/Units"
              },
              "buy_label": {
                "type": "boolean",
                "default": false,
                "description": "Create a shipment and buy the label in a single API call instead of two. Default: `false`."
              },
              "buy_label_synchronous": {
                "type": "boolean",
                "default": false,
                "description": "Generate a label synchronously. Returns a label in the response. Default: `false`."
              },
              "b13a_filing": {
                "$ref": "#/components/schemas/Shipment/properties/shipping_settings/properties/b13a_filing"
              },
              "printing_options": {
                "type": "object",
                "description": "Specify the format and page sizes of the shipping documents. This will only be taken into account if buy_label_synchronous is `true`.",
                "properties": {
                  "format": {
                    "type": "string",
                    "description": "Options: `png`, `pdf`, `url`, `zpl` (Default: `png`)",
                    "default": "png",
                    "enum": [
                      "png",
                      "pdf",
                      "url",
                      "zpl"
                    ]
                  },
                  "label": {
                    "type": "string",
                    "description": "Label page size. Options: `4x6` / `A4` / `A5` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "A5"
                    ]
                  },
                  "commercial_invoice": {
                    "type": "string",
                    "description": "Commercial invoice page size. Options: `4x6` / `A4` (Default: `A4`)",
                    "default": "A4",
                    "enum": [
                      "4x6",
                      "A4"
                    ]
                  },
                  "packing_slip": {
                    "type": "string",
                    "description": "Packing slip page size. Options: `4x6` / `A4` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "none"
                    ]
                  },
                  "remarks": {
                    "type": "string",
                    "maxLength": 70,
                    "description": "Customized commercial invoice remarks for current shipment. It has higher priority than remarks from company settings."
                  }
                }
              },
              "label_customization_fields": {
                "description": "Label customization fields for the shipment. This is only applicable for specific couriers. For detailed explanation, please refer to [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "required": [
                    "value"
                  ],
                  "properties": {
                    "code": {
                      "description": "Courier accepted code, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                      "type": "string"
                    },
                    "value": {
                      "type": "string",
                      "description": "Content to display on the label, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    },
                    "convert_to_barcode": {
                      "description": "Identifying for converting value to barcode, specific application logic applies. See [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    }
                  }
                }
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/ParcelCreate"
            }
          }
        }
      },
      "ParcelCreate": {
        "type": "object",
        "description": "Parcel",
        "additionalProperties": false,
        "properties": {
          "total_actual_weight": {
            "type": "number",
            "description": "Total weight of the shipment, including the box weight. If you provide the total weight of the shipment, then the weight for items can be optional."
          },
          "box": {
            "type": "object",
            "nullable": true,
            "description": "The box dimensions for the shipment. If the box dimensions are provided, then dimensions for items are optional.",
            "additionalProperties": false,
            "properties": {
              "slug": {
                "type": "string",
                "nullable": true,
                "description": "Courier or Custom Box Slug. Use the [Boxes API](https://developers.easyship.com/reference/boxes_index) to retrieve a list of available boxes."
              },
              "length": {
                "type": "number",
                "description": "Length of the box"
              },
              "width": {
                "type": "number",
                "description": "Width of the box"
              },
              "height": {
                "type": "number",
                "description": "Height of the box"
              }
            }
          },
          "items": {
            "type": "array",
            "description": "Array of all shipment items",
            "items": {
              "anyOf": [
                {
                  "$ref": "#/components/schemas/ParcelItemCreate"
                },
                {
                  "$ref": "#/components/schemas/ParcelProductItemCreate"
                },
                {
                  "$ref": "#/components/schemas/ParcelReturnItemCreate"
                }
              ]
            },
            "minItems": 1,
            "maxItems": 200
          }
        }
      },
      "ParcelItemCreate": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "required": [
          "description",
          "declared_currency",
          "declared_customs_value"
        ],
        "properties": {
          "description": {
            "type": "string",
            "description": "Description of the item",
            "maximum": 200
          },
          "category": {
            "type": "string",
            "nullable": true,
            "description": "Item category name or slug. Required if hs_code is not provided. Use the [Item Categories API](https://developers.easyship.com/reference/item_categories_index) to retrieve a list of available item categories.",
            "maximum": 200
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item. Required if category is not provided."
          },
          "sku": {
            "type": "string",
            "description": "Item Stock Keeping Unit (SKU) as listed in your store.",
            "maximum": 100
          },
          "platform_product_id": {
            "$ref": "#/components/schemas/ParcelItem/properties/platform_product_id"
          },
          "manufacturer_part_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/manufacturer_part_number"
          },
          "global_trade_item_number": {
            "$ref": "#/components/schemas/ParcelItem/properties/global_trade_item_number"
          },
          "contains_battery_pi966": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi966"
          },
          "contains_battery_pi967": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_battery_pi967"
          },
          "contains_liquids": {
            "$ref": "#/components/schemas/ParcelItem/properties/contains_liquids"
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2Nullable"
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          },
          "dimensions": {
            "type": "object",
            "description": "Dimensions of the item",
            "additionalProperties": false,
            "properties": {
              "length": {
                "type": "number",
                "description": "Item length; Optional if the Box dimensions are provided."
              },
              "width": {
                "type": "number",
                "description": "Item width; Optional if the Box dimensions are provided."
              },
              "height": {
                "type": "number",
                "description": "Item height; Optional if the Box dimensions are provided."
              }
            }
          },
          "actual_weight": {
            "type": "number",
            "description": "Item actual weight in `kg`. Must be greater than 0.\nOptional when `total_actual_weight` is provided.\n**Required when the shipping rule action `split_parcels_by_sku` is enabled, regardless of the existence of `total_actual_weight`**\n"
          },
          "declared_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Item currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "declared_customs_value": {
            "type": "number",
            "description": "Item customs value, must be greater than 0 unless category is `documents`. Please note that this value refers to the unit rather than the total."
          }
        }
      },
      "ParcelProductItemCreate": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "properties": {
          "product": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid",
                "description": "Product ID. Required if the `sku` is not provided."
              },
              "sku": {
                "type": "string",
                "description": "Product SKU. Required if the `id` is not provided."
              }
            }
          },
          "quantity": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/quantity"
          },
          "declared_currency": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_currency"
          },
          "declared_customs_value": {
            "$ref": "#/components/schemas/ParcelItemCreate/properties/declared_customs_value"
          }
        }
      },
      "Units": {
        "type": "object",
        "description": "Units",
        "additionalProperties": false,
        "properties": {
          "weight": {
            "type": "string",
            "description": "Unit of weight values provided. Options: `kg` / `g` / `lb` / `oz` (Default: `kg`). Unit of values in the response will be in `kg`.",
            "default": "kg",
            "enum": [
              "kg",
              "g",
              "lb",
              "oz"
            ]
          },
          "dimensions": {
            "type": "string",
            "description": "Unit of dimension values provided. Options: `cm` / `in` (Default: `cm`) Unit of values in the response will be in `cm`.",
            "default": "cm",
            "enum": [
              "cm",
              "in"
            ]
          }
        }
      }
    }
  }
}
```