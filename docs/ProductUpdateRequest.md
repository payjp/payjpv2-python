# ProductUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_price_id** | **str** | この商品のデフォルト価格である価格オブジェクトのID。 | [optional] 
**description** | **str** | Checkoutなどで顧客に表示される商品説明。 | [optional] 
**unit_label** | **str** | この製品の単位を表すラベル。設定すると、Checkoutや請求書などに表示されます。（例：「個」、「ライセンス」、「時間」、「回」など） | [optional] 
**url** | **str** | この製品の公開されているウェブページのURL。 | [optional] 
**name** | **str** | Checkoutなどで顧客に表示される商品名。 | [optional] 
**active** | **bool** | 商品が購入可能かどうか。デフォルトは &#x60;true&#x60;。 | [optional] 

## Example

```python
from payjpv2.models.product_update_request import ProductUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductUpdateRequest from a JSON string
product_update_request_instance = ProductUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(ProductUpdateRequest.to_json())

# convert the object into a dict
product_update_request_dict = product_update_request_instance.to_dict()
# create an instance of ProductUpdateRequest from a dict
product_update_request_from_dict = ProductUpdateRequest.from_dict(product_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


