# PaymentMethodApplePayUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**PaymentMethodBillingDetailsRequest**](PaymentMethodBillingDetailsRequest.md) | 請求先情報 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**type** | **str** | Apple Pay 決済の場合は &#x60;apple_pay&#x60; を指定します。 | 

## Example

```python
from payjpv2.models.payment_method_apple_pay_update_request import PaymentMethodApplePayUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodApplePayUpdateRequest from a JSON string
payment_method_apple_pay_update_request_instance = PaymentMethodApplePayUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodApplePayUpdateRequest.to_json())

# convert the object into a dict
payment_method_apple_pay_update_request_dict = payment_method_apple_pay_update_request_instance.to_dict()
# create an instance of PaymentMethodApplePayUpdateRequest from a dict
payment_method_apple_pay_update_request_from_dict = PaymentMethodApplePayUpdateRequest.from_dict(payment_method_apple_pay_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


