# PaymentIntentCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_reason** | **str** | キャンセル理由 | [optional] 

## Example

```python
from payjpv2.models.payment_intent_cancel_request import PaymentIntentCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentCancelRequest from a JSON string
payment_intent_cancel_request_instance = PaymentIntentCancelRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentCancelRequest.to_json())

# convert the object into a dict
payment_intent_cancel_request_dict = payment_intent_cancel_request_instance.to_dict()
# create an instance of PaymentIntentCancelRequest from a dict
payment_intent_cancel_request_from_dict = PaymentIntentCancelRequest.from_dict(payment_intent_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


