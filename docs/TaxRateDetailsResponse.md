# TaxRateDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'tax_rate']
**id** | **str** | ID | [optional] 
**display_name** | **str** | 表示名。顧客に表示されます。 | [optional] 
**inclusive** | **bool** | 税込みかどうか。税込 &#x3D; &#x60;true&#x60; 税抜 &#x3D; &#x60;false&#x60; | [optional] 
**percentage** | **float** | 税率を % 単位で指定します（例： 10%の場合は「10」と入力） | [optional] 
**active** | **bool** | この税率が有効であるかどうか。無効にした場合でも、すでに設定されている定期課金などでは使用可能です。 | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**description** | **str** |  | [optional] 
**tax_type** | [**TaxType**](TaxType.md) |  | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 

## Example

```python
from payjpv2.models.tax_rate_details_response import TaxRateDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TaxRateDetailsResponse from a JSON string
tax_rate_details_response_instance = TaxRateDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(TaxRateDetailsResponse.to_json())

# convert the object into a dict
tax_rate_details_response_dict = tax_rate_details_response_instance.to_dict()
# create an instance of TaxRateDetailsResponse from a dict
tax_rate_details_response_from_dict = TaxRateDetailsResponse.from_dict(tax_rate_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


