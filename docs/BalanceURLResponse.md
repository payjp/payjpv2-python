# BalanceURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'balance_url']
**url** | **str** | 残高明細書ダウンロード URL | 
**expires** | **datetime** | 有効期限の日付  有効期限は発行から1時間です。 | 

## Example

```python
from payjpv2.models.balance_url_response import BalanceURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceURLResponse from a JSON string
balance_url_response_instance = BalanceURLResponse.from_json(json)
# print the JSON string representation of the object
print(BalanceURLResponse.to_json())

# convert the object into a dict
balance_url_response_dict = balance_url_response_instance.to_dict()
# create an instance of BalanceURLResponse from a dict
balance_url_response_from_dict = BalanceURLResponse.from_dict(balance_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


