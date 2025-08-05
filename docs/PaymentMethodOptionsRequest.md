# PaymentMethodOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**PaymentMethodOptionsCardRequest**](PaymentMethodOptionsCardRequest.md) | カード支払い方法に関するオプション | 

## Example

```python
from payjpv2.models.payment_method_options_request import PaymentMethodOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodOptionsRequest from a JSON string
payment_method_options_request_instance = PaymentMethodOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodOptionsRequest.to_json())

# convert the object into a dict
payment_method_options_request_dict = payment_method_options_request_instance.to_dict()
# create an instance of PaymentMethodOptionsRequest from a dict
payment_method_options_request_from_dict = PaymentMethodOptionsRequest.from_dict(payment_method_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


