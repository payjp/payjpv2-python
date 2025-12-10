# PaymentFlowPaymentMethodOptionsCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_extended_authorization** | **str** | オーソリ期間の延長要求。  | 指定できる値 | |:---| | **if_available**: オーソリ期間の延長が可能な場合に延長要求を行います。 | | **never**: オーソリ期間の延長要求を行いません。 | | [optional] 
**request_three_d_secure** | **str** | 3Dセキュア認証の要求方法。  | 指定できる値 | |:---| | **any**: 3Dセキュア認証を要求します。 | | **automatic**: 必要な場合にのみ3Dセキュア認証を要求します。 |  | [optional] 

## Example

```python
from payjpv2.models.payment_flow_payment_method_options_card_request import PaymentFlowPaymentMethodOptionsCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowPaymentMethodOptionsCardRequest from a JSON string
payment_flow_payment_method_options_card_request_instance = PaymentFlowPaymentMethodOptionsCardRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowPaymentMethodOptionsCardRequest.to_json())

# convert the object into a dict
payment_flow_payment_method_options_card_request_dict = payment_flow_payment_method_options_card_request_instance.to_dict()
# create an instance of PaymentFlowPaymentMethodOptionsCardRequest from a dict
payment_flow_payment_method_options_card_request_from_dict = PaymentFlowPaymentMethodOptionsCardRequest.from_dict(payment_flow_payment_method_options_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


