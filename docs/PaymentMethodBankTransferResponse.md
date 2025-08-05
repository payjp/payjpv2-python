# PaymentMethodBankTransferResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_method']
**id** | **str** | 支払い方法ID | 
**type** | **str** |  | 
**livemode** | **bool** | 本番環境かどうか | 
**created_at** | **datetime** | 支払い方法作成時の日時(UTC) | 
**updated_at** | **datetime** | 支払い方法更新時の日時(UTC) | 
**bank_transfer** | **object** | 銀行振込情報 | 

## Example

```python
from payjpv2.models.payment_method_bank_transfer_response import PaymentMethodBankTransferResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBankTransferResponse from a JSON string
payment_method_bank_transfer_response_instance = PaymentMethodBankTransferResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBankTransferResponse.to_json())

# convert the object into a dict
payment_method_bank_transfer_response_dict = payment_method_bank_transfer_response_instance.to_dict()
# create an instance of PaymentMethodBankTransferResponse from a dict
payment_method_bank_transfer_response_from_dict = PaymentMethodBankTransferResponse.from_dict(payment_method_bank_transfer_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


