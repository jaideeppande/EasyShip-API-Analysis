# List HS Codes

Retrieve a list of HS codes.

Required authorization scope: `public.hs_code:read`

**Rate limit**: This endpoint is rate-limited by 100 requests per second, 1,000 requests per minute, 1,000 requests per hour, 1,000 requests per day, and 30,000 requests per month.
Exceeding this limit returns a `429 Too Many Requests` response for subsequent requests. If you need a higher rate limit, get in touch with us.

> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).

Calls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.


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
      "name": "HS codes"
    }
  ],
  "paths": {
    "/2024-09/hs_codes": {
      "get": {
        "summary": "List HS Codes",
        "tags": [
          "HS codes"
        ],
        "operationId": "hs_code_index",
        "description": "Retrieve a list of HS codes.\n\nRequired authorization scope: `public.hs_code:read`\n\n**Rate limit**: This endpoint is rate-limited by 100 requests per second, 1,000 requests per minute, 1,000 requests per hour, 1,000 requests per day, and 30,000 requests per month.\nExceeding this limit returns a `429 Too Many Requests` response for subsequent requests. If you need a higher rate limit, get in touch with us.\n\n> **Note:** This endpoint requires an **advanced scope**. You can enable advanced scopes when creating or editing your [API connection](https://developers.easyship.com/reference/scopes).\n\nCalls to this endpoint count towards your API usage allowance. You can monitor your current usage in the [Subscription section](https://app.easyship.com/account/subscription) of your account.\n",
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
            "name": "code",
            "in": "query",
            "required": false,
            "description": "Filter records by HS code",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "description",
            "in": "query",
            "required": false,
            "description": "Filter records by description",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "200": {
            "description": "list of hs codes",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "hs_codes": [
                        {
                          "code": "01234567",
                          "description": "This is a book"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 1
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of hs codes"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/hs_code_list"
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
      "hs_code_list": {
        "type": "object",
        "description": "List of HS codes",
        "additionalProperties": false,
        "properties": {
          "hs_codes": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/HSCode"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
      "HSCode": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "description",
          "code"
        ],
        "properties": {
          "description": {
            "type": "string",
            "description": "Description of the HS code"
          },
          "code": {
            "type": "string",
            "description": "HS code"
          }
        }
      }
    }
  }
}
```