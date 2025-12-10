# PaymentRefundCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_flow_id** | **str** | 返金対象となる PaymentFlow の ID | 
**amount** | **int** | 返金金額 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**reason** | [**PaymentRefundReason**](PaymentRefundReason.md) | 返金理由  | 指定できる値 | |:---| | **duplicate**: 重複した支払い | | **fraudulent**: 不正な支払い | | **requested_by_customer**: 顧客の要求 | | [optional] 

## Example

```python
from payjpv2.models.payment_refund_create_request import PaymentRefundCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundCreateRequest from a JSON string
payment_refund_create_request_instance = PaymentRefundCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundCreateRequest.to_json())

# convert the object into a dict
payment_refund_create_request_dict = payment_refund_create_request_instance.to_dict()
# create an instance of PaymentRefundCreateRequest from a dict
payment_refund_create_request_from_dict = PaymentRefundCreateRequest.from_dict(payment_refund_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


