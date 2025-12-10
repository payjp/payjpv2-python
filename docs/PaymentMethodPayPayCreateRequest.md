# PaymentMethodPayPayCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | 顧客ID | [optional] 
**billing_details** | [**PaymentMethodBillingDetailsRequest**](PaymentMethodBillingDetailsRequest.md) | 請求先情報 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**type** | **str** | PayPay決済の場合は &#x60;paypay&#x60; を指定します。 | 

## Example

```python
from payjpv2.models.payment_method_pay_pay_create_request import PaymentMethodPayPayCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodPayPayCreateRequest from a JSON string
payment_method_pay_pay_create_request_instance = PaymentMethodPayPayCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodPayPayCreateRequest.to_json())

# convert the object into a dict
payment_method_pay_pay_create_request_dict = payment_method_pay_pay_create_request_instance.to_dict()
# create an instance of PaymentMethodPayPayCreateRequest from a dict
payment_method_pay_pay_create_request_from_dict = PaymentMethodPayPayCreateRequest.from_dict(payment_method_pay_pay_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


