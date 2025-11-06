# StatementItemResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | [**StatementSubject**](StatementSubject.md) | 明細項目の種別 | 
**name** | **str** |  | 
**amount** | **int** | 明細項目の金額 | 
**tax_rate** | **str** |  | [optional] 

## Example

```python
from payjpv2.models.statement_item_response import StatementItemResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementItemResponse from a JSON string
statement_item_response_instance = StatementItemResponse.from_json(json)
# print the JSON string representation of the object
print(StatementItemResponse.to_json())

# convert the object into a dict
statement_item_response_dict = statement_item_response_instance.to_dict()
# create an instance of StatementItemResponse from a dict
statement_item_response_from_dict = StatementItemResponse.from_dict(statement_item_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


