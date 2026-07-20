# Warehouse State Updates

Update the warehouse state of one or multiple shipments.

Required authorization scope: `public.shipment:write`, `public.efulfillment:write`

> This endpoint is only available to eFulfillment clients with shipments fulfilled at one of Easyship's integrated warehouses.

> If a shipment contains the `metadata` object, it will persist unless you change existing keys or create new ones: in this case, corresponding keys will be updated or added.

The `warehouse_state` field has the following possible statuses:
<table>
  <tr>
    <th>warehouse_state</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>
      <code>created</code>
    </td>
    <td>
      An order has been created in the warehouse management system and is ready to be fulfilled.<br><br><i>Note:</i> This update is not needed if a success response is sent when Easyship sends the label callback.
    </td>
  </tr>
  <tr>
    <td>
      <code>failed</code>
    </td>
    <td>
      The order creation was rejected for an internal reason by the WMS. This can happen if the order information doesn't meet the WMS' requirements, or a product SKU is not defined in your WMS.<br><br>A message can be added using the message parameter. This will allow the client and Easyship to understand the reason for rejection.
    </td>
  </tr>
  <tr>
    <td>
      <code>packed</code>
    </td>
    <td>
      The order has been processed and packed and is waiting to be handed over to the courier
    </td>
  </tr>
  <tr>
    <td>
      <code>shipped</code>
    </td>
    <td>
      The order has been handed over to the courier and has left the warehouse.<br><br><i>Note:</i> This status update will trigger the following:
      <ul>
        <li>If the shipment was created through a store integration, Easyship will mark the order as "shipped" on the store</li>
        <li>If the company has the email notification option turned on, Easyship will send an email notification to the receiver, with the tracking number and the tracking page URL</li>
        <li>Easyship will start tracking the shipment, and update its status based on the courier's tracking events</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <code>cancellation_requested</code>
    </td>
    <td>
      A cancellation request has been sent to the warehouse management system. It is awaiting confirmation by the warehouse.<br><br><i>Note:</i> This status is set by clients requesting a cancellation through the dashboard. It should not be set by a warehouse.
    </td>
  </tr>
  <tr>
    <td>
      <code>cancelled</code>
    </td>
    <td>
      The order has been cancelled in the warehouse management system.<br><br><i>Note:</i> This status update will trigger Easyship to cancel the shipment.
    </td>
  </tr>
  <tr>
    <td>
      <code>cancelled_no_stock</code>
    </td>
    <td>
     The order has been cancelled in the warehouse management system because the products are out of stock.<br><br><i>Note:</i> This status update will trigger Easyship to cancel the shipment.
    </td>
  </tr>
  <tr>
    <td>
      <code>backorder_no_stock</code>
    </td>
    <td>
      The order is set as backorder because of the products are out of stock. It may be packed and shipped at a later date.
    </td>
  </tr>
  <tr>
    <td>
      <code>returned</code>
    </td>
    <td>
      The package was returned by the courier or by the receiver, and received at the warehouse.
    </td>
  </tr>
