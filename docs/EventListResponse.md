# EventListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[EventResponse]**](EventResponse.md) | イベントリスト | 

## Example

```python
from payjpv2.models.event_list_response import EventListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventListResponse from a JSON string
event_list_response_instance = EventListResponse.from_json(json)
# print the JSON string representation of the object
print(EventListResponse.to_json())

# convert the object into a dict
event_list_response_dict = event_list_response_instance.to_dict()
# create an instance of EventListResponse from a dict
event_list_response_from_dict = EventListResponse.from_dict(event_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


