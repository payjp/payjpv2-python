# PayPayConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_preference** | [**DisplayPreferenceRequest**](DisplayPreferenceRequest.md) |  | [optional] 

## Example

```python
from payjpv2.models.pay_pay_config_request import PayPayConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PayPayConfigRequest from a JSON string
pay_pay_config_request_instance = PayPayConfigRequest.from_json(json)
# print the JSON string representation of the object
print(PayPayConfigRequest.to_json())

# convert the object into a dict
pay_pay_config_request_dict = pay_pay_config_request_instance.to_dict()
# create an instance of PayPayConfigRequest from a dict
pay_pay_config_request_from_dict = PayPayConfigRequest.from_dict(pay_pay_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


