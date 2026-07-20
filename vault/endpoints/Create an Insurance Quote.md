---
method: POST
endpoint: "/2024-09/insurances/quotes"
api: Public API
slug: insurances_quotes_create
scopes:
  - "public.insurance_quote:write"
---
# Create an Insurance Quote

**`POST /2024-09/insurances/quotes`** · [[Insurance]] · [[Easyship Public API]]

Create an insurance quote for products to be shipped.
Returns a quote with fee calculations per product and an overall total.
The quote is valid for 48 hours and can be converted to a policy using the
Create Insurance Policy from Quote endpoint.

## Source

- [Official docs](https://developers.easyship.com/reference/insurances_quotes_create)
- Local mirror: `docs/reference/insurances_quotes_create.md`
