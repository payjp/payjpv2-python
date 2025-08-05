# PaymentIntentIncrementAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。支払い手段によって上限金額は異なります。 | 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 

## Example

```python
from payjpv2.models.payment_intent_increment_authorization_request import PaymentIntentIncrementAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentIncrementAuthorizationRequest from a JSON string
payment_intent_increment_authorization_request_instance = PaymentIntentIncrementAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentIncrementAuthorizationRequest.to_json())

# convert the object into a dict
payment_intent_increment_authorization_request_dict = payment_intent_increment_authorization_request_instance.to_dict()
# create an instance of PaymentIntentIncrementAuthorizationRequest from a dict
payment_intent_increment_authorization_request_from_dict = PaymentIntentIncrementAuthorizationRequest.from_dict(payment_intent_increment_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


