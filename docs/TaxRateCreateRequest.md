# TaxRateCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_name** | **str** | 表示名。顧客に表示されます。 | 
**inclusive** | **bool** | 税込みかどうか。税込 &#x3D; &#x60;true&#x60; 税抜 &#x3D; &#x60;false&#x60; | 
**percentage** | **float** | 税率を % 単位で指定します（例: 10%の場合は「10」と入力） | 
**active** | **bool** | この税率が有効であるかどうか。無効にした場合でも、すでに設定されている定期課金などでは使用可能です。 | [optional] [default to True]
**country** | [**Country**](Country.md) | 有効な2文字の &lt;a href&#x3D;\&quot;https://ja.wikipedia.org/wiki/ISO_3166-1\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 国コード&lt;/a&gt; | [optional] 
**description** | **str** | 説明。管理画面内のみで表示され、顧客には表示されません。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.tax_rate_create_request import TaxRateCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateCreateRequest from a JSON string
tax_rate_create_request_instance = TaxRateCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TaxRateCreateRequest.to_json())

# convert the object into a dict
tax_rate_create_request_dict = tax_rate_create_request_instance.to_dict()
# create an instance of TaxRateCreateRequest from a dict
tax_rate_create_request_from_dict = TaxRateCreateRequest.from_dict(tax_rate_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


