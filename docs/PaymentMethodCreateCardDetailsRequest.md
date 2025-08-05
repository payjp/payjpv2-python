# PaymentMethodCreateCardDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | カード番号 | 
**exp_month** | **int** | カードの有効期限（月） | 
**exp_year** | **int** | カードの有効期限（年） | 
**cvc** | **str** | カードのセキュリティコード | 

## Example

```python
from payjpv2.models.payment_method_create_card_details_request import PaymentMethodCreateCardDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCreateCardDetailsRequest from a JSON string
payment_method_create_card_details_request_instance = PaymentMethodCreateCardDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCreateCardDetailsRequest.to_json())

# convert the object into a dict
payment_method_create_card_details_request_dict = payment_method_create_card_details_request_instance.to_dict()
# create an instance of PaymentMethodCreateCardDetailsRequest from a dict
payment_method_create_card_details_request_from_dict = PaymentMethodCreateCardDetailsRequest.from_dict(payment_method_create_card_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


