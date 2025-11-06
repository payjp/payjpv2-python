# PaymentFlow

`payment` モードの Checkout Session の PaymentFlow の ID。PaymentFlow を確定 (confirm)、またはキャンセルすることはできません。キャンセルするには、代わりに Checkout Session を期限切れにしてください。

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from payjpv2.models.payment_flow import PaymentFlow

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlow from a JSON string
payment_flow_instance = PaymentFlow.from_json(json)
# print the JSON string representation of the object
print(PaymentFlow.to_json())

# convert the object into a dict
payment_flow_dict = payment_flow_instance.to_dict()
# create an instance of PaymentFlow from a dict
payment_flow_from_dict = PaymentFlow.from_dict(payment_flow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


