# List UPS Locations

Retrieve UPS locations.

This endpoint routes requests to the UPS locator API. For further information, kindly look into the UPS API documentation available at https://developer.ups.com/api/reference?loc=en_US#operation/Locator.

Required authorization scope: `public.location:read`


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
      "name": "Locations"
    }
  ],
  "paths": {
    "/2024-09/locations/ups": {
      "get": {
        "summary": "List UPS Locations",
        "tags": [
          "Locations"
        ],
        "operationId": "locations_ups_index",
        "description": "Retrieve UPS locations.\n\nThis endpoint routes requests to the UPS locator API. For further information, kindly look into the UPS API documentation available at https://developer.ups.com/api/reference?loc=en_US#operation/Locator.\n\nRequired authorization scope: `public.location:read`\n",
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
            "name": "country_alpha2",
            "in": "query",
            "required": true,
            "description": "Country code: Alpha-2 format (ISO 3166-1).",
            "example": "US",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "line_1",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 100
            },
            "required": true,
            "description": "The first line of the address."
          },
          {
            "name": "line_2",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 64
            },
            "required": false,
            "description": "The second line of the address."
          },
          {
            "name": "city",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 50
            },
            "required": true,
            "description": "City or town"
          },
          {
            "name": "state",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 50
            },
            "required": true,
            "description": "State or province"
          },
          {
            "name": "postal_code",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 10
            },
            "required": true,
            "description": "A unique location code used by postal services to sort and deliver mail."
          }
        ],
        "responses": {
          "200": {
            "description": "get courier service points",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "locations": [
                        {
                          "address": {
                            "line_1": "220 EAST AVE",
                            "line_2": null,
                            "city": "KETCHUM",
                            "state": "ID",
                            "postal_code": "83340",
                            "country_alpha2": "US",
                            "longitude": "-114.362091",
                            "latitude": "43.68143081"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": null,
                              "close_time": null
                            },
                            {
                              "day": "Monday",
                              "open_time": "830",
                              "close_time": "1830"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "830",
                              "close_time": "1830"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "830",
                              "close_time": "1830"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "830",
                              "close_time": "1830"
                            },
                            {
                              "day": "Friday",
                              "open_time": "830",
                              "close_time": "1830"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1700"
                            }
                          ],
                          "phone_number": "2087266896",
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "280 E 5TH N&#xD;280",
                            "line_2": null,
                            "city": "MOUNTAIN HOME",
                            "state": "ID",
                            "postal_code": "83647",
                            "country_alpha2": "US",
                            "longitude": "-115.695220",
                            "latitude": "43.13491821"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": null,
                              "close_time": null
                            },
                            {
                              "day": "Monday",
                              "open_time": "830",
                              "close_time": "1930"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "830",
                              "close_time": "1930"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "830",
                              "close_time": "1930"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "830",
                              "close_time": "1930"
                            },
                            {
                              "day": "Friday",
                              "open_time": "830",
                              "close_time": "1930"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "1000",
                              "close_time": "1500"
                            }
                          ],
                          "phone_number": "2085802209",
                          "service_types": [
                            "001-Direct To Retail",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "280 E 5TH N",
                            "line_2": null,
                            "city": "MOUNTAIN HOME",
                            "state": "ID",
                            "postal_code": "83647",
                            "country_alpha2": "US",
                            "longitude": "-115.695228",
                            "latitude": "43.13491821"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": null,
                              "close_time": null
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1900"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1900"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1900"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1900"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1900"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "1000",
                              "close_time": "1500"
                            }
                          ],
                          "phone_number": "2085802209",
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "6568 S FEDERAL WAY",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83716",
                            "country_alpha2": "US",
                            "longitude": "-116.156120",
                            "latitude": "43.54331588"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": null,
                              "close_time": null
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1600"
                            }
                          ],
                          "phone_number": "2083389979",
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "1775 W STATE ST",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83702",
                            "country_alpha2": "US",
                            "longitude": "-116.211868",
                            "latitude": "43.62440490"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": "1000",
                              "close_time": "1500"
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1830"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1700"
                            }
                          ],
                          "phone_number": "2083848500",
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "1116 S VISTA AVE",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83705",
                            "country_alpha2": "US",
                            "longitude": "-116.213676",
                            "latitude": "43.59402465"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": "1000",
                              "close_time": "1500"
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1700"
                            }
                          ],
                          "phone_number": "2083452042",
                          "service_types": [
                            "001-Direct To Retail",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "7154 W STATE ST",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83714",
                            "country_alpha2": "US",
                            "longitude": "-116.278617",
                            "latitude": "43.66933441"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": null,
                              "close_time": null
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1700"
                            }
                          ],
                          "phone_number": "2088536400",
                          "service_types": [
                            "001-Direct To Retail",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "7402 W FAIRVIEW AVE",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83704",
                            "country_alpha2": "US",
                            "longitude": "-116.274269",
                            "latitude": "43.61936187"
                          },
                          "name": "CVS STORE # 11169",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "2200"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "800",
                              "close_time": "2200"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "001-Direct To Retail",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "1553 N MILWAUKEE ST",
                            "line_2": null,
                            "city": "BOISE",
                            "state": "ID",
                            "postal_code": "83704",
                            "country_alpha2": "US",
                            "longitude": "-116.284278",
                            "latitude": "43.61757659"
                          },
                          "name": "THE UPS STORE",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": "1000",
                              "close_time": "1500"
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "900",
                              "close_time": "1700"
                            }
                          ],
                          "phone_number": "2083773849",
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles",
                            "015-Accepts Mobile Barcodes"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "4379 W CHINDEN BLVD",
                            "line_2": null,
                            "city": "GARDEN CITY",
                            "state": "ID",
                            "postal_code": "83714",
                            "country_alpha2": "US",
                            "longitude": "-116.306602",
                            "latitude": "43.65802764"
                          },
                          "name": "ADVANCE AUTO PARTS STORE 3147",
                          "opening_hours": [
                            {
                              "day": "Sunday",
                              "open_time": "900",
                              "close_time": "1900"
                            },
                            {
                              "day": "Monday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Tuesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Wednesday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Thursday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Friday",
                              "open_time": "800",
                              "close_time": "1800"
                            },
                            {
                              "day": "Saturday",
                              "open_time": "800",
                              "close_time": "1800"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "001-Direct To Retail",
                            "002-Not In One ADL",
                            "004-Retail to Retail",
                            "007-PUDO",
                            "008-Early Pickup Delivery Time",
                            "010-DCO DCR intercept accepted",
                            "013-Accepts Restricted Articles"
                          ]
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": null,
                          "count": 10
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "get courier service points"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/location_ups_list"
                }
              }
            }
          },
          "422": {
            "description": "location service not found for provided courier",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "invalid_content",
                        "details": [
                          "We do not support locations for UPS in Andorra."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List UPS Locations",
                            "url": "https://developers.easyship.com/reference/locations_ups_index"
                          }
                        ],
                        "message": "The request body content is not valid.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "invalid_request_error"
                      }
                    },
                    "summary": "location service not found for provided courier"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/Error"
                }
              }
            }
          },
          "500": {
            "description": "forward request failed",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "error": {
                        "code": "internal_server_error",
                        "details": [
                          "Unable to retrieve UPS service points location. Please contact Easyship support."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List UPS Locations",
                            "url": "https://developers.easyship.com/reference/locations_ups_index"
                          }
                        ],
                        "message": "Unexpected internal error.",
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "type": "api_error"
                      }
                    },
                    "summary": "forward request failed"
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
      "location_ups_list": {
        "type": "object",
        "description": "List of UPS locations",
        "additionalProperties": false,
        "properties": {
          "locations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LocationUps"
            }
          },
          "meta": {
            "$ref": "#/components/schemas/MetaWithPagination"
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
      "Address": {
        "type": "object",
        "properties": {
          "line_1": {
            "type": "string",
            "description": "First line of the street address",
            "maximum": 35
          },
          "line_2": {
            "type": "string",
            "nullable": true,
            "description": "Second line of the street address",
            "maximum": 35
          },
          "state": {
            "type": "string",
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names.",
            "maximum": 200
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "nullable": true,
            "description": "Postal code. Leave it null or 0 if the country does not have postal codes. Mandatory for these countries: AD, AF, AI, AL, AM, AQ, AR, AS, AT, AU, AX, AZ, BA, BB, BD, BE, BG, BL, BM, BN, BQ, BR, BT, BV, BY, CA, CC, CH, CL, CN, CO, CR, CU, CV, CX, CY, CZ, DE, DK, DO, DZ, EC, EE, EG, EH, ES, ET, FI, FK, FM, FO, FR, GA, GB, GE, GF, GG, GI, GL, GP, GR, GS, GT, GU, GW, HM, HN, HR, HT, HU, ID, IE, IL, IM, IN, IO, IQ, IR, IS, IT, JE, JO, JP, KG, KH, KR, KW, KY, KZ, LA, LB, LI, LK, LR, LS, LT, LU, LV, MA, MC, MD, ME, MF, MG, MH, MK, MM, MN, MP, MQ, MT, MV, MX, MY, MZ, NA, NC, NE, NF, NG, NI, NL, NO, NP, NZ, OM, PE, PF, PG, PH, PK, PL, PM, PN, PR, PS, PT, PW, PY, RE, RO, RS, RU, SD, SE, SG, SH, SI, SJ, SK, SM, SN, SS, SV, SX, SZ, TC, TD, TH, TJ, TM, TN, TR, TW, UA, UM, US, UY, UZ, VA, VC, VE, VG, VI, VN, WF, WS, YT, ZA, ZM."
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 27
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 22
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20,
            "nullable": true
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name\"",
            "maximum": 50
          }
        }
      },
      "CountryAlpha2": {
        "type": "string",
        "description": "Country Code in Alpha-2 format (ISO 3166-1)",
        "enum": [
          "AD",
          "AE",
          "AF",
          "AG",
          "AI",
          "AL",
          "AM",
          "AN",
          "AO",
          "AQ",
          "AR",
          "AS",
          "AT",
          "AU",
          "AW",
          "AX",
          "AZ",
          "BA",
          "BB",
          "BD",
          "BE",
          "BF",
          "BG",
          "BH",
          "BI",
          "BJ",
          "BL",
          "BM",
          "BN",
          "BO",
          "BQ",
          "BR",
          "BS",
          "BT",
          "BV",
          "BW",
          "BY",
          "BZ",
          "CA",
          "CC",
          "CD",
          "CF",
          "CG",
          "CH",
          "CI",
          "CK",
          "CL",
          "CM",
          "CN",
          "CO",
          "CR",
          "CU",
          "CV",
          "CW",
          "CX",
          "CY",
          "CZ",
          "DE",
          "DJ",
          "DK",
          "DM",
          "DO",
          "DZ",
          "EC",
          "EE",
          "EG",
          "EH",
          "ER",
          "ES",
          "ET",
          "FI",
          "FJ",
          "FK",
          "FM",
          "FO",
          "FR",
          "GA",
          "GB",
          "GD",
          "GE",
          "GF",
          "GG",
          "GH",
          "GI",
          "GL",
          "GM",
          "GN",
          "GP",
          "GQ",
          "GR",
          "GS",
          "GT",
          "GU",
          "GW",
          "GY",
          "HK",
          "HM",
          "HN",
          "HR",
          "HT",
          "HU",
          "ID",
          "IE",
          "IL",
          "IM",
          "IN",
          "IO",
          "IQ",
          "IR",
          "IS",
          "IT",
          "JE",
          "JM",
          "JO",
          "JP",
          "KE",
          "KG",
          "KH",
          "KI",
          "KM",
          "KN",
          "KP",
          "KR",
          "KW",
          "KY",
          "KZ",
          "LA",
          "LB",
          "LC",
          "LI",
          "LK",
          "LR",
          "LS",
          "LT",
          "LU",
          "LV",
          "LY",
          "MA",
          "MC",
          "MD",
          "ME",
          "MF",
          "MG",
          "MH",
          "MK",
          "ML",
          "MM",
          "MN",
          "MO",
          "MP",
          "MQ",
          "MR",
          "MS",
          "MT",
          "MU",
          "MV",
          "MW",
          "MX",
          "MY",
          "MZ",
          "NA",
          "NC",
          "NE",
          "NF",
          "NG",
          "NI",
          "NL",
          "NO",
          "NP",
          "NR",
          "NU",
          "NZ",
          "OM",
          "PA",
          "PE",
          "PF",
          "PG",
          "PH",
          "PK",
          "PL",
          "PM",
          "PN",
          "PR",
          "PS",
          "PT",
          "PW",
          "PY",
          "QA",
          "RE",
          "RO",
          "RS",
          "RU",
          "RW",
          "SA",
          "SB",
          "SC",
          "SD",
          "SE",
          "SG",
          "SH",
          "SI",
          "SJ",
          "SK",
          "SL",
          "SM",
          "SN",
          "SO",
          "SR",
          "SS",
          "ST",
          "SV",
          "SX",
          "SY",
          "SZ",
          "TC",
          "TD",
          "TF",
          "TG",
          "TH",
          "TJ",
          "TK",
          "TL",
          "TM",
          "TN",
          "TO",
          "TR",
          "TT",
          "TV",
          "TW",
          "TZ",
          "UA",
          "UG",
          "UM",
          "US",
          "UY",
          "UZ",
          "VA",
          "VC",
          "VE",
          "VG",
          "VI",
          "VN",
          "VU",
          "WF",
          "WS",
          "YE",
          "YT",
          "ZA",
          "ZM",
          "ZW"
        ]
      },
      "Location": {
        "description": "Location",
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the location"
          },
          "phone_number": {
            "type": "string",
            "description": "The phone number associated with the location",
            "nullable": true
          },
          "address": {
            "type": "object",
            "additionalProperties": false,
            "description": "The address of the location",
            "properties": {
              "line_1": {
                "$ref": "#/components/schemas/Address/properties/line_1"
              },
              "line_2": {
                "$ref": "#/components/schemas/Address/properties/line_2"
              },
              "state": {
                "$ref": "#/components/schemas/Address/properties/state"
              },
              "city": {
                "$ref": "#/components/schemas/Address/properties/city"
              },
              "postal_code": {
                "$ref": "#/components/schemas/Address/properties/postal_code"
              },
              "country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              },
              "longitude": {
                "description": "The longitude of the location",
                "type": "string",
                "nullable": true
              },
              "latitude": {
                "description": "The latitude of the location",
                "type": "string",
                "nullable": true
              }
            }
          },
          "opening_hours": {
            "type": "array",
            "minItems": 1,
            "items": {
              "type": "object",
              "additionalProperties": false,
              "properties": {
                "day": {
                  "type": "string",
                  "description": "The day of the week"
                },
                "open_time": {
                  "type": "string",
                  "description": "The opening time for the specified day",
                  "nullable": true
                },
                "close_time": {
                  "type": "string",
                  "description": "The closing time for the specified day",
                  "nullable": true
                }
              }
            }
          }
        }
      },
      "LocationUps": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Location"
          },
          {
            "description": "UPS Location",
            "type": "object",
            "properties": {
              "service_types": {
                "type": "array",
                "description": "Service code and details",
                "minItems": 1,
                "items": {
                  "type": "string",
                  "enum": [
                    "001-Direct To Retail",
                    "002-Not In One ADL",
                    "003-Click and Collect",
                    "004-Retail to Retail",
                    "005-Pickup 006-Drop Off",
                    "007-PUDO",
                    "008-Early Pickup Delivery Time",
                    "009-Accept prepaid drop offs",
                    "010-DCO DCR intercept accepted",
                    "011-Accepts Payments",
                    "012-Pay At Store",
                    "013-Accepts Restricted Articles",
                    "015-Accepts Mobile Barcodes"
                  ]
                }
              }
            }
          }
        ]
      }
    }
  }
}
```