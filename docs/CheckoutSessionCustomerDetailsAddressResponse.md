# CheckoutSessionCustomerDetailsAddressResponse

customer_details.address のレスポンスモデル

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
from payjpv2.models.checkout_session_customer_details_address_response import CheckoutSessionCustomerDetailsAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionCustomerDetailsAddressResponse from a JSON string
checkout_session_customer_details_address_response_instance = CheckoutSessionCustomerDetailsAddressResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionCustomerDetailsAddressResponse.to_json())

# convert the object into a dict
checkout_session_customer_details_address_response_dict = checkout_session_customer_details_address_response_instance.to_dict()
# create an instance of CheckoutSessionCustomerDetailsAddressResponse from a dict
checkout_session_customer_details_address_response_from_dict = CheckoutSessionCustomerDetailsAddressResponse.from_dict(checkout_session_customer_details_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


