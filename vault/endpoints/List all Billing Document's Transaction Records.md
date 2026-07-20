---
method: GET
endpoint: "/2024-09/billing_documents/{id}/transaction_records"
api: Public API
slug: billing_documents_transactions_index
scopes:
  - "public.transaction_record:read"
---
# List all Billing Document's Transaction Records

**`GET /2024-09/billing_documents/{id}/transaction_records`** · [[Billing Documents]] · [[Easyship Public API]]

Retrieve a list of all billing document's transactions.
Pagination of this endpoint is not indexed.
`count` on the response body will always be `null`.

## References

- [[Shipments]]

## Source

- [Official docs](https://developers.easyship.com/reference/billing_documents_transactions_index)
- Local mirror: `docs/reference/billing_documents_transactions_index.md`
