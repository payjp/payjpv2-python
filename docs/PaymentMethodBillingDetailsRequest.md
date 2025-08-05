# PaymentMethodBillingDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 請求先の名義 | [optional] 
**phone** | **str** | 請求先の電話番号（ &#x60;type&#x3D;card&#x60; の場合、 &#x60;phone&#x60; または &#x60;email&#x60; のどちらかは必須） | [optional] 
**email** | **str** | 請求先のメールアドレス（ &#x60;type&#x3D;card&#x60; の場合、 &#x60;phone&#x60; または &#x60;email&#x60; のどちらかは必須） | [optional] 
**address** | [**PaymentMethodBillingAddressRequest**](PaymentMethodBillingAddressRequest.md) | 請求先の住所 | [optional] 

## Example

```python
from payjpv2.models.payment_method_billing_details_request import PaymentMethodBillingDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodBillingDetailsRequest from a JSON string
payment_method_billing_details_request_instance = PaymentMethodBillingDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodBillingDetailsRequest.to_json())

# convert the object into a dict
payment_method_billing_details_request_dict = payment_method_billing_details_request_instance.to_dict()
# create an instance of PaymentMethodBillingDetailsRequest from a dict
payment_method_billing_details_request_from_dict = PaymentMethodBillingDetailsRequest.from_dict(payment_method_billing_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


