# Create Label

Create a label for an existing shipment and retrieve it synchronously.

Required authorization scope: `public.label:write`

This API **finalizes** a shipment created via the Shipment API. Executing this call will **book** the shipment with the selected courier, trigger label generation, and prepare all necessary shipping documents—provided your account balance is sufficient.

> You can enter a `courier_service_id` to assign a specific courier service in case your shipment has no assigned courier yet, or you need to overwrite the one suggested by default. Your shipment will be confirmed. If there is no assigned courier service and you leave the `courier_service_id` field blank, we will automatically assign the best value for money courier to your shipment.

> 🚧 This API is in beta (subject to change).


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
    "/2024-09/shipments/{shipment_id}/label": {
      "post": {
        "summary": "Create Label",
        "tags": [
          "Shipments"
        ],
        "operationId": "shipment_labels_create",
        "description": "Create a label for an existing shipment and retrieve it synchronously.\n\nRequired authorization scope: `public.label:write`\n\nThis API **finalizes** a shipment created via the Shipment API. Executing this call will **book** the shipment with the selected courier, trigger label generation, and prepare all necessary shipping documents—provided your account balance is sufficient.\n\n> You can enter a `courier_service_id` to assign a specific courier service in case your shipment has no assigned courier yet, or you need to overwrite the one suggested by default. Your shipment will be confirmed. If there is no assigned courier service and you leave the `courier_service_id` field blank, we will automatically assign the best value for money courier to your shipment.\n\n> 🚧 This API is in beta (subject to change).\n",
        "security": [
          {
            "Bearer": []
          }
        ],
        "parameters": [
          {
            "name": "shipment_id",
            "in": "path",
            "required": true,
            "description": "Easyship Shipment ID",
            "schema": {
              "type": "string"
            }
          }
        ],
        "responses": {
          "201": {
            "description": "label successfully created",
            "content": {
              "application/json": {
                "examples": {
                  "default": {
                    "value": {
                      "shipment": {
                        "easyship_shipment_id": "ESSG10006001",
                        "buyer_regulatory_identifiers": {
                          "ein": null,
                          "ssn": null,
                          "vat_number": null
                        },
                        "consignee_tax_id": null,
                        "courier_service": {
                          "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "courier_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                          "easyship_courier_service": true,
                          "name": "FedEx Economy HK",
                          "umbrella_name": "FedEx"
                        },
                        "created_at": "2022-02-22T12:21:00Z",
                        "currency": "HKD",
                        "delivery_state": "not_created",
                        "destination_address": {
                          "city": "SINGAPORE",
                          "company_name": null,
                          "contact_email": "test@test.com",
                          "contact_name": "Test McTest",
                          "contact_phone": "+6512345678",
                          "country_alpha2": "SG",
                          "delivery_instructions": "Beware of the dog",
                          "line_1": "Orchard Road 5th",
                          "line_2": null,
                          "postal_code": "546080",
                          "state": "SINGAPORE"
                        },
                        "eei_reference": null,
                        "incoterms": "DDU",
                        "insurance": {
                          "is_insured": true,
                          "insured_amount": 10,
                          "insured_currency": "HKD"
                        },
                        "label_generated_at": null,
                        "label_paid_at": "2022-02-22T12:21:00Z",
                        "label_state": "failed",
                        "last_failure_http_response_messages": [],
                        "metadata": {},
                        "order_data": {
                          "buyer_notes": null,
                          "buyer_selected_courier_name": null,
                          "order_created_at": null,
                          "order_tag_list": [],
                          "platform_name": null,
                          "platform_order_number": null,
                          "seller_notes": null
                        },
                        "origin_address": {
                          "city": "City",
                          "company_name": "Test Plc.",
                          "contact_email": "asd@asd.com",
                          "contact_name": "Foo Bar",
                          "contact_phone": "+852-1234-5678",
                          "country_alpha2": "HK",
                          "line_1": "123 Test Street",
                          "line_2": "Block 3",
                          "postal_code": "ABC123",
                          "state": "State"
                        },
                        "parcels": [
                          {
                            "box": {
                              "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                              "name": "small_box",
                              "outer_dimensions": {
                                "length": 15,
                                "width": 7,
                                "height": 25
                              },
                              "slug": "small_box",
                              "type": "box",
                              "weight": 3
                            },
                            "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                            "items": [
                              {
                                "actual_weight": 2,
                                "category": "Mobile Phones",
                                "contains_battery_pi966": false,
                                "contains_battery_pi967": true,
                                "contains_liquids": false,
                                "declared_currency": "HKD",
                                "declared_customs_value": 100,
                                "description": "Testing Testing",
                                "dimensions": {
                                  "length": 10,
                                  "width": 10,
                                  "height": 10
                                },
                                "hs_code": null,
                                "id": "01563646-58c1-4607-8fe0-cae3e33c0000",
                                "origin_country_alpha2": null,
                                "origin_currency": "HKD",
                                "origin_customs_value": 100,
                                "quantity": 1,
                                "sku": "12341234"
                              },
                              {
                                "actual_weight": 2,
                                "category": "Mobile Phones",
                                "contains_battery_pi966": false,
                                "contains_battery_pi967": true,
                                "contains_liquids": false,
                                "declared_currency": "HKD",
                                "declared_customs_value": 100,
                                "description": "Testing Testing",
                                "dimensions": {
                                  "length": 10,
                                  "width": 10,
                                  "height": 10
                                },
                                "hs_code": null,
                                "id": "01563646-58c1-4607-8fe0-cae3e33c0001",
                                "origin_country_alpha2": null,
                                "origin_currency": "HKD",
                                "origin_customs_value": 100,
                                "quantity": 1,
                                "sku": "12341234"
                              }
                            ],
                            "total_actual_weight": 30
                          }
                        ],
                        "pickup_state": "not_requested",
                        "rates": [],
                        "regulatory_identifiers": {
                          "eori": null,
                          "ioss": null,
                          "vat_number": null
                        },
                        "return": false,
                        "return_address": {
                          "city": "City",
                          "company_name": "Test Plc.",
                          "contact_email": "asd@asd.com",
                          "contact_name": "Foo Bar",
                          "contact_phone": "+852-1234-5678",
                          "country_alpha2": "HK",
                          "line_1": "123 Test Street",
                          "line_2": "Block 3",
                          "postal_code": "ABC123",
                          "state": "State"
                        },
                        "sender_address": {
                          "city": "City",
                          "company_name": "Test Plc.",
                          "contact_email": "asd@asd.com",
                          "contact_name": "Foo Bar",
                          "contact_phone": "+852-1234-5678",
                          "country_alpha2": "HK",
                          "line_1": "123 Test Street",
                          "line_2": "Block 3",
                          "postal_code": "ABC123",
                          "state": "State"
                        },
                        "set_as_residential": false,
                        "shipment_state": "created",
                        "shipping_documents": [
                          {
                            "base64_encoded_strings": [
                              "JVBERi0xLjUKJf//////AAAAAAoxIDAgb2JqCjw8Ci9Qcm9kdWNlciAoUnVieSBDb21iaW5lUERGIDEuMC4zMSBMaWJyYXJ5KQovQ3JlYXRpb25EYXRlIChEOjIwMjIwMjIyMTIyMTAwKzAwJzAwKQo+PgplbmRvYmoKCjIgMCBvYmoKPDwKL1R5cGUgL0NhdGFsb2cKL1BhZ2VzIDMgMCBSCj4+CmVuZG9iagoKMyAwIG9iago8PAovVHlwZSAvUGFnZXMKL0NvdW50IDAKL0tpZHMgW10KPj4KZW5kb2JqCgp4cmVmCjAgNAowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwMjAgMDAwMDAgbiAKMDAwMDAwMDEyNCAwMDAwMCBuIAowMDAwMDAwMTc0IDAwMDAwIG4gCnRyYWlsZXIKPDwKL1Jvb3QgMiAwIFIKL1NpemUgNAovSW5mbyAxIDAgUgo+PgpzdGFydHhyZWYKMjI3CiUlRU9G"
                            ],
                            "category": "label",
                            "format": "pdf",
                            "page_size": "a4",
                            "required": true,
                            "url": null
                          },
                          {
                            "base64_encoded_strings": [
                              "JVBERi0xLjQKJf////8KMSAwIG9iago8PCAvQ3JlYXRvciA8ZmVmZjAwNTAwMDcyMDA2MTAwNzcwMDZlPgovUHJvZHVjZXIgPGZlZmYwMDUwMDA3MjAwNjEwMDc3MDA2ZT4KPj4KZW5kb2JqCjIgMCBvYmoKPDwgL1BhZ2VzIDMgMCBSCi9UeXBlIC9DYXRhbG9nCj4+CmVuZG9iagozIDAgb2JqCjw8IC9Db3VudCAxCi9LaWRzIFs1IDAgUl0KL1R5cGUgL1BhZ2VzCj4+CmVuZG9iago0IDAgb2JqCjw8IC9MZW5ndGggMTk2MDkKPj4Kc3RyZWFtCnEKCkJUCjEzMi45ODggODAxLjAgVGQKL0YyLjAgMTIgVGYKPDUzNjg2OTcwNzA2NTcyZDU3MzIwNDQ2NTYzNmM2MTcyNjE3NDY5NmY2ZTIwNjY2ZjcyMjA1MzY1NjM3NDY5NmY2ZTIwNDk0OTIwNGM2OTc0Njg2OTc1NmQyMDQzNjU2YzZjNzMyMDJmMjA0MjYxNzQ3NDY1NzI2OTY1NzM+IFRqCkVUCgoKQlQKMzIuNSA3NzkuNDg0IFRkCi9GMS4wIDEwIFRmCls8NTc+IDI0IDw0MTUyNGU0OTRlNDc+XSBUSgpFVAoKMzIuNSA3NzguMjM0IG0KNzkuNDcgNzc4LjIzNCBsClMKCkJUCjc5LjQ3IDc3OS40ODQgVGQKL0YxLjAgMTAgVGYKWzwzYTIwNGM0OTU0NDg0OTU1NGQyMDQyNDE+IDkyIDw1NDU0NDU1MjQ5NDU1MzIwNDk0NDQ1NGU1NDQ5NDY0OTQ1NDQyMDQyNTkyMDU0NDg0NTIwNGQ0MTRlNTU0Nj4gNTUgPDQxNDM1NDU1NTI0NTUyMjA0MTUzMjA0MjQ1NDk0ZTQ3MjA0NDQ1NDY0NTQzNTQ0OTU2NDUyMDQ2NGY1MjIwNTM0MTQ2NDU1NDU5Pl0gVEoKRVQKCgpCVAozMi41IDc2OS42ODQgVGQKL0YxLjAgMTAgVGYKWzw1MjQ1NDE1MzRmNGU1MzJjMjA0ZjUyMjA1NDQ4NDE+IDkyIDw1NDIwNDg0MT4gNDYgPDU2NDUyMDQyNDU0NTRlMjA0NDQxNGQ0MTQ3NDU0NDJjMjA0ZDU1NTM1NDIwNGU0ZjU0MjA0MjQ1MjA1MzQ4NDk1MDUwNDU0NDIwNDI1OTIwNDE0OTUyMmU+XSBUSgpFVAoKMSB3Ci9EZXZpY2VSR0IgQ1MKMC4wIDAuMCAwLjAgU0NOCgpCVAozNy41IDc1NC43MTYgVGQKL0YxLjAgOCBUZgo8NTM2ODY5NzA2ZDY1NmU3NDIwNDQ2NTc0NjE2OTZjNzMyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuNSA3MzYuODc2IFRkCi9GMS4wIDggVGYKWzw0ZDYxNzM3NDY1NzIyMDQxNjk3MjIwNTc+IDM3IDw2MTc5NjI2OTZjNmMyMDRlNzU2ZDYyNjU3MjIwM2E+XSBUSgpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTcyLjUgNzM2Ljg3NiBUZAovRjEuMCA4IFRmCjw0NTUzNTM0NzMxMzAzMDMwMzYzMDMwMzE+IFRqCkVUCgoxNzIuNSA3MzUuNjI2IG0KMjI5LjQxMiA3MzUuNjI2IGwKUwoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozMDcuNSA3MzYuODc2IFRkCi9GMS4wIDggVGYKPDRmNzI2OTY3Njk2ZTIwMjg0ZjcwNzQ2OTZmNmU2MTZjMjkyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKNDQyLjUgNzM2Ljg3NiBUZAovRjEuMCA4IFRmCjw0ODZmNmU2NzIwNGI2ZjZlNjc+IFRqCkVUCgo0NDIuNSA3MzUuNjI2IG0KNDgzLjEgNzM1LjYyNiBsClMKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjMwNy41IDcxOS4wMzYgVGQKL0YxLjAgOCBUZgo8NDQ2NTczNzQ2OTZlNjE3NDY5NmY2ZTIwMjg0ZjcwNzQ2OTZmNmU2MTZjMjkyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKNDQyLjUgNzE5LjAzNiBUZAovRjEuMCA4IFRmCls8NTM2OTZlNjc2MTcwNmY3Mj4gMTggPDY1Pl0gVEoKRVQKCjQ0Mi41IDcxNy43ODYgbQo0NzguOTQ4IDcxNy43ODYgbApTCjEgdwowLjAgMC4wIDAuMCBTQ04KMzIuNSA3MDkuNTA0IG0KMTA1Ljk1MTU2IDcwOS41MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMyLjUgNzEwLjAwNCBtCjMyLjUgNjgzLjgyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3LjUgNjk3LjE5NiBUZAovRjEuMCA4IFRmCjw1MzY4Njk3MDcwNjU3MjI3NzM+IFRqCkVUCgoKQlQKMzcuNSA2ODkuMzU2IFRkCi9GMS4wIDggVGYKPDQ5NmU2NjZmNzI2ZDYxNzQ2OTZmNmUyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoxMDUuOTUxNTYgNzA5LjUwNCBtCjMwMi44NDkzIDcwOS41MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KMzAyLjg0OTMgNzA5LjUwNCBtCjM4Mi40ODUwMiA3MDkuNTA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzA3Ljg0OTMgNjk3LjE5NiBUZAovRjEuMCA4IFRmCjw0MzZmNmU3MzY5Njc2ZTY1NjUyNzczPiBUagpFVAoKCkJUCjMwNy44NDkzIDY4OS4zNTYgVGQKL0YxLjAgOCBUZgo8NDk2ZTY2NmY3MjZkNjE3NDY5NmY2ZTNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozODIuNDg1MDIgNzA5LjUwNCBtCjU3Mi41IDcwOS41MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDcxMC4wMDQgbQo1NzIuNSA2ODMuODI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCjMyLjUgNjgzLjgyNCBtCjMyLjUgNjY1Ljk4NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3LjUgNjcxLjUxNiBUZAovRjEuMCA4IFRmCjw0ZTYxNmQ2NTNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTEwLjk1MTU2IDY3MS41MTYgVGQKL0YxLjAgOCBUZgo8NDY2ZjZmMjA0MjYxNzI+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozMDcuODQ5MyA2NzEuNTE2IFRkCi9GMS4wIDggVGYKPDRlNjE2ZDY1M2E+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDY4My44MjQgbQo1NzIuNSA2NjUuOTg0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzg3LjQ4NTAyIDY3MS41MTYgVGQKL0YxLjAgOCBUZgpbPDU0PiAxMTEgPDY1NzM3NDIwNGQ2MzU0PiAxMTEgPDY1NzM3ND5dIFRKCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjMyLjUgNjY1Ljk4NCBtCjMyLjUgNjQwLjMwNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3LjUgNjUzLjY3NiBUZAovRjEuMCA4IFRmCls8NDE2NDY0NzI+IDE4IDw2NTczNzMyMDNhPl0gVEoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjExMC45NTE1NiA2NTMuNjc2IFRkCi9GMS4wIDggVGYKWzwzMTMyMzMyMDU0PiAxMTEgPDY1NzM3NDIwNTM3NDcyPiAxOCA8NjU2NTc0MmMyMDQyNmM2ZjYzNmIyMDMzMmMyMDU1NmU2OTc0MjAzMTMwMzAzMDJjMjA0MTQyNDMzMTMyMzMyMDQzNjk3NDc5PiA3NCA8MmM+XSBUSgpFVAoKCkJUCjExMC45NTE1NiA2NDUuODM2IFRkCi9GMS4wIDggVGYKPDUzNzQ2MTc0NjUyYzIwNDg2ZjZlNjcyMDRiNmY2ZTY3PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzA3Ljg0OTMgNjUzLjY3NiBUZAovRjEuMCA4IFRmCls8NDE2NDY0NzI+IDE4IDw2NTczNzMyMDNhPl0gVEoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KNTcyLjUgNjY1Ljk4NCBtCjU3Mi41IDY0MC4zMDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozODcuNDg1MDIgNjUzLjY3NiBUZAovRjEuMCA4IFRmCls8NGY3Mj4gMTggPDYzNjg2MTcyPiAxOCA8NjQyMDUyNmY2MTY0MjAzNTc0NjgyYzIwMzUzNDM2MzAzODMwMjA1MzQ5NGU0NzQxNTA0ZjUyNDUyYz5dIFRKCkVUCgoKQlQKMzg3LjQ4NTAyIDY0NS44MzYgVGQKL0YxLjAgOCBUZgpbPDUzNDk0ZTQ3NDE1MDRmNTI0NTJjMjA1MzY5NmU2NzYxNzA2ZjcyPiAxOCA8NjU+XSBUSgpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMi41IDYyMi40NjQgbQoxMDUuOTUxNTYgNjIyLjQ2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzIuNSA2NDAuMzA0IG0KMzIuNSA2MjEuOTY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuNSA2MjcuOTk2IFRkCi9GMS4wIDggVGYKPDQzNmY2ZTc0NjE2Mzc0MjA0ZTc1NmQ2MjY1NzIyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoxMDUuOTUxNTYgNjIyLjQ2NCBtCjMwMi44NDkzIDYyMi40NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAoxMTAuOTUxNTYgNjI3Ljk5NiBUZAovRjEuMCA4IFRmCjwyYjM4MzUzMjJkMzEzMjMzMzQyZDM1MzYzNzM4PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMDIuODQ5MyA2MjIuNDY0IG0KMzgyLjQ4NTAyIDYyMi40NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozMDcuODQ5MyA2MjcuOTk2IFRkCi9GMS4wIDggVGYKPDQzNmY2ZTc0NjE2Mzc0MjA0ZTc1NmQ2MjY1NzIyMDNhPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozODIuNDg1MDIgNjIyLjQ2NCBtCjU3Mi41IDYyMi40NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDY0MC4zMDQgbQo1NzIuNSA2MjEuOTY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzg3LjQ4NTAyIDYyNy45OTYgVGQKL0YxLjAgOCBUZgo8MmIzNjM1MzEzMjMzMzQzNTM2MzczOD4gVGoKRVQKCgpCVAozMi41IDYxMS43NTIgVGQKL0YxLjAgOCBUZgo8NTM2NTZjNjU2Mzc0MjA3NDY4NjUyMDYxNzA3MDZjNjk2MzYxNjI2YzY1MjA2MjYxNzQ3NDY1NzI3OTIwNzQ3OTcwNjUyODczMjkyMDYxNmU2NDIwNjY2OTZjNmMyMDY5NmUyMDc0Njg2NTIwNjI2YzYxNmU2YjczMjAzYT4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDYwNC42MjQgbQozMTIuNSA2MDQuNjI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDU4Ni43ODQgbQozMTIuNSA1ODYuNzg0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDYwNS4xMjQgbQo1Mi41IDU4Ni4yODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDYwNS4xMjQgbQozMTIuNSA1ODYuMjg0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTM2LjkyIDU5Mi4zMTYgVGQKL0YxLjAgOCBUZgpbPDQyNjE3NDc0NjU3Mjc5MjA1ND4gMTExIDw3OTcwNjUyMDViMjA0OTRkNTAyMDQzNGY0NDQ1NWQ+XSBUSgpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA2MDQuNjI0IG0KNDQyLjUgNjA0LjYyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTg2Ljc4NCBtCjQ0Mi41IDU4Ni43ODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDYwNS4xMjQgbQozMTIuNSA1ODYuMjg0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA2MDUuMTI0IG0KNDQyLjUgNTg2LjI4NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM2OC4wNzYgNTkyLjMxNiBUZAovRjEuMCA4IFRmCjw1MDY5NjU2MzY1PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA2MDQuNjI0IG0KNTcyLjUgNjA0LjYyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTg2Ljc4NCBtCjU3Mi41IDU4Ni43ODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDYwNS4xMjQgbQo0NDIuNSA1ODYuMjg0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1NzIuNSA2MDUuMTI0IG0KNTcyLjUgNTg2LjI4NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjQ1Ny4xMTIgNTkyLjMxNiBUZAovRjEuMCA4IFRmCls8NGU2NTc0MjA1Nz4gNTcgPDY1Njk2NzY4NzQyMDcwNjU3MjIwNTA2MTYzNmI2MTY3NjUyMDI4NmI2NzI5Pl0gVEoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3Ljg4NSA1NzIuMTk4IFRkCi9GMy4xIDEwIFRmCjwyMT4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSA1ODYuNzg0IG0KMTgyLjUgNTg2Ljc4NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSA1MjUuNTI0IG0KMTgyLjUgNTI1LjUyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSA1ODcuMjg0IG0KNTIuNSA1MjUuMDI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA1ODcuMjg0IG0KMTgyLjUgNTI1LjAyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjgwLjA0OCA1NzMuNzk2IFRkCi9GMS4wIDggVGYKPDU1NGUzMzM0MzgzMD4gVGoKRVQKCgpCVAoxMDkuMzkyIDU3My43OTYgVGQKL0YzLjEgOCBUZgo8MjI+IFRqCkVUCgoKQlQKMTE3LjU3NiA1NzMuNzk2IFRkCi9GMS4wIDggVGYKPDUwNDkzOTM2MzUyMDViNDU0YzQ5NWQ+IFRqCkVUCgoKQlQKODUuODQ0IDU2NS45NTYgVGQKL0YxLjAgOCBUZgo8NGM2OTc0Njg2OTc1NmQyMDQ5NmY2ZTIwNDM2NTZjNmM3MzIwMmY+IFRqCkVUCgoKQlQKOTAuNjY0IDU1OC4xMTYgVGQKL0YxLjAgOCBUZgpbPDQyNjE3NDc0NjU3MjY5NjU3MzIwNGY0ZTRjPiAxMTEgPDU5Pl0gVEoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNTg2Ljc4NCBtCjMxMi41IDU4Ni43ODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDU2Ni4zNjQgbQozMTIuNSA1NjYuMzY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA1ODcuMjg0IG0KMTgyLjUgNTY1Ljg2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTg3LjI4NCBtCjMxMi41IDU2NS44NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAoyMTEuMzg4IDU3My43OTYgVGQKL0YxLjAgOCBUZgo8NDM2NTZjNmMyZjQyNjE3NDc0NjU3Mjc5PiBUagpFVAoKCkJUCjI1My40NTIgNTczLjc5NiBUZAovRjMuMCA4IFRmCjxiMj4gVGoKRVQKCgpCVAoyNjEuNjM2IDU3My43OTYgVGQKL0YxLjAgOCBUZgo8MzIyZTM3NTc2OD4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTg2Ljc4NCBtCjQ0Mi41IDU4Ni43ODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDU2Ni4zNjQgbQo0NDIuNSA1NjYuMzY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA1ODcuMjg0IG0KMzEyLjUgNTY1Ljg2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTg3LjI4NCBtCjQ0Mi41IDU2NS44NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTg2Ljc4NCBtCjU3Mi41IDU4Ni43ODQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDU2Ni4zNjQgbQo1NzIuNSA1NjYuMzY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA1ODcuMjg0IG0KNDQyLjUgNTY1Ljg2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTcyLjUgNTg3LjI4NCBtCjU3Mi41IDU2NS44NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3Ljg4NSA1NTEuNzc4IFRkCi9GMy4xIDEwIFRmCjwyMT4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNTY2LjM2NCBtCjMxMi41IDU2Ni4zNjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDU0NS45NDQgbQozMTIuNSA1NDUuOTQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA1NjYuODY0IG0KMTgyLjUgNTQ1LjQ0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTY2Ljg2NCBtCjMxMi41IDU0NS40NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAoxOTkuMTkyIDU1My4zNzYgVGQKL0YxLjAgOCBUZgo8NDM2NTZjNmMyMDNlMjAzMjJlMzcyMDU3NjgyMDYyNzU3NDIwPiBUagpFVAoKCkJUCjI2My40MjQgNTUzLjM3NiBUZAovRjMuMCA4IFRmCjxiMj4gVGoKRVQKCgpCVAoyNzEuNjA4IDU1My4zNzYgVGQKL0YxLjAgOCBUZgo8MjAzMjMwMjA1NzY4PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA1NjYuMzY0IG0KNDQyLjUgNTY2LjM2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTQ1Ljk0NCBtCjQ0Mi41IDU0NS45NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDU2Ni44NjQgbQozMTIuNSA1NDUuNDQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA1NjYuODY0IG0KNDQyLjUgNTQ1LjQ0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA1NjYuMzY0IG0KNTcyLjUgNTY2LjM2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTQ1Ljk0NCBtCjU3Mi41IDU0NS45NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDU2Ni44NjQgbQo0NDIuNSA1NDUuNDQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1NzIuNSA1NjYuODY0IG0KNTcyLjUgNTQ1LjQ0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuODg1IDUzMS4zNTggVGQKL0YzLjEgMTAgVGYKPDIxPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA1NDUuOTQ0IG0KMzEyLjUgNTQ1Ljk0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNTI1LjUyNCBtCjMxMi41IDUyNS41MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDU0Ni40NDQgbQoxODIuNSA1MjUuMDI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA1NDYuNDQ0IG0KMzEyLjUgNTI1LjAyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjE5MC44OTIgNTMyLjk1NiBUZAovRjEuMCA4IFRmCjw0MjYxNzQ3NDY1NzI3OTIwM2UyMDMyMmUzNzIwNTc2ODIwNjI3NTc0MjA+IFRqCkVUCgoKQlQKMjY3LjI3NiA1MzIuOTU2IFRkCi9GMy4wIDggVGYKPGIyPiBUagpFVAoKCkJUCjI3NS40NiA1MzIuOTU2IFRkCi9GMS4wIDggVGYKPDIwMzEzMDMwMjA1NzY4PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA1NDUuOTQ0IG0KNDQyLjUgNTQ1Ljk0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTI1LjUyNCBtCjQ0Mi41IDUyNS41MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDU0Ni40NDQgbQozMTIuNSA1MjUuMDI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA1NDYuNDQ0IG0KNDQyLjUgNTI1LjAyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA1NDUuOTQ0IG0KNTcyLjUgNTQ1Ljk0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTI1LjUyNCBtCjU3Mi41IDUyNS41MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDU0Ni40NDQgbQo0NDIuNSA1MjUuMDI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1NzIuNSA1NDYuNDQ0IG0KNTcyLjUgNTI1LjAyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuODg1IDUxMC45MzggVGQKL0YzLjEgMTAgVGYKPDIxPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDUyNS41MjQgbQozMTIuNSA1MjUuNTI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDQ5OS44NDQgbQozMTIuNSA0OTkuODQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDUyNi4wMjQgbQo1Mi41IDQ5OS4zNDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDUyNi4wMjQgbQozMTIuNSA0OTkuMzQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTQ2LjAyOCA1MTMuMjE2IFRkCi9GMS4wIDggVGYKPDU1NGUzMzM0MzgzMTIwN2MyMDUwNDkzOTM2MzYyMDViNDU0YzQ5NWQ+IFRqCkVUCgoKQlQKOTAuMjQgNTA1LjM3NiBUZAovRjEuMCA4IFRmCjw0YzY5NzQ2ODY5NzU2ZDIwNDk2ZjZlMjA0MzY1NmM2YzczMjAyZjIwNDI2MTc0NzQ2NTcyNjk2NTczMjA1MDYxNjM2YjY1NjQyMDc3Njk3NDY4MjA0NTcxNzU2OTcwNmQ2NTZlNzQ+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDUyNS41MjQgbQo0NDIuNSA1MjUuNTI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0OTkuODQ0IG0KNDQyLjUgNDk5Ljg0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTI2LjAyNCBtCjMxMi41IDQ5OS4zNDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDUyNi4wMjQgbQo0NDIuNSA0OTkuMzQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDUyNS41MjQgbQo1NzIuNSA1MjUuNTI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0OTkuODQ0IG0KNTcyLjUgNDk5Ljg0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTI2LjAyNCBtCjQ0Mi41IDQ5OS4zNDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDUyNi4wMjQgbQo1NzIuNSA0OTkuMzQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozNy44ODUgNDg1LjI1OCBUZAovRjMuMSAxMCBUZgo8MjM+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjUyLjUgNDk5Ljg0NCBtCjMxMi41IDQ5OS44NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjUyLjUgNDc0LjE2NCBtCjMxMi41IDQ3NC4xNjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjUyLjUgNTAwLjM0NCBtCjUyLjUgNDczLjY2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNTAwLjM0NCBtCjMxMi41IDQ3My42NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAoxNDYuMDI4IDQ4Ny41MzYgVGQKL0YxLjAgOCBUZgo8NTU0ZTMzMzQzODMxMjA3YzIwNTA0OTM5MzYzNzIwNWI0NTRjNDk1ZD4gVGoKRVQKCgpCVAo4OS41NjggNDc5LjY5NiBUZAovRjEuMCA4IFRmCjw0YzY5NzQ2ODY5NzU2ZDIwNDk2ZjZlMjA0MzY1NmM2YzczMjAyZjIwNDI2MTc0NzQ2NTcyNjk2NTczMjA0MzZmNmU3NDYxNjk2ZTY1NjQyMDY5NmUyMDQ1NzE3NTY5NzA2ZDY1NmU3ND4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNDk5Ljg0NCBtCjQ0Mi41IDQ5OS44NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQ3NC4xNjQgbQo0NDIuNSA0NzQuMTY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA1MDAuMzQ0IG0KMzEyLjUgNDczLjY2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTAwLjM0NCBtCjQ0Mi41IDQ3My42NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozNzUuNzc2IDQ4Ny41MzYgVGQKL0YxLjAgOCBUZgo8MzI+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDQ5OS44NDQgbQo1NzIuNSA0OTkuODQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0NzQuMTY0IG0KNTcyLjUgNDc0LjE2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNTAwLjM0NCBtCjQ0Mi41IDQ3My42NjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDUwMC4zNDQgbQo1NzIuNSA0NzMuNjY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKNTAyLjQ0IDQ4Ny41MzYgVGQKL0YxLjAgOCBUZgo8MzQyZTMwPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuODg1IDQ1OS41NzggVGQKL0YzLjEgMTAgVGYKPDIxPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDQ3NC4xNjQgbQoxODIuNSA0NzQuMTY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDQxMi45MDQgbQoxODIuNSA0MTIuOTA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1Mi41IDQ3NC42NjQgbQo1Mi41IDQxMi40MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDQ3NC42NjQgbQoxODIuNSA0MTIuNDA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKNzguNTggNDYxLjg1NiBUZAovRjEuMCA4IFRmCjw1NTRlMzMzMDM5MzAyMDdjMjA1MDQ5MzkzNjM4MjA1YjQ1NGM0ZDVkPiBUagpFVAoKCkJUCjY0LjQzNiA0NTQuMDE2IFRkCi9GMS4wIDggVGYKPDRjNjk3NDY4Njk3NTZkMjA0ZDY1NzQ2MTZjMjA0MzY1NmM2YzczMjAyZjIwNDI2MTc0NzQ2NTcyNjk2NTczPiBUagpFVAoKCkJUCjEwNy43IDQ0Ni4xNzYgVGQKL0YxLjAgOCBUZgpbPDRmNGU0Yz4gMTExIDw1OT5dIFRKCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDQ3NC4xNjQgbQozMTIuNSA0NzQuMTY0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA0NTMuNzQ0IG0KMzEyLjUgNDUzLjc0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNDc0LjY2NCBtCjE4Mi41IDQ1My4yNDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQ3NC42NjQgbQozMTIuNSA0NTMuMjQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTk3LjY3NiA0NjEuMTc2IFRkCi9GMS4wIDggVGYKPDQzNjU2YzZjMjAyZjIwNDI2MTc0NzQ2NTcyNzkyMD4gVGoKRVQKCgpCVAoyNDYuNDEyIDQ2MS4xNzYgVGQKL0YzLjAgOCBUZgo8YjI+IFRqCkVUCgoKQlQKMjU0LjU5NiA0NjEuMTc2IFRkCi9GMS4wIDggVGYKPDIwMzAyZTMzNjcyMDZjNjk3NDY4Njk3NTZkPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0NzQuMTY0IG0KNDQyLjUgNDc0LjE2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNDUzLjc0NCBtCjQ0Mi41IDQ1My43NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQ3NC42NjQgbQozMTIuNSA0NTMuMjQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0NzQuNjY0IG0KNDQyLjUgNDUzLjI0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0NzQuMTY0IG0KNTcyLjUgNDc0LjE2NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDUzLjc0NCBtCjU3Mi41IDQ1My43NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDQ3NC42NjQgbQo0NDIuNSA0NTMuMjQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1NzIuNSA0NzQuNjY0IG0KNTcyLjUgNDUzLjI0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMzcuODg1IDQzOS4xNTggVGQKL0YzLjEgMTAgVGYKPDIxPiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA0NTMuNzQ0IG0KMzEyLjUgNDUzLjc0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNDMzLjMyNCBtCjMxMi41IDQzMy4zMjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDQ1NC4yNDQgbQoxODIuNSA0MzIuODI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0NTQuMjQ0IG0KMzEyLjUgNDMyLjgyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjE5OC4wMDggNDQwLjc1NiBUZAovRjEuMCA4IFRmCjw0MzY1NmM2YzIwM2UyMDMwMmUzMzY3MjA2Mjc1NzQyMD4gVGoKRVQKCgpCVAoyNTIuNzUyIDQ0MC43NTYgVGQKL0YzLjAgOCBUZgo8YjI+IFRqCkVUCgoKQlQKMjYwLjkzNiA0NDAuNzU2IFRkCi9GMS4wIDggVGYKPDIwMzE2NzIwNmM2OTc0Njg2OTc1NmQ+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQ1My43NDQgbQo0NDIuNSA0NTMuNzQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0MzMuMzI0IG0KNDQyLjUgNDMzLjMyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNDU0LjI0NCBtCjMxMi41IDQzMi44MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDQ1NC4yNDQgbQo0NDIuNSA0MzIuODI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDQ1My43NDQgbQo1NzIuNSA0NTMuNzQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0MzMuMzI0IG0KNTcyLjUgNDMzLjMyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDU0LjI0NCBtCjQ0Mi41IDQzMi44MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjU3Mi41IDQ1NC4yNDQgbQo1NzIuNSA0MzIuODI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxIHcKMC4wIDAuMCAwLjAgU0NOCgpCVAozNy44ODUgNDE4LjczOCBUZAovRjMuMSAxMCBUZgo8MjE+IFRqCkVUCgoxIHcKMC4wIDAuMCAwLjAgU0NOCjE4Mi41IDQzMy4zMjQgbQozMTIuNSA0MzMuMzI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoxODIuNSA0MTIuOTA0IG0KMzEyLjUgNDEyLjkwNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMTgyLjUgNDMzLjgyNCBtCjE4Mi41IDQxMi40MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQzMy44MjQgbQozMTIuNSA0MTIuNDA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgoKQlQKMTkxLjkzMiA0MjAuMzM2IFRkCi9GMS4wIDggVGYKPDQyNjE3NDc0NjU3Mjc5MjAzZTIwMzAyZTMzNjcyMDYyNzU3NDIwPiBUagpFVAoKCkJUCjI1OC44MjggNDIwLjMzNiBUZAovRjMuMCA4IFRmCjxiMj4gVGoKRVQKCgpCVAoyNjcuMDEyIDQyMC4zMzYgVGQKL0YxLjAgOCBUZgo8MjAzMjY3MjA2YzY5NzQ2ODY5NzU2ZD4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNDMzLjMyNCBtCjQ0Mi41IDQzMy4zMjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDQxMi45MDQgbQo0NDIuNSA0MTIuOTA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0MzMuODI0IG0KMzEyLjUgNDEyLjQwNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDMzLjgyNCBtCjQ0Mi41IDQxMi40MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDMzLjMyNCBtCjU3Mi41IDQzMy4zMjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDQxMi45MDQgbQo1NzIuNSA0MTIuOTA0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0MzMuODI0IG0KNDQyLjUgNDEyLjQwNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTcyLjUgNDMzLjgyNCBtCjU3Mi41IDQxMi40MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3Ljg4NSAzOTguMzE4IFRkCi9GMy4xIDEwIFRmCjwyMT4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSA0MTIuOTA0IG0KMzEyLjUgNDEyLjkwNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSAzODcuMjI0IG0KMzEyLjUgMzg3LjIyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSA0MTMuNDA0IG0KNTIuNSAzODYuNzI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0MTMuNDA0IG0KMzEyLjUgMzg2LjcyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjE0My41OCA0MDAuNTk2IFRkCi9GMS4wIDggVGYKPDU1NGUzMzMwMzkzMTIwN2MyMDUwNDkzOTM2MzkyMDViNDU0YzRkNWQ+IFRqCkVUCgoKQlQKODUuODY4IDM5Mi43NTYgVGQKL0YxLjAgOCBUZgo8NGM2OTc0Njg2OTc1NmQyMDRkNjU3NDYxNmMyMDQzNjU2YzZjNzMyMDJmMjA0MjYxNzQ3NDY1NzI2OTY1NzMyMDUwNjE2MzZiNjU2NDIwNzc2OTc0NjgyMDQ1NzE3NTY5NzA2ZDY1NmU3ND4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgNDEyLjkwNCBtCjQ0Mi41IDQxMi45MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDM4Ny4yMjQgbQo0NDIuNSAzODcuMjI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSA0MTMuNDA0IG0KMzEyLjUgMzg2LjcyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDEzLjQwNCBtCjQ0Mi41IDM4Ni43MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgNDEyLjkwNCBtCjU3Mi41IDQxMi45MDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDM4Ny4yMjQgbQo1NzIuNSAzODcuMjI0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSA0MTMuNDA0IG0KNDQyLjUgMzg2LjcyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTcyLjUgNDEzLjQwNCBtCjU3Mi41IDM4Ni43MjQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjM3Ljg4NSAzNzIuNjM4IFRkCi9GMy4xIDEwIFRmCjwyMT4gVGoKRVQKCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSAzODcuMjI0IG0KMzEyLjUgMzg3LjIyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSAzNjEuNTQ0IG0KMzEyLjUgMzYxLjU0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNTIuNSAzODcuNzI0IG0KNTIuNSAzNjEuMDQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSAzODcuNzI0IG0KMzEyLjUgMzYxLjA0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjE0My41OCAzNzQuOTE2IFRkCi9GMS4wIDggVGYKPDU1NGUzMzMwMzkzMTIwN2MyMDUwNDkzOTM3MzAyMDViNDU0YzRkNWQ+IFRqCkVUCgoKQlQKODUuMTk2IDM2Ny4wNzYgVGQKL0YxLjAgOCBUZgo8NGM2OTc0Njg2OTc1NmQyMDRkNjU3NDYxNmMyMDQzNjU2YzZjNzMyMDJmMjA0MjYxNzQ3NDY1NzI2OTY1NzMyMDQzNmY2ZTc0NjE2OTZlNjU2NDIwNjk2ZTIwNDU3MTc1Njk3MDZkNjU2ZTc0PiBUagpFVAoKMSB3CjAuMCAwLjAgMC4wIFNDTgozMTIuNSAzODcuMjI0IG0KNDQyLjUgMzg3LjIyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMzEyLjUgMzYxLjU0NCBtCjQ0Mi41IDM2MS41NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjMxMi41IDM4Ny43MjQgbQozMTIuNSAzNjEuMDQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSAzODcuNzI0IG0KNDQyLjUgMzYxLjA0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KMSB3CjAuMCAwLjAgMC4wIFNDTgo0NDIuNSAzODcuMjI0IG0KNTcyLjUgMzg3LjIyNCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KNDQyLjUgMzYxLjU0NCBtCjU3Mi41IDM2MS41NDQgbApTCltdIDAgZAoxIHcKMC4wIDAuMCAwLjAgU0NOCjQ0Mi41IDM4Ny43MjQgbQo0NDIuNSAzNjEuMDQ0IGwKUwpbXSAwIGQKMSB3CjAuMCAwLjAgMC4wIFNDTgo1NzIuNSAzODcuNzI0IG0KNTcyLjUgMzYxLjA0NCBsClMKW10gMCBkCjEgdwowLjAgMC4wIDAuMCBTQ04KCkJUCjMyLjUgMzQ4LjU1NCBUZAovRjMuMSAxMCBUZgo8MjM+IFRqCkVUCgoKQlQKNDIuNzMgMzQ4LjU1NCBUZAovRjEuMCAxMCBUZgo8MjA0YzY5NzQ2ODY5NzU2ZDIwPiBUagpFVAoKCkJUCjgxLjA5IDM0OC41NTQgVGQKL0YxLjAgMTAgVGYKPDQ5NGY0ZT4gVGoKRVQKCjgxLjA5IDM0Ny4zMDQgbQo5OC41IDM0Ny4zMDQgbApTCgpCVAo5OC41IDM0OC41NTQgVGQKL0YxLjAgMTAgVGYKPDIwNjI2MTc0NzQ2NTcyNjk2NTczMjA2OTZlMjA2MzZmNmQ3MDZjNjk2MTZlNjM2NTIwNzc2OTc0NjgyMDUzNjU2Mzc0Njk2ZjZlMjA0OTQ5MjA2ZjY2MjA1MDQ5MzkzNjM3PiBUagpFVAoKCkJUCjMyLjUgMzM4LjEzNCBUZApFVAoKCkJUCjMyLjUgMzM4LjEzNCBUZAovRjMuMSAxMCBUZgo8MjE+IFRqCkVUCgoKQlQKNDIuNzMgMzM4LjEzNCBUZAovRjEuMCAxMCBUZgo8MjA0YzY5NzQ2ODY5NzU2ZDIwPiBUagpFVAoKCkJUCjgxLjA5IDMzOC4xMzQgVGQKL0YxLjAgMTAgVGYKWzw0ZDQ1NTQ+IDkyIDw0MTRjPl0gVEoKRVQKCjgxLjA5IDMzNi44ODQgbQoxMTIuNzcgMzM2Ljg4NCBsClMKCkJUCjExMi43NyAzMzguMTM0IFRkCi9GMS4wIDEwIFRmCjwyMDYyNjE3NDc0NjU3MjY5NjU3MzIwNjk2ZTIwNjM2ZjZkNzA2YzY5NjE2ZTYzNjUyMDc3Njk3NDY4MjA1MzY1NjM3NDY5NmY2ZTIwNDk0OTIwNmY2NjIwNTA0OTIwPiBUagpFVAoKCkJUCjMxMS40OSAzMzguMTM0IFRkCi9GMS4wIDEwIFRmCjwyMDIwMjAyMDIwMjAyMDIwMjA+IFRqCkVUCgozMTEuNDkgMzM2Ljg4NCBtCjMzNi41MSAzMzYuODg0IGwKUwoKQlQKMzM2LjUxIDMzOC4xMzQgVGQKL0YxLjAgMTAgVGYKPDJlPiBUagpFVAoKCkJUCjMyLjUgMzI4LjMzNCBUZAovRjEuMCAxMCBUZgpbPGE1NTQ2ODY5NzMyMDcwNjE2MzZiNjE2NzY1MjA2NDZmNjU3MzIwNmU2Zjc0MjA2MzZmNmU3NDYxNjk2ZTIwNjE2ZTc5MjA3Mj4gMTggPDY1NjM2MTZjNmM2NTY0MjA2MTZlNjQyZjZmNzIyMDY0NjU2NjY1NjM3NDY5NzY2NTIwNjM2NTZjNmM3MzIwNmY3MjIwNjI2MTc0NzQ2NTcyNjk2NTczPl0gVEoKRVQKCgpCVAozMi41IDMxOC41MzQgVGQKL0YxLjAgMTAgVGYKWzxhNTU0Njg2OTczMjA3MDYxNjM2YjYxNjc2NTIwNmQ3NTczNzQyMDYyNjUyMDY4NjE2ZTY0NmM2NTY0MjA3NzY5NzQ2ODIwNjM2MTcyPiAxOCA8NjUyMDYxNmU2NDIwNzQ2ODYxNzQyMDYxMjA2NjZjNjE2ZDZkNjE2MjY5NmM2OTc0NzkyMDY4NjE3YTYxNzI+IDE4IDw2NDIwNjU3ODY5NzM3NDczMjA2OTY2MjA3NDY4NjUyMDcwNjE2MzZiNjE2NzY1MjA2OTczMjA2NDYxNmQ2MTY3NjU2NDJlPl0gVEoKRVQKCgpCVAozMi41IDMwOC43MzQgVGQKL0YxLjAgMTAgVGYKWzxhNTUzNzA2NTYzNjk2MTZjMjA3MDcyPiAxOCA8NmY2MzY1NjQ3NTcyPiAxOCA8NjU3MzIwNmQ3NTczNzQyMDYyNjUyMDY2NmY2YzZjNmY3NzY1NjQyMDY5NmUyMDc0Njg2NTIwNjU3NjY1NmU3NDIwNzQ2ODY1MjA3MDYxNjM2YjYxNjc2NTIwNjk3MzIwNjQ2MTZkNjE2NzY1NjQyYzIwNzQ2ZjIwNjk2ZTYzNmM3NTY0NjUyMDY5NmU3MzcwNjU2Mzc0Njk2ZjZlMjA2MTZlNjQyMDcyPiAxOCA8NjU3MDYxNjM2YjY5NmU2NzIwNjk2Nj5dIFRKCkVUCgoKQlQKMzIuNSAyOTguOTM0IFRkCi9GMS4wIDEwIFRmCjw2ZTY1NjM2NTczNzM2MTcyNzk+IFRqCkVUCgoKQlQKMzIuNSAyODQuMTM0IFRkCi9GMS4wIDEwIFRmCls8NTM3MDY1NjM2OTYxNmMyMDUwNzI+IDE4IDw2ZjYzNjU2NDc1NzI+IDE4IDw2NTczMjAzYT5dIFRKCkVUCgozMi41IDI4Mi44ODQgbQoxMjQuOTIgMjgyLjg4NCBsClMKCkJUCjMyLjUgMjc0LjMzNCBUZAovRjEuMCAxMCBUZgo8NDk2NjIwNzQ2ODY5NzMyMDcwNjE2MzZiNjE2NzY1MjA2OTczMjA2NDYxNmQ2MTY3NjU2NDIwNjk2ZTIwNzQ3MjYxNmU3MzcwNmY3Mjc0NjE3NDY5NmY2ZTJjMjA2OTc0MjA2ZDc1NzM3NDIwNmU2Zjc0MjA2MjY1MjA2YzZmNjE2NDY1NjQyMDc1NmU3NDY5NmMyMDc0Njg2NTIwNjM2ZjZlNjQ2OTc0Njk2ZjZlMjA2ZjY2MjA3NDY4NjUyMDYzNmY2ZTc0NjU2ZTc0NzMyMDYzNjE2ZTIwNjI2NTIwNzY2NTcyNjk2NjY5NjU2NDJlPiBUagpFVAoKMzIuNSAyNzMuMDg0IG0KNTUzLjIgMjczLjA4NCBsClMKCnEKMTUwLjAgMC4wIDAuMCA2Ni4wIDcyLjUgMTY1LjY3NCBjbQovSTEgRG8KUQoxIHcKMC4wIDAuMCAwLjAgU0NOCgpxCjIyMC4wIDAuMCAwLjAgMTYuMCAzNy41IDk0LjY3NCBjbQovSTIgRG8KUQoxIHcKMC4wIDAuMCAwLjAgU0NOCgpxCjE2OC4wIDAuMCAwLjAgMjAuMCAzMDcuNSA5MC42NzQgY20KL0kzIERvClEKUQoKZW5kc3RyZWFtCmVuZG9iago1IDAgb2JqCjw8IC9BcnRCb3ggWzAgMCA1OTUuNDQgODQxLjY4XQovQmxlZWRCb3ggWzAgMCA1OTUuNDQgODQxLjY4XQovQ29udGVudHMgNCAwIFIKL0Nyb3BCb3ggWzAgMCA1OTUuNDQgODQxLjY4XQovTWVkaWFCb3ggWzAgMCA1OTUuNDQgODQxLjY4XQovUGFyZW50IDMgMCBSCi9SZXNvdXJjZXMgPDwgL0ZvbnQgPDwgL0YxLjAgNyAwIFIKL0YyLjAgNiAwIFIKL0YzLjAgOSAwIFIKL0YzLjEgOCAwIFIKPj4KL1Byb2NTZXQgWy9QREYgL1RleHQgL0ltYWdlQiAvSW1hZ2VDIC9JbWFnZUldCi9YT2JqZWN0IDw8IC9JMSAxMCAwIFIKL0kyIDEyIDAgUgovSTMgMTQgMCBSCj4+Cj4+Ci9UcmltQm94IFswIDAgNTk1LjQ0IDg0MS42OF0KL1R5cGUgL1BhZ2UKPj4KZW5kb2JqCjYgMCBvYmoKPDwgL0Jhc2VGb250IC80ZjdlZmIrSGVsdmV0aWNhLUJvbGQKL0ZpcnN0Q2hhciAzMgovRm9udERlc2NyaXB0b3IgMTcgMCBSCi9MYXN0Q2hhciAyMTMKL1N1YnR5cGUgL1RydWVUeXBlCi9Ub1VuaWNvZGUgMTggMCBSCi9UeXBlIC9Gb250Ci9XaWR0aHMgMTkgMCBSCj4+CmVuZG9iago3IDAgb2JqCjw8IC9CYXNlRm9udCAvMjZkMjI1K0hlbHZldGljYU5ldWVMVC1Sb21hbgovRmlyc3RDaGFyIDMyCi9Gb250RGVzY3JpcHRvciAyMSAwIFIKL0xhc3RDaGFyIDE2NQovU3VidHlwZSAvVHJ1ZVR5cGUKL1RvVW5pY29kZSAyMiAwIFIKL1R5cGUgL0ZvbnQKL1dpZHRocyAyMyAwIFIKPj4KZW5kb2JqCjggMCBvYmoKPDwgL0Jhc2VGb250IC9jMzc2YWUrWmVuS2FpLVVuaQovRmlyc3RDaGFyIDMyCi9Gb250RGVzY3JpcHRvciAyNSAwIFIKL0xhc3RDaGFyIDM1Ci9TdWJ0eXBl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WS/9LbgAOSxLILADJlBYUViwgEQbsEBEWRshISBFsMBQWLDARBshWVktuAA6LCAgRWlEsAFgICBFfWkYRLABYC24ADssuAA6Ki24ADwsSyCwAyZTWLCAG7BAWYqKILADJlNYIyGwwIqKG4ojWSCwAyZTWCMhuAEAioobiiNZILADJlNYIyG4AUCKihuKI1kguAADJlNYsAMlRbgBgFBYIyG4AYAjIRuwAyVFIyEjIVkbIVlELbgAPSxLU1hFRBshIVktuAA+LEu4AAlQWLEBAY5ZuAH/hbgARB25AAkAA19eLbgAPywgIEVpRLABYC24AEAsuAA/KiEtuABBLCBGsAMlRlJYI1kgiiCKSWSKIEYgaGFksAQlRiBoYWRSWCNlilkvILAAU1hpILAAVFghsEBZG2kgsABUWCGwQGVZWTotuABCLCBGsAQlRlJYI4pZIEYgamFksAQlRiBqYWRSWCOKWS/9LbgAQyxLILADJlBYUViwgEQbsEBEWRshISBFsMBQWLDARBshWVktuABELCAgRWlEsAFgICBFfWkYRLABYC24AEUsuABEKi24AEYsSyCwAyZTWLCAG7BAWYqKILADJlNYIyGwwIqKG4ojWSCwAyZTWCMhuAEAioobiiNZILADJlNYIyG4AUCKihuKI1kguAADJlNYsAMlRbgBgFBYIyG4AYAjIRuwAyVFIyEjIVkbIVlELbgARyxLU1hFRBshIVktuABILEu4AAlQWLEBAY5ZuAH/hbgARB25AAkAA19eLbgASSwgIEVpRLABYC24AEosuABJKiEtuABLLCBGsAMlRlJYI1kgiiCKSWSKIEYgaGFksAQlRiBoYWRSWCNlilkvILAAU1hpILAAVFghsEBZG2kgsABUWCGwQGVZWTotuABMLCBGsAQlRlJYI4pZIEYgamFksAQlRiBqYWRSWCOKWS/9LbgATSxLILADJlBYUViwgEQbsEBEWRshISBFsMBQWLDARBshWVktuABOLCAgRWlEsAFgICBFfWkYRLABYC24AE8suABOKi24AFAsSyCwAyZTWLCAG7BAWYqKILADJlNYIyGwwIqKG4ojWSCwAyZTWCMhuAEAioobiiNZILADJlNYIyG4AUCKihuKI1kguAADJlNYsAMlRbgBgFBYIyG4AYAjIRuwAyVFIyEjIVkbIVlELbgAUSxLU1hFRBsh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ATIA2QEdASoA2AD+ANsA4gAaAIsAoAAaAEUA6AH2AAkA6QEoATIANgCCAJ4An/9wAHAAPwA/AOgBBQAVADgA6f97/8j/+QBCAIoAxAEHARMBHf+5AC8AhwCHAJoAnAEMAmL/sQAYAEwAdwCAAIIAyQDa/7L/6gAaADYA5QERAS8EO//dAAIABQAaADkAiQCqALcBIQEjASoBW//lAAIAGAAjAFwAqv9N/3b/sv/vABoALwBOAHsAigDhAR8BJgErAZoB3gPt/4D/jgAHABwATgBVAGMAYwBtAIEAmACcAK0BHwEmAWIEHAUVADkARABLAGMAjgDMAOgA8gEAASkBQgF4AtUD6gPwBDsEmv/EAAUAVQBcAGAAnwEDAR0BJAFVAWQBcAGtAbQBwwH2AjcCYQM5A9UEcAShAAIAVQCIAKEAvQDHANMA3QDrAO0A+gD9AQQBKwE+AU8BewGdAa0B4gIzAl0CfQKMAtoC7wMxA94EBwSLBYUFu/8E/9X/+gAHAB4AKgA7AEcAUQBYAGUAZQBmAG4AdQB/AIQBBwCXALEAwwDMAN8A3wEKARABLwExAUcBVAFbAWsBeQCRAaQBugHcAeQB5gHpAfYCEwIfAiMCLwJ2An0CggKJAq0CsgK5Au0DEQN0A30DwAPeA/YEFQRdBMAEwATfBS0FdAYcBksHUf6U/t//Lf+Q/5r/6gAWABYAJAApAC0APgEEAG0AbQCEAIcAiQCOAJwApACrAK4AsgCy//sBOQDEANEA3wDhAO8A9wEhARwBHAEhATIBOAFQAVEBVAFsAW0BfwGYAaQBqgG2AboBuwG7ANcB1wH7AfsB/gAZAgkCLQJbAmECeQJ5ApoAmALTAtoC7wMMAyEDKAMtA0sDU//xA60DsQPyBCUEWgRxBHsEigSYBJ8FHAU9BVcFWgVwBZUFtgXLBdYF7wX0Bh0GhwakBrQG0wcIBzQHmAf+ASIBMgEgASUAtAC+AIIAlgNwATIBJABDAYQBHQFWAMwBBQDtAMUA+wD5AMAApwEdAP4DVQCIACb/oQC4/4gA3QC9ALUDfAA8AJECkwJK/z8DqAMJATL/9wCCADAAKgAqACoAKgAqACoAAAA0ADQAcADiAVQBqgHSAfgCmAM8A6oEPgSkBO4FIgVCBeoGOgaQBu4HOAe+CAgIXAiKAAIAmgAABT0FwgADAAcAPkAh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AAYBCgADAAEEBgAHAHgBEAADAAEEBwACAAgBiAADAAEEBwAEABwBkAADAAEEBwAHAHgBrAADAAEECQAAAKACJAADAAEECQABABICxAADAAEECQACAAgC1gADAAEECQADAEYC3gADAAEECQAEABwDJAADAAEECQAFAA4DQAADAAEECQAHAGQDTgADAAEECQASABwDsgADAAEECgAEACIDzgADAAEECgAHAGAD8AADAAEECwACABYEUAADAAEECwAEACAEZgADAAEEDAACAAgEhgADAAEEDAAEABwEjgADAAEEDAAHAF4EqgADAAEEDQAEABoFCAADAAEEEAACABIFIgADAAEEEAAEACYFNAADAAEEEAAHAGAFWgADAAEEEQACAAgFugADAAEEEgACAAYFwgADAAEEEwACAAYFyAADAAEEEwAEABoFzgADAAEEEwAHAHQF6AADAAEEFAACAAYGXAADAAEEFAAEACIGYgADAAEEFgACAA4GhAADAAEEFgAEACYGkgADAAEEGQACAAwGuAADAAEEHQACAAYGxAADAAEEHQAEABoGygADAAEEHQAHAGwG5AADAAEEKQAEACAHUAADAAEIBAACAAQHcAADAAEMAQACAAgHdAADAAEMCgACAA4HfKkgMTk5MC0yMDA2IEFwcGxlIENvbXB1dGVyIEluYy4gqSAxOTgxIExpbm90eXBlIEFHIKkgMTk5MC05MSBUeXBlIFNvbHV0aW9ucyBJbmMuSGVsdmV0aWNhQm9sZEhlbHZldGljYSBCb2xkOyA4LjBkM2UxOyAyMDEyLTAzLTI3SGVsdmV0aWNhIEJvbGQ4LjBkM2UxNGY3ZWZiK0hlbHZldGljYS1Cb2xkSGVsdmV0aWNhIGlzIGEgcmVnaXN0ZXJlZCB0cmFkZW1hcmsgb2YgTGlub3R5cGUgQUdIZWx2ZXRpY2EgQm9sZABIAGUAbAB2AGUAdABpAGMAYQAgBiMGMwZIBi98l5rUAEYAZQBkAEgAZQBsAHYAZQB0AGkAYwBhACAAZQByACAAZQB0ACAAcgBlAGcAaQBzAHQAcgBlAHIAZQB0ACAAdgBhAHIAZQBtAOYAcgBrAGUAIAB0AGkAbABoAPgAcgBlAG4AZABlACAATABpAG4AbwB0AHkAcABlACAAQQBHAEYAZQB0AHQASABlAGwAdgBlAHQAaQBjAGEAIABGAGUAdAB0AEgAZQBsAHYAZQB0AGkAYwBhACAAaQBzAHQAIABlAGkAbgAgAGUAaQBuAGcAZQB0AHIAYQBnAGUAbgBlAHMAIABXAGEAcgBlAG4AegBlAGkAYwBoAGUAbgAgAGQAZQByACAATABpAG4AbwB0AHkAcABlACAAQQBHAKkAIAAxADkAOQAwAC0AMgAwADAANgAgAEEAcABwAGwAZQAgAEMAbwBtAHAAdQB0AGUAcgAgAEkAbgBjAC4AIACpACAAMQA5ADgAMQAgAEwAaQBuAG8AdAB5AHAAZQAgAEEARwAgAKkAIAAxADkAOQAwAC0AOQAxACAAVAB5AHAAZQAgAFMAbwBsAHUAdABpAG8AbgBzACAASQBuAGMALgBIAGUAbAB2AGUAdABpAGMAYQBCAG8AbABkAEgAZQBsAHYAZQB0AGkAYwBhACAAQgBvAGwAZAA7ACAAOAAuADAAZAAzAGUAMQA7ACAAMgAwADEAMgAtADAAMwAtADIANwBIAGUAbAB2AGUAdABpAGMAYQAgAEIAbwBsAGQAOAAuADAAZAAzAGUAMQBIAGUAbAB2AGUAdABpAGMAYQAgAGkAcwAgAGEAIAByAGUAZwBpAHMAdABlAHIAZQBkACAAdAByAGEAZABlAG0AYQByAGsAIABvAGYAIABMAGkAbgBvAHQAeQBwAGUAIABBAEcASABlAGwAdgBlAHQAaQBjAGEAIABCAG8AbABkAEgAZQBsAHYAZQB0AGkAYwBhACAATgBlAGcAcgBpAHQAYQBIAGUAbAB2AGUAdABpAGMAYQAgAGUAcwAgAHUAbgBhACAAbQBhAHIAYwBhACAAcgBlAGcAaQBzAHQAcgBhAGQAYQAgAGQAZQAgAEwAaQBuAG8AdAB5AHAAZQAgAEEARwBQAHUAbwBsAGkAbABpAGgAYQB2AGEASABlAGwAdgBlAHQAaQBjAGEAIABsAGkAaABhAHYAYQBHAHIAYQBzAEgAZQBsAHYAZQB0AGkAYwBhACAARwByAGEAcwBIAGUAbAB2AGUAdABpAGMAYQAgAGUAcwB0ACAAdQBuAGUAIABtAGEAcgBxAHUAZQAgAGQA6QBwAG8AcwDpAGUAIABkAGUAIABMAGkAbgBvAHQAeQBwAGUAIABBAEcASABlAGwAdgBlAHQAaQBjAGEAIAXiBdEF1ABHAHIAYQBzAHMAZQB0AHQAbwBIAGUAbAB2AGUAdABpAGMAYQAgAGcAcgBhAHMAcwBlAHQAdABvAEgAZQBsAHYAZQB0AGkAYwBhACAA6AAgAHUAbgAgAG0AYQByAGMAaABpAG8AIAByAGUAZwBpAHMAdAByAGEAdABvACAAZABpACAATABpAG4AbwB0AHkAcABlACAAQQBHMNww/DDrMMm8/LTczLQAVgBlAHQASABlAGwAdgBlAHQAaQBjAGEAIAB2AGUAdABIAGUAbAB2AGUAdABpAGMAYQAgAGkAcwAgAGUAZQBuACAAZwBlAHIAZQBnAGkAcwB0AHIAZQBlAHIAZAAgAGgAYQBuAGQAZQBsAHMAbQBlAHIAawAgAHYAYQBuACAATABpAG4AbwB0AHkAcABlACAAQQBHAEYAZQB0AEgAZQBsAHYAZQB0AGkAYwBhACAASABhAGwAdgBmAGUAdABOAGUAZwByAGkAdABvAEgAZQBsAHYAZQB0AGkAYwBhACAAQwBhAHIAcgBlAGcAYQBkAG8EFgQ4BEAEPQRLBDkARgBlAHQASABlAGwAdgBlAHQAaQBjAGEAIABGAGUAdABIAGUAbAB2AGUAdABpAGMAYQAgAOQAcgAgAGUAdAB0ACAAcgBlAGcAaQBzAHQAcgBlAHIAYQB0ACAAdgBhAHIAdQBtAOQAcgBrAGUAIABmAPYAcgAgAEwAaQBuAG8AdAB5AHAAZQAgAEEARwBIAGUAbAB2AGUAdABpAGMAYQAgBigGMQYsBjMGKgZHfJdPUwY5BjEGSgY2AE4AZQBnAHIAaQB0AGEAAgAAAAAAAP9lAGUAAAAAAAAAAAAAAAAAAAAAAAAAAAAZAAAAAwASACUAJgAnACwALwA2AEQARgBIAEkASwBMAE8AUABRAFIAUwBVAFYAVwBYALcKZW5kc3RyZWFtCmVuZG9iagoxNyAwIG9iago8PCAvQXNjZW50IDc1MAovQ2FwSGVpZ2h0IDE0NzQKL0Rlc2NlbnQgLTE2OQovRmxhZ3MgNAovRm9udEJCb3ggWy0xMDE3IC00ODAgMTQzNiAxMTU5XQovRm9udEZpbGUyIDE2IDAgUgovRm9udE5hbWUgLzRmN2VmYitIZWx2ZXRpY2EtQm9sZAovSXRhbGljQW5nbGUgMAovU3RlbVYgMAovVHlwZSAvRm9udERlc2NyaXB0b3IKL1hIZWlnaHQgMTA5MAo+PgplbmRvYmoKMTggMCBvYmoKPDwgL0xlbmd0aCA1NDAKPj4Kc3RyZWFtCi9DSURJbml0IC9Qcm9jU2V0IGZpbmRyZXNvdXJjZSBiZWdpbgoxMiBkaWN0IGJlZ2luCmJlZ2luY21hcAovQ0lEU3lzdGVtSW5mbyAzIGRpY3QgZHVwIGJlZ2luCiAgL1JlZ2lzdHJ5IChBZG9iZSkgZGVmCiAgL09yZGVyaW5nIChVQ1MpIGRlZgogIC9TdXBwbGVtZW50IDAgZGVmCmVuZCBkZWYKL0NNYXBOYW1lIC9BZG9iZS1JZGVudGl0eS1VQ1MgZGVmCi9DTWFwVHlwZSAyIGRlZgoxIGJlZ2luY29kZXNwYWNlcmFuZ2UKPDAwPjxENT4KZW5kY29kZXNwYWNlcmFuZ2UKNSBiZWdpbmJmcmFuZ2UKPDQyPjw0ND48MDA0Mj4KPDY1Pjw2Nj48MDA2NT4KPDY4Pjw2OT48MDA2OD4KPDZDPjw3MD48MDA2Yz4KPDcyPjw3NT48MDA3Mj4KZW5kYmZyYW5nZQo4IGJlZ2luYmZjaGFyCjwyMD48MDAyMD4KPDJGPjwwMDJmPgo8NDk+PDAwNDk+Cjw0Qz48MDA0Yz4KPDUzPjwwMDUzPgo8NjE+PDAwNjE+Cjw2Mz48MDA2Mz4KPEQ1PjwyMDE5PgplbmRiZmNoYXIKZW5kY21hcApDTWFwTmFtZSBjdXJyZW50ZGljdCAvQ01hcCBkZWZpbmVyZXNvdXJjZSBwb3AKZW5kCmVuZAplbmRzdHJlYW0KZW5kb2JqCjE5IDAgb2JqClsyNzcgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDI3NyAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCA3MjIgNzIyIDcyMiAwIDAgMCAwIDI3NyAwIDAgNjEwIDAgMCAwIDAgMCAwIDY2NiAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDU1NiAwIDU1NiAwIDU1NiAzMzMgMCA2MTAgMjc3IDAgMCAyNzcgODg5IDYxMCA2MTAgNjEwIDAgMzg5IDU1NiAzMzMgNjEwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAw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AIYABQAJXUEFAJUABQClAAUAAl1BBQCaAA8AqgAPAAJdQRMACQAPABkADwApAA8AOQAPAEkADwBZAA8AaQAPAHkADwCJAA8ACV26ADcADwAlERI5uAA3L7kAFAAE/LoAHQAvAAUREjm4ACUQuAA53AC4AABFWLgAKi8buQAqAAc+WbsANAABABcABCu7ACAAAQAAAAQruAAqELkACgAB/EETAAcACgAXAAoAJwAKADcACgBHAAoAVwAKAGcACgB3AAoAhwAKAAldQQUAlgAKAKYACgACXTAxASIOAhUUHgIzMj4CNTQuAjcuASMiDgIHFz4BMzIeAhUUDgIjIi4CNTQ+AjMyFhcBHiQ2JhMUJTcjIjYkExEkNlwGPjM2QyQOAQIeWTozUTceGDdbQ09gNBEZPGRMWGgIAX0ZKzshIToqGRksOCAhOysakzA6NVFeKQIxLCM+VDEnVEYtQWR4OEmJakBeVwABADIAAAH9ArkADgAouwAFAAYABgAEKwC4AABFWLgABS8buQAFAAc+WbsADgABAAsABCswMQEOAwcjPgM3ITUhAf02XkkuBV8GL0phOP6MAcsCcDWSprBTWqudjDtQAAADACj/9AIEAsUAEQAxAEEBfrsAIgAEAAgABCu7AAAABAAsAAQrQRMABgAAABYAAAAmAAAANgAAAEYAAABWAAAAZgAAAHYAAACGAAAACV1BBQCVAAAApQAAAAJdQQUAmgAIAKoACAACXUETAAkACAAZAAgAKQAIADkACABJAAgAWQAIAGkACAB5AAgAiQAIAAldugASACwAABESObgAEi+6ABwACAAiERI5uAAcL7oAHwAsACIREjm6AC8ALAAiERI5uAASELkAMgAE/LgAHBC5ADoABPxBBQCaADoAqgA6AAJdQRMACQA6ABkAOgApADoAOQA6AEkAOgBZADoAaQA6AHkAOgCJADoACV24ACIQuABD3AC4AABFWLgAJy8buQAnAAc+WbsAFwABAD0ABCu7ADcAAgAfAAQruAAnELkAAwAB/EETAAcAAwAXAAMAJwADADcAAwBHAAMAVwADAGcAAwB3AAMAhwADAAldQQUAlgADAKYAAwACXbgANxC5AA0AAfy6AC8ANwANERI5MDE3FBYzMj4CNTQuAiMiDgIDND4CMzIeAhUUBgceARUUDgIjIi4CNTQ2Ny4BNxQe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MDEFDgMjIiYnNR4BMzI2PwEDMxMzEzMBCw8dIiwcDx4ODBkNGiAMI81glwKRWkUmNCEPBAVOBAgYF1gCAv5ZAacAAAEAFgAAAcoCBQAJADkAuAAARVi4AAMvG7kAAwALPlm4AABFWLgACC8buQAIAAc+WbgAAxC5AAEAAfy4AAgQuQAGAAH8MDE3ASE1IRUBIRUhFgE4/twBkv7EAUr+TEEBeUs6/oBLAAAAAQBN/yoAkQMSAAMAFbsAAQAFAAAABCsAugABAAIAAyswMRMzESNNREQDEvwYAAAAAQBIALIBrQIXABMAYboACgAAAAMrQQUA2gAAAOoAAAACXUEbAAkAAAAZAAAAKQAAADkAAABJAAAAWQAAAGkAAAB5AAAAiQAAAJkAAACpAAAAuQAAAMkAAAANXbgAChC4ABXcALoABQAPAAMrMDETND4CMzIeAhUUDgIjIi4CSBwwQSUlQTEcHDFBJSVBMBwBZSVBMBwcMEElJUExHBwxQQAAAAAAACABhgABAAAAAAAAAsUAAAABAAAAAAABABECxQABAAAAAAACAAgC1gABAAAAAAADACgC3gABAAAAAAAEABUDBgABAAAAAAAFABIDGwABAAAAAAAGABwDLQABAAAAAAAHAJcDSQABAAAAAAAIAA0D4AABAAAAAAAJABYD7QABAAAAAAAKBjAEAwABAAAAAAALABcKMwABAAAAAAAMACUKSgABAAAAAAANA88KbwABAAAAAAAOAB8OPgABAAAAAAASABkOXQADAAEECQAABYoOdgADAAEECQABADIUAAADAAEECQACAA4UMgADAAEECQADAFAUQAADAAEECQAEACoUkAADAAEECQAFACQUugADAAEECQAHAS4U3gADAAEECQAIABoWDAADAAEECQAJACwWJgADAAEECQAKDGAWUgADAAEECQALAC4isgADAAEECQAMAEoi4AADAAEECQANB54jKgADAAEECQAOAD4qyAADAAEECQAQACIrBgADAAEECQARABArKFBhcnQgb2YgdGhlIGRpZ2l0YWxseSBlbmNvZGVkIG1hY2hpbmUgcmVhZGFibGUgb3V0bGluZSBkYXRhIGZvciBwcm9kdWNpbmcgdGhlIFR5cGVmYWNlcyBwcm92aWRlZCBpcyBjb3B5cmlnaHRlZCCpIDE5ODggLSAyMDA2IExpbm90eXBlIEdtYkgsIHd3dy5saW5vdHlwZS5jb20uIEFsbCByaWdodHMgcmVzZXJ2ZWQuIFRoaXMgc29mdHdhcmUgaXMgdGhlIHByb3BlcnR5IG9mIExpbm90eXBlIEdtYkgsIGFuZCBtYXkgbm90IGJlIHJlcHJvZHVjZWQsIHVzZWQsIGRpc3BsYXllZCwgbW9kaWZpZWQsIGRpc2Nsb3NlZCBvciB0cmFuc2ZlcnJlZCB3aXRob3V0IHRoZSBleHByZXNzIHdyaXR0ZW4gYXBwcm92YWwgb2YgTGlub3R5cGUgR21iSC4gIENvcHlyaWdodCAoYykgMTk4OCwgMTk5MCwgMTk5MyBBZG9iZSBTeXN0ZW1zIEluY29ycG9yYXRlZC4gQWxsIFJpZ2h0cyBSZXNlcnZlZC4gSGVsdmV0aWNhIGlzIGEgdHJhZGVtYXJrIG9mIEhlaWRlbGJlcmdlciBEcnVja21hc2NoaW5lbiBBRywgZXhjbHVzaXZlbHkgbGljZW5zZWQgdGhyb3VnaCBMaW5vdHlwZSBHbWJILCBhbmQgbWF5IGJlIHJlZ2lzdGVyZWQgaW4gY2VydGFpbiBqdXJpc2RpY3Rpb25zLiBUaGlzIHR5cGVmYWNlIGlzIG9yaWdpbmFsIGFydHdvcmsgb2YgTGlub3R5cGUgRGVzaWduIFN0dWRpby4gVGhlIGRlc2lnbiBtYXkgYmUgcHJvdGVjdGVkIGluIGNlcnRhaW4ganVyaXNkaWN0aW9ucy5IZWx2ZXRpY2EgTmV1ZSBMVDU1IFJvbWFuTGlub3R5cGUgR21iSDpIZWx2ZXRpY2EgTFQgNTUgUm9tYW46MjAwNkhlbHZldGljYSBMVCA1NSBSb21hblZlcnNpb24gNi43MDsgMjAwNjI2ZDIyNStIZWx2ZXRpY2FOZXVlTFQtUm9tYW5IZWx2ZXRpY2EgaXMgYSB0cmFkZW1hcmsgb2YgSGVpZGVsYmVyZ2VyIERydWNrbWFzY2hpbmVuIEFHLCBleGNsdXNpdmVseSBsaWNlbnNlZCB0aHJvdWdoIExpbm90eXBlIEdtYkgsIGFuZCBtYXkgYmUgcmVnaXN0ZXJlZCBpbiBjZXJ0YWluIGp1cmlzZGljdGlvbnMuTGlub3R5cGUgR21iSExpbm90eXBlIERlc2lnbiBTdHVkaW9IZWx2ZXRpY2EgaXMgb25lIG9mIHRoZSBtb3N0IGZhbW91cyBhbmQgcG9wdWxhciB0eXBlZmFjZXMgaW4gdGhlIHdvcmxkLiBJdCBsZW5kcyBhbiBhaXIgb2YgbHVjaWQgZWZmaWNpZW5jeSB0byBhbnkgdHlwb2dyYXBoaWMgbWVzc2FnZSB3aXRoIGl0cyBjbGVhbiwgbm8tbm9uc2Vuc2Ugc2hhcGVzLiBUaGUgb3JpZ2luYWwgdHlwZWZhY2Ugd2FzIGNhbGxlZCBIYWFzIEdyb3Rlc2ssIGFuZCB3YXMgZGVzaWduZWQgaW4gMTk1NyBieSBNYXggTWllZGluZ2VyIGZvciB0aGUgSGFhcydzY2hlIFNjaHJpZnRnaWVzc2VyZWkgKEhhYXMgVHlwZSBGb3VuZHJ5KSBpbiBTd2l0emVybGFuZC4gSW4gMTk2MCB0aGUgbmFtZSB3YXMgY2hhbmdlZCB0byBIZWx2ZXRpY2EgKGFuIGFkYXB0YXRpb24gb2YgIkhlbHZldGlhIiwgdGhlIExhdGluIG5hbWUgZm9yIFN3aXR6ZXJsYW5kKS4gT3ZlciB0aGUgeWVhcnMsIHRoZSBIZWx2ZXRpY2EgZmFtaWx5IHdhcyBleHBhbmRlZCB0byBpbmNsdWRlIG1hbnkgZGlmZmVyZW50IHdlaWdodHMsIGJ1dCB0aGVzZSB3ZXJlIG5vdCBhcyB3ZWxsIGNvb3JkaW5hdGVkIHdpdGggZWFjaCBvdGhlciBhcyB0aGV5IG1pZ2h0IGhhdmUgYmVlbi4gSW4gMTk4MywgRC4gU3RlbXBlbCBBRyBhbmQgTGlub3R5cGUgcmUtZGVzaWduZWQgYW5kIGRpZ2l0aXplZCBOZXVlIEhlbHZldGljYSBhbmQgdXBkYXRlZCBpdCBpbnRvIGEgY29oZXNpdmUgZm9udCBmYW1pbHkuIFRvZGF5LCB0aGUgb3JpZ2luYWwgSGVsdmV0aWNhIGZhbWlseSBjb25zaXN0cyBvZiAzNCBkaWZmZXJlbnQgZm9udCB3ZWlnaHRzLCBhbmQgdGhlIE5ldWUgSGVsdmV0aWNhIGZhbWlseSBjb25zaXN0cyBvZiA1MSBmb250IHdlaWdodHMuIFRoZSBIZWx2ZXRpY2EgZmFtaWx5IG5vdyBmb3JtcyBhbiBpbnRlZ3JhbCBwYXJ0IG9mIG1hbnkgZGlnaXRhbCBwcmludGVycyBhbmQgb3BlcmF0aW5nIHN5c3RlbXMgYW5kIGhhcyBiZWNvbWUgYSBzdHlsaXN0aWMgYW5jaG9yIGluIG91ciB2aXN1YWwgY3VsdHVyZS4gSXQgaXMgdGhlIHF1aW50ZXNzZW50aWFsIHNhbnMgc2VyaWYgZm9udCwgdGltZWxlc3MgYW5kIG5ldXRyYWwsIGFuZCBjYW4gYmUgdXNlZCBmb3IgYWxsIHR5cGVzIG9mIGNvbW11bmljYXRpb24uIEhlbHZldGljYSBXb3JsZCwgYW4gdXBkYXRlIHRvIHRoZSBjbGFzc2ljIEhlbHZldGljYSBkZXNpZ24gdXNpbmcgdGhlIE9wZW5UeXBlIGZvbnQgZm9ybWF0LCBjb250YWlucyB0aGUgZm9sbG93aW5nIE1pY3Jvc29mdCBjb2RlIHBhZ2VzOiAxMjUyIExhdGluIDEsIDEyNTAgTGF0aW4gMiBFYXN0ZXJuLCAxMjUxIEN5cmlsbGljLCAxMjUzIEdyZWVrLCAxMjU0IFR1cmssIDEyNTUgSGVicmV3LCAxMjU2IEFyYWJpYywgMTI1NyBXaW5kb3dzIEJhbHRpYywgMTI1OCBXaW5kb3dzIFZpZXRuYW1lc2UsIGFzIHdlbGwgYXMgYSBtaXh0dXJlIG9mIGJveCBkcmF3aW5nIGVsZW1lbnQgZ2x5cGhzIGFuZCBtYXRoZW1hdGljYWwgc3ltYm9scyAmIG9wZXJhdG9ycy4gSW4gdG90YWwsIGVhY2ggd2VpZ2h0IG9mIEhlbHZldGljYSBXb3JsZCBjb250YWlucyBtb3JlIHRoYW4gMTg1MCBkaWZmZXJlbnQgZ2x5cGggY2hhcmFjdGVycyFodHRwOi8vd3d3Lmxpbm90eXBlLmNvbWh0dHA6Ly93d3cubGlub3R5cGUuY29tL2ZvbnRkZXNpZ25lcnNOT1RJRklDQVRJT04gT0YgTElDRU5TRSBBR1JFRU1FTlQNCg0KWW91IGhhdmUgb2J0YWluZWQgdGhpcyBmb250IHNvZnR3YXJlIGVpdGhlciBkaXJlY3RseSBmcm9tIExpbm90eXBlIEdtYkggb3IgdG9nZXRoZXIgd2l0aCBzb2Z0d2FyZSBkaXN0cmlidXRlZCBieSBvbmUgb2YgTGlub3R5cGUncyBsaWNlbnNlZXMuDQoNClRoaXMgZm9udCBzb2Z0d2FyZSBpcyBhIHZhbHVhYmxlIGFzc2V0IG9mIExpbm90eXBlIEdtYkguIFVubGVzcyB5b3UgaGF2ZSBlbnRlcmVkIGludG8gYSBzcGVjaWZpYyBsaWNlbnNlIGFncmVlbWVudCBncmFudGluZyB5b3UgYWRkaXRpb25hbCByaWdodHMsIHlvdXIgdXNlIG9mIHRoaXMgZm9udCBzb2Z0d2FyZSBpcyBsaW1pdGVkIHRvIHlvdXIgd29ya3N0YXRpb24gZm9yIHlvdXIgb3duIHVzZS4gWW91IG1heSBub3QgY29weSBvciBkaXN0cmlidXRlIHRoaXMgZm9udCBzb2Z0d2FyZS4gSWYgeW91IGhhdmUgYW55IHF1ZXN0aW9ucyByZWdhcmRpbmcgeW91ciBsaWNlbnNlIHRlcm1zLCBwbGVhc2UgcmV2aWV3IHRoZSBsaWNlbnNlIGFncmVlbWVudCB5b3UgcmVjZWl2ZWQgd2l0aCB0aGUgc29mdHdhcmUuDQoNCkdlbmVyYWwgbGljZW5zZSB0ZXJtcyBhbmQgdXNhZ2UgcmlnaHRzIGNhbiBiZSB2aWV3ZWQgYXQgd3d3Lmxpbm90eXBlLmNvbS9saWNlbnNlLg0KDQpHZW5lcmVsbGUgTGl6ZW56YmVkaW5ndW5nZW4gdW5kIE51dHp1bmdzcmVjaHRlIGZpbmRlbiBTaWUgdW50ZXIgd3d3Lmxpbm90eXBlLmNvbS9saWNlbnNlLg0KDQpQb3VyIHBsdXMgZCdpbmZvcm1hdGlvbnMgY29uY2VybmFudCBsZSBjb250cmF0IGQndXRpbGlzYXRpb24gZHUgbG9naWNpZWwgZGUgcG9saWNlcywgdmV1aWxsZXogY29uc3VsdGVyIG5vdHJlIHNpdGUgd2ViIHd3dy5saW5vdHlwZS5jb20vbGljZW5zZS4NCg0KTGlub3R5cGUgR21iSCBjYW4gYmUgY29udGFjdGVkIGF0Og0KDQpUZWwuOiArNDkoMCk2MTcyIDQ4NC00MThodHRwOi8vd3d3Lmxpbm90eXBlLmNvbS9saWNlbnNlSGVsdmV0aWNhTmV1ZSBMVCA1NSBSb21hbgBQAGEAcgB0ACAAbwBmACAAdABoAGUAIABkAGkAZwBpAHQAYQBsAGwAeQAgAGUAbgBjAG8AZABlAGQAIABtAGEAYwBoAGkAbgBlACAAcgBlAGEAZABhAGIAbABlACAAbwB1AHQAbABpAG4AZQAgAGQAYQB0AGEAIABmAG8AcgAgAHAAcgBvAGQAdQBjAGkAbgBnACAAdABoAGUAIABUAHkAcABlAGYAYQBjAGUAcwAgAHAAcgBvAHYAaQBkAGUAZAAgAGkAcwAgAGMAbwBwAHkAcgBpAGcAaAB0AGUAZAAgAKkAIAAxADkAOAA4ACAALQAgADIAMAAwADYAIABMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIACwAIAB3AHcAdwAuAGwAaQBuAG8AdAB5AHAAZQAuAGMAbwBtAC4AIABBAGwAbAAgAHIAaQBnAGgAdABzACAAcgBlAHMAZQByAHYAZQBkAC4AIABUAGgAaQBzACAAcwBvAGYAdAB3AGEAcgBlACAAaQBzACAAdABoAGUAIABwAHIAbwBwAGUAcgB0AHkAIABvAGYAIABMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIACwAIABhAG4AZAAgAG0AYQB5ACAAbgBvAHQAIABiAGUAIAByAGUAcAByAG8AZAB1AGMAZQBkACwAIAB1AHMAZQBkACwAIABkAGkAcwBwAGwAYQB5AGUAZAAsACAAbQBvAGQAaQBmAGkAZQBkACwAIABkAGkAcwBjAGwAbwBzAGUAZAAgAG8AcgAgAHQAcgBhAG4AcwBmAGUAcgByAGUAZAAgAHcAaQB0AGgAbwB1AHQAIAB0AGgAZQAgAGUAeABwAHIAZQBzAHMAIAB3AHIAaQB0AHQAZQBuACAAYQBwAHAAcgBvAHYAYQBsACAAbwBmACAATABpAG4AbwB0AHkAcABlACAARwBtAGIASAAuACAAIABDAG8AcAB5AHIAaQBnAGgAdAAgACgAYwApACAAMQA5ADgAOAAsACAAMQA5ADkAMAAsACAAMQA5ADkAMwAgAEEAZABvAGIAZQAgAFMAeQBzAHQAZQBtAHMAIABJAG4AYwBvAHIAcABvAHIAYQB0AGUAZAAuACAAQQBsAGwAIABSAGkAZwBoAHQAcwAgAFIAZQBzAGUAcgB2AGUAZAAuACAASABlAGwAdgBlAHQAaQBjAGEAIABpAHMAIABhACAAdAByAGEAZABlAG0AYQByAGsAIABvAGYAIABIAGUAaQBkAGUAbABiAGUAcgBnAGUAcgAgAEQAcgB1AGMAawBtAGEAcwBjAGgAaQBuAGUAbgAgAEEARwAsACAAZQB4AGMAbAB1AHMAaQB2AGUAbAB5ACAAbABpAGMAZQBuAHMAZQBkACAAdABoAHIAbwB1AGcAaAAgAEwAaQBuAG8AdAB5AHAAZQAgAEcAbQBiAEgALAAgAGEAbgBkACAAbQBhAHkAIABiAGUAIAByAGUAZwBpAHMAdABlAHIAZQBkACAAaQBuACAAYwBlAHIAdABhAGkAbgAgAGoAdQByAGkAcwBkAGkAYwB0AGkAbwBuAHMALgAgAFQAaABpAHMAIAB0AHkAcABlAGYAYQBjAGUAIABpAHMAIABvAHIAaQBnAGkAbgBhAGwAIABhAHIAdAB3AG8AcgBrACAAbwBmACAATABpAG4AbwB0AHkAcABlACAARABlAHMAaQBnAG4AIABTAHQAdQBkAGkAbwAuACAAVABoAGUAIABkAGUAcwBpAGcAbgAgAG0AYQB5ACAAYgBlACAAcAByAG8AdABlAGMAdABlAGQAIABpAG4AIABjAGUAcgB0AGEAaQBuACAAagB1AHIAaQBzAGQAaQBjAHQAaQBvAG4AcwAuAEgAZQBsAHYAZQB0AGkAYwBhAE4AZQB1AGUAIABMAFQAIAA1ADUAIABSAG8AbQBhAG4AUgBlAGcAdQBsAGEAcgBMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIADoASABlAGwAdgBlAHQAaQBjAGEAIABMAFQAIAA1ADUAIABSAG8AbQBhAG4AOgAyADAAMAA2AEgAZQBsAHYAZQB0AGkAYwBhACAATABUACAANQA1ACAAUgBvAG0AYQBuAFYAZQByAHMAaQBvAG4AIAA2AC4ANwAwADsAIAAyADAAMAA2AEgAZQBsAHYAZQB0AGkAYwBhACAAaQBzACAAYQAgAHQAcgBhAGQAZQBtAGEAcgBrACAAbwBmACAASABlAGkAZABlAGwAYgBlAHIAZwBlAHIAIABEAHIAdQBjAGsAbQBhAHMAYwBoAGkAbgBlAG4AIABBAEcALAAgAGUAeABjAGwAdQBzAGkAdgBlAGwAeQAgAGwAaQBjAGUAbgBzAGUAZAAgAHQAaAByAG8AdQBnAGgAIABMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIACwAIABhAG4AZAAgAG0AYQB5ACAAYgBlACAAcgBlAGcAaQBzAHQAZQByAGUAZAAgAGkAbgAgAGMAZQByAHQAYQBpAG4AIABqAHUAcgBpAHMAZABpAGMAdABpAG8AbgBzAC4ATABpAG4AbwB0AHkAcABlACAARwBtAGIASABMAGkAbgBvAHQAeQBwAGUAIABEAGUAcwBpAGcAbgAgAFMAdAB1AGQAaQBvAEgAZQBsAHYAZQB0AGkAYwBhACAAaQBzACAAbwBuAGUAIABvAGYAIAB0AGgAZQAgAG0AbwBzAHQAIABmAGEAbQBvAHUAcwAgAGEAbgBkACAAcABvAHAAdQBsAGEAcgAgAHQAeQBwAGUAZgBhAGMAZQBzACAAaQBuACAAdABoAGUAIAB3AG8AcgBsAGQALgAgAEkAdAAgAGwAZQBuAGQAcwAgAGEAbgAgAGEAaQByACAAbwBmACAAbAB1AGMAaQBkACAAZQBmAGYAaQBjAGkAZQBuAGMAeQAgAHQAbwAgAGEAbgB5ACAAdAB5AHAAbwBnAHIAYQBwAGgAaQBjACAAbQBlAHMAcwBhAGcAZQAgAHcAaQB0AGgAIABpAHQAcwAgAGMAbABlAGEAbgAsACAAbgBvAC0AbgBvAG4AcwBlAG4AcwBlACAAcwBoAGEAcABlAHMALgAgAFQAaABlACAAbwByAGkAZwBpAG4AYQBsACAAdAB5AHAAZQBmAGEAYwBlACAAdwBhAHMAIABjAGEAbABsAGUAZAAgAEgAYQBhAHMAIABHAHIAbwB0AGUAcwBrACwAIABhAG4AZAAgAHcAYQBzACAAZABlAHMAaQBnAG4AZQBkACAAaQBuACAAMQA5ADUANwAgAGIAeQAgAE0AYQB4ACAATQBpAGUAZABpAG4AZwBlAHIAIABmAG8AcgAgAHQAaABlACAASABhAGEAcwAnAHMAYwBoAGUAIABTAGMAaAByAGkAZgB0AGcAaQBlAHMAcwBlAHIAZQBpACAAKABIAGEAYQBzACAAVAB5AHAAZQAgAEYAbwB1AG4AZAByAHkAKQAgAGkAbgAgAFMAdwBpAHQAegBlAHIAbABhAG4AZAAuACAASQBuACAAMQA5ADYAMAAgAHQAaABlACAAbgBhAG0AZQAgAHcAYQBzACAAYwBoAGEAbgBnAGUAZAAgAHQAbwAgAEgAZQBsAHYAZQB0AGkAYwBhACAAKABhAG4AIABhAGQAYQBwAHQAYQB0AGkAbwBuACAAbwBmACAAIgBIAGUAbAB2AGUAdABpAGEAIgAsACAAdABoAGUAIABMAGEAdABpAG4AIABuAGEAbQBlACAAZgBvAHIAIABTAHcAaQB0AHoAZQByAGwAYQBuAGQAKQAuACAATwB2AGUAcgAgAHQAaABlACAAeQBlAGEAcgBzACwAIAB0AGgAZQAgAEgAZQBsAHYAZQB0AGkAYwBhACAAZgBhAG0AaQBsAHkAIAB3AGEAcwAgAGUAeABwAGEAbgBkAGUAZAAgAHQAbwAgAGkAbgBjAGwAdQBkAGUAIABtAGEAbgB5ACAAZABpAGYAZgBlAHIAZQBuAHQAIAB3AGUAaQBnAGgAdABzACwAIABiAHUAdAAgAHQAaABlAHMAZQAgAHcAZQByAGUAIABuAG8AdAAgAGEAcwAgAHcAZQBsAGwAIABjAG8AbwByAGQAaQBuAGEAdABlAGQAIAB3AGkAdABoACAAZQBhAGMAaAAgAG8AdABoAGUAcgAgAGEAcwAgAHQAaABlAHkAIABtAGkAZwBoAHQAIABoAGEAdgBlACAAYgBlAGUAbgAuACAASQBuACAAMQA5ADgAMwAsACAARAAuACAAUwB0AGUAbQBwAGUAbAAgAEEARwAgAGEAbgBkACAATABpAG4AbwB0AHkAcABlACAAcgBlAC0AZABlAHMAaQBnAG4AZQBkACAAYQBuAGQAIABkAGkAZwBpAHQAaQB6AGUAZAAgAE4AZQB1AGUAIABIAGUAbAB2AGUAdABpAGMAYQAgAGEAbgBkACAAdQBwAGQAYQB0AGUAZAAgAGkAdAAgAGkAbgB0AG8AIABhACAAYwBvAGgAZQBzAGkAdgBlACAAZgBvAG4AdAAgAGYAYQBtAGkAbAB5AC4AIABUAG8AZABhAHkALAAgAHQAaABlACAAbwByAGkAZwBpAG4AYQBsACAASABlAGwAdgBlAHQAaQBjAGEAIABmAGEAbQBpAGwAeQAgAGMAbwBuAHMAaQBzAHQAcwAgAG8AZgAgADMANAAgAGQAaQBmAGYAZQByAGUAbgB0ACAAZgBvAG4AdAAgAHcAZQBpAGcAaAB0AHMALAAgAGEAbgBkACAAdABoAGUAIABOAGUAdQBlACAASABlAGwAdgBlAHQAaQBjAGEAIABmAGEAbQBpAGwAeQAgAGMAbwBuAHMAaQBzAHQAcwAgAG8AZgAgADUAMQAgAGYAbwBuAHQAIAB3AGUAaQBnAGgAdABzAC4AIABUAGgAZQAgAEgAZQBsAHYAZQB0AGkAYwBhACAAZgBhAG0AaQBsAHkAIABuAG8AdwAgAGYAbwByAG0AcwAgAGEAbgAgAGkAbgB0AGUAZwByAGEAbAAgAHAAYQByAHQAIABvAGYAIABtAGEAbgB5ACAAZABpAGcAaQB0AGEAbAAgAHAAcgBpAG4AdABlAHIAcwAgAGEAbgBkACAAbwBwAGUAcgBhAHQAaQBuAGcAIABzAHkAcwB0AGUAbQBzACAAYQBuAGQAIABoAGEAcwAgAGIAZQBjAG8AbQBlACAAYQAgAHMAdAB5AGwAaQBzAHQAaQBjACAAYQBuAGMAaABvAHIAIABpAG4AIABvAHUAcgAgAHYAaQBzAHUAYQBsACAAYwB1AGwAdAB1AHIAZQAuACAASQB0ACAAaQBzACAAdABoAGUAIABxAHUAaQBuAHQAZQBzAHMAZQBuAHQAaQBhAGwAIABzAGEAbgBzACAAcwBlAHIAaQBmACAAZgBvAG4AdAAsACAAdABpAG0AZQBsAGUAcwBzACAAYQBuAGQAIABuAGUAdQB0AHIAYQBsACwAIABhAG4AZAAgAGMAYQBuACAAYgBlACAAdQBzAGUAZAAgAGYAbwByACAAYQBsAGwAIAB0AHkAcABlAHMAIABvAGYAIABjAG8AbQBtAHUAbgBpAGMAYQB0AGkAbwBuAC4AIABIAGUAbAB2AGUAdABpAGMAYQAgAFcAbwByAGwAZAAsACAAYQBuACAAdQBwAGQAYQB0AGUAIAB0AG8AIAB0AGgAZQAgAGMAbABhAHMAcwBpAGMAIABIAGUAbAB2AGUAdABpAGMAYQAgAGQAZQBzAGkAZwBuACAAdQBzAGkAbgBnACAAdABoAGUAIABPAHAAZQBuAFQAeQBwAGUAIABmAG8AbgB0ACAAZgBvAHIAbQBhAHQALAAgAGMAbwBuAHQAYQBpAG4AcwAgAHQAaABlACAAZgBvAGwAbABvAHcAaQBuAGcAIABNAGkAYwByAG8AcwBvAGYAdAAgAGMAbwBkAGUAIABwAGEAZwBlAHMAOgAgADEAMgA1ADIAIABMAGEAdABpAG4AIAAxACwAIAAxADIANQAwACAATABhAHQAaQBuACAAMgAgAEUAYQBzAHQAZQByAG4ALAAgADEAMgA1ADEAIABDAHkAcgBpAGwAbABpAGMALAAgADEAMgA1ADMAIABHAHIAZQBlAGsALAAgADEAMgA1ADQAIABUAHUAcgBrACwAIAAxADIANQA1ACAASABlAGIAcgBlAHcALAAgADEAMgA1ADYAIABBAHIAYQBiAGkAYwAsACAAMQAyADUANwAgAFcAaQBuAGQAbwB3AHMAIABCAGEAbAB0AGkAYwAsACAAMQAyADUAOAAgAFcAaQBuAGQAbwB3AHMAIABWAGkAZQB0AG4AYQBtAGUAcwBlACwAIABhAHMAIAB3AGUAbABsACAAYQBzACAAYQAgAG0AaQB4AHQAdQByAGUAIABvAGYAIABiAG8AeAAgAGQAcgBhAHcAaQBuAGcAIABlAGwAZQBtAGUAbgB0ACAAZwBsAHkAcABoAHMAIABhAG4AZAAgAG0AYQB0AGgAZQBtAGEAdABpAGMAYQBsACAAcwB5AG0AYgBvAGwAcwAgACYAIABvAHAAZQByAGEAdABvAHIAcwAuACAASQBuACAAdABvAHQAYQBsACwAIABlAGEAYwBoACAAdwBlAGkAZwBoAHQAIABvAGYAIABIAGUAbAB2AGUAdABpAGMAYQAgAFcAbwByAGwAZAAgAGMAbwBuAHQAYQBpAG4AcwAgAG0AbwByAGUAIAB0AGgAYQBuACAAMQA4ADUAMAAgAGQAaQBmAGYAZQByAGUAbgB0ACAAZwBsAHkAcABoACAAYwBoAGEAcgBhAGMAdABlAHIAcwAhAGgAdAB0AHAAOgAvAC8AdwB3AHcALgBsAGkAbgBvAHQAeQBwAGUALgBjAG8AbQBoAHQAdABwADoALwAvAHcAdwB3AC4AbABpAG4AbwB0AHkAcABlAC4AYwBvAG0ALwBmAG8AbgB0AGQAZQBzAGkAZwBuAGUAcgBzAE4ATwBUAEkARgBJAEMAQQBUAEkATwBOACAATwBGACAATABJAEMARQBOAFMARQAgAEEARwBSAEUARQBNAEUATgBUAA0ACgANAAoAWQBvAHUAIABoAGEAdgBlACAAbwBiAHQAYQBpAG4AZQBkACAAdABoAGkAcwAgAGYAbwBuAHQAIABzAG8AZgB0AHcAYQByAGUAIABlAGkAdABoAGUAcgAgAGQAaQByAGUAYwB0AGwAeQAgAGYAcgBvAG0AIABMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIACAAbwByACAAdABvAGcAZQB0AGgAZQByACAAdwBpAHQAaAAgAHMAbwBmAHQAdwBhAHIAZQAgAGQAaQBzAHQAcgBpAGIAdQB0AGUAZAAgAGIAeQAgAG8AbgBlACAAbwBmACAATABpAG4AbwB0AHkAcABlACcAcwAgAGwAaQBjAGUAbgBzAGUAZQBzAC4ADQAKAA0ACgBUAGgAaQBzACAAZgBvAG4AdAAgAHMAbwBmAHQAdwBhAHIAZQAgAGkAcwAgAGEAIAB2AGEAbAB1AGEAYgBsAGUAIABhAHMAcwBlAHQAIABvAGYAIABMAGkAbgBvAHQAeQBwAGUAIABHAG0AYgBIAC4AIABVAG4AbABlAHMAcwAgAHkAbwB1ACAAaABhAHYAZQAgAGUAbgB0AGUAcgBlAGQAIABpAG4AdABvACAAYQAgAHMAcABlAGMAaQBmAGkAYwAgAGwAaQBjAGUAbgBzAGUAIABhAGcAcgBlAGUAbQBlAG4AdAAgAGcAcgBhAG4AdABpAG4AZwAgAHkAbwB1ACAAYQBkAGQAaQB0AGkAbwBuAGEAbAAgAHIAaQBnAGgAdABzACwAIAB5AG8AdQByACAAdQBzAGUAIABvAGYAIAB0AGgAaQBzACAAZgBvAG4AdAAgAHMAbwBmAHQAdwBhAHIAZQAgAGkAcwAgAGwAaQBtAGkAdABlAGQAIAB0AG8AIAB5AG8AdQByACAAdwBvAHIAawBzAHQAYQB0AGkAbwBuACAAZgBvAHIAIAB5AG8AdQByACAAbwB3AG4AIAB1AHMAZQAuACAAWQBvAHUAIABtAGEAeQAgAG4AbwB0ACAAYwBvAHAAeQAgAG8AcgAgAGQAaQBzAHQAcgBpAGIAdQB0AGUAIAB0AGgAaQBzACAAZgBvAG4AdAAgAHMAbwBmAHQAdwBhAHIAZQAuACAASQBmACAAeQBvAHUAIABoAGEAdgBlACAAYQBuAHkAIABxAHUAZQBzAHQAaQBvAG4AcwAgAHIAZQBnAGEAcgBkAGkAbgBnACAAeQBvAHUAcgAgAGwAaQBjAGUAbgBzAGUAIAB0AGUAcgBtAHMALAAgAHAAbABlAGEAcwBlACAAcgBlAHYAaQBlAHcAIAB0AGgAZQAgAGwAaQBjAGUAbgBzAGUAIABhAGcAcgBlAGUAbQBlAG4AdAAgAHkAbwB1ACAAcgBlAGMAZQBpAHYAZQBkACAAdwBpAHQAaAAgAHQAaABlACAAcwBvAGYAdAB3AGEAcgBlAC4ADQAKAA0ACgBHAGUAbgBlAHIAYQBsACAAbABpAGMAZQBuAHMAZQAgAHQAZQByAG0AcwAgAGEAbgBkACAAdQBzAGEAZwBlACAAcgBpAGcAaAB0AHMAIABjAGEAbgAgAGIAZQAgAHYAaQBlAHcAZQBkACAAYQB0ACAAdwB3AHcALgBsAGkAbgBvAHQAeQBwAGUALgBjAG8AbQAvAGwAaQBjAGUAbgBzAGUALgANAAoADQAKAEcAZQBuAGUAcgBlAGwAbABlACAATABpAHoAZQBuAHoAYgBlAGQAaQBuAGcAdQBuAGcAZQBuACAAdQBuAGQAIABOAHUAdAB6AHUAbgBnAHMAcgBlAGMAaAB0AGUAIABmAGkAbgBkAGUAbgAgAFMAaQBlACAAdQBuAHQAZQByACAAdwB3AHcALgBsAGkAbgBvAHQAeQBwAGUALgBjAG8AbQAvAGwAaQBjAGUAbgBzAGUALgANAAoADQAKAFAAbwB1AHIAIABwAGwAdQBzACAAZAAnAGkAbgBmAG8AcgBtAGEAdABpAG8AbgBzACAAYwBvAG4AYwBlAHIAbgBhAG4AdAAgAGwAZQAgAGMAbwBuAHQAcgBhAHQAIABkACcAdQB0AGkAbABpAHMAYQB0AGkAbwBuACAAZAB1ACAAbABvAGcAaQBjAGkAZQBsACAAZABlACAAcABvAGwAaQBjAGUAcwAsACAAdgBlAHUAaQBsAGwAZQB6ACAAYwBvAG4AcwB1AGwAdABlAHIAIABuAG8AdAByAGUAIABzAGkAdABlACAAdwBlAGIAIAB3AHcAdwAuAGwAaQBuAG8AdAB5AHAAZQAuAGMAbwBtAC8AbABpAGMAZQBuAHMAZQAuAA0ACgANAAoATABpAG4AbwB0AHkAcABlACAARwBtAGIASAAgAGMAYQBuACAAYgBlACAAYwBvAG4AdABhAGMAdABlAGQAIABhAHQAOgANAAoADQAKAFQAZQBsAC4AOgAgACsANAA5ACgAMAAp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IDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMCAwIDAgMTAyM10KZW5kb2JqCnhyZWYKMCAzMgowMDAwMDAwMDAwIDY1NTM1IGYgCjAwMDAwMDAwMTUgMDAwMDAgbiAKMDAwMDAwMDEwOSAwMDAwMCBuIAowMDAwMDAwMTU4IDAwMDAwIG4gCjAwMDAwMDAyMTUgMDAwMDAgbiAKMDAwMDAxOTg3NyAwMDAwMCBuIAowMDAwMDIwMjU3IDAwMDAwIG4gCjAwMDAwMjA0MjYgMDAwMDAgbiAKMDAwMDAyMDYwMiAwMDAwMCBuIAowMDAwMDIwNzY2IDAwMDAwIG4gCjAwMDAwMjA5MzEgMDAwMDAgbiAKMDAwMDAzNDU2MSAwMDAwMCBuIAowMDAwMDQwMzA5IDAwMDAwIG4gCjAwMDAwNDM4MDcgMDAwMDAgbiAKMDAwMDA0NDEzNCAwMDAwMCBuIAowMDAwMDQ5NjY0IDAwMDAwIG4gCjAwMDAwNTAwMTEgMDAwMDAgbiAKMDAwMDA2MjgxNiAwMDAwMCBuIAowMDAwMDYzMDMzIDAwMDAwIG4gCjAwMDAwNjM2MjUgMDAwMDAgbiAKMDAwMDA2NDA1NSAwMDAwMCBuIAowMDAwMDk0ODM2IDAwMDAwIG4gCjAwMDAwOTUwNTYgMDAwMDAgbiAKMDAwMDA5NTY2NyAwMDAwMCBuIAowMDAwMDk2MDk3IDAwMDAwIG4gCjAwMDAwOTgyNjAgMDAwMDAgbiAKMDAwMDA5ODQ2NyAwMDAwMCBuIAowMDAwMDk4OTA3IDAwMDAwIG4gCjAwMDAwOTg5NDQgMDAwMDAgbiAKMDAwMDEwMTAxOSAwMDAwMCBuIAowMDAwMTAxMjI2IDAwMDAwIG4gCjAwMDAxMDE2NTEgMDAwMDAgbiAKdHJhaWxlcgo8PCAvSW5mbyAxIDAgUgovUm9vdCAyIDAgUgovU2l6ZSAzMgo+PgpzdGFydHhyZWYKMTAxOTY4CiUlRU9GCg=="
                            ],
                            "category": "battery_form",
                            "format": "pdf",
                            "page_size": "a4",
                            "required": true,
                            "url": null
                          }
                        ],
                        "shipping_settings": {
                          "b13a_filing": null,
                          "label_customization_fields": []
                        },
                        "tracking_page_url": "http://api.easyship.com:9003/shipment-tracking/ESSG10006001",
                        "trackings": [],
                        "updated_at": "2022-02-22T12:21:00Z",
                        "warehouse_state": "none"
                      },
                      "examples": {
                        "label_successfully_created": {
                          "summary": "label successfully created",
                          "value": {
                            "printing_options": {
                              "format": "pdf",
                              "label": "A4"
                            }
                          }
                        }
                      },
                      "meta": {
                        "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
                        "unavailable_couriers": []
                      }
                    },
                    "summary": "label successfully created"
                  }
                },
                "schema": {
                  "$ref": "#/components/schemas/shipment_single"
                }
              }
            }
          }
        },
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/SingleLabelCreate"
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
      "shipment_single": {
        "type": "object",
        "description": "Single shipment with all its details",
        "additionalProperties": false,
        "properties": {
          "shipment": {
            "$ref": "#/components/schemas/Shipment"
          },
          "meta": {
            "type": "object",
            "additionalProperties": false,
            "properties": {
              "status": {
                "type": "string"
              },
              "errors": {
                "type": "array",
                "items": {
                  "type": "string"
                }
              },
              "unavailable_couriers": {
                "$ref": "#/components/schemas/UnavailableCouriers"
              },
              "request_id": {
                "$ref": "#/components/schemas/Meta/properties/request_id"
              }
            }
          }
        }
      },
      "CourierService": {
        "type": "object",
        "description": "Courier service",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "ID"
          },
          "name": {
            "type": "string",
            "description": "If the courier service is connected through your own courier account, this will be \"{nickname} - {official_name}\". If the courier service is provided by Easyship, this will be the official name of the courier service."
          },
          "umbrella_name": {
            "type": "string",
            "description": "Human-readable name for the courier company that offers this service."
          },
          "official_name": {
            "type": "string",
            "description": "Official name of the courier service."
          },
          "nickname": {
            "type": "string",
            "description": "Nickname you set when creating/updating the courier service. Only applicable for LYOC services.",
            "nullable": true
          },
          "service_name": {
            "type": "string",
            "description": "Service that offered by the courier company."
          },
          "logo_url": {
            "type": "string",
            "description": "Logo of the courier. Deprecated in favor of `courier_logo_url`.",
            "nullable": true,
            "deprecated": true
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "active": {
            "type": "boolean",
            "nullable": true,
            "description": "Whether the courier is active or not."
          },
          "restricted_to_origin_states": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "List of origin states that the service is available for (US only)."
          },
          "restricted_to_destination_states": {
            "type": "array",
            "nullable": true,
            "items": {
              "type": "string"
            },
            "description": "List of destination states that the service is available for (US only)."
          },
          "supported_incoterms": {
            "description": "Terms of Sale\nDDP: Seller pays all import duties/taxes.\nDDU: Buyer pays all import duties/taxes.\n",
            "type": "array",
            "items": {
              "type": "string",
              "enum": [
                "DDU",
                "DDP"
              ],
              "default": "DDU"
            }
          },
          "ioss_support": {
            "type": "string",
            "nullable": true,
            "enum": [
              "supported_mandatory",
              "supported_optional",
              "not_supported",
              null
            ]
          },
          "customer_reference_id": {
            "type": "string",
            "nullable": true,
            "description": "An identifier for the customer who owns the account. Available only for selected customers."
          },
          "accepts_outbounds": {
            "deprecated": true,
            "type": "boolean",
            "description": "Whether the courier can be used to generate outbound labels."
          },
          "accepts_prepaid_returns": {
            "deprecated": true,
            "type": "boolean",
            "description": "Returns `true` if returns are billed upon label generation."
          },
          "accepts_pay_on_scan_returns": {
            "deprecated": true,
            "type": "boolean",
            "description": "Returns `true` if returns are billed upon label scan."
          },
          "domestic": {
            "type": "boolean",
            "description": "Returns `true` if the courier service is a domestic service. Both `domestic` and `international` can be `true` at the same time."
          },
          "international": {
            "type": "boolean",
            "description": "Returns `true` if the courier service is an international service. Both `domestic` and `international` can be `true` at the same time."
          },
          "courier_id": {
            "type": "string",
            "format": "uuid",
            "description": "The Courier ID is associated with this service."
          },
          "courier_logo_url": {
            "type": "string",
            "description": "The URL of the Courier logo."
          },
          "easyship_courier_service": {
            "type": "boolean",
            "description": "Whether the Courier Service belongs to Easyship or not."
          },
          "accepts": {
            "type": "object",
            "description": "Acceptance criteria for the courier.",
            "properties": {
              "outbounds": {
                "type": "boolean",
                "description": "Whether the courier can be used to generate outbound labels."
              },
              "prepaid_returns": {
                "type": "boolean",
                "description": "Returns `true` if returns are billed upon label generation."
              },
              "pay_on_scan_returns": {
                "type": "boolean",
                "description": "Returns `true` if returns are billed upon label scan."
              },
              "pi965_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi965)."
              },
              "pi966_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi966)."
              },
              "pi967_batteries": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts battery (pi967)."
              },
              "liquids": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts liquids."
              },
              "specific_dangerous_goods": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts other dangerous goods that are not batteries (pi966, pi967, or pi968)."
              },
              "documents": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts documents."
              },
              "parcels": {
                "type": "boolean",
                "description": "Returns `true` if courier accepts parcels."
              }
            }
          },
          "available_handover_options": {
            "type": "array",
            "description": "A list of one or more of `dropoff`, `free_pickup`, and `paid_pickup`",
            "items": {
              "type": "string",
              "enum": [
                "dropoff",
                "free_pickup",
                "paid_pickup"
              ]
            }
          },
          "tracking_rating": {
            "type": "number",
            "description": "Quality of tracking information provided by the courier\n\n-1: No tracking number\n0: Limited\n1: Basic\n2: Regular\n3: Excellent\n",
            "enum": [
              -1,
              0,
              1,
              2,
              3
            ]
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
      "DestinationAddress": {
        "type": "object",
        "additionalProperties": false,
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
            "nullable": true,
            "maximum": 200,
            "description": "State, Province, or other top-level administrative region. Mandatory for these countries: AU, CA, CN, ID, MX, MY, TH, US, VN. Use abbreviations for naming the state if possible (2 letters for the US/CA, 2 or 3 letters for AU). For countries using provinces, use the full province names."
          },
          "city": {
            "type": "string",
            "description": "City or Suburb",
            "maximum": 200
          },
          "postal_code": {
            "type": "string",
            "description": "Postal code. Mandatory for most countries (if not applicable, for example Hong Kong, leave null or 0)"
          },
          "country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2"
          },
          "company_name": {
            "type": "string",
            "nullable": true,
            "description": "The company or organization at the address",
            "maximum": 50
          },
          "contact_name": {
            "type": "string",
            "description": "The full name of a person at the address",
            "maximum": 50
          },
          "contact_phone": {
            "type": "string",
            "description": "Phone number used to reach the person in contact_name (may or may not be SMS-ready)",
            "maximum": 20
          },
          "contact_email": {
            "type": "string",
            "format": "email",
            "description": "Email address used to reach the person in `contact_name`",
            "maximum": 50
          },
          "delivery_instructions": {
            "type": "string",
            "description": "Delivery instructions for the address, see [Delivery Instructions](https://developers.easyship.com/page/delivery-instructions).",
            "maximum": 200,
            "nullable": true
          }
        }
      },
      "Box": {
        "type": "object",
        "description": "User-defined details of a box used for shipments",
        "externalDocs": {
          "description": "Saving Shipping Boxes Dimensions - Easyship Support",
          "url": "https://support.easyship.com/hc/en-us/articles/360025430011-Saving-Shipping-Boxes-Dimensions"
        },
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "nullable": true,
            "description": "ID"
          },
          "courier": {
            "type": "object",
            "nullable": true,
            "additionalProperties": false,
            "properties": {
              "umbrella_name": {
                "type": "string",
                "description": "Human-readable name for the courier company that offers this service, when applicable."
              },
              "country_alpha2": {
                "$ref": "#/components/schemas/CountryAlpha2"
              }
            }
          },
          "name": {
            "type": "string",
            "nullable": true,
            "description": "Name"
          },
          "slug": {
            "type": "string",
            "nullable": true,
            "description": "Slug"
          },
          "outer_dimensions": {
            "type": "object",
            "additionalProperties": false,
            "description": "A measure of the space taken by the box itself, in cm.",
            "properties": {
              "length": {
                "type": "number"
              },
              "width": {
                "type": "number"
              },
              "height": {
                "type": "number"
              }
            }
          },
          "weight": {
            "type": "number",
            "description": "The weight of the box's packaging materials (excluding items inside), in kg."
          },
          "type": {
            "type": "string",
            "description": "Box type."
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
      "CountryAlpha2Nullable": {
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
          "ZW",
          null
        ],
        "nullable": true
      },
      "Currency": {
        "type": "string",
        "nullable": false,
        "enum": [
          "AED",
          "AFN",
          "ALL",
          "AMD",
          "ANG",
          "AOA",
          "ARS",
          "AUD",
          "AWG",
          "AZN",
          "BAM",
          "BBD",
          "BDT",
          "BGN",
          "BHD",
          "BIF",
          "BMD",
          "BND",
          "BOB",
          "BRL",
          "BSD",
          "BTN",
          "BWP",
          "BYR",
          "BZD",
          "CAD",
          "CDF",
          "CHF",
          "CLF",
          "CLP",
          "CNY",
          "COP",
          "CRC",
          "CUC",
          "CUP",
          "CVE",
          "CZK",
          "DJF",
          "DKK",
          "DOP",
          "DZD",
          "EGP",
          "ERN",
          "ETB",
          "EUR",
          "FJD",
          "FKP",
          "GBP",
          "GEL",
          "GHS",
          "GIP",
          "GMD",
          "GNF",
          "GTQ",
          "GYD",
          "HKD",
          "HNL",
          "HRK",
          "HTG",
          "HUF",
          "IDR",
          "ILS",
          "INR",
          "IQD",
          "IRR",
          "ISK",
          "JMD",
          "JOD",
          "JPY",
          "KES",
          "KGS",
          "KHR",
          "KMF",
          "KPW",
          "KRW",
          "KWD",
          "KYD",
          "KZT",
          "LAK",
          "LBP",
          "LKR",
          "LRD",
          "LSL",
          "LTL",
          "LVL",
          "LYD",
          "MAD",
          "MDL",
          "MGA",
          "MKD",
          "MMK",
          "MNT",
          "MOP",
          "MRO",
          "MUR",
          "MVR",
          "MWK",
          "MXN",
          "MYR",
          "MZN",
          "NAD",
          "NGN",
          "NIO",
          "NOK",
          "NPR",
          "NZD",
          "OMR",
          "PAB",
          "PEN",
          "PGK",
          "PHP",
          "PKR",
          "PLN",
          "PYG",
          "QAR",
          "RON",
          "RSD",
          "RUB",
          "RWF",
          "SAR",
          "SBD",
          "SCR",
          "SDG",
          "SEK",
          "SGD",
          "SHP",
          "SKK",
          "SLL",
          "SOS",
          "SRD",
          "SSP",
          "STD",
          "SVC",
          "SYP",
          "SZL",
          "THB",
          "TJS",
          "TMT",
          "TND",
          "TOP",
          "TRY",
          "TTD",
          "TWD",
          "TZS",
          "UAH",
          "UGX",
          "USD",
          "UYU",
          "UZS",
          "VES",
          "VND",
          "VUV",
          "WST",
          "XAF",
          "XAG",
          "XAU",
          "XCD",
          "XDR",
          "XOF",
          "XPF",
          "YER",
          "ZAR",
          "ZMW",
          "BTC",
          "JEP",
          "EEK",
          "GHC",
          "MTL",
          "TMM",
          "YEN",
          "ZWD",
          "ZWL",
          "ZWN",
          "ZWR"
        ],
        "example": "USD",
        "description": "ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)"
      },
      "Parcel": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of the parcel",
            "nullable": true
          },
          "total_actual_weight": {
            "type": "number",
            "description": "Total weight of the shipment, including the box weight. If you provide the total weight of the shipment, then the weight for items can be optional."
          },
          "box": {
            "$ref": "#/components/schemas/Box"
          },
          "items": {
            "type": "array",
            "description": "Array of all shipment items. May be empty for multi-parcel shipments (e.g. additional boxes).",
            "minItems": 0,
            "maxItems": 200,
            "items": {
              "$ref": "#/components/schemas/ParcelItem"
            }
          },
          "tracking_number": {
            "type": "string",
            "nullable": true,
            "description": "Per-parcel tracking number assigned by the courier for multi-parcel shipments.\nOnly present when the courier returns individual tracking numbers per parcel (FedEx, UPS, DHL, DPD GB).\nNull for single-parcel shipments or unsupported couriers."
          }
        }
      },
      "ParcelItem": {
        "type": "object",
        "description": "A line item in a shipment manifest; may be multiple physical objects.",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of the item"
          },
          "description": {
            "type": "string",
            "description": "Description of the item",
            "maximum": 200
          },
          "category": {
            "type": "string",
            "nullable": true,
            "description": "Item Category slug. Use the Item Categories API to retrieve a list of available item categories or use HS Code field.",
            "maximum": 200
          },
          "sku": {
            "type": "string",
            "description": "Item Stock Keeping Unit (SKU) as listed in your store.",
            "maximum": 100,
            "nullable": true
          },
          "platform_product_id": {
            "type": "string",
            "nullable": true,
            "description": "Platform Product ID (PPID). Unique identifier from your store platform (e.g. Shopify variant ID, WooCommerce product ID). Used to link shipment items to product catalog entries for auto-population of product attributes."
          },
          "manufacturer_part_number": {
            "type": "string",
            "nullable": true,
            "description": "Manufacturer Part Number (MPN). The manufacturer's internal code or part number for the product. Useful for wholesale and B2B operations to identify products by their source."
          },
          "global_trade_item_number": {
            "type": "string",
            "nullable": true,
            "description": "Global Trade Item Number (GTIN). Internationally recognized unique identifier for trade items, including UPC (US/Canada), EAN (Europe), JAN (Japan), and ISBN (books). Used by retailers and carriers for product identification and inventory tracking."
          },
          "hs_code": {
            "type": "string",
            "description": "HS Code of the item",
            "nullable": true
          },
          "origin_country_alpha2": {
            "$ref": "#/components/schemas/CountryAlpha2Nullable"
          },
          "contains_battery_pi966": {
            "type": "boolean",
            "description": "Whether the item contains a PI966 battery (applicable when HS code is used).",
            "nullable": true
          },
          "contains_battery_pi967": {
            "type": "boolean",
            "description": "Whether the item contains a PI967 battery (applicable when HS code is used).",
            "nullable": true
          },
          "contains_liquids": {
            "type": "boolean",
            "description": "Whether the item contains liquids (applicable when HS code is used).",
            "nullable": true
          },
          "quantity": {
            "type": "integer",
            "description": "Item quantity",
            "default": 1
          },
          "dimensions": {
            "type": "object",
            "description": "Dimensions of the item",
            "additionalProperties": false,
            "properties": {
              "length": {
                "type": "number",
                "description": "Item length; Optional if the Box dimensions are provided."
              },
              "width": {
                "type": "number",
                "description": "Item width; Optional if the Box dimensions are provided."
              },
              "height": {
                "type": "number",
                "description": "Item height; Optional if the Box dimensions are provided."
              }
            }
          },
          "actual_weight": {
            "type": "number",
            "description": "Item actual weight in `kg`, must be greater than 0; Optional if `total_actual_weight` is provided."
          },
          "origin_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Item customs value currency. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "origin_customs_value": {
            "type": "number",
            "description": "Customs value of the item"
          },
          "declared_currency": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Currency"
              },
              {
                "description": "Currency of the item. ISO-4217 three-letter alphabetic currency code (e.g. USD, EUR, GBP)."
              }
            ]
          },
          "declared_customs_value": {
            "type": "number",
            "description": "Item customs value, must be greater than 0 unless category is `documents`. Please note that this value refers to the unit rather than the total."
          }
        }
      },
      "ShipmentTracking": {
        "type": "object",
        "description": "A source of tracking data for the shipment's journey",
        "additionalProperties": false,
        "properties": {
          "tracking_number": {
            "type": "string",
            "description": "Reference provided by the courier for this leg"
          },
          "local_tracking_number": {
            "type": "string",
            "nullable": true,
            "description": "Local tracking number provided by DHL eCommerce"
          },
          "alternate_tracking_number": {
            "type": "string",
            "nullable": true,
            "description": "Alternate tracking number provided by DHL eCommerce"
          },
          "leg_number": {
            "type": "integer",
            "minimum": 1,
            "description": "Sequential index of the different portions of the shipment's journey. If a shipment is passed to a new courier, it begins a new leg."
          },
          "handler": {
            "type": "string",
            "description": "The service that is handling the tracking process"
          },
          "tracking_state": {
            "type": "string",
            "description": "The current state of the tracking",
            "enum": [
              "created",
              "active",
              "pending",
              "completed",
              "overwritten_by_admin"
            ]
          }
        }
      },
      "ShipmentDocument": {
        "type": "object",
        "additionalProperties": false,
        "properties": {
          "category": {
            "type": "string",
            "description": "Document category"
          },
          "required": {
            "type": "boolean",
            "description": "Whether the document is required"
          },
          "format": {
            "type": "string",
            "nullable": true,
            "description": "Document format"
          },
          "page_size": {
            "type": "string",
            "nullable": true,
            "description": "Page size"
          },
          "base64_encoded_strings": {
            "type": "array",
            "description": "Base64 encoded strings",
            "items": {
              "type": "string",
              "format": "byte"
            }
          },
          "url": {
            "type": "string",
            "nullable": true,
            "description": "URL of the document"
          }
        }
      },
      "Rate": {
        "type": "object",
        "description": "Result of a quote request, including shipping & tax costs for a specific courier service.",
        "additionalProperties": false,
        "properties": {
          "courier_service": {
            "$ref": "#/components/schemas/RateCourierService"
          },
          "min_delivery_time": {
            "type": "integer",
            "description": "The fastest estimate of delivery time for this courier service, in days."
          },
          "max_delivery_time": {
            "type": "integer",
            "description": "The slowest estimate of delivery time for this courier service, in days."
          },
          "value_for_money_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options. 1 indicates the best value for money."
          },
          "delivery_time_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options, in minimum delivery time estimate; 1 indicates the fastest option."
          },
          "cost_rank": {
            "type": "number",
            "description": "Where this courier service ranks among the other offered options, in total price; 1 indicates the best value for money."
          },
          "currency": {
            "$ref": "#/components/schemas/Currency"
          },
          "shipment_charge": {
            "type": "number",
            "description": "Base cost of the courier service"
          },
          "fuel_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when fuel costs are high"
          },
          "remote_area_surcharge": {
            "type": "number",
            "description": "Sum of the origin and destination base fees listed in `remote_area_surcharges`"
          },
          "remote_area_surcharges": {
            "description": "Origin and destination remote area surcharges",
            "type": "object",
            "additionalProperties": false,
            "nullable": true,
            "properties": {
              "origin": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "name": {
                    "type": "string",
                    "example": "Pickup Area Surcharge"
                  },
                  "base": {
                    "type": "number"
                  }
                }
              },
              "destination": {
                "type": "object",
                "additionalProperties": false,
                "properties": {
                  "name": {
                    "type": "string",
                    "example": "Delivery Area Surcharge"
                  },
                  "base": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "other_surcharges": {
            "type": "object",
            "nullable": true,
            "description": "Other surcharges",
            "additionalProperties": false,
            "properties": {
              "total_fee": {
                "type": "number",
                "description": "Sum of the surcharge fees, in the currency specified for the shipment"
              },
              "details": {
                "type": "array",
                "description": "An array of individual surcharges being applied",
                "items": {
                  "type": "object",
                  "additionalProperties": false,
                  "properties": {
                    "name": {
                      "type": "string",
                      "description": "Surcharge name, in English, to be displayed to user",
                      "example": "Peak Surcharge"
                    },
                    "fee": {
                      "type": "number",
                      "description": "Surcharge fee in the currency of the shipment"
                    },
                    "origin_fee": {
                      "type": "number",
                      "description": "Surcharge fee in the currency of the shipment's origin country"
                    }
                  }
                }
              }
            }
          },
          "oversized_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when parcels exceed a specified threshold size or weight"
          },
          "additional_services_surcharge": {
            "type": "number",
            "description": "A fee added by the courier when additional services are added (e.g. delivery confirmation)"
          },
          "residential_full_fee": {
            "type": "number",
            "description": "A fee added by the courier when the receiver is at a residential address"
          },
          "residential_discounted_fee": {
            "type": "number",
            "description": "A discounted fee added by the courier when the receiver is at a residential address"
          },
          "shipment_charge_total": {
            "type": "number",
            "description": "Subtotal of `shipment_charge`, `fuel_surcharge`, `residential_*_fee`, `remote_area_surcharge`, `additional_services_surcharge`, & `oversized_surcharge`"
          },
          "warehouse_handling_fee": {
            "type": "number",
            "description": "A fee added by the fulfillment service for managing warehouse operations"
          },
          "insurance_fee": {
            "type": "number",
            "description": "The cost of the insurance policy purchased for this shipment"
          },
          "sales_tax": {
            "type": "number",
            "description": "National government taxes, calculated as a portion of the purchase price"
          },
          "provincial_sales_tax": {
            "type": "number",
            "description": "State, province, or local government taxes, calculated as a portion of the purchase price"
          },
          "ddp_handling_fee": {
            "type": "number",
            "description": "A fee added by the courier when they pay import taxes and duties on the sender's behalf. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_tax_charge": {
            "type": "number",
            "description": "Import tax charge. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_tax_non_chargeable": {
            "type": "number",
            "description": "Import tax non-chargeable. Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "import_duty_charge": {
            "type": "number",
            "description": "Import duty amount collected upfront with the shipment (DDP only). `0` for DDU shipments where the buyer pays duty at customs. Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false.",
            "nullable": true
          },
          "total_charge": {
            "type": "number",
            "description": "The sum of shipping_charge and all applicable fees for this shipment"
          },
          "is_above_threshold": {
            "type": "boolean",
            "nullable": true,
            "description": "True if the purchase price exceeds the threshold set by the import country for customs charges. If `false`, `import_tax_charge`, `import_duty_charge`, `estimated_import_tax`, and `estimated_import_duty` should be zero."
          },
          "is_above_duty_threshold": {
            "type": "boolean",
            "nullable": true,
            "description": "True if the shipment value exceeds the import country's de minimis threshold for duty. Distinct from `is_above_threshold`, which covers the combined tax and duty threshold. May be `true` while `import_duty_charge` is `0` on DDU rates. Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false."
          },
          "import_duty_details": {
            "type": "array",
            "nullable": true,
            "description": "Per line-item duty calculation breakdown in the rate's `currency`, including HS codes used, fallback flags, rates applied, and amounts. On DDU rates, amounts align with `estimated_import_duty`. On DDP rates, amounts align with `import_duty_charge`. Present when a duty calculation was performed, including when the duty amount is zero (e.g. FTA preferential rate). Null when the subscription lacks taxes and duties or when `calculate_tax_and_duties` is false. Only returned on the top-level rate object, not within `rates_in_origin_currency`.",
            "items": {
              "$ref": "#/components/schemas/ImportDutyDetails"
            }
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "estimated_import_tax": {
            "type": "number",
            "description": "An estimate of import taxes that will be charged to the buyer when the shipment clears customs (only applicable for DDU incoterms). Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "estimated_import_duty": {
            "type": "number",
            "description": "An estimate of import duty that will be charged to the buyer when the shipment clears customs (only applicable for DDU incoterms). Null is returned when there is an insufficient subscription tier for feature taxes and duties.",
            "nullable": true
          },
          "minimum_pickup_fee": {
            "type": "number",
            "minimum": 0,
            "description": "The minimum fee applied for `paid_pickup` options, for this courier service"
          },
          "available_handover_options": {
            "type": "array",
            "description": "A list of one or more of `dropoff`, `free_pickup`, and `paid_pickup`",
            "items": {
              "type": "string"
            }
          },
          "tracking_rating": {
            "type": "number",
            "description": "A characterization of the level of detail provided by the courier's tracking data.\n  * -1 - No tracking number\n  * 0 - Infrequent tracking events\n  * 1 - Infrequent tracking events\n  * 2 - Tracking main milestones with delivery confirmation\n  * 3 - Tracking all steps of transit with delivery confirmation\n",
            "minimum": -1,
            "maximum": 3
          },
          "easyship_rating": {
            "type": "number",
            "minimum": 0,
            "maximum": 5,
            "description": "Average of customer ratings of this courier service; provided by Easyship users and their buyers."
          },
          "courier_remarks": {
            "type": "string",
            "nullable": true,
            "description": "Additional details relevant to choosing the appropriate courier service"
          },
          "payment_recipient": {
            "type": "string",
            "description": "Who collects payment for this shipment (and when)",
            "enum": [
              "Easyship",
              "EasyshipPayOnScan",
              "Courier"
            ]
          },
          "discount": {
            "$ref": "#/components/schemas/RateDiscount"
          },
          "rates_in_origin_currency": {
            "type": "object",
            "description": "Rates in origin currency",
            "additionalProperties": false,
            "properties": {
              "currency": {
                "$ref": "#/components/schemas/Currency"
              },
              "shipment_charge": {
                "$ref": "#/components/schemas/Rate/properties/shipment_charge"
              },
              "fuel_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/fuel_surcharge"
              },
              "remote_area_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/remote_area_surcharge"
              },
              "additional_services_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/additional_services_surcharge"
              },
              "oversized_surcharge": {
                "$ref": "#/components/schemas/Rate/properties/oversized_surcharge"
              },
              "shipment_charge_total": {
                "$ref": "#/components/schemas/Rate/properties/shipment_charge_total"
              },
              "warehouse_handling_fee": {
                "$ref": "#/components/schemas/Rate/properties/warehouse_handling_fee"
              },
              "insurance_fee": {
                "$ref": "#/components/schemas/Rate/properties/insurance_fee"
              },
              "ddp_handling_fee": {
                "$ref": "#/components/schemas/Rate/properties/ddp_handling_fee"
              },
              "import_tax_charge": {
                "$ref": "#/components/schemas/Rate/properties/import_tax_charge"
              },
              "import_tax_non_chargeable": {
                "$ref": "#/components/schemas/Rate/properties/import_tax_non_chargeable"
              },
              "import_duty_charge": {
                "$ref": "#/components/schemas/Rate/properties/import_duty_charge"
              },
              "residential_discounted_fee": {
                "$ref": "#/components/schemas/Rate/properties/residential_discounted_fee"
              },
              "residential_full_fee": {
                "$ref": "#/components/schemas/Rate/properties/residential_full_fee"
              },
              "total_charge": {
                "$ref": "#/components/schemas/Rate/properties/total_charge"
              },
              "estimated_import_tax": {
                "$ref": "#/components/schemas/Rate/properties/estimated_import_tax"
              },
              "estimated_import_duty": {
                "$ref": "#/components/schemas/Rate/properties/estimated_import_duty"
              },
              "sales_tax": {
                "$ref": "#/components/schemas/Rate/properties/sales_tax"
              },
              "provincial_sales_tax": {
                "$ref": "#/components/schemas/Rate/properties/provincial_sales_tax"
              },
              "minimum_pickup_fee": {
                "$ref": "#/components/schemas/Rate/properties/minimum_pickup_fee"
              }
            }
          },
          "description": {
            "type": "string",
            "description": "Details that the user should know when preparing to hand over the shipment to the courier (e.g. pick-up or drop-off)"
          },
          "full_description": {
            "type": "string",
            "description": "Full description"
          }
        }
      },
      "RateDiscount": {
        "type": "object",
        "description": "A discount applied to the rate. Amount and percentage should not both be defined at the same time",
        "nullable": true,
        "additionalProperties": false,
        "properties": {
          "amount": {
            "type": "number",
            "description": "A fixed amount to discount from the price"
          },
          "origin_amount": {
            "type": "number",
            "description": "Discount origin amount"
          }
        }
      },
      "RateCourierService": {
        "type": "object",
        "description": "Courier Service for Rate",
        "additionalProperties": false,
        "properties": {
          "id": {
            "type": "string",
            "format": "uuid",
            "description": "unique identifier for a courier service"
          },
          "name": {
            "type": "string",
            "description": "Human-readable name for the courier service used in this rate."
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
          "logo": {
            "$ref": "#/components/schemas/CourierService/properties/logo_url"
          },
          "easyship_courier_service": {
            "type": "boolean",
            "description": "Whether the Courier Service belongs to Easyship or not.",
            "nullable": true
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
      "ShipmentCreate": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "parcels"
        ],
        "properties": {
          "origin_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Origin Address",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "origin_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of origin address. Required if the `origin_address` object is not provided. If provided, the origin address will be ignored."
          },
          "sender_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Sender Address. Only applies if the courier allows a different address to be displayed on the label. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "sender_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of sender address. Required if the `sender_address` object is not provided."
          },
          "return_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/Address"
              },
              {
                "description": "Return Address. If not specified, the origin address is used by default.",
                "required": [
                  "line_1",
                  "city",
                  "company_name",
                  "contact_name",
                  "contact_phone",
                  "contact_email"
                ]
              }
            ]
          },
          "return_address_id": {
            "type": "string",
            "format": "uuid",
            "description": "ID of return address. Required if the `return_address` object is not provided."
          },
          "destination_address": {
            "allOf": [
              {
                "$ref": "#/components/schemas/DestinationAddress"
              },
              {
                "required": [
                  "line_1",
                  "city",
                  "contact_name",
                  "contact_email",
                  "contact_phone"
                ]
              }
            ]
          },
          "return": {
            "type": "boolean",
            "description": "Set the shipment as a return shipment"
          },
          "metadata": {
            "$ref": "#/components/schemas/Shipment/properties/metadata"
          },
          "set_as_residential": {
            "type": "boolean",
            "description": "US addresses will be automatically validated when not specified. If specified, the validation will be bypassed."
          },
          "consignee_tax_id": {
            "type": "string",
            "description": "The consignee's tax identification number or EIN. This is required for customs clearance when shipping to certain countries, such as China and Brazil."
          },
          "eei_reference": {
            "type": "string",
            "description": "The Electronic Export Identifier (EEI). This is required when shipping goods over USD2500 in value (Applies to US-outbound shipments only)."
          },
          "regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/regulatory_identifiers"
          },
          "buyer_regulatory_identifiers": {
            "$ref": "#/components/schemas/Shipment/properties/buyer_regulatory_identifiers"
          },
          "incoterms": {
            "$ref": "#/components/schemas/Shipment/properties/incoterms"
          },
          "insurance": {
            "$ref": "#/components/schemas/Shipment/properties/insurance"
          },
          "order_data": {
            "$ref": "#/components/schemas/Shipment/properties/order_data"
          },
          "courier_settings": {
            "type": "object",
            "properties": {
              "courier_service_id": {
                "type": "string",
                "description": "Select a specific courier service to create the shipment with, only the rate for this courier service will be returned. If provided, all other courier service lookup parameters (`courier_umbrella`, `courier_service_name`, `courier_account_number`) will be ignored.",
                "nullable": true
              },
              "courier_umbrella": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The umbrella name of the courier service (e.g., \"FedEx\"). This field is optional; however, if provided, `courier_service_name` and `courier_account_number` must also be included."
              },
              "courier_service_name": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The official name of the courier service (e.g., \"FedEx International Priority®\"). This field is optional; however, if provided, `courier_umbrella` and `courier_account_number` must also be included."
              },
              "courier_account_number": {
                "type": "string",
                "nullable": true,
                "description": "(support LYOC couriers only) The account number of the courier account. This field is optional; however, if provided, `courier_umbrella` and `courier_service_name` must also be included."
              },
              "allow_fallback": {
                "type": "boolean",
                "default": false,
                "description": "If `courier_service_id` is provided but the courier can’t be selected, allow the shipment to be created and the next best rate to be selected. Default: `false`. When false and rates for the `courier_service_id` can't be found, an error will be raised and the shipment won’t be created."
              },
              "apply_shipping_rules": {
                "type": "boolean",
                "default": true,
                "description": "Apply any [shipping rules](https://support.easyship.com/hc/en-us/articles/115003580152-Automate-Shipping-Process-Shipping-Rules) created on the Easyship dashboard (Default: `true`)"
              },
              "list_unavailable_services": {
                "type": "boolean",
                "description": "Setting this option will return detailed information with reasons for each courier in the response."
              }
            }
          },
          "shipping_settings": {
            "type": "object",
            "properties": {
              "additional_services": {
                "type": "object",
                "description": "Configuration for additional services",
                "additionalProperties": false,
                "properties": {
                  "delivery_confirmation": {
                    "description": "Currently officially supported only for selected customers. **Subject to change.**",
                    "type": "string",
                    "enum": [
                      "ups_delivery_confirmation_adult_signature_required",
                      "ups_delivery_confirmation_signature_required",
                      "dpd_uk_signature_required",
                      "dpd_uk_proof_of_identity",
                      "dpd_uk_proof_of_age",
                      "dpd_uk_pin_required"
                    ]
                  },
                  "qr_code": {
                    "type": "string",
                    "description": "Generate QR code when generating label. If a courier does not support it, label will be generated without the QR code. Currently officially supported only for USPS courier. When set to `qr_code`, both the QR code and the original label are returned. `qr_code_with_label` is deprecated and no longer supported; if provided, it silently falls back to `qr_code`. Label customization is not available for USPS. **Subject to change.**",
                    "default": "none",
                    "enum": [
                      "qr_code",
                      "qr_code_with_label",
                      "none"
                    ]
                  }
                }
              },
              "units": {
                "$ref": "#/components/schemas/Units"
              },
              "buy_label": {
                "type": "boolean",
                "default": false,
                "description": "Create a shipment and buy the label in a single API call instead of two. Default: `false`."
              },
              "buy_label_synchronous": {
                "type": "boolean",
                "default": false,
                "description": "Generate a label synchronously. Returns a label in the response. Default: `false`."
              },
              "b13a_filing": {
                "$ref": "#/components/schemas/Shipment/properties/shipping_settings/properties/b13a_filing"
              },
              "printing_options": {
                "type": "object",
                "description": "Specify the format and page sizes of the shipping documents. This will only be taken into account if buy_label_synchronous is `true`.",
                "properties": {
                  "format": {
                    "type": "string",
                    "description": "Options: `png`, `pdf`, `url`, `zpl` (Default: `png`)",
                    "default": "png",
                    "enum": [
                      "png",
                      "pdf",
                      "url",
                      "zpl"
                    ]
                  },
                  "label": {
                    "type": "string",
                    "description": "Label page size. Options: `4x6` / `A4` / `A5` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "A5"
                    ]
                  },
                  "commercial_invoice": {
                    "type": "string",
                    "description": "Commercial invoice page size. Options: `4x6` / `A4` (Default: `A4`)",
                    "default": "A4",
                    "enum": [
                      "4x6",
                      "A4"
                    ]
                  },
                  "packing_slip": {
                    "type": "string",
                    "description": "Packing slip page size. Options: `4x6` / `A4` (Default: `4x6`)",
                    "default": "4x6",
                    "enum": [
                      "4x6",
                      "A4",
                      "none"
                    ]
                  },
                  "remarks": {
                    "type": "string",
                    "maxLength": 70,
                    "description": "Customized commercial invoice remarks for current shipment. It has higher priority than remarks from company settings."
                  }
                }
              },
              "label_customization_fields": {
                "description": "Label customization fields for the shipment. This is only applicable for specific couriers. For detailed explanation, please refer to [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                "type": "array",
                "minItems": 1,
                "items": {
                  "type": "object",
                  "required": [
                    "value"
                  ],
                  "properties": {
                    "code": {
                      "description": "Courier accepted code, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages).",
                      "type": "string"
                    },
                    "value": {
                      "type": "string",
                      "description": "Content to display on the label, see [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    },
                    "convert_to_barcode": {
                      "description": "Identifying for converting value to barcode, specific application logic applies. See [Label Customization Messages](https://developers.easyship.com/page/label-customization-messages)."
                    }
                  }
                }
              }
            }
          },
          "parcels": {
            "type": "array",
            "description": "Parcels",
            "items": {
              "$ref": "#/components/schemas/ParcelCreate"
            }
          }
        }
      },
      "UnavailableCouriers": {
        "type": "array",
        "items": {
          "type": "object",
          "additionalProperties": false,
          "properties": {
            "id": {
              "type": "string",
              "format": "uuid",
              "description": "unique identifier for a courier service"
            },
            "name": {
              "type": "string",
              "description": "Unavailable courier name"
            },
            "message": {
              "type": "string",
              "description": "Unavailable reason"
            }
          }
        }
      },
      "ImportDutyAdditionalRate": {
        "type": "object",
        "description": "An additional duty surcharge applied on top of the base duty rate.",
        "additionalProperties": false,
        "properties": {
          "description": {
            "type": "string",
            "nullable": true,
            "description": "Description of the additional duty surcharge."
          },
          "rate": {
            "type": "number",
            "nullable": true,
            "description": "Additional duty rate as a decimal (e.g. `0.025` = 2.5%)."
          },
          "amount": {
            "type": "number",
            "nullable": true,
            "description": "Computed additional duty amount for this surcharge in the response currency."
          }
        }
      },
      "ImportDutyDetails": {
        "type": "object",
        "description": "Duty calculation details for a line item, including HS code fallback and rate breakdown.",
        "additionalProperties": false,
        "properties": {
          "hs_code_provided": {
            "type": "string",
            "nullable": true,
            "description": "Raw HS code as provided in the request, before normalisation or fallback.",
            "example": "42029100"
          },
          "hs_code_applied": {
            "type": "string",
            "nullable": true,
            "description": "HS code used to determine the duty rate after normalising to 10 digits and applying fallback, if any.",
            "example": "4202910010"
          },
          "subheading": {
            "type": "boolean",
            "nullable": true,
            "description": "True if a shorter parent subheading was used to determine the duty rate because no record existed for the full code."
          },
          "duty_origin_country_id_provided": {
            "type": "integer",
            "nullable": true,
            "description": "Country of origin ID explicitly provided on the item. Null when COO was not provided and fell back to the shipment origin."
          },
          "duty_origin_country_id_applied": {
            "type": "integer",
            "nullable": true,
            "description": "Country of origin ID actually used to determine the duty rate (either provided or the shipment origin fallback)."
          },
          "duty_calculation_method": {
            "type": "string",
            "nullable": true,
            "description": "Customs valuation method used for this destination.",
            "enum": [
              "CIF",
              "FOB"
            ]
          },
          "line_item_shipment_value": {
            "type": "number",
            "nullable": true,
            "description": "Shipment value used for duty calculation (customs value × quantity, plus allocated shipping and insurance for CIF destinations). Returned in the response currency."
          },
          "applied_rate_type": {
            "type": "string",
            "nullable": true,
            "description": "Whether the FTA preferential rate or the general rate was applied.",
            "enum": [
              "fta",
              "general"
            ]
          },
          "additional_rates": {
            "type": "array",
            "nullable": true,
            "description": "Additional duty surcharges applied on top of the base duty rate (e.g. anti-dumping duties, section tariffs).",
            "items": {
              "$ref": "#/components/schemas/ImportDutyAdditionalRate"
            }
          },
          "base_duty_rate": {
            "type": "number",
            "nullable": true,
            "description": "Base duty rate as a decimal (e.g. `0.12` = 12%)."
          },
          "base_duty_amount": {
            "type": "number",
            "nullable": true,
            "description": "Computed base duty amount for the line item in the response currency."
          },
          "line_item_total_duty": {
            "type": "number",
            "nullable": true,
            "description": "Total duty for the line item including base and all additional surcharges, in the response currency."
          }
        }
      },
      "SingleLabelCreate": {
        "type": "object",
        "description": "Single Label Create",
        "additionalProperties": false,
        "properties": {
          "courier_service_id": {
            "type": "string",
            "description": "Courier service ID in case you need to overwrite"
          },
          "printing_options": {
            "type": "object",
            "description": "Specify the format and page sizes of the shipping documents. This will only be taken into account if buy_label_synchronous is `true`.",
            "properties": {
              "format": {
                "type": "string",
                "description": "Options: `png`, `pdf`, `url`, `zpl` (Default: `png`)",
                "default": "png",
                "enum": [
                  "png",
                  "pdf",
                  "url",
                  "zpl"
                ]
              },
              "label": {
                "type": "string",
                "description": "Label page size. Options: `4x6` / `A4` / `A5` (Default: `4x6`)",
                "default": "4x6",
                "enum": [
                  "4x6",
                  "A4",
                  "A5"
                ]
              },
              "commercial_invoice": {
                "type": "string",
                "description": "Commercial invoice page size. Options: `4x6` / `A4` (Default: `A4`)",
                "default": "A4",
                "enum": [
                  "4x6",
                  "A4"
                ]
              },
              "packing_slip": {
                "type": "string",
                "description": "Packing slip page size. Options: `4x6` / `A4` (Default: `4x6`)",
                "default": "4x6",
                "enum": [
                  "4x6",
                  "A4",
                  "none"
                ]
              },
              "remarks": {
                "type": "string",
                "maxLength": 70,
                "description": "Customized commercial invoice remarks for current shipment. It has higher priority than remarks from company settings."
              }
            }
          }
        }
      }
    }
  }
}
```