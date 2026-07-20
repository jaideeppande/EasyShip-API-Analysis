# List all LYOC

LYOC (Link Your Own Courier) allows merchants to connect their existing courier accounts — such as DHL, UPS, FedEx, or Royal Mail — to Easyship, enabling shipments to be rated and labeled using their own negotiated rates.

Use this endpoint to discover which couriers can be linked for a given country and the supported methods of connection. Each result includes a `creation` object that indicates how the courier can be linked for that country: `creation.api: true` means you can link programmatically via `POST /2024-09/courier_accounts`; `creation.ui: true` means linking is available through the Easyship Dashboard; `creation.contact: true` means you need to contact Easyship sales to arrange linkage.

Filter by `country_alpha2` (ISO 3166-1 Alpha-2, e.g. `GB`) or `country_id`. Both are optional — omitting both returns all available LYOC couriers. If both are provided, `country_id` takes precedence.

Required authorization scope: `public.courier:read`


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
    "/2024-09/couriers/lyoc": {
      "get": {
        "summary": "List all LYOC",
        "tags": [
          "Couriers"
        ],
        "operationId": "courier_lyoc_index",
        "description": "LYOC (Link Your Own Courier) allows merchants to connect their existing courier accounts — such as DHL, UPS, FedEx, or Royal Mail — to Easyship, enabling shipments to be rated and labeled using their own negotiated rates.\n\nUse this endpoint to discover which couriers can be linked for a given country and the supported methods of connection. Each result includes a `creation` object that indicates how the courier can be linked for that country: `creation.api: true` means you can link programmatically via `POST /2024-09/courier_accounts`; `creation.ui: true` means linking is available through the Easyship Dashboard; `creation.contact: true` means you need to contact Easyship sales to arrange linkage.\n\nFilter by `country_alpha2` (ISO 3166-1 Alpha-2, e.g. `GB`) or `country_id`. Both are optional — omitting both returns all available LYOC couriers. If both are provided, `country_id` takes precedence.\n\nRequired authorization scope: `public.courier:read`\n",
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
            "schema": {
              "type": "string"
            },
            "required": false,
            "description": "Filter records by country code: Alpha-2 format (ISO 3166-1).",
            "example": "CA"
          },
          {
            "name": "country_id",
            "in": "query",
            "schema": {
              "type": "string"
            },
            "required": false,
            "description": "Filter records by country ID.",
            "example": "103"
          }
        ],
        "responses": {
          "200": {
            "description": "list of LYOC for a specific country",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "couriers": [
                        {
                          "key": "dhl",
                          "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/dhl.png",
                          "name": "DHL",
                          "supported_countries": [
                            {
                              "id": 78,
                              "alpha2": "GB",
                              "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                              "creation": {
                                "contact": false,
                                "ui": true,
                                "api": true
                              }
                            }
                          ]
                        },
                        {
                          "key": "ups",
                          "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/ups.png",
                          "name": "UPS",
                          "supported_countries": [
                            {
                              "id": 78,
                              "alpha2": "GB",
                              "courier_id": null,
                              "creation": {
                                "contact": false,
                                "ui": true,
                                "api": false
                              }
                            }
                          ]
                        },
                        {
                          "key": "fedex",
                          "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/fedex.png",
                          "name": "FedEx",
                          "supported_countries": [
                            {
                              "id": 78,
                              "alpha2": "GB",
                              "courier_id": null,
                              "creation": {
                                "contact": false,
                                "ui": true,
                                "api": false
                              }
                            }
                          ]
                        },
                        {
                          "key": "royal-mail",
                          "logo_url": "https://storage.googleapis.com/easyship-assets/website/courier-logos/color-img/royal-mail.png",
                          "name": "Royal Mail",
                          "supported_countries": [
                            {
                              "id": 78,
                              "alpha2": "GB",
                              "courier_id": null,
                              "creation": {
                                "contact": false,
                                "ui": true,
                                "api": true
                              }
                            }
                          ]
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 4
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of LYOC for a specific country"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/lyoc_list"
                }
              }
            }
          },
          "404": {
            "description": "country not found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Country was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "country not found"
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
      "lyoc_list": {
        "type": "object",
        "description": "List of LYOCs",
        "additionalProperties": false,
        "properties": {
          "couriers": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LYOC"
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
      "LYOC": {
        "type": "object",
        "description": "A courier available for LYOC (Link Your Own Courier) — a carrier that merchants can connect to Easyship using their own account credentials and negotiated rates.",
        "additionalProperties": false,
        "properties": {
          "key": {
            "type": "string",
            "description": "Unique machine-readable identifier for the courier type (e.g. `dhl`, `ups`, `fedex`, `royal-mail`)."
          },
          "name": {
            "type": "string",
            "description": "Human-readable display name of the courier (e.g. `DHL`, `UPS`, `FedEx`)."
          },
          "logo_url": {
            "type": "string",
            "description": "URL of the Courier logo."
          },
          "supported_countries": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "id": {
                  "type": "number",
                  "description": "Easyship internal country ID."
                },
                "alpha2": {
                  "type": "string",
                  "description": "Country code in ISO 3166-1 Alpha-2 format (e.g. `GB`, `US`, `SG`)."
                },
                "creation": {
                  "type": "object",
                  "additionalProperties": false,
                  "description": "How the courier can be created for the country.",
                  "properties": {
                    "contact": {
                      "type": "boolean",
                      "description": "Contacting Easyship sales representative."
                    },
                    "ui": {
                      "type": "boolean",
                      "description": "Easyship UI (Dashboard or LYOC application)."
                    },
                    "api": {
                      "type": "boolean",
                      "description": "Easyship Public API."
                    }
                  }
                },
                "courier_id": {
                  "type": "string",
                  "description": "The courier account ID of an already-linked account for this country. Non-null indicates an account has been connected via LYOC and can be referenced in other API calls (e.g. `POST /2024-09/manifests`). `null` means no account has been linked yet for this country — use `creation` to determine how to proceed.",
                  "nullable": true
                }
              }
            }
          }
        }
      }
    }
  }
}
```