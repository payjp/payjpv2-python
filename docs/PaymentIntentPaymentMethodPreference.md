# PaymentIntentPaymentMethodPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_intent** | [**PaymentIntentResponse**](PaymentIntentResponse.md) |  | 

## Example

```python
from payjpv2.models.payment_intent_payment_method_preference import PaymentIntentPaymentMethodPreference

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentPaymentMethodPreference from a JSON string
payment_intent_payment_method_preference_instance = PaymentIntentPaymentMethodPreference.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentPaymentMethodPreference.to_json())

# convert the object into a dict
payment_intent_payment_method_preference_dict = payment_intent_payment_method_preference_instance.to_dict()
# create an instance of PaymentIntentPaymentMethodPreference from a dict
payment_intent_payment_method_preference_from_dict = PaymentIntentPaymentMethodPreference.from_dict(payment_intent_payment_method_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


