# PaymentTransactionListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentTransactionResponse]**](PaymentTransactionResponse.md) | PaymentTransaction一覧 | 

## Example

```python
from payjpv2.models.payment_transaction_list_response import PaymentTransactionListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTransactionListResponse from a JSON string
payment_transaction_list_response_instance = PaymentTransactionListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentTransactionListResponse.to_json())

# convert the object into a dict
payment_transaction_list_response_dict = payment_transaction_list_response_instance.to_dict()
# create an instance of PaymentTransactionListResponse from a dict
payment_transaction_list_response_from_dict = PaymentTransactionListResponse.from_dict(payment_transaction_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


