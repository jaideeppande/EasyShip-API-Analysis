---
type: concept
---
# Errors

In this version, we are introducing refactored errors. You can find examples in each related API endpoint. Here is some basic information.

## Example structure

```json
{
  "error": {
    "code": "invalid_content",
    "details": [
      "Target is not included in the list"
    ],
    "links": [
      {
        "kind": "documentation",
        "name": "Errors",
        "url": "https://developers.easyship.com/reference/errors"
      }
    ],
    "message": "The request body content is not valid.",
    "request_id": "01563646-58c1-4607-8fe0-cae3e92c4477",
    "type": "invalid_request_error"
  }
}
```

## Types

* `api_error`: our internal or 3rd party error
* `invalid_request_error`: error related to your request

## Codes

| Code                    | HTTP status | Type                    | Info                                                                                                                                             |
| ----------------------- | ----------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `api_error`             | 400         | `api_error`             | Internal or 3rd party API error.                                                                                                                 |
| `forbidden`             | 403         | `invalid_request_error` | Used API token does not have the required scope.                                                                                                 |
| `internal_server_error` | 500         | `api_error`             | Unexpected internal error.                                                                                                                       |
| `invalid_content`       | 422         | `invalid_request_error` | The request body content is not valid.                                                                                                           |
| `invalid_endpoint`      | 404         | `invalid_request_error` | The requested endpoint does not exist.                                                                                                           |
| `invalid_token`         | 401         | `invalid_request_error` | Invalid API token.                                                                                                                               |
| `invalid_request`       | 400         | `invalid_request_error` | The request body is malformed or not valid.                                                                                                      |
| `invalid_url_param`     | 422         | `invalid_request_error` | The request URL param is invalid.                                                                                                                |
| `resource_not_found`    | 404         | `invalid_request_error` | The requested resource was not found.                                                                                                            |
| `too_many_requests`     | 429         | `invalid_request_error` | Rate Limit Exceeded. You have reached the maximum number of requests. Try again later or contact your account manager to request a higher limit. |
| `over_limit`            | 402         | `invalid_request_error` | You have reached your plan limit. Upgrade your plan.                                                                                             |
| `payment_required`      | 402         | `invalid_request_error` | Insufficient balance on your account. Add more funds.                                                                                            |
