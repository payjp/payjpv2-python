# PaymentMethodBillingDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**phone** | **str** |  | 
**email** | **str** |  | 
**address** | [**PaymentMethodBillingAddressResponse**](PaymentMethodBillingAddressResponse.md) | 請求先の住所 | 

## Example

```python
from payjpv2.models.payment_method_billing_details_response import PaymentMethodBillingDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBillingDetailsResponse from a JSON string
payment_method_billing_details_response_instance = PaymentMethodBillingDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBillingDetailsResponse.to_json())

# convert the object into a dict
payment_method_billing_details_response_dict = payment_method_billing_details_response_instance.to_dict()
# create an instance of PaymentMethodBillingDetailsResponse from a dict
payment_method_billing_details_response_from_dict = PaymentMethodBillingDetailsResponse.from_dict(payment_method_billing_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


