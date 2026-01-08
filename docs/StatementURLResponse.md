# StatementURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'statement_url']
**url** | **str** | 取引明細書ダウンロード URL | 
**expires** | **datetime** | 有効期限の日付  有効期限は発行から1時間です。 | 

## Example

```python
from payjpv2.models.statement_url_response import StatementURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatementURLResponse from a JSON string
statement_url_response_instance = StatementURLResponse.from_json(json)
# print the JSON string representation of the object
print(StatementURLResponse.to_json())

# convert the object into a dict
statement_url_response_dict = statement_url_response_instance.to_dict()
# create an instance of StatementURLResponse from a dict
statement_url_response_from_dict = StatementURLResponse.from_dict(statement_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


