---
method: GET
endpoint: "/2024-09/billing_documents"
api: Public API
slug: billing_documents_index
scopes:
  - "public.billing_document:read"
---
# List all Billing Documents

**`GET /2024-09/billing_documents`** · [[Billing Documents]] · [[Easyship Public API]]

Retrieve a list of all billing documents within range.
Pagination of this endpoint is not indexed.
`count` on the response body will always be `null`.

## Source

- [Official docs](https://developers.easyship.com/reference/billing_documents_index)
- Local mirror: `docs/reference/billing_documents_index.md`
