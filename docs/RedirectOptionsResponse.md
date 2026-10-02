# RedirectOptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_client_secret** | **bool** | return_url へリダイレクトする際、クエリパラメーターに client_secret を付与するかどうか。デフォルトは &#x60;true&#x60; です。 | [optional] [default to True]

## Example

```python
from payjpv2.models.redirect_options_response import RedirectOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RedirectOptionsResponse from a JSON string
redirect_options_response_instance = RedirectOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(RedirectOptionsResponse.to_json())

# convert the object into a dict
redirect_options_response_dict = redirect_options_response_instance.to_dict()
# create an instance of RedirectOptionsResponse from a dict
redirect_options_response_from_dict = RedirectOptionsResponse.from_dict(redirect_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


