---
type: concept
---
# Rate Limit

All endpoints have a limit of 60 requests per minute and 10 requests per second.

In sandbox mode, the limit is 6 requests per minute and 1 request per second.

Once you exceed the limit, you will be unable to make further API requests and will receive a `429 Too many requests` error until the next time window begins.
