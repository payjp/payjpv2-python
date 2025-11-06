# PaymentMethodCardBillingDetailsRequest

3DSのためにカードの登録時はphoneまたはemailのいずれか必須という制限を追加したPaymentMethodBillingDetailsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 請求先の名義 | [optional] 
**phone** | **str** | 請求先の電話番号（ &#x60;type&#x3D;card&#x60; の場合、 &#x60;phone&#x60; または &#x60;email&#x60; のどちらかは必須） | [optional] 
**email** | **str** | 請求先のメールアドレス（ &#x60;type&#x3D;card&#x60; の場合、 &#x60;phone&#x60; または &#x60;email&#x60; のどちらかは必須） | [optional] 
**address** | [**PaymentMethodBillingAddressRequest**](PaymentMethodBillingAddressRequest.md) | 請求先の住所 | [optional] 

## Example

```python
from payjpv2.models.payment_method_card_billing_details_request import PaymentMethodCardBillingDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardBillingDetailsRequest from a JSON string
payment_method_card_billing_details_request_instance = PaymentMethodCardBillingDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCardBillingDetailsRequest.to_json())

# convert the object into a dict
payment_method_card_billing_details_request_dict = payment_method_card_billing_details_request_instance.to_dict()
# create an instance of PaymentMethodCardBillingDetailsRequest from a dict
payment_method_card_billing_details_request_from_dict = PaymentMethodCardBillingDetailsRequest.from_dict(payment_method_card_billing_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


