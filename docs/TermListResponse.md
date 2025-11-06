# TermListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[TermResponse]**](TermResponse.md) |  | 

## Example

```python
from payjpv2.models.term_list_response import TermListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TermListResponse from a JSON string
term_list_response_instance = TermListResponse.from_json(json)
# print the JSON string representation of the object
print(TermListResponse.to_json())

# convert the object into a dict
term_list_response_dict = term_list_response_instance.to_dict()
# create an instance of TermListResponse from a dict
term_list_response_from_dict = TermListResponse.from_dict(term_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


