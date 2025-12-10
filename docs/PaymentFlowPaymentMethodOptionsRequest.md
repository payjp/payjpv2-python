# PaymentFlowPaymentMethodOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**PaymentFlowPaymentMethodOptionsCardRequest**](PaymentFlowPaymentMethodOptionsCardRequest.md) | カード支払い方法に関するオプション | [optional] 

## Example

```python
from payjpv2.models.payment_flow_payment_method_options_request import PaymentFlowPaymentMethodOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowPaymentMethodOptionsRequest from a JSON string
payment_flow_payment_method_options_request_instance = PaymentFlowPaymentMethodOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowPaymentMethodOptionsRequest.to_json())

# convert the object into a dict
payment_flow_payment_method_options_request_dict = payment_flow_payment_method_options_request_instance.to_dict()
# create an instance of PaymentFlowPaymentMethodOptionsRequest from a dict
payment_flow_payment_method_options_request_from_dict = PaymentFlowPaymentMethodOptionsRequest.from_dict(payment_flow_payment_method_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


