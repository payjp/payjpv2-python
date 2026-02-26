# ApplePayConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_preference** | [**DisplayPreferenceRequest**](DisplayPreferenceRequest.md) |  | [optional] 

## Example

```python
from payjpv2.models.apple_pay_config_request import ApplePayConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApplePayConfigRequest from a JSON string
apple_pay_config_request_instance = ApplePayConfigRequest.from_json(json)
# print the JSON string representation of the object
print(ApplePayConfigRequest.to_json())

# convert the object into a dict
apple_pay_config_request_dict = apple_pay_config_request_instance.to_dict()
# create an instance of ApplePayConfigRequest from a dict
apple_pay_config_request_from_dict = ApplePayConfigRequest.from_dict(apple_pay_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


