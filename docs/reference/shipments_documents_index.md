# List All Documents

Retrieve shipping documents of specific shipment.

Required authorization scope: `public.shipment_document:read`


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
    "/2024-09/shipments/{easyship_shipment_id}/documents": {
      "get": {
        "summary": "List All Documents",
        "tags": [
          "Shipments"
        ],
        "operationId": "shipments_documents_index",
        "description": "Retrieve shipping documents of specific shipment.\n\nRequired authorization scope: `public.shipment_document:read`\n",
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
          },
          {
            "name": "document_type",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "commercial_invoice"
              ]
            },
            "required": true,
            "description": "Document type"
          },
          {
            "name": "page_size",
            "in": "query",
            "schema": {
              "type": "string",
              "enum": [
                "4x6",
                "A4"
              ]
            },
            "description": "Page size of shipping documents"
          }
        ],
        "responses": {
          "200": {
            "description": "list of documents",
            "content": {
              "application/pdf": {
                "examples": {
                  "default": {
                    "value": "JVBERi0xLjMKJf____8KMSAwIG9iago8PCAvQ3JlYXRvciA8ZmVmZjAwNTAwMDcyMDA2MTAwNzcwMDZlPgovUHJvZHVjZXIgPGZlZmYwMDUwMDA3MjAwNjEwMDc3MDA2ZT4KPj4KZW5kb2JqCjIgMCBvYmoKPDwgL1R5cGUgL0NhdGFsb2cKL1BhZ2VzIDMgMCBSCj4-CmVuZG9iagozIDAgb2JqCjw8IC9UeXBlIC9QYWdlcwovQ291bnQgMQovS2lkcyBbNSAwIFJdCj4-CmVuZG9iago0IDAgb2JqCjw8IC9MZW5ndGggMTIyCj4-CnN0cmVhbQpxCgpCVAozNi4wIDc0Ny4zODQgVGQKL0YxLjAgMTIgVGYKWzw3MzY4Njk3MDZkNjU2ZTc0MjA2NDZmNjM3NTZkNjU2ZTc0MjA3MjY1NzM3MDZmNmU3MzY1MjA2NT4gMzAgPDc4NjE2ZDcwNmM2NT5dIFRKCkVUCgpRCgplbmRzdHJlYW0KZW5kb2JqCjUgMCBvYmoKPDwgL1R5cGUgL1BhZ2UKL1BhcmVudCAzIDAgUgovTWVkaWFCb3ggWzAgMCA2MTIgNzkyXQovQ3JvcEJveCBbMCAwIDYxMiA3OTJdCi9CbGVlZEJveCBbMCAwIDYxMiA3OTJdCi9UcmltQm94IFswIDAgNjEyIDc5Ml0KL0FydEJveCBbMCAwIDYxMiA3OTJdCi9Db250ZW50cyA0IDAgUgovUmVzb3VyY2VzIDw8IC9Qcm9jU2V0IFsvUERGIC9UZXh0IC9JbWFnZUIgL0ltYWdlQyAvSW1hZ2VJXQovRm9udCA8PCAvRjEuMCA2IDAgUgo-Pgo-Pgo-PgplbmRvYmoKNiAwIG9iago8PCAvVHlwZSAvRm9udAovU3VidHlwZSAvVHlwZTEKL0Jhc2VGb250IC9IZWx2ZXRpY2EKL0VuY29kaW5nIC9XaW5BbnNpRW5jb2RpbmcKPj4KZW5kb2JqCnhyZWYKMCA3CjAwMDAwMDAwMDAgNjU1MzUgZiAKMDAwMDAwMDAxNSAwMDAwMCBuIAowMDAwMDAwMTA5IDAwMDAwIG4gCjAwMDAwMDAxNTggMDAwMDAgbiAKMDAwMDAwMDIxNSAwMDAwMCBuIAowMDAwMDAwMzg4IDAwMDAwIG4gCjAwMDAwMDA2NTQgMDAwMDAgbiAKdHJhaWxlcgo8PCAvU2l6ZSA3Ci9Sb290IDIgMCBSCi9JbmZvIDEgMCBSCj4-CnN0YXJ0eHJlZgo3NTEKJSVFT0YK",
                    "summary": "list of documents"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipping_documents_list"
                }
              }
            }
          },
          "400": {
            "description": "shipment has been cancelled",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_request",
                        "details": [
                          "The shipment has been canceled or the label hasn't been purchased."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List All Documents",
                            "url": "https://developers.easyship.com/reference/shipments_documents_index"
                          }
                        ],
                        "message": "The request body is malformed or not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "shipment has been cancelled"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
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
                            "name": "List All Documents",
                            "url": "https://developers.easyship.com/reference/shipments_documents_index"
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
            "description": "invalid document type",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_url_param",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "\"packing_slip\" isn't part of the enum in #/paths/~12024-09~1shipments~1{easyship_shipment_id}~1documents/get/parameters/1/schema"
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          }
                        ],
                        "message": "The request URL param is invalid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "invalid document type"
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
      "shipping_documents_list": {
        "type": "string",
        "format": "binary"
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
      }
    }
  }
}
```