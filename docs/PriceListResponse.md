# PriceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PriceDetailsResponse]**](PriceDetailsResponse.md) |  | 

## Example

```python
from payjpv2.models.price_list_response import PriceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListResponse from a JSON string
price_list_response_instance = PriceListResponse.from_json(json)
# print the JSON string representation of the object
print(PriceListResponse.to_json())

# convert the object into a dict
price_list_response_dict = price_list_response_instance.to_dict()
# create an instance of PriceListResponse from a dict
price_list_response_from_dict = PriceListResponse.from_dict(price_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


