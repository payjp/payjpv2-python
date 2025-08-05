# TaxRateListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[TaxRateDetailsResponse]**](TaxRateDetailsResponse.md) |  | 

## Example

```python
from payjpv2.models.tax_rate_list_response import TaxRateListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateListResponse from a JSON string
tax_rate_list_response_instance = TaxRateListResponse.from_json(json)
# print the JSON string representation of the object
print(TaxRateListResponse.to_json())

# convert the object into a dict
tax_rate_list_response_dict = tax_rate_list_response_instance.to_dict()
# create an instance of TaxRateListResponse from a dict
tax_rate_list_response_from_dict = TaxRateListResponse.from_dict(tax_rate_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


