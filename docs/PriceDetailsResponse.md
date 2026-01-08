# PriceDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'price']
**id** | **str** | 料金 ID | 
**livemode** | **bool** | 本番環境かどうか | 
**product_id** | **str** | この価格が紐付く商品の ID | 
**unit_amount** | **int** | 価格の単価 | 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | 
**active** | **bool** | 価格が有効かどうか | 
**nickname** | **str** |  | 
**type** | [**PriceType**](PriceType.md) | 一度限りの購入を表す &#x60;one_time&#x60; が入ります。 | 
**lookup_key** | **str** |  | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 

## Example

```python
from payjpv2.models.price_details_response import PriceDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDetailsResponse from a JSON string
price_details_response_instance = PriceDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PriceDetailsResponse.to_json())

# convert the object into a dict
price_details_response_dict = price_details_response_instance.to_dict()
# create an instance of PriceDetailsResponse from a dict
price_details_response_from_dict = PriceDetailsResponse.from_dict(price_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


