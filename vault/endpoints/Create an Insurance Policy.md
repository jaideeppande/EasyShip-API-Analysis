---
method: POST
endpoint: "/2024-09/insurances/policies"
api: Public API
slug: insurances_policies_create
scopes:
  - "public.insurance_policy_3p:write"
---
# Create an Insurance Policy

**`POST /2024-09/insurances/policies`** · [[Insurance]] · [[Easyship Public API]]

Create insurance for a shipment whose label isn't provided by Easyship.
For the shipment whose label is provided by Easyship, please use Shipment Insurance Endpoint to insure it.

## References

- [[Addresses]]
- [[Courier Services]]
- [[Couriers]]
- [[Shipments]]
- [[Trackings]]

## Source

- [Official docs](https://developers.easyship.com/reference/insurances_policies_create)
- Local mirror: `docs/reference/insurances_policies_create.md`
