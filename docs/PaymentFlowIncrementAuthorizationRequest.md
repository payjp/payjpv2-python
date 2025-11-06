# PaymentFlowIncrementAuthorizationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。支払い手段によって上限金額は異なります。 | 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 

## Example

```python
from payjpv2.models.payment_flow_increment_authorization_request import PaymentFlowIncrementAuthorizationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowIncrementAuthorizationRequest from a JSON string
payment_flow_increment_authorization_request_instance = PaymentFlowIncrementAuthorizationRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowIncrementAuthorizationRequest.to_json())

# convert the object into a dict
payment_flow_increment_authorization_request_dict = payment_flow_increment_authorization_request_instance.to_dict()
# create an instance of PaymentFlowIncrementAuthorizationRequest from a dict
payment_flow_increment_authorization_request_from_dict = PaymentFlowIncrementAuthorizationRequest.from_dict(payment_flow_increment_authorization_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


