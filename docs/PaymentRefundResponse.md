# PaymentRefundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 返金対象となる PaymentFlow の ID | 
**object** | **str** |  | [optional] [default to 'refund']
**created_at** | **datetime** | 作成時の日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新時の日時 (UTC, ISO 8601 形式) | 
**livemode** | **bool** | 本番環境かどうか | 
**amount** | **int** | 返金金額 | 
**status** | [**PaymentRefundStatus**](PaymentRefundStatus.md) | 返金ステータス  &lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/payment_refunds#refund_status\&quot; target&#x3D;\&quot;_blank\&quot;&gt;返金ステータスの詳細についてはこちらを参照してください。&lt;/a&gt;  | 指定できる値 | |:---| | **succeeded**: 成功 | | **failed**: 失敗 | | **pending**: 保留中 | | **canceled**: キャンセル | | 
**payment_flow** | **str** | 返金対象となる PaymentFlow の ID | 
**reason** | [**PaymentRefundReason**](PaymentRefundReason.md) |  | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 

## Example

```python
from payjpv2.models.payment_refund_response import PaymentRefundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundResponse from a JSON string
payment_refund_response_instance = PaymentRefundResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundResponse.to_json())

# convert the object into a dict
payment_refund_response_dict = payment_refund_response_instance.to_dict()
# create an instance of PaymentRefundResponse from a dict
payment_refund_response_from_dict = PaymentRefundResponse.from_dict(payment_refund_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


