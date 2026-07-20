# Create a Redirect

Create a redirect to the Easyship Dashboard.

Required authorization scope: `public.redirect:write`


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
  "paths": {
    "/2024-09/account/redirects": {
      "post": {
        "summary": "Create a Redirect",
        "tags": [
          "Redirects"
        ],
        "operationId": "redirects_create",
        "description": "Create a redirect to the Easyship Dashboard.\n\nRequired authorization scope: `public.redirect:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "redirect to UPS DAP",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "redirect": {
                        "expires_at": "2022-02-22T12:21:30Z",
                        "url": "/redirect?jwt=eyJhbGciOiJIUzI1NiJ9.eyJzZXNzaW9uX2lkIjoic2Vzc2lvbl9pZCIsInJlZGlyZWN0X3VybCI6Imh0dHA6Ly9sb2NhbGhvc3Q6OTAwMC9kYXNoYm9hcmQiLCJleHAiOjE2OTg3NTcwMjF9.dFHwtbnUgjQgRM7hzmQqbic3a2DpNc64NcrqsryCW2g"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "redirect to UPS DAP"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/redirect_single"
                }
              }
            }
          },
          "422": {
            "description": "missing redirect_back_url",
            "content": {
              "application/json": {
                "examples": {
                  "missing_value": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Value is missing or invalid (Easyship Shipment ID was not found)"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create a Redirect",
                            "url": "https://developers.easyship.com/reference/redirects_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "missing value"
                  },
                  "missing_redirect_back_url": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "#/components/schemas/RedirectUPSDAPCreate missing required parameters: country, redirect_back_url"
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
                    "summary": "missing redirect_back_url"
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
                "$ref": "#/components/schemas/RedirectCreate"
              },
              "examples": {
                "redirect_with_target_only": {
                  "summary": "with target only",
                  "value": {
                    "target": "shipments_all"
                  }
                },
                "redirect_with_target_and_value": {
                  "summary": "with target and value",
                  "value": {
                    "target": "shipment",
                    "value": "ESGB171617963"
                  }
                },
                "redirect_to_ups_dap": {
                  "summary": "with UPS DAP",
                  "value": {
                    "target": "ups_dap",
                    "redirect_back_url": "https://easyship.com",
                    "country": "US"
                  }
                },
                "missing_value": {
                  "summary": "missing value",
                  "value": {
                    "target": "shipment",
                    "value": ""
                  }
                },
                "missing_redirect_back_url": {
                  "summary": "missing redirect_back_url",
                  "value": {
                    "target": "ups_dap"
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
      "redirect_single": {
        "type": "object",
        "description": "Redirect Detail",
        "additionalProperties": false,
        "properties": {
          "redirect": {
            "$ref": "#/components/schemas/Redirect"
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
      "Redirect": {
        "type": "object",
        "description": "Redirect Detail",
        "additionalProperties": false,
        "properties": {
          "url": {
            "type": "string",
            "format": "uri",
            "description": "The URL that the user should be redirected to."
          },
          "expires_at": {
            "type": "string",
            "format": "date-time",
            "description": "The date and time that the redirect will expire."
          }
        }
      },
      "RedirectCreate": {
        "oneOf": [
          {
            "$ref": "#/components/schemas/RedirectBaseCreate"
          },
          {
            "$ref": "#/components/schemas/RedirectWithShipmentIDCreate"
          },
          {
            "$ref": "#/components/schemas/RedirectUPSDAPCreate"
          }
        ],
        "discriminator": {
          "propertyName": "target",
          "mapping": {
            "account_addresses": "#/components/schemas/RedirectBaseCreate",
            "account_billing": "#/components/schemas/RedirectBaseCreate",
            "account_company": "#/components/schemas/RedirectBaseCreate",
            "account_payment_methods": "#/components/schemas/RedirectBaseCreate",
            "account_profile": "#/components/schemas/RedirectBaseCreate",
            "account_subscription": "#/components/schemas/RedirectBaseCreate",
            "account_team": "#/components/schemas/RedirectBaseCreate",
            "analytics": "#/components/schemas/RedirectBaseCreate",
            "connect": "#/components/schemas/RedirectBaseCreate",
            "couriers": "#/components/schemas/RedirectBaseCreate",
            "help": "#/components/schemas/RedirectBaseCreate",
            "pickups": "#/components/schemas/RedirectBaseCreate",
            "products": "#/components/schemas/RedirectBaseCreate",
            "settings_boxes": "#/components/schemas/RedirectBaseCreate",
            "settings_email": "#/components/schemas/RedirectBaseCreate",
            "settings_insurance": "#/components/schemas/RedirectBaseCreate",
            "settings_notifications": "#/components/schemas/RedirectBaseCreate",
            "settings_packing_slip": "#/components/schemas/RedirectBaseCreate",
            "settings_printing_options": "#/components/schemas/RedirectBaseCreate",
            "settings_tracking_page": "#/components/schemas/RedirectBaseCreate",
            "shipment_create": "#/components/schemas/RedirectBaseCreate",
            "shipment_create_advanced": "#/components/schemas/RedirectBaseCreate",
            "shipments_all": "#/components/schemas/RedirectBaseCreate",
            "shipments_pending": "#/components/schemas/RedirectBaseCreate",
            "shipments_rejected": "#/components/schemas/RedirectBaseCreate",
            "shipments_to_print": "#/components/schemas/RedirectBaseCreate",
            "shipping_rules": "#/components/schemas/RedirectBaseCreate",
            "webhooks": "#/components/schemas/RedirectBaseCreate",
            "ups_dap": "#/components/schemas/RedirectUPSDAPCreate",
            "shipment": "#/components/schemas/RedirectWithShipmentIDCreate",
            "shipment_order": "#/components/schemas/RedirectWithShipmentIDCreate"
          }
        }
      },
      "RedirectBaseCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "target"
        ],
        "properties": {
          "target": {
            "type": "string",
            "description": "The target of the redirect.",
            "enum": [
              "account_addresses",
              "account_billing",
              "account_company",
              "account_payment_methods",
              "account_profile",
              "account_subscription",
              "account_team",
              "analytics",
              "connect",
              "couriers",
              "help",
              "pickups",
              "products",
              "settings_boxes",
              "settings_email",
              "settings_insurance",
              "settings_notifications",
              "settings_packing_slip",
              "settings_printing_options",
              "settings_tracking_page",
              "shipment_create",
              "shipment_create_advanced",
              "shipments_all",
              "shipments_pending",
              "shipments_rejected",
              "shipments_to_print",
              "shipping_rules",
              "webhooks"
            ]
          }
        }
      },
      "RedirectWithShipmentIDCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "target",
          "value"
        ],
        "properties": {
          "target": {
            "type": "string",
            "description": "The target of the redirect.",
            "enum": [
              "shipment",
              "shipment_order",
              "ups_dap"
            ]
          },
          "value": {
            "type": "string",
            "description": "Easyship Shipment ID"
          }
        }
      },
      "RedirectUPSDAPCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "target",
          "country",
          "redirect_back_url"
        ],
        "properties": {
          "target": {
            "type": "string",
            "description": "The target of the redirect.",
            "enum": [
              "ups_dap"
            ]
          },
          "country": {
            "type": "string",
            "description": "Country Code in Alpha-2 format (ISO 3166-1)",
            "enum": [
              "US",
              "GB",
              "CA",
              "DE",
              "NL"
            ]
          },
          "redirect_back_url": {
            "type": "string",
            "format": "uri",
            "description": "Where to redirect back to after the target has been completed. A query param `ups_dap_status` will be added to the URL with the status of the UPS DAP (`accepted` or `cancelled`)."
          }
        }
      }
    }
  }
}
```