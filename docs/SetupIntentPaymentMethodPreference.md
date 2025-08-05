# SetupIntentPaymentMethodPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**setup_intent** | [**SetupIntentResponse**](SetupIntentResponse.md) |  | 

## Example

```python
from payjpv2.models.setup_intent_payment_method_preference import SetupIntentPaymentMethodPreference

# TODO update the JSON string below
json = "{}"
# create an instance of SetupIntentPaymentMethodPreference from a JSON string
setup_intent_payment_method_preference_instance = SetupIntentPaymentMethodPreference.from_json(json)
# print the JSON string representation of the object
print(SetupIntentPaymentMethodPreference.to_json())

# convert the object into a dict
setup_intent_payment_method_preference_dict = setup_intent_payment_method_preference_instance.to_dict()
# create an instance of SetupIntentPaymentMethodPreference from a dict
setup_intent_payment_method_preference_from_dict = SetupIntentPaymentMethodPreference.from_dict(setup_intent_payment_method_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


