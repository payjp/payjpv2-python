# DisplayPreferenceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preference** | **str** | この支払い方法がアカウントで有効になっているかどうか。  | 指定できる値 | |:---| | **on**: この決済手段を決済画面に表示する | | **off**: この決済手段を決済画面に表示しない | | **none**: デフォルト設定を使用 | | 

## Example

```python
from payjpv2.models.display_preference_request import DisplayPreferenceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DisplayPreferenceRequest from a JSON string
display_preference_request_instance = DisplayPreferenceRequest.from_json(json)
# print the JSON string representation of the object
print(DisplayPreferenceRequest.to_json())

# convert the object into a dict
display_preference_request_dict = display_preference_request_instance.to_dict()
# create an instance of DisplayPreferenceRequest from a dict
display_preference_request_from_dict = DisplayPreferenceRequest.from_dict(display_preference_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


