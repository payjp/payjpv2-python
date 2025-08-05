# PaymentMethodBillingAddressRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** | 請求先の住所（国） | [optional] 
**zip** | **str** | 請求先の住所（郵便番号） | [optional] 
**state** | **str** | 請求先の住所（都道府県） | [optional] 
**city** | **str** | 請求先の住所（市区町村） | [optional] 
**line1** | **str** | 請求先の住所（番地など） | [optional] 
**line2** | **str** | 請求先の住所（建物名など） | [optional] 

## Example

```python
from payjpv2.models.payment_method_billing_address_request import PaymentMethodBillingAddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBillingAddressRequest from a JSON string
payment_method_billing_address_request_instance = PaymentMethodBillingAddressRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBillingAddressRequest.to_json())

# convert the object into a dict
payment_method_billing_address_request_dict = payment_method_billing_address_request_instance.to_dict()
# create an instance of PaymentMethodBillingAddressRequest from a dict
payment_method_billing_address_request_from_dict = PaymentMethodBillingAddressRequest.from_dict(payment_method_billing_address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


