# How to Validate Addresses

Use Easyship address validation feature to make sure the end user’s address is valid and correct. With a single endpoint, you perform four operations related to physical delivery addresses:

1. Confirm address deliverability. It ensures a courier is aware of this address and your shipment can be delivered. Deliverability check **does not change the destination address**: it only confirms whether provided address corresponds to the courier database address or not.
2. Ensure correctness of the address format for couriers. It confirms the address format is correct according to regional postal system and courier requirements. Address format check **changes the destination address** if needed.
3. Correct invalid addresses. It ensures the address does not contain user-side errors and **modifies the destination address** in case this address is invalid in terms of:
   * Postal code missing
   * Address and postal code mismatch
   * Duplicate data
   * Spelling errors
4. Transliterate non-Latin addresses into their Latin formats. For countries using non-Latin alphabets, the address is transliterated into the Latin format ensuring that the Latin version of this address is deliverable and correct. Address transliteration **changes the destination address** by creating its Latin version (transliterated, not translated) understandable for English speakers.

> 📘
>
> Transliteration is conversion of text from one writing system to another:
>
> Улица Ленина 12, Москва, 143350 → Ulica Lenina 12, Moskva, 143350

To enable shipment addresses validation, send

`POST /2023-01/addresses/validations`

## Body parameters

This endpoint includes the following request body:

| Field name       | Type   | Required or optional | Description          |
| :--------------- | :----- | :------------------- | :------------------- |
| `line_1`         | String | Required             | First address line   |
| `line_2`         | String | Optional             | Second address line  |
| `city`           | String | Required             | City                 |
| `postal_code`    | String | Required             | Postal code          |
| `country_alpha2` | String | Required             | Alpha 2 country code |

## Request body example

```
{
  "line_1": "10 Downing Street",
  "city": "London",
  "postal_code": "SW1A 2AA",
  "country_alpha2": "GB"
}
```

## Response examples

### Successful response

In response, this method returns a validation object containing the address details and validation results:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Field name
      </th>

      <th>
        Type
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        String
      </td>

      <td>
        Object identifier
      </td>
    </tr>

    <tr>
      <td>
        `line_1`
      </td>

      <td>
        String
      </td>

      <td>
        First address line
      </td>
    </tr>

    <tr>
      <td>
        `line_2`
      </td>

      <td>
        String
      </td>

      <td>
        Second address line
      </td>
    </tr>

    <tr>
      <td>
        `company_name`
      </td>

      <td>
        String
      </td>

      <td>
        Name of a company on the address
      </td>
    </tr>

    <tr>
      <td>
        `city`
      </td>

      <td>
        String
      </td>

      <td>
        City
      </td>
    </tr>

    <tr>
      <td>
        `state`
      </td>

      <td>
        String
      </td>

      <td>
        State
      </td>
    </tr>

    <tr>
      <td>
        `postal_code`
      </td>

      <td>
        String
      </td>

      <td>
        Postal code
      </td>
    </tr>

    <tr>
      <td>
        `country_alpha2`
      </td>

      <td>
        String
      </td>

      <td>
        Alpha 2 country code
      </td>
    </tr>

    <tr>
      <td>
        `engine`
      </td>

      <td>
        String
      </td>

      <td>
        Lookup engine (currently, `melissa` by default)
      </td>
    </tr>

    <tr>
      <td>
        `validation`
      </td>

      <td>
        Array(String):  

        `detail`  

        `status`
      </td>

      <td>
        Validation results:  

        `detail`: detailed message in case of unsuccessful status  

        `status`: short validation status
      </td>
    </tr>
  </tbody>
</Table>

Example:

```
{
  "city": "London",
  "company_name": "Prime Minister's Office",
  "country_alpha2": "GB",
  "id": "2376ae82-3d3e-44bf-bc91-a5e727056833",
  "line_1": "10 Downing Street",
  "line_2": "",
  "postal_code": "SW1A 2AA",
  "state": "London",
  "validation": {
    "detail": "",
    "status": "verified"
  }
}
```

Follow our [shipping address format](https://www.easyship.com/blog/address-a-package) guidelines to learn more about address formats for individual countries.