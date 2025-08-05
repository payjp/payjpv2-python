# PaymentMethodOptionsCardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_extended_authorization** | **str** | オーソリ期間の延長要求。  | 指定できる値 | |:---| | **if_available**: オーソリ期間の延長が可能な場合に延長要求を行います。 | | **never**: オーソリ期間の延長要求を行いません。 | | [optional] 
**request_three_d_secure** | **str** | 3Dセキュア認証の要求方法。  | 指定できる値 | |:---| | **any**: 基本的に3Dセキュア認証を要求します。 | | **automatic**: 必要な場合にのみ3Dセキュア認証を要求します。 | &lt;!-- | **challenge**: 3Dセキュア認証を手動で要求します。 | --&gt;  | [optional] 
**setup_future_usage** | **str** | セットアップ後の使用方法。  | 指定できる値 | |:---| | **off_session**: 顧客がその場にいない状態（例：定期課金や後日請求など）でも決済したい場合に使用します。事前の同意に基づいて自動的に課金されます。 | | **on_session**: 顧客が支払い操作中（例：Web画面で「支払う」ボタンを押す）でのみ決済できればいい場合に指定します。リアルタイムに同意が得られている状態です。 | | [optional] 

## Example

```python
from payjpv2.models.payment_method_options_card_request import PaymentMethodOptionsCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodOptionsCardRequest from a JSON string
payment_method_options_card_request_instance = PaymentMethodOptionsCardRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodOptionsCardRequest.to_json())

# convert the object into a dict
payment_method_options_card_request_dict = payment_method_options_card_request_instance.to_dict()
# create an instance of PaymentMethodOptionsCardRequest from a dict
payment_method_options_card_request_from_dict = PaymentMethodOptionsCardRequest.from_dict(payment_method_options_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


