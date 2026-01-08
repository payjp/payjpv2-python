# EventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'event']
**id** | **str** | イベント ID | 
**livemode** | **bool** | 本番環境かどうか | 
**type** | **str** | イベントの種類 | 
**pending_webhooks** | **int** | 設定された URL への通知が完了していない (2xx のレスポンスが得られていない) webhook の数 | 
**data** | **Dict[str, object]** | このイベントに関連したリソースオブジェクト | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 

## Example

```python
from payjpv2.models.event_response import EventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponse from a JSON string
event_response_instance = EventResponse.from_json(json)
# print the JSON string representation of the object
print(EventResponse.to_json())

# convert the object into a dict
event_response_dict = event_response_instance.to_dict()
# create an instance of EventResponse from a dict
event_response_from_dict = EventResponse.from_dict(event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


