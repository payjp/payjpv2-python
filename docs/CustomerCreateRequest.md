# CustomerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | 顧客のメールアドレス。メールアドレスの形式が正しいかどうかは検証されます。 | [optional] 
**description** | **str** | 顧客オブジェクトに付加できる任意の文字列です。これは、ダッシュボードで顧客と一緒に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**id** | **str** | 顧客ID。100桁までの一意な文字列を指定できます。使える文字は半角英数字、ハイフン(-)、アンダースコア(_)です。未指定時は &#x60;cus_&#x60; で始まる32桁までの一意な文字列が自動生成されます。 | [optional] 

## Example

```python
from payjpv2.models.customer_create_request import CustomerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerCreateRequest from a JSON string
customer_create_request_instance = CustomerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerCreateRequest.to_json())

# convert the object into a dict
customer_create_request_dict = customer_create_request_instance.to_dict()
# create an instance of CustomerCreateRequest from a dict
customer_create_request_from_dict = CustomerCreateRequest.from_dict(customer_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


