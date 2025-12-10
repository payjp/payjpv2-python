# SetupFlowPaymentMethodOptionsCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_three_d_secure** | **str** | 3Dセキュア認証の要求方法。  | 指定できる値 | |:---| | **any**: 3Dセキュア認証を要求します。 | | **automatic**: 必要な場合にのみ3Dセキュア認証を要求します。 |  | [optional] 

## Example

```python
from payjpv2.models.setup_flow_payment_method_options_card_request import SetupFlowPaymentMethodOptionsCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowPaymentMethodOptionsCardRequest from a JSON string
setup_flow_payment_method_options_card_request_instance = SetupFlowPaymentMethodOptionsCardRequest.from_json(json)
# print the JSON string representation of the object
print(SetupFlowPaymentMethodOptionsCardRequest.to_json())

# convert the object into a dict
setup_flow_payment_method_options_card_request_dict = setup_flow_payment_method_options_card_request_instance.to_dict()
# create an instance of SetupFlowPaymentMethodOptionsCardRequest from a dict
setup_flow_payment_method_options_card_request_from_dict = SetupFlowPaymentMethodOptionsCardRequest.from_dict(setup_flow_payment_method_options_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


