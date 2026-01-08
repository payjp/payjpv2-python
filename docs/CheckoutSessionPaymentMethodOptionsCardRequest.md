# CheckoutSessionPaymentMethodOptionsCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_extended_authorization** | **str** | オーソリ期間の延長要求  | 指定できる値 | |:---| | **if_available**: オーソリ期間の延長が可能な場合に延長要求を行います。 | | **never**: オーソリ期間の延長要求を行いません。 | | [optional] 
**request_three_d_secure** | **str** | 3D セキュア認証の要求方法  | 指定できる値 | |:---| | **any**: 3D セキュア認証を要求します。 | | **automatic**: 必要な場合にのみ 3D セキュア認証を要求します。 | | [optional] 

## Example

```python
from payjpv2.models.checkout_session_payment_method_options_card_request import CheckoutSessionPaymentMethodOptionsCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionPaymentMethodOptionsCardRequest from a JSON string
checkout_session_payment_method_options_card_request_instance = CheckoutSessionPaymentMethodOptionsCardRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionPaymentMethodOptionsCardRequest.to_json())

# convert the object into a dict
checkout_session_payment_method_options_card_request_dict = checkout_session_payment_method_options_card_request_instance.to_dict()
# create an instance of CheckoutSessionPaymentMethodOptionsCardRequest from a dict
checkout_session_payment_method_options_card_request_from_dict = CheckoutSessionPaymentMethodOptionsCardRequest.from_dict(checkout_session_payment_method_options_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


