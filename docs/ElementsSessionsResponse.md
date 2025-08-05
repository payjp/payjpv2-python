# ElementsSessionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_preference** | [**PaymentMethodPreference**](PaymentMethodPreference.md) |  | 

## Example

```python
from payjpv2.models.elements_sessions_response import ElementsSessionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ElementsSessionsResponse from a JSON string
elements_sessions_response_instance = ElementsSessionsResponse.from_json(json)
# print the JSON string representation of the object
print(ElementsSessionsResponse.to_json())

# convert the object into a dict
elements_sessions_response_dict = elements_sessions_response_instance.to_dict()
# create an instance of ElementsSessionsResponse from a dict
elements_sessions_response_from_dict = ElementsSessionsResponse.from_dict(elements_sessions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


