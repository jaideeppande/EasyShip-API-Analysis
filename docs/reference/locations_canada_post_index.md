# List Canada Post Locations

Retrieve Canada Post locations.

This endpoint routes requests to the Canada Post `Get Nearest Post Office` API. For further information, kindly look into the Canada Post API documentation available at https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/findpostoffice/nearestpostoffice.jsf

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
    "/2024-09/locations/canada_post": {
      "get": {
        "summary": "List Canada Post Locations",
        "tags": [
          "Locations"
        ],
        "operationId": "locations_canada_post_index",
        "description": "Retrieve Canada Post locations.\n\nThis endpoint routes requests to the Canada Post `Get Nearest Post Office` API. For further information, kindly look into the Canada Post API documentation available at https://www.canadapost-postescanada.ca/info/mc/business/productsservices/developers/services/findpostoffice/nearestpostoffice.jsf\n\nRequired authorization scope: `public.location:read`\n",
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
            "example": "CA",
            "schema": {
              "type": "string"
            }
          },
          {
            "name": "postal_code",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 10
            },
            "required": false,
            "description": "A unique location code used by postal services to sort and deliver mail."
          },
          {
            "name": "city",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 50
            },
            "required": false,
            "description": "If Postal Code is not specified, both State and City should be provided to obtain meaningful information. For larger municipalities all of State, City and Line_1 may be required."
          },
          {
            "name": "state",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 50
            },
            "required": false,
            "description": "Two character representation of Canadian provinces - ISO 3166-2"
          },
          {
            "name": "latitude",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 10
            },
            "required": false,
            "description": "If you use longitude and latitude to define the location, both longitude and latitude must be present and all other search fields (postalCode, state, city, and line_1) should be omitted. (If any of these other search fields are present, they will be ignored)"
          },
          {
            "name": "longitude",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 10
            },
            "required": false,
            "description": "If you use longitude and latitude to define the location, both longitude and latitude must be present and all other search fields (postalCode, state, city, and line_1) should be omitted. (If any of these other search fields are present, they will be ignored)"
          },
          {
            "name": "tonight",
            "in": "query",
            "schema": {
              "type": "boolean"
            },
            "required": false,
            "description": "Indicates whether to return only post offices that are open tonight."
          },
          {
            "name": "limit",
            "in": "query",
            "schema": {
              "type": "integer",
              "minimum": 1,
              "maximum": 50
            },
            "required": false,
            "description": "Maximum number of records to return. Default is 10.",
            "example": 20
          },
          {
            "name": "line_1",
            "in": "query",
            "schema": {
              "type": "string",
              "maximum": 100
            },
            "required": false,
            "description": "Street Name only—without the house or apartment number (a search with house or apartment number will not be successful). Street Name can be a multi-part name with embedded spaces."
          },
          {
            "name": "bflf",
            "in": "query",
            "schema": {
              "type": "boolean"
            },
            "required": false,
            "description": "Indicates whether to return only post offices that accept the `Box Free Label` delivery of parcels."
          },
          {
            "name": "d2po",
            "in": "query",
            "schema": {
              "type": "boolean"
            },
            "required": false,
            "description": "Indicates whether to return a list of Post Offices that accept the `Deliver to Post Office` delivery of parcels."
          }
        ],
        "responses": {
          "200": {
            "description": "get post offices",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "locations": [
                        {
                          "address": {
                            "line_1": "174 BANK ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K2P1W0",
                            "country_alpha2": "CA",
                            "latitude": "45.41833",
                            "longitude": "-75.69919"
                          },
                          "name": "LAURIER WEST PO SHOPPERS DRUG MART #0988",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "12:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "3",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "4",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "5",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "6",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "7",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "58 SPARKS ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1P5A0",
                            "country_alpha2": "CA",
                            "latitude": "45.42321",
                            "longitude": "-75.69619"
                          },
                          "name": "OTTAWA POSTAL STATION B OTTAWA POSTAL STATION B",
                          "opening_hours": [
                            {
                              "day": "2",
                              "open_time": "09:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "3",
                              "open_time": "09:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "4",
                              "open_time": "09:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "5",
                              "open_time": "09:00",
                              "close_time": "17:00"
                            },
                            {
                              "day": "6",
                              "open_time": "09:00",
                              "close_time": "17:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "407 LAURIER AVE W",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1R7Z0",
                            "country_alpha2": "CA",
                            "latitude": "45.41751",
                            "longitude": "-75.70226"
                          },
                          "name": "MINTO PLACE PO SPOT PLUS",
                          "opening_hours": [
                            {
                              "day": "2",
                              "open_time": "08:00",
                              "close_time": "17:30"
                            },
                            {
                              "day": "3",
                              "open_time": "08:00",
                              "close_time": "17:30"
                            },
                            {
                              "day": "4",
                              "open_time": "08:00",
                              "close_time": "17:30"
                            },
                            {
                              "day": "5",
                              "open_time": "08:00",
                              "close_time": "17:30"
                            },
                            {
                              "day": "6",
                              "open_time": "08:00",
                              "close_time": "17:30"
                            },
                            {
                              "day": "7",
                              "open_time": "09:00",
                              "close_time": "14:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "437 ALBERT ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1R7X0",
                            "country_alpha2": "CA",
                            "latitude": "45.41710",
                            "longitude": "-75.70722"
                          },
                          "name": "ALBERT PD QUICKIE CONVENIENCE #25",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "3",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "4",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "5",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "6",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "7",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "332 BANK ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K2P1X0",
                            "country_alpha2": "CA",
                            "latitude": "45.41421",
                            "longitude": "-75.69555"
                          },
                          "name": "BANK AND GILMOUR PO QUICKIE CONVENIENCE #26",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "12:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "09:00",
                              "close_time": "19:30"
                            },
                            {
                              "day": "3",
                              "open_time": "09:00",
                              "close_time": "19:30"
                            },
                            {
                              "day": "4",
                              "open_time": "09:00",
                              "close_time": "19:30"
                            },
                            {
                              "day": "5",
                              "open_time": "09:00",
                              "close_time": "19:30"
                            },
                            {
                              "day": "6",
                              "open_time": "09:00",
                              "close_time": "19:30"
                            },
                            {
                              "day": "7",
                              "open_time": "12:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "348 ELGIN ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K2P1M0",
                            "country_alpha2": "CA",
                            "latitude": "45.41571",
                            "longitude": "-75.68867"
                          },
                          "name": "ELGIN PD QUICKIE CONVENIENCE #05",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "3",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "4",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "5",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "6",
                              "open_time": "10:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "7",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "9 RUE LAURIER",
                            "line_2": null,
                            "city": "GATINEAU",
                            "state": "QC",
                            "postal_code": "J8X3X0",
                            "country_alpha2": "CA",
                            "latitude": "45.42499",
                            "longitude": "-75.71551"
                          },
                          "name": "BP HULL B BP HULL B",
                          "opening_hours": [
                            {
                              "day": "2",
                              "open_time": "08:30",
                              "close_time": "16:00"
                            },
                            {
                              "day": "3",
                              "open_time": "08:30",
                              "close_time": "16:00"
                            },
                            {
                              "day": "4",
                              "open_time": "08:30",
                              "close_time": "16:00"
                            },
                            {
                              "day": "5",
                              "open_time": "08:30",
                              "close_time": "16:00"
                            },
                            {
                              "day": "6",
                              "open_time": "08:30",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "322 RIDEAU ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1N5W0",
                            "country_alpha2": "CA",
                            "latitude": "45.42916",
                            "longitude": "-75.68455"
                          },
                          "name": "NELSON PO SHOPPERS DRUG MART #1243",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "10:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "09:00",
                              "close_time": "21:00"
                            },
                            {
                              "day": "3",
                              "open_time": "09:00",
                              "close_time": "21:00"
                            },
                            {
                              "day": "4",
                              "open_time": "09:00",
                              "close_time": "21:00"
                            },
                            {
                              "day": "5",
                              "open_time": "09:00",
                              "close_time": "21:00"
                            },
                            {
                              "day": "6",
                              "open_time": "09:00",
                              "close_time": "21:00"
                            },
                            {
                              "day": "7",
                              "open_time": "10:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "163 BELL ST N",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1R6P0",
                            "country_alpha2": "CA",
                            "latitude": "45.40674",
                            "longitude": "-75.70580"
                          },
                          "name": "BELL ST PO QUICKIE CONVENIENCE #55",
                          "opening_hours": [
                            {
                              "day": "2",
                              "open_time": "10:00",
                              "close_time": "19:00"
                            },
                            {
                              "day": "3",
                              "open_time": "10:00",
                              "close_time": "19:00"
                            },
                            {
                              "day": "4",
                              "open_time": "10:00",
                              "close_time": "19:00"
                            },
                            {
                              "day": "5",
                              "open_time": "10:00",
                              "close_time": "19:00"
                            },
                            {
                              "day": "6",
                              "open_time": "10:00",
                              "close_time": "19:00"
                            },
                            {
                              "day": "7",
                              "open_time": "12:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
                          ]
                        },
                        {
                          "address": {
                            "line_1": "700 BANK ST",
                            "line_2": null,
                            "city": "OTTAWA",
                            "state": "ON",
                            "postal_code": "K1S3V0",
                            "country_alpha2": "CA",
                            "latitude": "45.40479",
                            "longitude": "-75.68983"
                          },
                          "name": "GLEBE PO SHOPPERS DRUG MART #1258",
                          "opening_hours": [
                            {
                              "day": "1",
                              "open_time": "12:00",
                              "close_time": "16:00"
                            },
                            {
                              "day": "2",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "3",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "4",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "5",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "6",
                              "open_time": "08:00",
                              "close_time": "20:00"
                            },
                            {
                              "day": "7",
                              "open_time": "11:00",
                              "close_time": "16:00"
                            }
                          ],
                          "phone_number": null,
                          "service_types": [
                            "bilingual_designation"
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
                    "summary": "get post offices"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/location_canada_post_list"
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
                          "We do not support locations for Canada Post in United States."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List Canada Post Locations",
                            "url": "https://developers.easyship.com/reference/locations_canada_post_index"
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
                          "Unable to retrieve Canada Post service point location. Please contact Easyship support."
                        ],
                        "links": [
                          {
                            "kind": "documentation",
                            "name": "Errors",
                            "url": "https://developers.easyship.com/reference/errors"
                          },
                          {
                            "kind": "documentation",
                            "name": "List Canada Post Locations",
                            "url": "https://developers.easyship.com/reference/locations_canada_post_index"
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
      "location_canada_post_list": {
        "type": "object",
        "description": "List of Canada Post locations",
        "additionalProperties": false,
        "properties": {
          "locations": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/LocationCanadaPost"
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
      "LocationCanadaPost": {
        "allOf": [
          {
            "$ref": "#/components/schemas/Location"
          },
          {
            "description": "Canada Post Location",
            "type": "object",
            "properties": {
              "service_types": {
                "type": "array",
                "description": "Supported types for the location\n* bilingual-designation: Indicates that the Post Office provides bilingual services (English and French)\n",
                "items": {
                  "type": "string",
                  "enum": [
                    "bilingual_designation"
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