# PaymentDisputeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_dispute']
**id** | **str** | PaymentDispute ID | 
**livemode** | **bool** | 本番環境かどうか | 
**payment_flow_id** | **str** | 関連する PaymentFlow の ID | 
**amount** | **int** | 金額 | 
**currency** | [**Currency**](Currency.md) | 通貨コード (ISO 4217) | 
**status** | [**PaymentDisputeStatus**](PaymentDisputeStatus.md) | disputeのステータス  | 値 | |:---| | **pre_warning_needs_response**: 利用照会 | | **warning_needs_response**: 配送保留 | | **warning_needs_refund**: 配送停止 | | **warning_under_review**: 加盟店回答済 | | **needs_response**: チャージバック | | **under_review**: 反証済 | | **lost**: チャージバック受入 | | **cancel**: 取下げ | | 
**reason** | [**PaymentDisputeReason**](PaymentDisputeReason.md) |  | 
**due_by** | **datetime** |  | 
**payment_method_type** | [**PaymentMethodTypes**](PaymentMethodTypes.md) | 支払い方法の種類 | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 

## Example

```python
from payjpv2.models.payment_dispute_response import PaymentDisputeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDisputeResponse from a JSON string
payment_dispute_response_instance = PaymentDisputeResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentDisputeResponse.to_json())

# convert the object into a dict
payment_dispute_response_dict = payment_dispute_response_instance.to_dict()
# create an instance of PaymentDisputeResponse from a dict
payment_dispute_response_from_dict = PaymentDisputeResponse.from_dict(payment_dispute_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


