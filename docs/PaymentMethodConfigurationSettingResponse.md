# PaymentMethodConfigurationSettingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **bool** | この支払い方法が決済画面に表示されるかどうか。&#x60;display_preference.preference&#x60; と &#x60;display_preference.value&#x60; の両方が &#x60;on&#x60; の場合に決済画面に表示されます。 | [optional] 
**display_preference** | [**PaymentMethodConfigurationDisplayPreference**](PaymentMethodConfigurationDisplayPreference.md) | 支払い方法の表示設定 | [optional] 

## Example

```python
from payjpv2.models.payment_method_configuration_setting_response import PaymentMethodConfigurationSettingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodConfigurationSettingResponse from a JSON string
payment_method_configuration_setting_response_instance = PaymentMethodConfigurationSettingResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodConfigurationSettingResponse.to_json())

# convert the object into a dict
payment_method_configuration_setting_response_dict = payment_method_configuration_setting_response_instance.to_dict()
# create an instance of PaymentMethodConfigurationSettingResponse from a dict
payment_method_configuration_setting_response_from_dict = PaymentMethodConfigurationSettingResponse.from_dict(payment_method_configuration_setting_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


