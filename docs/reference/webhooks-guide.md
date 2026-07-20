# Webhooks Guide

This guide will walk you through the webhooks functionality to obtain messages about shipment events. Messages are sent on triggering the following events:

* [Creating a shipment label](https://developers.easyship.com/reference/shipmentlabelcreated)
* [Failing to create a shipment label](https://developers.easyship.com/reference/shipmentlabelfailed)
* [Creating a shipment tracking checkpoint](https://developers.easyship.com/reference/shipmenttrackingcheckpointscreated)
* [Changing tracking status of a shipment](https://developers.easyship.com/reference/shipmenttrackingstatuschanged)
* [Cancelling a shipment](https://developers.easyship.com/reference/shipmentcancelled)
* [Updating a shipment's warehouse state](https://developers.easyship.com/reference/shipmentwarehousestateupdated)
* [Processing the first shipment in a batch](https://developers.easyship.com/reference/batchstarted)
* [End of processing the last shipment in a batch](https://developers.easyship.com/reference/batchfinished)
* [End of processing an individual batch shipment](https://developers.easyship.com/reference/batchitemfinished)
* [Credit balance lower than your configured threshold](https://developers.easyship.com/reference/creditbalancelow)
* [Creating a company within an organization (**Enterprise API only**)](https://developers.easyship.com/reference/enterprisecompanycreation)
* [Changing the state of a courier](https://developers.easyship.com/reference/courierstatechanged)
* [Revoking access to an oauth application](https://developers.easyship.com/reference/oauthauthorizationrevoked)

Easyship can send webhook events to notify your application when a specific event occurs. This is useful for some endpoints, for example, when generating labels asynchronously: [Create a Shipment](https://developers.easyship.com/reference/shipments_create) with `buy_label: true` or [Create a Batch of Labels](https://developers.easyship.com/reference/batch_labels_create), which do not give you a real-time response. If you subscribe to the webhook to receive shipment status updates, you will be notified when the shipment's label is ready without polling our API.

The payload for each webhook event will include information about the related API response. Your provided endpoint should be set up to receive an HTTP POST request and must always return a 2XX HTTP response.

## Configuring your webhooks settings

Use [Create a Webhook](https://developers.easyship.com/reference/webhooks_create), [Activate a Webhook](https://developers.easyship.com/reference/webhooks_activate), and [Test a Webhook](https://developers.easyship.com/reference/webhooks_test) to configure and test your webhook through our public API.

Or you can register your webhook endpoint (URL) via the [Easyship Dashboard](http://app.easyship.com/webhooks). Simply click **Add new webhook**, enter your **Webhook Endpoint URL**, select the event types you wish to receive notifications for, and click **Create**.

Before activating your webhook endpoints, you can test your endpoint by clicking **Test** next to each event. If the test is successful, you will see the **Webhook test succeeded** message.

> ❗️ Note
>
> You need to returning a `2XX` HTTP response immediately or we will consider the webhook POST action to have failed.

```json
{
  "label_received": true
}
```

If this is your first time setting up a webhook, we suggest testing your endpoint with [ngrok](https://ngrok.com/). It's amazingly simple and useful. You can even take a closer look at the event payload as you test each event.

After you activate your webhook endpoints, you will start to get incoming events. You can deactivate or delete the endpoint at any time.

## Verifying an incoming event with Easyship's signature

To prevent your application against a [replay attack](https://en.wikipedia.org/wiki/Replay_attack), we recommend that you verify all incoming webhook events by validating our unique signature, `X-EASYSHIP-SIGNATURE`, in the headers.

The signature is a JSON web token that can be decoded with the value of your `secret_key`. You can find it on the [dashboard webhook configuration page](https://app.easyship.com/webhooks). It will always be a hash string starting with `webh_`.

```ruby
secret_key = 'webh_092dflkjhwelkjr109834wlkejhr8sdh'
signature = request.env['X-EASYSHIP-SIGNATURE']
JWT.decode signature, secret_key, true, { algorithm: 'HS256' }
# => [{easyship_company_id: 'easyship_company_id'}, {...algorithm information...}]
```

## Webhook suspension

Easyship will retry sending a webhook a total of 30 times when the receiver fails to respond with a `2XX` status. Each retry will be at 1-minute intervals.

If the final retry fails, the webhook will be deactivated (ie. the `active` property set to `false`). This means Easyship will not send the webhook again for subsequent events until the webhook is activated again from the dashboard.