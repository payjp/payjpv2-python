# SetupFlowPaymentMethodOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card** | [**SetupFlowPaymentMethodOptionsCardRequest**](SetupFlowPaymentMethodOptionsCardRequest.md) | カード支払い方法に関するオプション | [optional] 

## Example

```python
from payjpv2.models.setup_flow_payment_method_options_request import SetupFlowPaymentMethodOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowPaymentMethodOptionsRequest from a JSON string
setup_flow_payment_method_options_request_instance = SetupFlowPaymentMethodOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(SetupFlowPaymentMethodOptionsRequest.to_json())

# convert the object into a dict
setup_flow_payment_method_options_request_dict = setup_flow_payment_method_options_request_instance.to_dict()
# create an instance of SetupFlowPaymentMethodOptionsRequest from a dict
setup_flow_payment_method_options_request_from_dict = SetupFlowPaymentMethodOptionsRequest.from_dict(setup_flow_payment_method_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


