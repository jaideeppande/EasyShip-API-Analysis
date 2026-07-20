# HS Codes, Address Validation and T&Ds Features

This guide provides detailed insights into three features of the Easyship platform:

* Taxes and Duties (T\&D) calculation
* HS (WTO Harmonised System) customs codes for delivered items
* Delivery address validation

## Taxes and duties

Easyship's T\&D feature enables you to accurately calculate taxes and duties for international shipments. While our system utilizes up-to-date data to provide precise cost estimations, there are a couple of considerations:

> 📘
>
> 1. **Non-percentage duty tariffs are not supported**. Certain countries, such as Switzerland, impose a one-off import duty fee instead of calculating percentage, which is currently not supported.
> 2. **Import regulation changes**. Certain countries, such as Saudi Arabia, may undergo frequent import regulation changes. Currently, there might be a time gap before Easyship accommodates these adjustments.

This endpoint is rate-limited by **100 requests per day and 3,000 requests per month**. To leverage the [Taxes and Duties](https://developers.easyship.com/reference/taxes_and_duties_calculate) API or the Dashboard functionality, you need to provide essential data:

* origin country
* destination country
* shipment insurance fee
* shipment delivery fee
* for each item: HS code and total value

For a detailed guide on endpoint behavior and error handling, refer to [How to Calculate Taxes and Duties](https://developers.easyship.com/docs/how-to-calculate-taxes-and-duties).

See our T\&D calculators for functionality testing:

1. [Free Duties and Taxes Calculator United Kingdom | Easyship ](https://www.easyship.com/duties-and-taxes-calculator/unitedkingdom)
2. [Free Import Duty & Taxes Calculator United States | Easyship ](https://www.easyship.com/duties-and-taxes-calculator/usa)

## HS codes

Utilize Easyship's HS codes feature to search for universal codes that categorize your shipped products. HS codes, part of the Harmonized System, are internationally recognized for classifying goods.

> 👍
>
> HS code feature can be easily integrated into any third-party platform via Easyship API to get access to the Easyship HS Code database. Below, you will find an example of what it looks like in the Easyship dashboard.

<Image align="center" className="border" border={true} src="https://files.readme.io/a45c052-image.png" />

Access all available HS codes on the Easyship dashboard or through the [HS Code](https://developers.easyship.com/reference/hs_code_index) API. The HS Code API endpoint is rate-limited by **1,000 requests per day and 30,000 requests per month**.

Easyship employs eight-digit WTO Harmonized System codes, where the last two digits are always `00` (e.g., `42029100`). For a more specific category, leave the first six digits unchanged and replace the last two with `00` (e.g., `42029190` → `42029100`).

## Address validation

Easyship's address validation feature performs four critical operations related to physical delivery addresses:

1. Confirm address deliverability.
2. Ensure correctness of address format for couriers.
3. Correct invalid addresses.
4. Transliterate non-Latin addresses into their Latin formats.

The Address Validation API endpoint has standard Easyship rate limits: **10 requests per second and 60 requests per minute**.

### Address deliverability

Deliverability of a physical address confirms that a courier is aware of this address and your shipment can be delivered.

In terms of Easyship, deliverability check **does not change a destination address**: it only confirms whether it corresponds to the courier database address or not.

### Address format correctness

Address format can be correct in accordance with regional postal system requirements and courier requirements.

In terms of Easyship, address format correctness check **changes a destination address** to ensure that:

* The address is deliverable
* The final version of the address corresponds to the local postage requirements
* All address fields are correctly passed to a courier

### Address format correction

A delivery address can be entered in an invalid way, e.g.:

* Postal code missing
* Address and postal code mismatch
* Duplicate data
* Spelling errors

The Easyship address validation feature includes automatic correctness check which **changes a destination address** to ensure it does not include user-side errors.

## Address transliteration

For countries using non-Latin alphabets, the address is transliterated into the Latin format ensuring that the Latin version of an address is deliverable and correct.

> 📘
>
> Transliteration is conversion of text from one writing system to another.

In terms of Easyship, address transliteration **changes a destination address** by creating its Latin version (transliterated, not translated) understandable for English speakers.