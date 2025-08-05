# PaymentPageDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | [optional] [default to 'checkout.session']
**checkout_session** | [**CheckoutSessionDetailsResponse**](CheckoutSessionDetailsResponse.md) |  | 

## Example

```python
from payjpv2.models.payment_page_details_response import PaymentPageDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPageDetailsResponse from a JSON string
payment_page_details_response_instance = PaymentPageDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentPageDetailsResponse.to_json())

# convert the object into a dict
payment_page_details_response_dict = payment_page_details_response_instance.to_dict()
# create an instance of PaymentPageDetailsResponse from a dict
payment_page_details_response_from_dict = PaymentPageDetailsResponse.from_dict(payment_page_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


