# CheckoutSessionCustomerDetailsResponse

customer_details のレスポンスモデル

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**email** | **str** |  | 
**phone** | **str** |  | 
**address** | [**CheckoutSessionCustomerDetailsAddressResponse**](CheckoutSessionCustomerDetailsAddressResponse.md) |  | 

## Example

```python
from payjpv2.models.checkout_session_customer_details_response import CheckoutSessionCustomerDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionCustomerDetailsResponse from a JSON string
checkout_session_customer_details_response_instance = CheckoutSessionCustomerDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionCustomerDetailsResponse.to_json())

# convert the object into a dict
checkout_session_customer_details_response_dict = checkout_session_customer_details_response_instance.to_dict()
# create an instance of CheckoutSessionCustomerDetailsResponse from a dict
checkout_session_customer_details_response_from_dict = CheckoutSessionCustomerDetailsResponse.from_dict(checkout_session_customer_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


