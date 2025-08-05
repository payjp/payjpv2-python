# ProductDeletedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 商品ID | 
**object** | **str** |  | [optional] [default to 'product']
**deleted** | **bool** | 削除されたかどうか | [readonly] 

## Example

```python
from payjpv2.models.product_deleted_response import ProductDeletedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDeletedResponse from a JSON string
product_deleted_response_instance = ProductDeletedResponse.from_json(json)
# print the JSON string representation of the object
print(ProductDeletedResponse.to_json())

# convert the object into a dict
product_deleted_response_dict = product_deleted_response_instance.to_dict()
# create an instance of ProductDeletedResponse from a dict
product_deleted_response_from_dict = ProductDeletedResponse.from_dict(product_deleted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


