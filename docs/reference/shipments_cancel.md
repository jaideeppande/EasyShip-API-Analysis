# Cancel a Shipment

Cancel a shipment after a label has been requested, as long as the shipment is not yet in transit.

Required authorization scope: `public.shipment:write`

> **Cancel vs Delete:** Use **Delete** to remove a shipment before a label has been requested (`label_state: not_created`). Use **Cancel** after a label has been requested, as long as the shipment is not yet in transit.

**When can you cancel?**

The shipment's `label_state` must be one of: `pending`, `generated`, `printed`, `shipping_document_generated`, `failed`, `technical_failed`, or `reported`.

The shipment's `delivery_state` must be pre-transit: `not_created`, `pending`, `info_received`, or `expired`.

**When can you NOT cancel?**

- `label_state: generating` — the label is actively being generated; wait until it resolves to `generated` or `failed` before retrying
- `label_state: voided` or `void_failed` — the label has already been voided; the shipment cannot be cancelled via this endpoint
- `delivery_state` is `in_transit_to_customer`, `out_for_delivery`, `delivered`, or similar — the shipment has left the origin facility
- The label was generated more than **6 months ago** (pre-paid shipments only)


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
      "name": "Shipments"
    }
  ],
  "paths": {
    "/2024-09/shipments/{easyship_shipment_id}/cancel": {
      "post": {
        "summary": "Cancel a Shipment",
        "tags": [
          "Shipments"
        ],
        "operationId": "shipments_cancel",
        "description": "Cancel a shipment after a label has been requested, as long as the shipment is not yet in transit.\n\nRequired authorization scope: `public.shipment:write`\n\n> **Cancel vs Delete:** Use **Delete** to remove a shipment before a label has been requested (`label_state: not_created`). Use **Cancel** after a label has been requested, as long as the shipment is not yet in transit.\n\n**When can you cancel?**\n\nThe shipment's `label_state` must be one of: `pending`, `generated`, `printed`, `shipping_document_generated`, `failed`, `technical_failed`, or `reported`.\n\nThe shipment's `delivery_state` must be pre-transit: `not_created`, `pending`, `info_received`, or `expired`.\n\n**When can you NOT cancel?**\n\n- `label_state: generating` — the label is actively being generated; wait until it resolves to `generated` or `failed` before retrying\n- `label_state: voided` or `void_failed` — the label has already been voided; the shipment cannot be cancelled via this endpoint\n- `delivery_state` is `in_transit_to_customer`, `out_for_delivery`, `delivered`, or similar — the shipment has left the origin facility\n- The label was generated more than **6 months ago** (pre-paid shipments only)\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "easyship_shipment_id",
            "in": "path",
            "required": true,
            "description": "Easyship Shipment ID provided when creating the shipment",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "shipment successfully canceled",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "success": {
                        "message": "Shipment successfully cancelled"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "shipment successfully canceled"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Success"
                }
              }
            }
          },
          "404": {
            "description": "record not found",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "resource_not_found",
                        "details": [
                          "The Shipment was not found"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Cancel a Shipment",
                            "url": "https://developers.easyship.com/reference/shipments_cancel"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Automate your Shipments",
                            "url": "https://developers.easyship.com/docs/how-to-automate-your-shipments"
                          }
                        ],
                        "message": "The requested resource was not found.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "record not found"
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
                          "This Shipment cannot be cancelled. Please contact our support."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Cancel a Shipment",
                            "url": "https://developers.easyship.com/reference/shipments_cancel"
                          },
                          {
                            "kind": "how-to-guide",
                            "name": "How to Automate your Shipments",
                            "url": "https://developers.easyship.com/docs/how-to-automate-your-shipments"
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
      "Success": {
        "type": "object",
        "description": "General success response",
        "additionalProperties": false,
        "properties": {
          "success": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "message": {
                "type": "string"
              }
            }
          },
          "meta": {
            "$ref": "#/components/schemas/Meta"
          }
        }
      }
    }
  }
}
```