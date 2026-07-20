---
method: GET
endpoint: "/2024-09/transaction_records"
api: Public API
slug: transactions_index
scopes:
  - "public.transaction_record:read"
---
# List all Transaction Records

**`GET /2024-09/transaction_records`** · [[Transaction Records]] · [[Easyship Public API]]

Retrieve a list of all transactions within range.
Pagination of this endpoint is not indexed.
`count` on the response body will always be `null`.

## References

- [[Couriers]]
- [[Shipments]]

## Source

- [Official docs](https://developers.easyship.com/reference/transactions_index)
- Local mirror: `docs/reference/transactions_index.md`
