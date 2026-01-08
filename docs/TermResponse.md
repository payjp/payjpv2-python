# TermResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'term']
**id** | **str** | 集計区間 ID | 
**livemode** | **bool** | 本番環境かどうか | 
**start_at** | **datetime** | 区間開始時刻 | 
**end_at** | **datetime** | 区間終了時刻  Term が表す区間は start_at 以上 end_at 未満の範囲となります。 翌サイクルの Term の場合 null を返します。 | 
**closed** | **bool** | 締め処理が完了済みなら true | 

## Example

```python
from payjpv2.models.term_response import TermResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TermResponse from a JSON string
term_response_instance = TermResponse.from_json(json)
# print the JSON string representation of the object
print(TermResponse.to_json())

# convert the object into a dict
term_response_dict = term_response_instance.to_dict()
# create an instance of TermResponse from a dict
term_response_from_dict = TermResponse.from_dict(term_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


