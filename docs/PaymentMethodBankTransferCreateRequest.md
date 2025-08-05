# PaymentMethodBankTransferCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_details** | [**PaymentMethodBillingDetailsRequest**](PaymentMethodBillingDetailsRequest.md) | 請求先情報 | [optional] 
**type** | **str** |  | 
**amount** | **int** | 振込金額 | 

## Example

```python
from payjpv2.models.payment_method_bank_transfer_create_request import PaymentMethodBankTransferCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBankTransferCreateRequest from a JSON string
payment_method_bank_transfer_create_request_instance = PaymentMethodBankTransferCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBankTransferCreateRequest.to_json())

# convert the object into a dict
payment_method_bank_transfer_create_request_dict = payment_method_bank_transfer_create_request_instance.to_dict()
# create an instance of PaymentMethodBankTransferCreateRequest from a dict
payment_method_bank_transfer_create_request_from_dict = PaymentMethodBankTransferCreateRequest.from_dict(payment_method_bank_transfer_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


