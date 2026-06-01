# PriceDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | [**Currency**](Currency.md) | 通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | 
**unit_amount** | **int** | 単価（0以上の整数） | 
**product_id** | **str** |  | [optional] 
**product_data** | [**ProductDataRequest**](ProductDataRequest.md) |  | [optional] 

## Example

```python
from payjpv2.models.price_data_request import PriceDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PriceDataRequest from a JSON string
price_data_request_instance = PriceDataRequest.from_json(json)
# print the JSON string representation of the object
print(PriceDataRequest.to_json())

# convert the object into a dict
price_data_request_dict = price_data_request_instance.to_dict()
# create an instance of PriceDataRequest from a dict
price_data_request_from_dict = PriceDataRequest.from_dict(price_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


