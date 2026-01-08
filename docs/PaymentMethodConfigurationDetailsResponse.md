# PaymentMethodConfigurationDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_method_configuration']
**id** | **str** | 支払い方法設定 ID | 
**livemode** | **bool** | 本番環境かどうか | 
**active** | **bool** | 設定が有効かどうか | 
**name** | **str** |  | 
**paypay** | [**PaymentMethodConfigurationSettingResponse**](PaymentMethodConfigurationSettingResponse.md) | PayPay の設定 | 
**card** | [**PaymentMethodConfigurationSettingResponse**](PaymentMethodConfigurationSettingResponse.md) | カードの設定 | 

## Example

```python
from payjpv2.models.payment_method_configuration_details_response import PaymentMethodConfigurationDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodConfigurationDetailsResponse from a JSON string
payment_method_configuration_details_response_instance = PaymentMethodConfigurationDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodConfigurationDetailsResponse.to_json())

# convert the object into a dict
payment_method_configuration_details_response_dict = payment_method_configuration_details_response_instance.to_dict()
# create an instance of PaymentMethodConfigurationDetailsResponse from a dict
payment_method_configuration_details_response_from_dict = PaymentMethodConfigurationDetailsResponse.from_dict(payment_method_configuration_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


