# List Account Settings

Retrieve account settings.

Required authorization scope: `public.setting:read`


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
      "name": "Settings"
    }
  ],
  "paths": {
    "/2024-09/account/settings": {
      "get": {
        "summary": "List Account Settings",
        "tags": [
          "Settings"
        ],
        "operationId": "settings_index",
        "description": "Retrieve account settings.\n\nRequired authorization scope: `public.setting:read`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "responses": {
          "200": {
            "description": "settings successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "setting": {
                        "tracking_email": {
                          "advertising": null,
                          "allowed_statuses": null,
                          "button": {
                            "background_color": "#50D4A4",
                            "text_color": "#FFFFFF"
                          },
                          "display_options": {
                            "header": false,
                            "contact": false
                          },
                          "footnote": "Thanks for supporting our business - clearly, you have great taste!"
                        },
                        "tracking_page": {
                          "advertising": null,
                          "button": {
                            "background_color": "#50D4A4",
                            "text_color": "#FFFFFF"
                          },
                          "display_options": {
                            "header": true,
                            "estimated_delivery_time": true,
                            "status_icon": true,
                            "contact_courier": true,
                            "contact": true
                          },
                          "footnote": "Thanks for supporting our business - clearly, you have great taste!"
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "settings successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/setting_single"
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
      "setting_single": {
        "type": "object",
        "description": "Setting",
        "additionalProperties": false,
        "properties": {
          "setting": {
            "$ref": "#/components/schemas/Setting"
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
      "Setting": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "tracking_email": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "display_options": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "header": {
                    "type": "boolean",
                    "default": false,
                    "description": "Show the company logo in the tracking email. If this parameter is set to `true` but no logo is uploaded, the header will display the company name."
                  },
                  "contact": {
                    "type": "boolean",
                    "default": false,
                    "description": "Show the contact page with social media"
                  }
                }
              },
              "allowed_statuses": {
                "type": "array",
                "nullable": true,
                "maxItems": 5,
                "items": {
                  "type": "string",
                  "enum": [
                    "in_transit",
                    "out_for_delivery",
                    "unsuccessful_delivery_attempt",
                    "delivered",
                    "exception"
                  ]
                },
                "description": "Select a shipment status to trigger a tracking updates email"
              },
              "button": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "background_color": {
                    "type": "string",
                    "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                    "default": "#50D4A4",
                    "description": "Background color in HEX color code format"
                  },
                  "text_color": {
                    "type": "string",
                    "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                    "default": "#FFFFFF",
                    "description": "Text color in HEX color code format"
                  }
                }
              },
              "footnote": {
                "type": "string",
                "default": "Thanks for supporting our business - clearly, you have great taste!",
                "maxLength": 350
              },
              "advertising": {
                "type": "object",
                "nullable": true,
                "additionalProperties": false,
                "required": [
                  "title",
                  "url"
                ],
                "properties": {
                  "title": {
                    "type": "string",
                    "enum": [
                      "Call Now",
                      "Book Now",
                      "Buy Now",
                      "Contact Us",
                      "Learn More",
                      "See Offer",
                      "Sign Up",
                      "Shop Now",
                      "Use App",
                      "Visit Us",
                      "Leave a Review",
                      "Leave a Comment"
                    ],
                    "description": "Advertising button in the tracking email"
                  },
                  "url": {
                    "type": "string",
                    "format": "uri",
                    "description": "Link for the advertising button"
                  }
                }
              }
            }
          },
          "tracking_page": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "display_options": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "header": {
                    "type": "boolean",
                    "default": true,
                    "description": "Show the company logo in the tracking page. If this parameter is set to `true` but no logo is uploaded, the header will display the company name."
                  },
                  "estimated_delivery_time": {
                    "type": "boolean",
                    "default": true,
                    "description": "Show estimated delivery time"
                  },
                  "status_icon": {
                    "type": "boolean",
                    "default": true,
                    "description": "Show an animated icon with delivery status"
                  },
                  "contact_courier": {
                    "type": "boolean",
                    "default": true,
                    "description": "Show the link of courier's contact page"
                  },
                  "contact": {
                    "type": "boolean",
                    "default": true,
                    "description": "Show the contact page with social media"
                  }
                }
              },
              "button": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "background_color": {
                    "type": "string",
                    "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                    "default": "#50D4A4",
                    "description": "Background color in HEX color code format"
                  },
                  "text_color": {
                    "type": "string",
                    "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$",
                    "default": "#FFFFFF",
                    "description": "Text color in HEX color code format"
                  }
                }
              },
              "footnote": {
                "type": "string",
                "default": "Thanks for supporting our business - clearly, you have great taste!",
                "maxLength": 350
              },
              "advertising": {
                "type": "object",
                "nullable": true,
                "additionalProperties": false,
                "required": [
                  "title",
                  "url"
                ],
                "properties": {
                  "title": {
                    "type": "string",
                    "enum": [
                      "Call Now",
                      "Book Now",
                      "Buy Now",
                      "Contact Us",
                      "Learn More",
                      "See Offer",
                      "Sign Up",
                      "Shop Now",
                      "Use App",
                      "Visit Us",
                      "Leave a Review",
                      "Leave a Comment"
                    ],
                    "description": "Advertising button in the tracking page"
                  },
                  "url": {
                    "type": "string",
                    "format": "uri",
                    "description": "Link for the advertising button"
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
```