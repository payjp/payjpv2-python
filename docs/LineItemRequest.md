# LineItemRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_id** | **str** | 料金 ID | 
**quantity** | **int** | 購入する商品の数量 | 
**tax_rates** | **List[str]** | 税率 ID | [optional] [default to []]

## Example

```python
from payjpv2.models.line_item_request import LineItemRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemRequest from a JSON string
line_item_request_instance = LineItemRequest.from_json(json)
# print the JSON string representation of the object
print(LineItemRequest.to_json())

# convert the object into a dict
line_item_request_dict = line_item_request_instance.to_dict()
# create an instance of LineItemRequest from a dict
line_item_request_from_dict = LineItemRequest.from_dict(line_item_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


