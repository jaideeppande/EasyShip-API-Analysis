---
method: POST
endpoint: "/2024-09/insurances/policies/{policy_id}/cancel"
api: Public API
slug: insurances_policies_cancel
scopes:
  - "public.insurance_policy_from_quote:write"
---
# Cancel an Insurance Policy

**`POST /2024-09/insurances/policies/{policy_id}/cancel`** · [[Insurance]] · [[Easyship Public API]]

Cancel an insurance policy. Only policies in `awaiting` state can be cancelled.

## Source

- [Official docs](https://developers.easyship.com/reference/insurances_policies_cancel)
- Local mirror: `docs/reference/insurances_policies_cancel.md`
