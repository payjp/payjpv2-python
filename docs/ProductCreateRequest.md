# ProductCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Checkout などで顧客に表示される商品名 | 
**id** | **str** | 商品 ID | [optional] 
**active** | **bool** | 商品が購入可能かどうか | [optional] [default to True]
**description** | **str** | Checkout などで顧客に表示される商品説明 | [optional] 
**unit_label** | **str** | この製品の単位を表すラベル。設定すると、Checkout などに表示されます。（例：「個」、「ライセンス」、「時間」、「回」など） | [optional] 
**url** | **str** | この製品の公開されているウェブページの URL | [optional] 

## Example

```python
from payjpv2.models.product_create_request import ProductCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductCreateRequest from a JSON string
product_create_request_instance = ProductCreateRequest.from_json(json)
# print the JSON string representation of the object
print(ProductCreateRequest.to_json())

# convert the object into a dict
product_create_request_dict = product_create_request_instance.to_dict()
# create an instance of ProductCreateRequest from a dict
product_create_request_from_dict = ProductCreateRequest.from_dict(product_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


