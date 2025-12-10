# CheckoutSessionPaymentMethodOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**CheckoutSessionPaymentMethodOptionsCardRequest**](CheckoutSessionPaymentMethodOptionsCardRequest.md) | カード支払い方法に関するオプション | [optional] 

## Example

```python
from payjpv2.models.checkout_session_payment_method_options_request import CheckoutSessionPaymentMethodOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionPaymentMethodOptionsRequest from a JSON string
checkout_session_payment_method_options_request_instance = CheckoutSessionPaymentMethodOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionPaymentMethodOptionsRequest.to_json())

# convert the object into a dict
checkout_session_payment_method_options_request_dict = checkout_session_payment_method_options_request_instance.to_dict()
# create an instance of CheckoutSessionPaymentMethodOptionsRequest from a dict
checkout_session_payment_method_options_request_from_dict = CheckoutSessionPaymentMethodOptionsRequest.from_dict(checkout_session_payment_method_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


