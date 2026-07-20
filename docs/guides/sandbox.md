# Sandbox

The sandbox environment allows you to test all of the APIs. The data, rates and labels are for illustrative purposes only.

> 🚧 Notes about the Sandbox Environment
>
> The Sandbox Environment won't show a full slate of courier options when you are making your requests. To see the full list for a given shipment, you will need to use the Production Environment instead.

To utilise the sandbox, you will need your Sandbox token (see [Authentication](https://developers.easyship.com/docs/authentication))

When making your requests, you will need to use the Sandbox token in place of the production token. You can differentiate between your sandbox and production tokens by checking the prefix of your token. For example:

**Production** tokens will have a prefix of *prod*, like below

```
prod_OWsLoYxxxxxxxxxxxxxxxxxxxxxxxxxxxRf5bh3GdnU=
```

**Sandbox** tokens will have a prefix of *sand*, like below

```
sand_458+7pxxxxxxxxxxxxxxxxxxxxxxxxxxCRWSLHfIkBIQ=
```

**Production Domains**

* Before v2023: `https://api.easyship.com/`
* v2024 and newer: `https://public-api.easyship.com/`

**Sandbox Domains**

* Before v2023: `https://api-sandbox.easyship.com/`
* v2024 and newer: `https://public-api-sandbox.easyship.com/`

> 🚧 Testing in Sandbox
>
> If you are receiving unexpected results when testing certain endpoints, try switching to the production environment to make sure you're passing in all of the required data.

All endpoints will remain the same, but the responses will contain sample data.