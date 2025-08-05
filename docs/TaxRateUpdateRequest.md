# TaxRateUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | この税率が有効であるかどうか。無効にした場合でも、すでに設定されている定期課金などでは使用可能です。 | [optional] 
**country** | [**Country**](Country.md) | 有効な2文字の &lt;a href&#x3D;\&quot;https://ja.wikipedia.org/wiki/ISO_3166-1\&quot; target&#x3D;\&quot;_blank\&quot;&gt;ISO 国コード&lt;/a&gt; | [optional] 
**description** | **str** | 説明。ダッシュボード内のみで表示され、顧客には表示されません。 | [optional] 
**display_name** | **str** | 表示名。顧客に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.tax_rate_update_request import TaxRateUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateUpdateRequest from a JSON string
tax_rate_update_request_instance = TaxRateUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TaxRateUpdateRequest.to_json())

# convert the object into a dict
tax_rate_update_request_dict = tax_rate_update_request_instance.to_dict()
# create an instance of TaxRateUpdateRequest from a dict
tax_rate_update_request_from_dict = TaxRateUpdateRequest.from_dict(tax_rate_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


