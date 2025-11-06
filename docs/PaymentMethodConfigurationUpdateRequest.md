# PaymentMethodConfigurationUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**card** | [**CardConfigRequest**](CardConfigRequest.md) |  | [optional] 
**paypay** | [**PayPayConfigRequest**](PayPayConfigRequest.md) |  | [optional] 

## Example

```python
from payjpv2.models.payment_method_configuration_update_request import PaymentMethodConfigurationUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodConfigurationUpdateRequest from a JSON string
payment_method_configuration_update_request_instance = PaymentMethodConfigurationUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodConfigurationUpdateRequest.to_json())

# convert the object into a dict
payment_method_configuration_update_request_dict = payment_method_configuration_update_request_instance.to_dict()
# create an instance of PaymentMethodConfigurationUpdateRequest from a dict
payment_method_configuration_update_request_from_dict = PaymentMethodConfigurationUpdateRequest.from_dict(payment_method_configuration_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


