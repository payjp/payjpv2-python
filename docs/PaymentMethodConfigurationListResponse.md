# PaymentMethodConfigurationListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentMethodConfigurationDetailsResponse]**](PaymentMethodConfigurationDetailsResponse.md) |  | 

## Example

```python
from payjpv2.models.payment_method_configuration_list_response import PaymentMethodConfigurationListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodConfigurationListResponse from a JSON string
payment_method_configuration_list_response_instance = PaymentMethodConfigurationListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodConfigurationListResponse.to_json())

# convert the object into a dict
payment_method_configuration_list_response_dict = payment_method_configuration_list_response_instance.to_dict()
# create an instance of PaymentMethodConfigurationListResponse from a dict
payment_method_configuration_list_response_from_dict = PaymentMethodConfigurationListResponse.from_dict(payment_method_configuration_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


