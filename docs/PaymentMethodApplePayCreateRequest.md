# PaymentMethodApplePayCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | 顧客ID | [optional] 
**billing_details** | [**PaymentMethodBillingDetailsRequest**](PaymentMethodBillingDetailsRequest.md) | 請求先情報 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**type** | **str** | Apple Pay決済の場合は &#x60;apple_pay&#x60; を指定します。 | 
**token** | **str** | Apple Payのトークン | 

## Example

```python
from payjpv2.models.payment_method_apple_pay_create_request import PaymentMethodApplePayCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodApplePayCreateRequest from a JSON string
payment_method_apple_pay_create_request_instance = PaymentMethodApplePayCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodApplePayCreateRequest.to_json())

# convert the object into a dict
payment_method_apple_pay_create_request_dict = payment_method_apple_pay_create_request_instance.to_dict()
# create an instance of PaymentMethodApplePayCreateRequest from a dict
payment_method_apple_pay_create_request_from_dict = PaymentMethodApplePayCreateRequest.from_dict(payment_method_apple_pay_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


