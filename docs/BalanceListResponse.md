# BalanceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[BalanceResponse]**](BalanceResponse.md) |  | 

## Example

```python
from payjpv2.models.balance_list_response import BalanceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceListResponse from a JSON string
balance_list_response_instance = BalanceListResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceListResponse.to_json())

# convert the object into a dict
balance_list_response_dict = balance_list_response_instance.to_dict()
# create an instance of BalanceListResponse from a dict
balance_list_response_from_dict = BalanceListResponse.from_dict(balance_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


