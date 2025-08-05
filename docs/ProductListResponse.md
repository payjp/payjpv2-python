# ProductListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[ProductDetailsResponse]**](ProductDetailsResponse.md) |  | 

## Example

```python
from payjpv2.models.product_list_response import ProductListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListResponse from a JSON string
product_list_response_instance = ProductListResponse.from_json(json)
# print the JSON string representation of the object
print(ProductListResponse.to_json())

# convert the object into a dict
product_list_response_dict = product_list_response_instance.to_dict()
# create an instance of ProductListResponse from a dict
product_list_response_from_dict = ProductListResponse.from_dict(product_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


