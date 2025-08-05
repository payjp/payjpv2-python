# PaymentMethodPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_intent** | [**PaymentIntentResponse**](PaymentIntentResponse.md) |  | 
**setup_intent** | [**SetupIntentResponse**](SetupIntentResponse.md) |  | 

## Example

```python
from payjpv2.models.payment_method_preference import PaymentMethodPreference

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodPreference from a JSON string
payment_method_preference_instance = PaymentMethodPreference.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodPreference.to_json())

# convert the object into a dict
payment_method_preference_dict = payment_method_preference_instance.to_dict()
# create an instance of PaymentMethodPreference from a dict
payment_method_preference_from_dict = PaymentMethodPreference.from_dict(payment_method_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


