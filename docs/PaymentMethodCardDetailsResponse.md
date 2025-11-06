# PaymentMethodCardDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last4** | **str** | カードの下4桁 | 
**brand** | **str** | カードのブランド | 
**exp_month** | **int** | カードの有効期限（月） | 
**exp_year** | **int** | カードの有効期限（年） | 
**fingerprint** | **str** | fingerprint | 
**country** | **str** |  | 

## Example

```python
from payjpv2.models.payment_method_card_details_response import PaymentMethodCardDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardDetailsResponse from a JSON string
payment_method_card_details_response_instance = PaymentMethodCardDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCardDetailsResponse.to_json())

# convert the object into a dict
payment_method_card_details_response_dict = payment_method_card_details_response_instance.to_dict()
# create an instance of PaymentMethodCardDetailsResponse from a dict
payment_method_card_details_response_from_dict = PaymentMethodCardDetailsResponse.from_dict(payment_method_card_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


