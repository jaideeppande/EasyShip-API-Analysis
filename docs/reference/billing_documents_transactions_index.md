# List all Billing Document's Transaction Records

Retrieve a list of all billing document's transactions.
Pagination of this endpoint is not indexed.
`count` on the response body will always be `null`.

Required authorization scope: `public.transaction_record:read`


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
      "name": "Billing Documents"
    }
  ],
  "paths": {
    "/2024-09/billing_documents/{id}/transaction_records": {
      "get": {
        "summary": "List all Billing Document's Transaction Records",
        "tags": [
          "Billing Documents"
        ],
        "operationId": "billing_documents_transactions_index",
        "description": "Retrieve a list of all billing document's transactions.\nPagination of this endpoint is not indexed.\n`count` on the response body will always be `null`.\n\nRequired authorization scope: `public.transaction_record:read`\n",
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
            "name": "id",
            "in": "path",
            "required": true,
            "description": "Billing document ID",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "from_date",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "date"
            },
            "example": "2023-01-01",
            "required": false,
            "description": "Beginning of date. Only accept `YYYY-MM-DD` format."
          },
          {
            "name": "to_date",
            "in": "query",
            "schema": {
              "type": "string",
              "format": "date"
            },
            "example": "2023-02-28",
            "required": false,
            "description": "End of date. Only accept `YYYY-MM-DD` format."
          }
        ],
        "responses": {
          "200": {
            "description": "list of billing document's transaction records",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "transaction_records": [
                        {
                          "adjustment_type": "Others",
                          "amount": 20,
                          "description": "billing INHK20220217001",
                          "easyship_shipment_id": null,
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0002",
                          "payment_recipient": "Easyship",
                          "settled_at": null
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": null
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of billing document's transaction records"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/transaction_record_list"
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
      "transaction_record_list": {
        "oneOf": [
          {
            "type": "object",
            "description": "List of Transaction Records",
            "additionalProperties": false,
            "properties": {
              "transaction_records": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/TransactionRecord"
                }
              },
              "meta": {
                "$ref": "#/components/schemas/MetaWithPagination"
              }
            }
          },
          {
            "type": "string",
            "description": "Transaction Records in CSV format"
          }
        ]
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
      "TransactionRecord": {
        "type": "object",
        "description": "Transaction Record",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "description": "ID of transaction record",
            "format": "uuid",
            "example": "01563646-58c1-4607-8fe0-cae3e33c0001"
          },
          "adjustment_type": {
            "type": "string",
            "description": "Type of adjustment",
            "nullable": true,
            "enum": [
              "Refund after Cancellation",
              "Remote Area Surcharge (ODA Reconciliation)",
              "Declared Value Revaluation (Tax Reconciliation)",
              "Adjustment based on Weight (Weight Reconciliation)",
              "Payment of Tax & Duty on behalf of Consignee",
              "Return Fees",
              "Declared Value Revaluation",
              "Address Correction Fee",
              "Refund (100%)",
              "Residential Area Surcharge",
              "Charge After Refund",
              "Warehouse Handling Fee",
              "Refund for Fixed Shipment",
              "Charge for Fixed Shipment",
              "Refund (50%)",
              "Oversized Surcharge",
              "Refund - Damaged",
              "Refund - Lost",
              "Pay On Scan",
              "Account Consolidation",
              "Others"
            ]
          },
          "amount": {
            "type": "number",
            "description": "Amount of adjustment"
          },
          "description": {
            "type": "string",
            "description": "Description of adjustment",
            "nullable": true
          },
          "payment_recipient": {
            "type": "string",
            "description": "Recipient of payment"
          },
          "settled_at": {
            "type": "string",
            "description": "Date and time of settlement",
            "format": "date-time",
            "nullable": true
          },
          "easyship_shipment_id": {
            "type": "string",
            "pattern": "^ES\\w{2}\\d{7,}$",
            "description": "Readable identifier prefixed with ES (Easyship) and destination country code",
            "nullable": true
          }
        }
      }
    }
  }
}
```