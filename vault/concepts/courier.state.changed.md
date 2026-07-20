---
type: concept
---
# courier.state.changed

When the status of your courier changes, you will receive the event payload as below:

```json
{
  "event_type": "courier.state.changed",
  "resource_type": "courier",
  "resource_id": "01563646-58c1-4607-8fe0-cae3e33c0001",
  "data": {
    "account_number": "953456789",
    "customer_reference_id": "reference id",
    "nickname": "Sample Account",
    "umbrella_name": "DHL",
    "origin_country_alpha2": "HK",
    "account_state": "active",
    "auth_state": "verified"
  }
}
```
