# PaymentRefundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_refund']
**id** | **str** | 返金 ID | 
**livemode** | **bool** | 本番環境かどうか | 
**payment_flow_id** | **str** | 返金対象となる PaymentFlow の ID | 
**amount** | **int** | 返金金額 | 
**status** | [**PaymentRefundStatus**](PaymentRefundStatus.md) | 返金ステータス  &lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/status-management/refund#%E8%BF%94%E9%87%91%E3%82%B9%E3%83%86%E3%83%BC%E3%82%BF%E3%82%B9%E3%81%AE%E7%9B%A3%E8%A6%96\&quot; target&#x3D;\&quot;_blank\&quot;&gt;返金ステータスの詳細についてはこちらを参照してください。&lt;/a&gt;  | 値 | |:---| | **succeeded**: 返金が成功しました | | **failed**: 返金が失敗しました | | **pending**: 返金処理中です | | **canceled**: 返金がキャンセルされました | | **requires_action**: 追加のアクションが必要です | | 
**reason** | [**PaymentRefundReason**](PaymentRefundReason.md) |  | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 

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


