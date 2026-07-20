---
type: webhook-event
---
# oauth.authorization.revoked

Webhook event · [[Webhooks]] · [[Authorization]]

When an oauth application has been revoked, you will receive the event payload as below:

```json
{
  "event_type": "oauth.authorization.revoked",
  "resource_type": "oauth_application",
  "resource_id": "UNwwHmEFWCUP1PUkZtHSziELYECsRC_9C00hxt4TL2I",
  "data": {
    "resource_owner_id": "CUS222890",
    "resource_owner_type": "Company",
    "name": "test webhook",
    "revoked_at": "2025-06-11T06:30:50.250Z"
  }
}
```
