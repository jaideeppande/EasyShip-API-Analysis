---
type: concept
---
# enterprise.company.creation

> 📘 Only available for Easyship Enterprise API

When a child company is created belonging to your organization, you will get the event payload as below:

```json
{
  "event_type": "enterprise.company.creation",
  "resource_type": "company",
  "resource_id": "CHK100000",
  "data": {
    "easyship_company_id": "CHK100000",
    "name": "Company Name",
    "owner": {
      "name": "Owner Company Name",
      "email": "easyship@test.com"
    },
    "created_at": "2023-01-25T11:30:00.000Z"
  }
}
```
