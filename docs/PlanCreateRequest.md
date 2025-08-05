# PlanCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | 必須。50~9,999,999の整数 | 
**currency** | **str** | 必須。3文字のISOコード(現状 &#39;jpy&#39; のみサポート) | 
**interval** | **str** | 必須。月次課金であれば&#39;month&#39;を、年次課金であれば&#39;year&#39;を指定 | 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**trial_days** | **int** |  | [optional] 
**billing_day** | **int** |  | [optional] 
**metadata** | **Dict[str, str]** |  | [optional] 

## Example

```python
from payjpv2.models.plan_create_request import PlanCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlanCreateRequest from a JSON string
plan_create_request_instance = PlanCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PlanCreateRequest.to_json())

# convert the object into a dict
plan_create_request_dict = plan_create_request_instance.to_dict()
# create an instance of PlanCreateRequest from a dict
plan_create_request_from_dict = PlanCreateRequest.from_dict(plan_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


