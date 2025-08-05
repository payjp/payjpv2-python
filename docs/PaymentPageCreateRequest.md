# PaymentPageCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_session_id** | **str** | CheckoutSession ID | 

## Example

```python
from payjpv2.models.payment_page_create_request import PaymentPageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentPageCreateRequest from a JSON string
payment_page_create_request_instance = PaymentPageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentPageCreateRequest.to_json())

# convert the object into a dict
payment_page_create_request_dict = payment_page_create_request_instance.to_dict()
# create an instance of PaymentPageCreateRequest from a dict
payment_page_create_request_from_dict = PaymentPageCreateRequest.from_dict(payment_page_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


