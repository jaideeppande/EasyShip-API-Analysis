# List Available Pickup Slots

Retrieve a list of pickup slots in local time for the coming seven days.

Required authorization scope: `public.pickup:read`


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
      "name": "Courier Services"
    }
  ],
  "paths": {
    "/2024-09/courier_services/{courier_service_id}/pickup_slots": {
      "get": {
        "summary": "List Available Pickup Slots",
        "tags": [
          "Courier Services"
        ],
        "operationId": "courier_services_pickup_slots_index",
        "description": "Retrieve a list of pickup slots in local time for the coming seven days.\n\nRequired authorization scope: `public.pickup:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "courier_service_id",
            "in": "path",
            "required": true,
            "description": "Courier Service ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "origin_address_id",
            "in": "query",
            "required": false,
            "description": "Origin Address ID",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "available pickup slots",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "courier_service_handover_option": {
                        "pickup_slots": [
                          {
                            "date": "2022-02-22",
                            "time_slots": []
                          },
                          {
                            "date": "2022-02-23",
                            "time_slots": [
                              {
                                "from_time": "12:00",
                                "time_slot_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                                "to_time": "16:00"
                              }
                            ]
                          },
                          {
                            "date": "2022-02-24",
                            "time_slots": []
                          },
                          {
                            "date": "2022-02-25",
                            "time_slots": []
                          },
                          {
                            "date": "2022-02-26",
                            "time_slots": []
                          },
                          {
                            "date": "2022-02-27",
                            "time_slots": []
                          },
                          {
                            "date": "2022-02-28",
                            "time_slots": []
                          },
                          {
                            "date": "2022-03-01",
                            "time_slots": []
                          }
                        ],
                        "provider_name": "USPS"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "available pickup slots"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/pickup_slot_list"
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
                          "Failed to retrieve the available Pickup Slots: Handover options are not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List Available Pickup Slots",
                            "url": "https://developers.easyship.com/reference/courier_services_pickup_slots_index"
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
          },
          "404": {
            "description": "pickup not supported by courier service",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "This Courier Service doesn't provide a pickup service. A list of drop-off points is available in the dropoff url: http://localhost:9000/dropoff/ninja_van"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List Available Pickup Slots",
                            "url": "https://developers.easyship.com/reference/courier_services_pickup_slots_index"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "pickup not supported by courier service"
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
      "pickup_slot_list": {
        "type": "object",
        "description": "List of Pickup Slots",
        "additionalProperties": false,
        "properties": {
          "courier_service_handover_option": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "provider_name": {
                "type": "string"
              },
              "pickup_slots": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/PickupSlot"
                }
              }
            }
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
      "PickupSlot": {
        "type": "object",
        "description": "Pickup slot",
        "additionalProperties": false,
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "time_slots": {
            "type": "array",
            "items": {
              "type": "object",
              "description": "Time slot",
              "additionalProperties": false,
              "properties": {
                "time_slot_id": {
                  "type": "string",
                  "format": "uuid"
                },
                "from_time": {
                  "type": "string"
                },
                "to_time": {
                  "type": "string"
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