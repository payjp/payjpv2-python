# RefundListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[RefundResponse]**](RefundResponse.md) | 支払いインテントリスト | 

## Example

```python
from payjpv2.models.refund_list_response import RefundListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RefundListResponse from a JSON string
refund_list_response_instance = RefundListResponse.from_json(json)
# print the JSON string representation of the object
print(RefundListResponse.to_json())

# convert the object into a dict
refund_list_response_dict = refund_list_response_instance.to_dict()
# create an instance of RefundListResponse from a dict
refund_list_response_from_dict = RefundListResponse.from_dict(refund_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


