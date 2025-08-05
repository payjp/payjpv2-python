# CheckoutSessionUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **object** |  | [optional] 

## Example

```python
from payjpv2.models.checkout_session_update_request import CheckoutSessionUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionUpdateRequest from a JSON string
checkout_session_update_request_instance = CheckoutSessionUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionUpdateRequest.to_json())

# convert the object into a dict
checkout_session_update_request_dict = checkout_session_update_request_instance.to_dict()
# create an instance of CheckoutSessionUpdateRequest from a dict
checkout_session_update_request_from_dict = CheckoutSessionUpdateRequest.from_dict(checkout_session_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


