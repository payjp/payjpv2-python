# SetupFlowListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[SetupFlowResponse]**](SetupFlowResponse.md) |  | 

## Example

```python
from payjpv2.models.setup_flow_list_response import SetupFlowListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowListResponse from a JSON string
setup_flow_list_response_instance = SetupFlowListResponse.from_json(json)
# print the JSON string representation of the object
print(SetupFlowListResponse.to_json())

# convert the object into a dict
setup_flow_list_response_dict = setup_flow_list_response_instance.to_dict()
# create an instance of SetupFlowListResponse from a dict
setup_flow_list_response_from_dict = SetupFlowListResponse.from_dict(setup_flow_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


