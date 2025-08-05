# LineItemAdjustableQuantityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | 数量が任意の 0 以上の整数に調整可能であれば、&#x60;true&#x60; を指定します。 | [optional] 
**maximum** | **int** | 顧客が Checkout Session で購入できる最大数量です。デフォルトではこの値は 99 です。999,999 までの値を指定できます。 | [optional] 
**minimum** | **int** | 顧客が Checkout Session で購入できる最小数量です。この値はデフォルトで 0 です。 | [optional] 

## Example

```python
from payjpv2.models.line_item_adjustable_quantity_request import LineItemAdjustableQuantityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LineItemAdjustableQuantityRequest from a JSON string
line_item_adjustable_quantity_request_instance = LineItemAdjustableQuantityRequest.from_json(json)
# print the JSON string representation of the object
print(LineItemAdjustableQuantityRequest.to_json())

# convert the object into a dict
line_item_adjustable_quantity_request_dict = line_item_adjustable_quantity_request_instance.to_dict()
# create an instance of LineItemAdjustableQuantityRequest from a dict
line_item_adjustable_quantity_request_from_dict = LineItemAdjustableQuantityRequest.from_dict(line_item_adjustable_quantity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


