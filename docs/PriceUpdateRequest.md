# PriceUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | 価格が有効かどうか | [optional] 
**nickname** | **str** | 価格の名称。PAY.JP の管理画面で識別するためのもので、顧客には表示されません。 | [optional] 
**lookup_key** | **str** | この価格を検索するためのキー | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.price_update_request import PriceUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceUpdateRequest from a JSON string
price_update_request_instance = PriceUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PriceUpdateRequest.to_json())

# convert the object into a dict
price_update_request_dict = price_update_request_instance.to_dict()
# create an instance of PriceUpdateRequest from a dict
price_update_request_from_dict = PriceUpdateRequest.from_dict(price_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


