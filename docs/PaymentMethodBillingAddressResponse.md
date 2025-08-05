# PaymentMethodBillingAddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country** | **str** |  | 
**zip** | **str** |  | 
**state** | **str** |  | 
**city** | **str** |  | 
**line1** | **str** |  | 
**line2** | **str** |  | 

## Example

```python
from payjpv2.models.payment_method_billing_address_response import PaymentMethodBillingAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBillingAddressResponse from a JSON string
payment_method_billing_address_response_instance = PaymentMethodBillingAddressResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBillingAddressResponse.to_json())

# convert the object into a dict
payment_method_billing_address_response_dict = payment_method_billing_address_response_instance.to_dict()
# create an instance of PaymentMethodBillingAddressResponse from a dict
payment_method_billing_address_response_from_dict = PaymentMethodBillingAddressResponse.from_dict(payment_method_billing_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


