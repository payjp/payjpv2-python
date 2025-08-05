# CheckoutSessionLineItemsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**data** | [**List[CheckoutSessionLineItemDataResponse]**](CheckoutSessionLineItemDataResponse.md) | データ | [optional] 
**has_more** | **bool** | 次のページがあるかどうか | [optional] [default to False]
**url** | **str** | URL | [optional] 

## Example

```python
from payjpv2.models.checkout_session_line_items_response import CheckoutSessionLineItemsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionLineItemsResponse from a JSON string
checkout_session_line_items_response_instance = CheckoutSessionLineItemsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionLineItemsResponse.to_json())

# convert the object into a dict
checkout_session_line_items_response_dict = checkout_session_line_items_response_instance.to_dict()
# create an instance of CheckoutSessionLineItemsResponse from a dict
checkout_session_line_items_response_from_dict = CheckoutSessionLineItemsResponse.from_dict(checkout_session_line_items_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


