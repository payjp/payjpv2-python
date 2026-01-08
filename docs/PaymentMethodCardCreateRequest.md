# PaymentMethodCardCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | 顧客 ID | [optional] 
**billing_details** | [**PaymentMethodCardBillingDetailsRequest**](PaymentMethodCardBillingDetailsRequest.md) | 請求先情報 | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**type** | **str** | クレジットカード決済の場合は &#x60;card&#x60; を指定します。 | 
**card** | [**PaymentMethodCreateCardDetailsRequest**](PaymentMethodCreateCardDetailsRequest.md) | カード情報 | 

## Example

```python
from payjpv2.models.payment_method_card_create_request import PaymentMethodCardCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardCreateRequest from a JSON string
payment_method_card_create_request_instance = PaymentMethodCardCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCardCreateRequest.to_json())

# convert the object into a dict
payment_method_card_create_request_dict = payment_method_card_create_request_instance.to_dict()
# create an instance of PaymentMethodCardCreateRequest from a dict
payment_method_card_create_request_from_dict = PaymentMethodCardCreateRequest.from_dict(payment_method_card_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


