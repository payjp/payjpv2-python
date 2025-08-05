# PaymentIntent

`payment` モードの Checkout Session の PaymentIntent の ID。PaymentIntent を確定 (confirm)、またはキャンセルすることはできません。キャンセルするには、代わりに Checkout Session を期限切れにしてください。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from payjpv2.models.payment_intent import PaymentIntent

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntent from a JSON string
payment_intent_instance = PaymentIntent.from_json(json)
# print the JSON string representation of the object
print(PaymentIntent.to_json())

# convert the object into a dict
payment_intent_dict = payment_intent_instance.to_dict()
# create an instance of PaymentIntent from a dict
payment_intent_from_dict = PaymentIntent.from_dict(payment_intent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


