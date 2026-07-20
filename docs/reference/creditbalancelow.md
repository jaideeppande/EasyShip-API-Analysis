# credit.balance.low

When your credit balance is lower than the configuration value `credit_balance_limit`, you will get the event payload as below:

```json
{
  "event_type": "credit.balance.low",
  "resource_type": "company",
  "resource_id": "CHK100000",
  "data": {
    "available_balance": 100.0,
    "balance": 150.00,
    "currency": "HKD"
  }
}
```