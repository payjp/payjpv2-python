# CheckoutSessionLineItemDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'line_item']
**id** | **str** | ID | [optional] 
**amount_subtotal** | **int** | 割引や税金が適用される前のすべての商品の合計金額 | [optional] 
**amount_tax** | **int** | 税額 | [optional] 
**amount_total** | **int** | 割引と税金が適用された後のすべての商品の合計金額 | [optional] 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | [optional] 
**description** | **str** | 説明 | [optional] 
**price** | [**PriceDetailsResponse**](PriceDetailsResponse.md) | 料金情報 | [optional] 
**quantity** | **int** | 数量 | [optional] 

## Example

```python
from payjpv2.models.checkout_session_line_item_data_response import CheckoutSessionLineItemDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionLineItemDataResponse from a JSON string
checkout_session_line_item_data_response_instance = CheckoutSessionLineItemDataResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionLineItemDataResponse.to_json())

# convert the object into a dict
checkout_session_line_item_data_response_dict = checkout_session_line_item_data_response_instance.to_dict()
# create an instance of CheckoutSessionLineItemDataResponse from a dict
checkout_session_line_item_data_response_from_dict = CheckoutSessionLineItemDataResponse.from_dict(checkout_session_line_item_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


