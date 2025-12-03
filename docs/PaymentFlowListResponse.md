# PaymentFlowListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentFlowResponse]**](PaymentFlowResponse.md) | 支払いフローリスト | 

## Example

```python
from payjpv2.models.payment_flow_list_response import PaymentFlowListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowListResponse from a JSON string
payment_flow_list_response_instance = PaymentFlowListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowListResponse.to_json())

# convert the object into a dict
payment_flow_list_response_dict = payment_flow_list_response_instance.to_dict()
# create an instance of PaymentFlowListResponse from a dict
payment_flow_list_response_from_dict = PaymentFlowListResponse.from_dict(payment_flow_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


