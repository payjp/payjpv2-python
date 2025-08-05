# PaymentIntentCaptureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_to_capture** | **int** | PaymentIntentから確定させる金額は、元の金額以下で指定します。指定されていない場合は、全額（&#x60;amount_capturable&#x60;）がデフォルトになります。 | [optional] 

## Example

```python
from payjpv2.models.payment_intent_capture_request import PaymentIntentCaptureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentCaptureRequest from a JSON string
payment_intent_capture_request_instance = PaymentIntentCaptureRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentCaptureRequest.to_json())

# convert the object into a dict
payment_intent_capture_request_dict = payment_intent_capture_request_instance.to_dict()
# create an instance of PaymentIntentCaptureRequest from a dict
payment_intent_capture_request_from_dict = PaymentIntentCaptureRequest.from_dict(payment_intent_capture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


