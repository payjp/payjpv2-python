# PaymentMethodAttachRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | 顧客ID | 

## Example

```python
from payjpv2.models.payment_method_attach_request import PaymentMethodAttachRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodAttachRequest from a JSON string
payment_method_attach_request_instance = PaymentMethodAttachRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodAttachRequest.to_json())

# convert the object into a dict
payment_method_attach_request_dict = payment_method_attach_request_instance.to_dict()
# create an instance of PaymentMethodAttachRequest from a dict
payment_method_attach_request_from_dict = PaymentMethodAttachRequest.from_dict(payment_method_attach_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