</table>


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
      "name": "eFulfillment"
    }
  ],
  "paths": {
    "/2024-09/shipments/warehouse_state_updates": {
      "post": {
        "summary": "Warehouse State Updates",
        "tags": [
          "eFulfillment"
        ],
        "operationId": "efulfillment_warehouse_state_update",
        "description": "Update the warehouse state of one or multiple shipments.\n\nRequired authorization scope: `public.shipment:write`, `public.efulfillment:write`\n\n> This endpoint is only available to eFulfillment clients with shipments fulfilled at one of Easyship's integrated warehouses.\n\n> If a shipment contains the `metadata` object, it will persist unless you change existing keys or create new ones: in this case, corresponding keys will be updated or added.\n\nThe `warehouse_state` field has the following possible statuses:\n<table>\n  <tr>\n    <th>warehouse_state</th>\n    <th>Description</th>\n  </tr>\n  <tr>\n    <td>\n      <code>created</code>\n    </td>\n    <td>\n      An order has been created in the warehouse management system and is ready to be fulfilled.<br><br><i>Note:</i> This update is not needed if a success response is sent when Easyship sends the label callback.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>failed</code>\n    </td>\n    <td>\n      The order creation was rejected for an internal reason by the WMS. This can happen if the order information doesn't meet the WMS' requirements, or a product SKU is not defined in your WMS.<br><br>A message can be added using the message parameter. This will allow the client and Easyship to understand the reason for rejection.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>packed</code>\n    </td>\n    <td>\n      The order has been processed and packed and is waiting to be handed over to the courier\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>shipped</code>\n    </td>\n    <td>\n      The order has been handed over to the courier and has left the warehouse.<br><br><i>Note:</i> This status update will trigger the following:\n      <ul>\n        <li>If the shipment was created through a store integration, Easyship will mark the order as \"shipped\" on the store</li>\n        <li>If the company has the email notification option turned on, Easyship will send an email notification to the receiver, with the tracking number and the tracking page URL</li>\n        <li>Easyship will start tracking the shipment, and update its status based on the courier's tracking events</li>\n      </ul>\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>cancellation_requested</code>\n    </td>\n    <td>\n      A cancellation request has been sent to the warehouse management system. It is awaiting confirmation by the warehouse.<br><br><i>Note:</i> This status is set by clients requesting a cancellation through the dashboard. It should not be set by a warehouse.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>cancelled</code>\n    </td>\n    <td>\n      The order has been cancelled in the warehouse management system.<br><br><i>Note:</i> This status update will trigger Easyship to cancel the shipment.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>cancelled_no_stock</code>\n    </td>\n    <td>\n     The order has been cancelled in the warehouse management system because the products are out of stock.<br><br><i>Note:</i> This status update will trigger Easyship to cancel the shipment.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>backorder_no_stock</code>\n    </td>\n    <td>\n      The order is set as backorder because of the products are out of stock. It may be packed and shipped at a later date.\n    </td>\n  </tr>\n  <tr>\n    <td>\n      <code>returned</code>\n    </td>\n    <td>\n      The package was returned by the courier or by the receiver, and received at the warehouse.\n    </td>\n  </tr>\n</table>\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [],
        "responses": {
          "200": {
            "description": "shipment warehouse state successfully updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "shipments": [
                        {
                          "easyship_shipment_id": "ESSG10006001",
                          "errors": [],
                          "status": "success"
                        }
                      ],
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "status": "success"
                      }
                    },
                    "summary": "shipment warehouse state successfully updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipment_warehouse_state_list"
                }
              }
            }
          },
          "202": {
            "description": "shipment warehouse state partially updated",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "shipments": [
                        {
                          "easyship_shipment_id": "ESSG10006001",
                          "errors": [],
                          "status": "success"
                        },
                        {
                          "easyship_shipment_id": "ESHK10000001",
                          "errors": [
                            "Shipment not found"
                          ],
                          "status": "failure"
                        }
                      ],
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "status": "partial_success"
                      }
                    },
                    "summary": "shipment warehouse state partially updated"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipment_warehouse_state_list"
                }
              }
            }
          },
          "422": {
            "description": "failure",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "The request does not comply with the OpenAPI Specification.",
                          "\"wrong_state\" isn't part of the enum in #/components/schemas/ShipmentWarehouseState/properties/warehouse_state"
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
                    "summary": "failure"
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
                "$ref": "#/components/schemas/shipment_warehouse_state_update"
              },
              "examples": {
                "shipment_warehouse_state_successfully_updated": {
                  "summary": "shipment warehouse state successfully updated",
                  "value": {
                    "shipments": [
                      {
                        "easyship_shipment_id": "ESSG10006001",
                        "warehouse_state": "shipped"
                      }
                    ]
                  }
                },
                "shipment_warehouse_state_partially_updated": {
                  "summary": "shipment warehouse state partially updated",
                  "value": {
                    "shipments": [
                      {
                        "easyship_shipment_id": "ESSG10006001",
                        "warehouse_state": "shipped"
                      },
                      {
                        "easyship_shipment_id": "ESHK10000001",
                        "warehouse_state": "shipped"
                      }
                    ]
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
      "shipment_warehouse_state_list": {
        "type": "object",
        "description": "List of shipment warehouse states",
        "additionalProperties": false,
        "properties": {
          "status": {
            "type": "string"
          },
          "shipments": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShipmentWarehouseStateResponse"
            }
          },
          "meta": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "status": {
                "type": "string"
              },
              "request_id": {
                "$ref": "#/components/schemas/Meta/properties/request_id"
              }
            }
          }
        }
      },
      "shipment_warehouse_state_update": {
        "type": "object",
        "description": "Data for updating shipments warehouse state",
        "additionalProperties": false,
        "properties": {
          "shipments": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ShipmentWarehouseState"
            }
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
      "Shipment": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "type": "string",
            "pattern": "^ES\\w{2}\\d{7,}$",
            "description": "Readable identifier prefixed with ES (Easyship) and destination country code"
          },
          "created_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was created in the Easyship system"
          },
          "updated_at": {
            "type": "string",
            "format": "date-time",
            "description": "When the shipment record was most recently modified"
          },
          "label_paid_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When Easyship was paid for the shipment"
          },
          "label_generated_at": {
            "type": "string",
            "nullable": true,
            "format": "date-time",
            "description": "When label was generated"
          },
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin address"
              }
            ]
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender address"
              }
            ]
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return address"
              }
            ]
          },
          "destination_address": {
            "$ref": "#/components/schemas/DestinationAddress"
          },
          "order_data": {
            "type": "object",
            "description": "Free-form data related to the eCommerce platform",
            "additionalProperties": false,
            "properties": {
              "platform_name": {
                "type": "string",
                "nullable": true,
                "description": "A display-ready sales channel or platform name",
                "maximum": 200
              },
              "platform_order_number": {
                "type": "string",
                "nullable": true,
                "description": "Order number that was either copied from an order synced from an ecommerce platform or manually edited in Easyship's order from",
                "maximum": 200
              },
              "order_created_at": {
                "type": "string",
                "nullable": true,
                "format": "date-time",
                "description": "When the order was created (e.g. in an online store connected to Easyship)"
              },
              "order_tag_list": {
                "type": "array",
                "description": "Tags that have been assigned to this shipment, either as an order on its e-commerce store or within the Easyship app",
                "items": {
                  "type": "string"
                },
                "maxItems": 500
              },
              "seller_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the merchant. Will not be shown to the receiver."
              },
              "buyer_notes": {
                "type": "string",
                "nullable": true,
                "description": "Text added by the buyer during order checkout. Will be displayed on the packing slip."
              },
              "buyer_selected_courier_name": {
                "type": "string",
                "nullable": true,
                "description": "Courier name for shipping rule condition `match_buyer_selected_courier_name`. If the name matches, actions of this shipping rule would apply to the current shipment."
              }
            }
          },
          "last_failure_http_response_messages": {
            "type": "array",
            "description": "This attribute stores the HTTP response of the most recent unsuccessful attempt to interact with an external service, such as a failed label creation.",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "code": {
                  "type": "string",
                  "nullable": true
                },
                "content": {
                  "type": "string",
                  "nullable": true
                }
              }
            }
          },
          "metadata": {
            "type": "object",
            "description": "Set of key-value pairs that you can attach to a shipment. This can be useful for storing additional information about the object in a structured format"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "Indicates whether or not the user believes the receiver address qualifies for a residential surcharge."
          },
          "consignee_tax_id": {
            "type": "string",
            "nullable": true,
            "description": "Tax ID for the receiver. Maybe helpful or required for customs clearance, depending on the destination country."
          },
          "eei_reference": {
            "type": "string",
            "nullable": true,
            "description": "References data (Electronic Export Information) filed through one of the systems for goods shipped from the U.S.\nto a foreign country. Currently only used for FedEx shipments. The following possibilities may or may not qualify:\n  * An Automated Export System (AES) citation\n  * A Foreign Trade Regulations (FTR) exemption number\n  * An International Traffic in Arms Reduction (ITAR) exemption code\n  * A US Department of Commerce export license number"
          },
          "regulatory_identifiers": {
            "type": "object",
            "description": "Seller's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "eori": {
                "type": "string",
                "nullable": true,
                "description": "Economic Operators Registration and Identification (EORI) number."
              },
              "ioss": {
                "type": "string",
                "nullable": true,
                "description": "Import One Stop Shop (IOSS) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              }
            }
          },
          "buyer_regulatory_identifiers": {
            "type": "object",
            "description": "Buyer's identifiers for various tax, import and export regulations.",
            "additionalProperties": false,
            "properties": {
              "ein": {
                "type": "string",
                "nullable": true,
                "description": "Employer Identification Number (EIN) number."
              },
              "vat_number": {
                "type": "string",
                "nullable": true,
                "description": "Value-Added Tax (VAT) number."
              },
              "ssn": {
                "type": "string",
                "nullable": true,
                "description": "Social Security Number (SSN) number."
              }
            }
          },
          "return": {
            "type": "boolean",
            "description": "Whether the shipment is a return shipment or not"
          },
          "incoterms": {
            "description": "Terms of Sale\nDDP: Seller pays all import duties/taxes.\nDDU: Buyer pays all import duties/taxes.\nnull: No incoterm specified; defaults to DDU.\n",
            "type": "string",
            "enum": [
              "DDU",
              "DDP",
              null
            ],
            "default": "DDU",
            "nullable": true
          },
          "insurance": {
            "type": "object",
            "description": "Insurance",
            "nullable": true,
            "additionalProperties": false,
            "properties": {
              "is_insured": {
                "type": "boolean",
                "description": "Indicates if premium insurance has been purchased for this shipment (either by the merchant or buyer).\nBasic, courier-supplied coverage is not applicable.",
                "default": false
              },
              "insured_amount": {
                "type": "number",
                "description": "Amount to insure with Easyship's insurance provider. If not specified, we'll use the sum of customs values and shipping cost."
              },
              "insured_currency": {
                "allOf": [
                  {
                    "$ref": "#/components/schemas/Currency"
                  },
                  {
                    "description": "Insurance currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP). If not specified, we will use the currency of the account country."
                  }
                ]
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/Parcel"
            }
          },
          "total_customs_value": {
            "type": "number",
            "minimum": 0,
            "description": "Sum of the value assigned to all shipment line items"
          },
          "total_actual_weight": {
            "type": "number",
            "description": "Sum of the specified weights of all *parcels* in the shipment (`parcel.actual_weight`), as measured on a scale in units specified by `company.weight_unit`."
          },
          "shipment_state": {
            "type": "string",
            "description": "The state of the shipment record within the Easyship system",
            "default": "created",
            "nullable": false,
            "enum": [
              "created",
              "draft",
              "calculating",
              "cancelling",
              "cancelled",
              "discarded",
              "deleted"
            ]
          },
          "pickup_state": {
            "type": "string",
            "default": "not_requested",
            "nullable": false,
            "description": "The state of the hand-over from shipper to courier. `pending_handover` applies only to eFulfillment companies."
          },
          "delivery_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the hand-over from courier to receiver.",
            "enum": [
              "not_created",
              "pending",
              "info_received",
              "in_transit_to_customer",
              "out_for_delivery",
              "delivered",
              "failed_attempt",
              "exception",
              "expired",
              "lost_by_courier",
              "returned_to_shipper"
            ]
          },
          "label_state": {
            "type": "string",
            "default": "not_created",
            "nullable": false,
            "description": "The state of the label(s) meant to be printed and attached to this shipment's parcels",
            "enum": [
              "not_created",
              "pending",
              "generating",
              "generated",
              "printed",
              "failed",
              "technical_failed",
              "reported",
              "voided",
              "void_failed"
            ]
          },
          "warehouse_state": {
            "type": "string",
            "default": "none",
            "nullable": false,
            "description": "The state of the fulfillment process within the warehouse",
            "enum": [
              "none",
              "pending",
              "created",
              "failed",
              "packed",
              "cancelled",
              "cancelled_no_stock",
              "backorder_no_stock",
              "shipped",
              "returned",
              "awaiting_dispatch"
            ]
          },
          "warehouse_code": {
            "type": "string",
            "description": "Warehouse code (warehouse/eFulfilment only)"
          },
          "original_easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "trackings": {
            "type": "array",
            "description": "Sources of tracking data for this shipment",
            "items": {
              "$ref": "#/components/schemas/ShipmentTracking"
            }
          },
          "tracking_page_url": {
            "type": "string",
            "description": "Tracking page URL"
          },
          "shipping_documents": {
            "type": "array",
            "description": "Shipping documents",
            "items": {
              "$ref": "#/components/schemas/ShipmentDocument"
            }
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "courier_service": {
            "type": "object",
            "nullable": true,
            "description": "Selected courier service for this shipment. May be null if no service has been selected yet, or if the shipment was created without selecting a service.\nMore information about the [courier service](https://developers.easyship.com/reference/courier_services_index)",
            "additionalProperties": false,
            "properties": {
              "id": {
                "type": "string",
                "format": "uuid"
              },
              "name": {
                "type": "string"
              },
              "courier_id": {
                "type": "string",
                "format": "uuid",
                "description": "The courier ID that the current courier service is associated with"
              },
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service."
              },
              "easyship_courier_service": {
                "$ref": "#/components/schemas/CourierService/properties/easyship_courier_service"
              }
            }
          },
          "rates": {
            "type": "array",
            "description": "Array of available courier services for this shipment, along with the rates charged. Courier services are excluded if the shipment's contents or destination do not meet each service's eligibility requirements.",
            "items": {
              "$ref": "#/components/schemas/Rate"
            }
          },
          "shipping_settings": {
            "type": "object",
            "description": "Shipping settings",
            "additionalProperties": false,
            "properties": {
              "b13a_filing": {
                "type": "object",
                "description": "B13A filing (currently available only for FedEx)",
                "additionalProperties": false,
                "nullable": true,
                "properties": {
                  "option": {
                    "type": "string",
                    "enum": [
                      "not_required",
                      "fedex_to_stamp",
                      "filed_electronically",
                      "manually_attached",
                      "summary_reporting"
                    ]
                  },
                  "option_export_compliance_statement": {
                    "type": "string",
                    "nullable": true,
                    "description": "Export compliance statement"
                  },
                  "permit_number": {
                    "type": "string",
                    "nullable": true,
                    "description": "Permit number"
                  }
                }
              },
              "label_customization_fields": {
                "anyOf": [
                  {
                    "$ref": "#/components/schemas/ShipmentCreate/properties/shipping_settings/properties/label_customization_fields"
                  },
                  {
                    "type": "array",
                    "minItems": 0
                  }
                ]
              }
            }
          }
        }
      },
      "ShipmentWarehouseState": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "warehouse_state": {
            "type": "string",
            "description": "Warehouse state",
            "enum": [
              "created",
              "failed",
              "packed",
              "shipped",
              "cancelled",
              "cancelled_no_stock",
              "backorder_no_stock",
              "returned"
            ]
          },
          "message": {
            "type": "string",
            "description": "An message can be added if the status is `creation_failed` to explain the reason for rejection."
          },
          "metadata": {
            "type": "object",
            "description": "Set of key-value pairs that you can attach to a shipment. This can be useful for storing additional information about the object in a structured format."
          }
        }
      },
      "ShipmentWarehouseStateResponse": {
        "type": "object",
        "description": "Shipment warehouse state response",
        "additionalProperties": false,
        "properties": {
          "easyship_shipment_id": {
            "$ref": "#/components/schemas/Shipment/properties/easyship_shipment_id"
          },
          "status": {
            "type": "string"
          },
          "errors": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  }
}
```