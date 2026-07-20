# How to connect Easyship users to your platform

This guide is for platforms as partner apps on Easyship to connect existing Easyship users or new signed up users.

## 1. Getting the OAuth2 credentials for your partner app

Our representative will request some information from you. Includes, but not limited to:

1. callback (redirect) URL(s), where users will be redirected to at the end of the [OAuth 2 Authorization Code Grant](https://www.oauth.com/oauth2-servers/server-side-apps/authorization-code/).
2. Logo of your platform (preferably with a transparent background)

You will receive OAuth2 credentials:

* `client_id`: can be used publicly
* `client_secret`:  cannot be used publicly (as the name suggests)
* `scopes`: the permitted scopes for the specific partner app to use within Easyship Public API

## 2. Redirect the user from your platform to the Easyship Auth Provider

> ⚠️ This is the only endpoint that uses the `auth.easyship.com` domain.

The flow will include asking users to create new accounts or use their existing accounts to connect to your platform.

The URL is based on [Authorize user on Easyship](https://developers.easyship.com/reference/oauth2_authorize) and you must provide these parameters:

* `client_id` provided by us in the 1st step.
* `redirect_uri`: one of the URIs provided by you in the 1st step.
* `scope`: list of scopes separated by space. The user will be asked to authorize these scopes. It can be the complete list of scopes provided in the 1st step.
* `response_type`: is a static value (`code`) that indicates the OAuth 2 Authorization Code grant.
* `state`: is the only optional parameter. You can use it to verify the user (it will be sent to the callback URI at the end of the flow).

### 💡 Example of the redirection to the Easyship Auth Provider

```
https://auth.easyship.com/oauth2/authorize?client_id=ixaj5e4L25axd_d6b4K2wG479_9c3itEN8eexE_67Qk&redirect_uri=https%3A%2F%2Fdomain.com%2Fcallback&response_type=code&scope=rate%20shipment%20label%20track%20company%20pickup%20location%20store%20product&state=Ml_Wdv6hFqy2N9EkNJdi7g
```

## 3. Exchange `code` for Access and Refresh tokens

After a successful OAuth2 Authorization Code grant flow, users will be redirected back to your platform to your callback URL with `code` and `state` (if provided).

To get the Access and Refresh tokens for the authorized user, you must use [Create an Access Token](https://developers.easyship.com/reference/oauth2_token-1) endpoint with the `AUTHORIZATION_CODE` request body.

### 💡 Example of the redirection back to your platform

Where the `https://your.platform.com/oauth/easyship` is the callback provided in the 1st step.

```
https://your.platform.com/oauth/easyship?code=UhLaQeeduKhGPLoEnQ29aLGuV077VSNEp7LPij_P6Tg&state=3m0V3q5MDgxNIR5Cglw
```

### 💡 Example of a successful response

```json
{
  "access_token": "test_3m0V3q5MDgxNIR5Cglw/ONL8ZMPNy91f1Kolt+BOWG8=",
  "token_type": "Bearer",
  "expires_in": 7200,
  "refresh_token": "UhLaQeeduKhGPLoEnQ29aLGuV077VSNEp7LPij_P6Tg",
  "scope": "rate shipment label track company pickup location store product",
  "created_at": 1645532460
}
```

The `access_token` and `refresh_token` should be associated with the authorized user.

## 4. Access the Easyship Public API

Now, you can access the [Easyship Public API](https://developers.easyship.com/reference/introduction) based on the scopes you stated with the `access_token` in the `Authorization` header.

In case of expired access tokens, you have to use the `refresh_token` to get a new access token using the [Create an Access Token](https://developers.easyship.com/reference/oauth2_token-1) with the `REFRESH_TOKEN` request body.