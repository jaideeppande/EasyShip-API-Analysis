---
method: POST
endpoint: "/2024-11/companies/{easyship_company_id}/downgrade_subscription"
api: Enterprise API
slug: downgrade_subscription_create
scopes:
  - "enterprise.company:write"
---
# Downgrade a Subscription

**`POST /2024-11/companies/{easyship_company_id}/downgrade_subscription`** · [[Companies]] · [[Easyship Enterprise API]]

Switch a specific child company to the free-tier subscription plan.
The free-tier plan takes effect upon expiration of the current plan period.

## References

- [[HS codes]]

## Source

- [Official docs](https://developers.easyship.com/reference/downgrade_subscription_create)
- Local mirror: `docs/reference/downgrade_subscription_create.md`
