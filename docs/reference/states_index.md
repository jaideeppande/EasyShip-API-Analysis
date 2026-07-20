# List all States

Retrieve a list of states. 

Required authorization scope: `public.reference:read` 

This endpoint in only used for the United States, Canada, Australia and Mexico.


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
      "name": "States"
    }
  ],
  "paths": {
    "/2024-09/states": {
      "get": {
        "summary": "List all States",
        "tags": [
          "States"
        ],
        "operationId": "states_index",
        "description": "Retrieve a list of states. \n\nRequired authorization scope: `public.reference:read` \n\nThis endpoint in only used for the United States, Canada, Australia and Mexico.\n",
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
          }
        ],
        "responses": {
          "200": {
            "description": "list of states",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "states": [
                        {
                          "abbr": "AL",
                          "country_id": 234,
                          "id": 1,
                          "name": "Alabama"
                        },
                        {
                          "abbr": "AK",
                          "country_id": 234,
                          "id": 2,
                          "name": "Alaska"
                        },
                        {
                          "abbr": "AZ",
                          "country_id": 234,
                          "id": 3,
                          "name": "Arizona"
                        },
                        {
                          "abbr": "AR",
                          "country_id": 234,
                          "id": 4,
                          "name": "Arkansas"
                        },
                        {
                          "abbr": "CA",
                          "country_id": 234,
                          "id": 5,
                          "name": "California"
                        },
                        {
                          "abbr": "CO",
                          "country_id": 234,
                          "id": 6,
                          "name": "Colorado"
                        },
                        {
                          "abbr": "CT",
                          "country_id": 234,
                          "id": 7,
                          "name": "Connecticut"
                        },
                        {
                          "abbr": "DE",
                          "country_id": 234,
                          "id": 8,
                          "name": "Delaware"
                        },
                        {
                          "abbr": "DC",
                          "country_id": 234,
                          "id": 9,
                          "name": "District of Columbia"
                        },
                        {
                          "abbr": "FL",
                          "country_id": 234,
                          "id": 10,
                          "name": "Florida"
                        },
                        {
                          "abbr": "GA",
                          "country_id": 234,
                          "id": 11,
                          "name": "Georgia"
                        },
                        {
                          "abbr": "HI",
                          "country_id": 234,
                          "id": 12,
                          "name": "Hawaii"
                        },
                        {
                          "abbr": "ID",
                          "country_id": 234,
                          "id": 13,
                          "name": "Idaho"
                        },
                        {
                          "abbr": "IL",
                          "country_id": 234,
                          "id": 14,
                          "name": "Illinois"
                        },
                        {
                          "abbr": "IN",
                          "country_id": 234,
                          "id": 15,
                          "name": "Indiana"
                        },
                        {
                          "abbr": "IA",
                          "country_id": 234,
                          "id": 16,
                          "name": "Iowa"
                        },
                        {
                          "abbr": "KS",
                          "country_id": 234,
                          "id": 17,
                          "name": "Kansas"
                        },
                        {
                          "abbr": "KY",
                          "country_id": 234,
                          "id": 18,
                          "name": "Kentucky"
                        },
                        {
                          "abbr": "LA",
                          "country_id": 234,
                          "id": 19,
                          "name": "Louisiana"
                        },
                        {
                          "abbr": "ME",
                          "country_id": 234,
                          "id": 20,
                          "name": "Maine"
                        }
                      ],
                      "meta": {
                        "pagination": {
                          "page": 1,
                          "next": 2,
                          "count": 112
                        },
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477"
                      }
                    },
                    "summary": "list of states"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/state_list"
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
      "state_list": {
        "type": "object",
        "description": "List of states",
        "additionalProperties": false,
        "properties": {
          "states": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/State"
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
      "CountryID": {
        "type": "integer",
        "description": "Country ID based on Countries API",
        "enum": [
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          10,
          11,
          12,
          13,
          14,
          15,
          16,
          17,
          18,
          19,
          20,
          21,
          22,
          23,
          24,
          25,
          26,
          27,
          28,
          29,
          30,
          31,
          32,
          33,
          34,
          35,
          36,
          37,
          38,
          39,
          40,
          41,
          42,
          43,
          44,
          45,
          46,
          47,
          48,
          49,
          50,
          51,
          52,
          53,
          54,
          55,
          56,
          57,
          58,
          59,
          60,
          61,
          62,
          63,
          64,
          65,
          66,
          67,
          68,
          69,
          70,
          71,
          72,
          73,
          74,
          75,
          76,
          77,
          78,
          79,
          80,
          81,
          82,
          83,
          84,
          85,
          86,
          87,
          88,
          89,
          90,
          91,
          92,
          93,
          94,
          95,
          96,
          97,
          98,
          99,
          100,
          101,
          102,
          103,
          104,
          105,
          106,
          107,
          108,
          109,
          110,
          111,
          112,
          113,
          114,
          115,
          116,
          117,
          118,
          119,
          120,
          121,
          122,
          123,
          124,
          125,
          126,
          127,
          128,
          129,
          130,
          131,
          132,
          133,
          134,
          135,
          136,
          137,
          138,
          139,
          140,
          141,
          142,
          143,
          144,
          145,
          146,
          147,
          148,
          149,
          150,
          151,
          152,
          153,
          154,
          155,
          156,
          157,
          158,
          159,
          160,
          161,
          162,
          163,
          164,
          165,
          166,
          167,
          168,
          169,
          170,
          171,
          172,
          173,
          174,
          175,
          176,
          177,
          178,
          179,
          180,
          181,
          182,
          183,
          184,
          185,
          186,
          187,
          188,
          189,
          190,
          191,
          192,
          193,
          194,
          195,
          196,
          197,
          198,
          199,
          200,
          201,
          202,
          203,
          204,
          205,
          206,
          207,
          208,
          209,
          210,
          211,
          212,
          213,
          214,
          215,
          216,
          217,
          218,
          219,
          220,
          221,
          222,
          223,
          224,
          225,
          226,
          227,
          228,
          229,
          230,
          231,
          232,
          233,
          234,
          235,
          236,
          237,
          238,
          239,
          240,
          241,
          242,
          243,
          244,
          245,
          246,
          247,
          248,
          249,
          250
        ]
      },
      "State": {
        "type": "object",
        "description": "State",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "integer",
            "description": "State ID",
            "example": 1
          },
          "name": {
            "type": "string",
            "description": "State name",
            "example": "Alabama"
          },
          "abbr": {
            "type": "string",
            "description": "2 letter abbreviations state name",
            "example": "AL"
          },
          "country_id": {
            "$ref": "#/components/schemas/CountryID"
          }
        }
      }
    }
  }
}
```