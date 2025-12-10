# ProductDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 商品ID | 
**object** | **str** |  | [optional] [default to 'product']
**name** | **str** | Checkoutなどで顧客に表示される商品名。 | 
**active** | **bool** | 商品が購入可能かどうか。デフォルトは &#x60;true&#x60;。 | 
**default_price_id** | **str** |  | 
**description** | **str** |  | 
**unit_label** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from payjpv2.models.product_details_response import ProductDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDetailsResponse from a JSON string
product_details_response_instance = ProductDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductDetailsResponse.to_json())

# convert the object into a dict
product_details_response_dict = product_details_response_instance.to_dict()
# create an instance of ProductDetailsResponse from a dict
product_details_response_from_dict = ProductDetailsResponse.from_dict(product_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


