# payjpv2.ElementsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_elements_sessions**](ElementsApi.md#get_elements_sessions) | **GET** /v2/elements/sessions | Get Elements Sessions


# **get_elements_sessions**
> ElementsSessionsResponse get_elements_sessions(client_secret, type, referrer_host=referrer_host, expand=expand)

Get Elements Sessions

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.elements_sessions_response import ElementsSessionsResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.ElementsApi(api_client)
    client_secret = 'client_secret_example' # str | クライアントシークレット
    type = 'type_example' # str | セッションのタイプ
    referrer_host = 'referrer_host_example' # str | リファラー (optional)
    expand = [] # List[str] | 拡張レスポンス (optional) (default to [])

    try:
        # Get Elements Sessions
        api_response = api_instance.get_elements_sessions(client_secret, type, referrer_host=referrer_host, expand=expand)
        print("The response of ElementsApi->get_elements_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ElementsApi->get_elements_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_secret** | **str**| クライアントシークレット | 
 **type** | **str**| セッションのタイプ | 
 **referrer_host** | **str**| リファラー | [optional] 
 **expand** | [**List[str]**](str.md)| 拡張レスポンス | [optional] [default to []]

### Return type

[**ElementsSessionsResponse**](ElementsSessionsResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

