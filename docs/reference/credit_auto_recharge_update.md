# Update Auto Recharge Credit Settings

Update the settings for auto recharging your credit when your account balance falls below the threshold specified through this endpoint.

This endpoint is in beta (subject to change). Please get in touch with customer support to enable it.

Required authorization scope: `public.payment:write`


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
      "name": "Auto Recharge"
    }
  ],
  "paths": {
    "/2024-09/account/credit/auto_recharge": {
      "patch": {
        "summary": "Update Auto Recharge Credit Settings",
        "tags": [
          "Auto Recharge"
        ],
        "operationId": "credit_auto_recharge_update",
        "description": "Update the settings for auto recharging your credit when your account balance falls below the threshold specified through this endpoint.\n\nThis endpoint is in beta (subject to change). Please get in touch with customer support to enable it.\n\nRequired authorization scope: `public.payment:write`\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "successfully update auto recharge settings",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "auto_recharge": {
                        "amount": 1000,
                        "enabled": true,
                        "threshold_amount": 500
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "successfully update auto recharge settings"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/auto_recharge_single"
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
                          "Threshold amount must be a kind of Integer"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "Update Auto Recharge Settings",
                            "url": "https://developers.easyship.com/reference/credit_auto_recharge_update"
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
                "$ref": "#/components/schemas/AutoRechargeUpdate"
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
      "auto_recharge_single": {
        "type": "object",
        "description": "Auto recharge setting details",
        "additionalProperties": false,
        "properties": {
          "auto_recharge": {
            "$ref": "#/components/schemas/AutoRecharge"
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
      "AutoRecharge": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "enabled": {
            "type": "boolean",
            "description": "Indicates if Auto Recharge is enabled."
          },
          "threshold_amount": {
            "type": "number",
            "description": "Amount of threshold to process auto recharge to the account balance."
          },
          "amount": {
            "type": "number",
            "description": "Amount to recharge."
          }
        }
      },
      "AutoRechargeUpdate": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "enabled": {
            "type": "boolean",
            "description": "Indicates if Auto Recharge is enabled."
          },
          "threshold_amount": {
            "type": "number",
            "description": "Amount of threshold to process auto recharge to the account balance."
          },
          "amount": {
            "type": "number",
            "description": "Amount to recharge. Amount of recharge should be over the threshold amount.\nThese are amount that allowed by countries.\n\n|Country|Minimum Amount|Maximum amount|\n|---|---|---|\n|United Arab Emirates|100|4000|\n|Albania|50000|2000000|\n|Austria|50|2000|\n|Australia|50|2000|\n|Bosnia and Herzegovina|100|4000|\n|Belgium|50|2000|\n|Bulgaria|100|4000|\n|Canada|50|2000|\n|Switzerland|50|2000|\n|China|500|20000|\n|Cyprus|50|2000|\n|Czech Republic|1000|40000|\n|Germany|50|2000|\n|Denmark|500|20000|\n|Estonia|50|2000|\n|Spain|50|2000|\n|Finland|50|2000|\n|France|50|2000|\n|United Kingdom|50|2000|\n|Greece|50|2000|\n|Hong Kong|500|20000|\n|Croatia|50|2000|\n|Hungary|10000|400000|\n|Indonesia|100000|4000000|\n|Ireland|50|2000|\n|Israel|100|4000|\n|India|5000|200000|\n|Iceland|5000|200000|\n|Italy|50|2000|\n|Japan|10000|400000|\n|Korea, Republic of|100000|4000000|\n|Lithuania|50|2000|\n|Luxembourg|50|2000|\n|Latvia|50|2000|\n|Malta|50|2000|\n|Mexico|1000|40000|\n|Malaysia|500|20000|\n|Netherlands|50|2000|\n|Norway|500|20000|\n|New Zealand|100|4000|\n|Philippines|5000|200000|\n|Poland|100|4000|\n|Portugal|50|2000|\n|Romania|100|4000|\n|Serbia|5000|200000|\n|Sweden|500|20000|\n|Singapore|50|2000|\n|Slovenia|50|2000|\n|Slovakia|50|2000|\n|Thailand|1000|40000|\n|Turkey|1000|40000|\n|Taiwan, Republic Of China|1000|40000|\n|Ukraine|1000|40000|\n|United States|50|2000|\n|Vietnam|1000000|40000000|\n"
          }
        }
      }
    }
  }
}
```