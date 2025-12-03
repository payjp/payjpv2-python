# PriceDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 料金ID | 
**object** | **str** |  | [optional] [default to 'price']
**livemode** | **bool** | 本番環境かどうか | 
**active** | **bool** | 価格が有効かどうか。デフォルトは &#x60;true&#x60;。 | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**nickname** | **str** |  | 
**type** | [**PriceType**](PriceType.md) | 価格が一度限りの購入か、継続的な（サブスクリプション）購入かに応じて、&#x60;one_time&#x60; または &#x60;recurring&#x60; のいずれかとなります。  | 指定できる値 | |:---| | **one_time**: 1回限りの価格。 | | **recurring**: 継続的な価格。 | | 
**lookup_key** | **str** |  | 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | 
**product** | **str** | この価格が紐付く商品のID。 | 
**unit_amount** | **int** | 価格の単価。0以上の整数となります。 | 
**created_at** | **datetime** | 支払い方法作成時の日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 支払い方法更新時の日時 (UTC, ISO 8601 形式) | 

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


