# SetupIntentConfirmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | この SetupIntent に紐付ける決済方法のID | [optional] 
**payment_method_data** | [**PaymentMethodCreateRequest**](PaymentMethodCreateRequest.md) | 支払い方法データ | [optional] 
**payment_method_options** | **object** | この SetupIntent の支払い方法の個別設定。 | [optional] 
**return_url** | **str** | 顧客が支払いを完了後、あるいはキャンセルした後にリダイレクトされるURL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。&#x60;confirm&#x3D;true&#x60; の場合のみ指定できます。 | [optional] 
**use_payjp_sdk** | **bool** | PAY.JP SDK を使用するかどうか | [optional] 

## Example

```python
from payjpv2.models.setup_intent_confirm_request import SetupIntentConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupIntentConfirmRequest from a JSON string
setup_intent_confirm_request_instance = SetupIntentConfirmRequest.from_json(json)
# print the JSON string representation of the object
print(SetupIntentConfirmRequest.to_json())

# convert the object into a dict
setup_intent_confirm_request_dict = setup_intent_confirm_request_instance.to_dict()
# create an instance of SetupIntentConfirmRequest from a dict
setup_intent_confirm_request_from_dict = SetupIntentConfirmRequest.from_dict(setup_intent_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


