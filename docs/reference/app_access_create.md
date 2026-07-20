# Create an App Access

Create a temporary app access redirect token

Required authorization scope: `public.app_access:write`


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
    "/2024-09/account/app_accesses": {
      "post": {
        "summary": "Create an App Access",
        "tags": [
          "App Access"
        ],
        "operationId": "app_access_create",
        "description": "Create a temporary app access redirect token\n\nRequired authorization scope: `public.app_access:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "201": {
            "description": "app access successfully created with target and redirect url",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "app_access": {
                        "expires_at": "2022-02-22T12:21:30Z",
                        "url": "https://lyoc.easyship.com/couriers?token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..S3mXgIgk-0kT78FG"
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "app access successfully created with target and redirect url"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/app_access_single"
                }
              }
            }
          },
          "422": {
            "description": "invalid target",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "Target is not included in the list"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Create an App Access",
                            "url": "https://developers.easyship.com/reference/app_access_create"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "invalid target"
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
                "$ref": "#/components/schemas/AppAccessCreate"
              },
              "examples": {
                "app_access_successfully_created": {
                  "summary": "minimal",
                  "value": {
                    "app_name": "lyoc"
                  }
                },
                "app_access_successfully_created_with_target_and_redirect_url": {
                  "summary": "complete",
                  "value": {
                    "app_name": "lyoc",
                    "target": "couriers",
                    "redirect_back_url": "https://example.com"
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
      "app_access_single": {
        "type": "object",
        "description": "App access",
        "additionalProperties": false,
        "properties": {
          "app_access": {
            "$ref": "#/components/schemas/AppAccess"
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
      "AppAccessCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "app_name"
        ],
        "properties": {
          "app_name": {
            "type": "string",
            "enum": [
              "lyoc",
              "enterprise_onboarding"
            ]
          },
          "redirect_back_url": {
            "type": "string",
            "format": "uri",
            "description": "Specifies the URL to which the user should be redirected when the connection needs to be completed in the courier's portal (for example, Canada Post or AU Post MyPost Business). This ensures the user can return to the app seamlessly after the external interaction."
          },
          "target": {
            "type": "string",
            "description": "Certain apps allow their own target paths\n\nApp Name: lyoc\nAvailable Targets:\n  \n  - couriers: /couriers\n  \n"
          }
        }
      },
      "AppAccess": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "url": {
            "type": "string",
            "format": "uri",
            "description": "App Access redirect URL with one time token"
          },
          "expires_at": {
            "type": "string",
            "format": "datetime",
            "description": "Expiry time for URI"
          }
        }
      }
    }
  }
}
```