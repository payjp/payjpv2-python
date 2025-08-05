# CheckoutSessionLineItemPriceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 料金ID | [optional] 
**object** | **str** |  | [optional] [default to 'price']
**livemode** | **bool** | 本番環境かどうか | [optional] 
**active** | **bool** | 有効かどうか | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 
**nickname** | **str** |  | [optional] 
**type** | [**PriceType**](PriceType.md) | 料金の種類 | [optional] 
**lookup_key** | **str** |  | [optional] 
**currency** | [**Currency**](Currency.md) | 通貨 | [optional] 
**product** | **str** | 商品ID | [optional] 
**unit_amount** | **int** | 単価 | [optional] 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | [optional] 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | [optional] 

## Example

```python
from payjpv2.models.checkout_session_line_item_price_response import CheckoutSessionLineItemPriceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionLineItemPriceResponse from a JSON string
checkout_session_line_item_price_response_instance = CheckoutSessionLineItemPriceResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionLineItemPriceResponse.to_json())

# convert the object into a dict
checkout_session_line_item_price_response_dict = checkout_session_line_item_price_response_instance.to_dict()
# create an instance of CheckoutSessionLineItemPriceResponse from a dict
checkout_session_line_item_price_response_from_dict = CheckoutSessionLineItemPriceResponse.from_dict(checkout_session_line_item_price_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


