# ProductDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Checkout などで顧客に表示される商品名 | 
**description** | **str** |  | [optional] 

## Example

```python
from payjpv2.models.product_data_request import ProductDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDataRequest from a JSON string
product_data_request_instance = ProductDataRequest.from_json(json)
# print the JSON string representation of the object
print(ProductDataRequest.to_json())

# convert the object into a dict
product_data_request_dict = product_data_request_instance.to_dict()
# create an instance of ProductDataRequest from a dict
product_data_request_from_dict = ProductDataRequest.from_dict(product_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


