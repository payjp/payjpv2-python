# PlanResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | プランID。一意なplanオブジェクトを識別する文字列。 | 
**object** | **str** | &#39;plan&#39;の固定文字列 | [optional] [default to 'plan']
**livemode** | **bool** | 本番環境かどうか | 
**created_at** | **datetime** | プラン作成時のUTCタイムスタンプ | 
**updated_at** | **datetime** | プラン作成時のUTCタイムスタンプ | 
**amount** | **int** | プランの金額 | 
**currency** | **str** | 3文字のISOコード(現状 &#39;jpy&#39; のみサポート) | 
**interval** | **str** |  | 
**name** | **str** |  | 
**trial_days** | **int** | トライアル日数(0-365) | 
**billing_day** | **int** |  | [optional] 

## Example

```python
from payjpv2.models.plan_response import PlanResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlanResponse from a JSON string
plan_response_instance = PlanResponse.from_json(json)
# print the JSON string representation of the object
print(PlanResponse.to_json())

# convert the object into a dict
plan_response_dict = plan_response_instance.to_dict()
# create an instance of PlanResponse from a dict
plan_response_from_dict = PlanResponse.from_dict(plan_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


