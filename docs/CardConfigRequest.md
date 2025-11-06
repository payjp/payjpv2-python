# CardConfigRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_preference** | [**DisplayPreferenceRequest**](DisplayPreferenceRequest.md) |  | [optional] 

## Example

```python
from payjpv2.models.card_config_request import CardConfigRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CardConfigRequest from a JSON string
card_config_request_instance = CardConfigRequest.from_json(json)
# print the JSON string representation of the object
print(CardConfigRequest.to_json())

# convert the object into a dict
card_config_request_dict = card_config_request_instance.to_dict()
# create an instance of CardConfigRequest from a dict
card_config_request_from_dict = CardConfigRequest.from_dict(card_config_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


