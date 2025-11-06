# PaymentMethodConfigurationDisplayPreference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preference** | **str** | この支払い方法がアカウントで有効になっているかどうか。  | 指定できる値 | |:---| | **on**: この決済手段を決済画面に表示する | | **off**: この決済手段を決済画面に表示しない | | **none**: デフォルト設定を使用 | | [optional] 
**value** | **str** | この支払い方法を決済画面に表示するかどうか。  | 指定できる値 | |:---| | **on**: この決済手段を決済画面に表示する | | **off**: この決済手段を決済画面に表示しない | | [optional] 

## Example

```python
from payjpv2.models.payment_method_configuration_display_preference import PaymentMethodConfigurationDisplayPreference

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodConfigurationDisplayPreference from a JSON string
payment_method_configuration_display_preference_instance = PaymentMethodConfigurationDisplayPreference.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodConfigurationDisplayPreference.to_json())

# convert the object into a dict
payment_method_configuration_display_preference_dict = payment_method_configuration_display_preference_instance.to_dict()
# create an instance of PaymentMethodConfigurationDisplayPreference from a dict
payment_method_configuration_display_preference_from_dict = PaymentMethodConfigurationDisplayPreference.from_dict(payment_method_configuration_display_preference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


