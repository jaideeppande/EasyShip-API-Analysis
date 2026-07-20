# How to Automate your Shipments

Use our [Shipping Rules ](https://developers.easyship.com/reference/shipping_rules_create)feature to automate your shipments by defining actions that will be automatically performed when specific conditions are met.

## Introduction to shipping rules

Shipping rules allow you to automate your shipping processes by defining conditions and actions. These rules can be applied to:

1. New shipments: by default, a newly created shipping rule applies only to shipments created after it.
2. Existing ones: simply set the `recalculate_shipments` body field to `true`.

You can apply more than one shipping rule to your shipments: for this purpose, specify priority for each rule defining the order of application. Rules are applied by their priority in incremental order.

## Creating a shipping rule

To create a shipping rule, send a `POST` request to `https://api.easyship.com/2023-01/shipping_rules` with the following body parameters:

1. `name` (required).
2. `description` (required).
3. `recalculate_shipments` (optional, `false` by default).
4. `priority` (optional).

Once you've set these parameters, proceed to define conditions and actions.

## Defining conditions for a shipping rule

Shipping rule conditions are checked using the `AND` Boolean operator. You can specify conditions based on various criteria, including destination country, item category, item SKU, and more. Here is the full conditions list:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Condition name (Easyship Dashboard)
      </th>

      <th>
        Name of condition field (Easyship API)
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Destination country
      </td>

      <td>
        `match_country`
      </td>

      <td>
        Apply the shipping rule to orders for specified destination countries. This field operates with country identifiers that can be obtained via the [Country API](https://developers.easyship.com/reference/countries_index).
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        `match_all`
      </td>

      <td>
        Apply the shipping rule to all shipments.
      </td>
    </tr>

    <tr>
      <td>
        Item category
      </td>

      <td>
        `match_category`
      </td>

      <td>
        Apply the shipping rule to orders including specified item categories. This field operates with category identifiers that can be obtained via the [Item Category API](https://developers.easyship.com/reference/item_categories_index).
      </td>
    </tr>

    <tr>
      <td>
        Destination state or province
      </td>

      <td>
        `match_state`
      </td>

      <td>
        Apply the shipping rule to orders for specified destination states. This option is available only for the United States, Canada, Australia and Mexico. The field operates with state identifiers that can be obtained via the [State API](https://developers.easyship.com/reference/states_index).
      </td>
    </tr>

    <tr>
      <td>
        Destination postal or ZIP code
      </td>

      <td>
        `match_zipcode`
      </td>

      <td>
        Apply the shipping rule to orders for specified postal or ZIP codes.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `is_any_of` — match any of specified codes  

        `is_none_of` — don’t match (exclude) specified codes  

        `starts_with` — match any codes starting with a specified symbols
      </td>
    </tr>

    <tr>
      <td>
        Item stock keeping unit (SKU)
      </td>

      <td>
        `match_sku`
      </td>

      <td>
        Apply the shipping rule to orders with specified stock keeping units.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `contains` — look for SKU containing specified symbols  

        `does_not_contain` — look for SKUs that do not contain specified symbols  

        `is_exactly` — look for SKU exactly matching specified symbols
      </td>
    </tr>

    <tr>
      <td>
        Store or platform
      </td>

      <td>
        `match_platform_name`
      </td>

      <td>
        Apply the shipping rule to orders placed within specified platforms.
      </td>
    </tr>

    <tr>
      <td>

      </td>

      <td>
        `match_store`
      </td>

      <td>
        Apply the shipping rule to orders placed in specified stores.
      </td>
    </tr>

    <tr>
      <td>
        Shipping option selected by buyer
      </td>

      <td>
        `match_buyer_selected_courier_name`
      </td>

      <td>
        Apply the shipping rule to orders containing specified buyer-selected couriers.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `contains` — look for a courier name containing specified symbols  

        `does_not_contain` — look for a courier name that does not contain specified symbols  

        `is_exactly` — look for a courier name exactly matching specified symbols
      </td>
    </tr>

    <tr>
      <td>
        Number of items
      </td>

      <td>
        `match_items_count`
      </td>

      <td>
        Apply the shipping rule to orders that contain specified number of items.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `greater_than` — greater than a specified number (`>`)  

        `greater_than_or_equal_to` — greater than or equal to a specified number (`>=`)  

        `less_than` — less than  a specified number (`\<`)  

        `less_than_or_equal_to` — less than or equal to a specified number (`\<=`)  

        `equal_to` — equal to a specified number (`=`)
      </td>
    </tr>

    <tr>
      <td>
        Total selling price
      </td>

      <td>
        `match_operation`
      </td>

      <td>
        Apply the shipping rule to orders that contain specified total selling price.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `greater_than` — greater than  a specified number (`>`)  

        `greater_than_or_equal_to` — greater than or equal to a specified number (`>=`)  

        `less_than` — less than  a specified number (`\<`)  

        `less_than_or_equal_to` — less than or equal to a specified number (`\<=`)  

        `equal_to` — equal to a specified number (`=`)
      </td>
    </tr>

    <tr>
      <td>
        Total shipment weight
      </td>

      <td>
        `match_weight`
      </td>

      <td>
        Apply the shipping rule to orders that contain specified total shipment weight. The measurement system in use depends on destination country of an order.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `greater_than` — greater than  a specified number (`>`)  

        `greater_than_or_equal_to` — greater than or equal to a specified number (`>=`)  

        `less_than` — less than  a specified number (`\<`)  

        `less_than_or_equal_to` — less than or equal to a specified number (`\<=`)  

        `equal_to` — equal to a specified number (`=`)
      </td>
    </tr>

    <tr>
      <td>
        Order tag
      </td>

      <td>
        `include_order_tag_name`
      </td>

      <td>
        Apply the shipping rule to orders including specified tags. The field operates with tag names that can be obtained via the [Tag API](https://developers.easyship.com/reference/tags_index).
      </td>
    </tr>
  </tbody>
</Table>

Once you’ve set the conditions, continue with actions.

## Defining actions for a shipping rule

To apply actions for the shipping rule conditions, configure the `actions` array:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Action name (Easyship Dashboard)
      </th>

      <th>
        Name of action field (Easyship API)
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Exclude specified courier services
      </td>

      <td>
        `add_never_courier`
      </td>

      <td>
        Remove specified courier services from applicable shipments. This field operates with courier identifiers that can be obtained via the [Courier ID](https://developers.easyship.com/reference/couriers_index).
      </td>
    </tr>

    <tr>
      <td>
        Prefer specified courier services
      </td>

      <td>
        `add_preferred_courier`
      </td>

      <td>
        Add specified courier services to applicable shipments. This field operates with courier identifiers that can be obtained via the [Courier ID]\(Courier ID).
      </td>
    </tr>

    <tr>
      <td>
        Set import tax and duty payor
      </td>

      <td>
        `force_incoterms`
      </td>

      <td>
        Set specified duty tax type and duty payor to all applicable shipments.  

        Behaviour of this condition is defined by the following operators (`operator` string):  

        `DDP` — pre-paid tax and duties included in shipping cost  

        `DDU` — post-paid tax and duties included in shipping cost  

        `DDU_and_Best_DDP` — tree post-paid and one pre-paid shipping options offered at checkout  

        `DDP_and_Best_DDU` — one post-paid and three pre-paid shipping options offered at checkout
      </td>
    </tr>

    <tr>
      <td>
        Select couriers by
      </td>

      <td>
        `force_sort_by`
      </td>

      <td>
        Change the sorting rule for selection of couriers for all applicable shipments.  

        Behaviour of this action is defined by the following operators (`operator` string):  

        `total_charge` — best price  

        `delivery_time_rank` — fastest delivery  

        `value_for_money_rank` — best value for money
      </td>
    </tr>

    <tr>
      <td>
        Set insurance as
      </td>

      <td>
        `force_insurance`
      </td>

      <td>
        Always set or reject insurance for all applicable shipments.  

        Behaviour of this action is defined by the `insured` boolean operator:  

        `true` — insure all applicable shipments  

        `false`  — don’t insure all applicable shipments
      </td>
    </tr>

    <tr>
      <td>
        Filter couriers by tracking quality
      </td>

      <td>
        `force_tracking_rating`
      </td>

      <td>
        Filter couriers by tracking quality for all applicable shipments.  

        Behaviour of this action is defined by the `force_tracking_rating` boolean operator:  

        `true` — always filter couriers by tracking quality  

        `false` — never filter couriers by tracking quality
      </td>
    </tr>

    <tr>
      <td>
        Select box
      </td>

      <td>
        `force_package`
      </td>

      <td>
        Automatically select specified box by [Box ID](https://developers.easyship.com/reference/boxes_index) for all applicable shipments.  

        This rule includes two options:  

        `force_box_id` — select specified box identifiers with the box type  

        `force_flat_rate_box_id` — select a specific flat rate box with an ID. For flat-rate shipping, the price is determined by the packaging rather than the weight or dimensions of an item.
      </td>
    </tr>

    <tr>
      <td>
        Exclude specified boxes
      </td>

      <td>
        `reject_packages`
      </td>

      <td>
        Exclude boxes by specific [Box ID](https://developers.easyship.com/reference/boxes_index).
      </td>
    </tr>

    <tr>
      <td>
        Declare residential address
      </td>

      <td>
        `force_residential_surcharge`
      </td>

      <td>
        Always set or reject setting a shipment destination address as residential for all applicable shipments.  

        Behaviour of this action is defined by the `set_as_residential` boolean operator:  

        `true` — set the destination address as residential for all applicable shipments  

        `false`  — unset the destination address as residential for all shipments
      </td>
    </tr>

    <tr>
      <td>
        Ship from
      </td>

      <td>
        `force_ship_from`
      </td>

      <td>
        Set the sender’s origin address for all applicable shipments. This field operates with address identifiers that can be obtained via the [Address ID](https://developers.easyship.com/reference/addresses_create).
      </td>
    </tr>

    <tr>
      <td>
        Include return labels (domestic)
      </td>

      <td>
        `force_automated_return_requested`
      </td>

      <td>
        Include or reject including return labels for all applicable domestic shipments.  

        Behaviour of this action is defined by the `automated_return_requested` boolean operator:  

        `true` — always include return labels  

        `false`  — never include return labels
      </td>
    </tr>

    <tr>
      <td>
        Filter couriers by delivery time
      </td>

      <td>
        `add_forced_delivery_time`
      </td>

      <td>
        Filter available couriers by delivery time for all applicable shipments.  

        Behaviour of this action is defined by the following operators (`operator` string):  

        `less_than` — less than  a specified number (`\<`)  

        `less_than_or_equal_to` — less than or equal to a specified number (`\<=`)  

        `greater_than_or_equal_to` — greater than or equal to a specified number (`>=`)  

        `greater_than` — greater than  a specified number (`>`)
      </td>
    </tr>
  </tbody>
</Table>

## Editing a shipping rule

You can modify an existing shipping rule by executing the `PATCH https://api.easyship.com/2023-01/shipping_rules/{shipping_rule_id}` request, where `{shipping_rule_id}` is the shipping rule identifier provided when you [create](https://developers.easyship.com/reference/shipping_rules_create) a new rule.

This method allows to change core fields, add and edit its conditions and actions, and adjust the rule to your requirements.

To edit a rule, specify the request body parameters:

1. Change `name`, `description` and `priority` if needed.
2. Change existing conditions and actions: in case you don’t specify existing conditions or actions, they will be removed from the shipping rule.
3. Add new conditions or actions if applicable.

## Activating and deactivating a shipping rule

Manage your shipping rules by activating and deactivating them as needed.

To activate a shipping rule, execute `POST https://api.easyship.com/2023-01/shipping_rules/{id}/activate` where `{id}` is the shipping rule ID provided when you [create](https://developers.easyship.com/reference/shipping_rules_create) a new rule.

To deactivate a shipping rule, execute `POST https://api.easyship.com/2023-01/shipping_rules/{id}/deactivate`.

## Deleting a shipping rule

To delete a shipping rule, execute `DELETE https://api.easyship.com/2023-01/shipping_rules/{shipping_rule_id}` where `{shipping_rule_id}` is the shipping rule ID provided when you [create](https://developers.easyship.com/reference/shipping_rules_create) a new rule.

To learn more about shipping rules functionality, see our Help Center article on [How to Automate Tasks with Shipping Rules](https://support.easyship.com/hc/en-us/articles/115003580152).