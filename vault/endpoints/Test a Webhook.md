---
method: POST
endpoint: "/2024-11/organizations/{organization_id}/webhooks/{webhook_id}/test"
api: Enterprise API
slug: organizations_webhooks_test
scopes:
  - "enterprise.webhook:write"
---
# Test a Webhook

**`POST /2024-11/organizations/{organization_id}/webhooks/{webhook_id}/test`** · [[Webhooks]] · [[Easyship Enterprise API]]

Test a single webhook in the organization. (The company ID of the organization owner will be included in the `X-EASYSHIP-COMPANY-ID` header.)

## References

- [[HS codes]]
- [[Organizations]]

## Source

- [Official docs](https://developers.easyship.com/reference/organizations_webhooks_test)
- Local mirror: `docs/reference/organizations_webhooks_test.md`
