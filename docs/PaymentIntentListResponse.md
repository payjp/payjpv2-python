# PaymentIntentListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentIntentResponse]**](PaymentIntentResponse.md) | 支払いインテントリスト | 

## Example

```python
from payjpv2.models.payment_intent_list_response import PaymentIntentListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentListResponse from a JSON string
payment_intent_list_response_instance = PaymentIntentListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentListResponse.to_json())

# convert the object into a dict
payment_intent_list_response_dict = payment_intent_list_response_instance.to_dict()
# create an instance of PaymentIntentListResponse from a dict
payment_intent_list_response_from_dict = PaymentIntentListResponse.from_dict(payment_intent_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


