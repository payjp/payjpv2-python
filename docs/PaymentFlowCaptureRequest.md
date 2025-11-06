# PaymentFlowCaptureRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount_to_capture** | **int** | PaymentFlowから確定させる金額は、元の金額以下で指定します。指定されていない場合は、全額（&#x60;amount_capturable&#x60;）がデフォルトになります。 | [optional] 

## Example

```python
from payjpv2.models.payment_flow_capture_request import PaymentFlowCaptureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowCaptureRequest from a JSON string
payment_flow_capture_request_instance = PaymentFlowCaptureRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowCaptureRequest.to_json())

# convert the object into a dict
payment_flow_capture_request_dict = payment_flow_capture_request_instance.to_dict()
# create an instance of PaymentFlowCaptureRequest from a dict
payment_flow_capture_request_from_dict = PaymentFlowCaptureRequest.from_dict(payment_flow_capture_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


