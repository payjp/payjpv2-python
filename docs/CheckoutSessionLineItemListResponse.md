# CheckoutSessionLineItemListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[CheckoutSessionLineItemDataResponse]**](CheckoutSessionLineItemDataResponse.md) |  | 

## Example

```python
from payjpv2.models.checkout_session_line_item_list_response import CheckoutSessionLineItemListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionLineItemListResponse from a JSON string
checkout_session_line_item_list_response_instance = CheckoutSessionLineItemListResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionLineItemListResponse.to_json())

# convert the object into a dict
checkout_session_line_item_list_response_dict = checkout_session_line_item_list_response_instance.to_dict()
# create an instance of CheckoutSessionLineItemListResponse from a dict
checkout_session_line_item_list_response_from_dict = CheckoutSessionLineItemListResponse.from_dict(checkout_session_line_item_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


