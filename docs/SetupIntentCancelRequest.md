# SetupIntentCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_reason** | **str** | この SetupIntent のキャンセル理由。  | 指定できる値 | |:---| | **abandoned**: 顧客が支払いを完了しなかった場合。 | | **requested_by_customer**: 顧客がキャンセルを要求した場合。 | | **duplicate**: 支払い方法が重複している場合。 | | [optional] 

## Example

```python
from payjpv2.models.setup_intent_cancel_request import SetupIntentCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupIntentCancelRequest from a JSON string
setup_intent_cancel_request_instance = SetupIntentCancelRequest.from_json(json)
# print the JSON string representation of the object
print(SetupIntentCancelRequest.to_json())

# convert the object into a dict
setup_intent_cancel_request_dict = setup_intent_cancel_request_instance.to_dict()
# create an instance of SetupIntentCancelRequest from a dict
setup_intent_cancel_request_from_dict = SetupIntentCancelRequest.from_dict(setup_intent_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


