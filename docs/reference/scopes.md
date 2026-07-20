# Scopes

Scopes define what endpoints and functionality an API connection has access to.

Some scopes can be controlled by the user, and some are controlled by Easyship.

## Create Public API Integration

There are two API categories that you can use for your API Integration.

* 2023-01 or earlier (legacy)
* 2024-09 or later

The 2024-09 is the latest stable (and recommended) version and will provide more flexibility for you to setup different integrations with different actions (read/write).

To create the integration.

1. Login to your Easyship account at [app.easyship.com](https://app.easyship.com)
2. Click New Integration under Connect on the sidebar
3. Click API Integration on the bottom of the page

<Image align="center" src="https://files.readme.io/2d6f2758dbbfe36d17f4f362a6ec26bdbab10eb5202273b8469ea588e1da1d48-501cff9c-ac71-40c8-9fa3-efeb6b25d014.png" />

4. Fill the details and select preferred API version

<Image align="center" src="https://files.readme.io/0265d88c9a62831c5e3aca07e7e843c5607f02ef07a9f7b0b31bcfa150954851-5aacc280-2c9c-46c7-b232-228b3c3899e6.png" />

5. Click Connect

## Version differences

### 2023-01 and older

For versions 2023-01 or earlier, the list of scopes is displayed without specific actions. This means that each scope enables both read and write operations within its context. For example, when you enable the Address scope, it grants access to endpoints requiring the **Address** scope with all relevant HTTP methods: `GET`, `POST`, `DELETE`, `PATCH`, and `PUT`.

### 2024-09 and newer

For versions 2024-09 or newer, the list of scopes is structured differently. Scopes are now displayed with a format like `<scope>.<resource>:<action>`. Example: `public.address:read`.

* The **scope** distinguishes between the Public API (`public`) and other APIs (e.g., `enterprise`)
* The **resource** represents the same scope you’re familiar with from previous versions.
* The new **action** (usually `read` or `write`), define specific access permissions:
  * `read` allows access to endpoints using the `GET` method. These endpoint do not create or modify data.
  * `write` grants access to endpoints using methods such as `POST`, `DELETE`, `PATCH`, and `PUT` and allows create, modify or destroy data.

## Edit or View available scopes

To edit or view the scopes available for an API connection:

1. Login to your Easyship account at [app.easyship.com](https://app.easyship.com)
2. Select the API connection under the connect tab on the left
3. Under the API Access token, you can see what scopes the token has access to.
4. To edit access, click edit, select/deselect the scopes and click save.

<Image align="center" width="500px" src="https://files.readme.io/cfad657-SCR-20240403-nwjm.png" />

If you require access to additional scopes (for advanced functionality or to get access to functionality currently under beta), please reach out to Easyship, either to your account manager or at <https://support.easyship.com/hc/en-us>