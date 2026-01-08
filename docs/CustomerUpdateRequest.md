# CustomerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_payment_method_id** | **str** |  | [optional] 
**email** | **str** | 顧客のメールアドレス。メールアドレスの形式が正しいかどうかは検証されます。 | [optional] 
**description** | **str** | 顧客オブジェクトに付加できる任意の文字列です。管理画面で顧客と一緒に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.customer_update_request import CustomerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerUpdateRequest from a JSON string
customer_update_request_instance = CustomerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CustomerUpdateRequest.to_json())

# convert the object into a dict
customer_update_request_dict = customer_update_request_instance.to_dict()
# create an instance of CustomerUpdateRequest from a dict
customer_update_request_from_dict = CustomerUpdateRequest.from_dict(customer_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


