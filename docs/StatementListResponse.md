# StatementListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[StatementResponse]**](StatementResponse.md) |  | 

## Example

```python
from payjpv2.models.statement_list_response import StatementListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementListResponse from a JSON string
statement_list_response_instance = StatementListResponse.from_json(json)
# print the JSON string representation of the object
print(StatementListResponse.to_json())

# convert the object into a dict
statement_list_response_dict = statement_list_response_instance.to_dict()
# create an instance of StatementListResponse from a dict
statement_list_response_from_dict = StatementListResponse.from_dict(statement_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


