# RedirectOptionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_client_secret** | **bool** | return_url へリダイレクトする際、クエリパラメーターに client_secret を付与するかどうか。デフォルトは &#x60;true&#x60; です。 | [optional] 

## Example

```python
from payjpv2.models.redirect_options_request import RedirectOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectOptionsRequest from a JSON string
redirect_options_request_instance = RedirectOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(RedirectOptionsRequest.to_json())

# convert the object into a dict
redirect_options_request_dict = redirect_options_request_instance.to_dict()
# create an instance of RedirectOptionsRequest from a dict
redirect_options_request_from_dict = RedirectOptionsRequest.from_dict(redirect_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


