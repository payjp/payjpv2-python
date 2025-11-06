# PaymentTransactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | 
**object** | **str** |  | [optional] [default to 'payment_transaction']
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**livemode** | **bool** | 本番環境かどうか | 
**resource_id** | **str** | PaymentTransaction生成の元になったリソースのID | 
**amount** | **int** | 金額 | 
**currency** | [**Currency**](Currency.md) | 通貨 | 
**fee_rate** | **str** | 手数料率 | 
**fee** | **int** | 手数料 | 
**type** | [**PaymentTransactionType**](PaymentTransactionType.md) | PaymentTransactionの種類 | 
**payment_method_type** | [**PaymentMethodTypes**](PaymentMethodTypes.md) | 支払い方法の種類 | 
**term** | **str** | 期間ID | 

## Example

```python
from payjpv2.models.payment_transaction_response import PaymentTransactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransactionResponse from a JSON string
payment_transaction_response_instance = PaymentTransactionResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTransactionResponse.to_json())

# convert the object into a dict
payment_transaction_response_dict = payment_transaction_response_instance.to_dict()
# create an instance of PaymentTransactionResponse from a dict
payment_transaction_response_from_dict = PaymentTransactionResponse.from_dict(payment_transaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


