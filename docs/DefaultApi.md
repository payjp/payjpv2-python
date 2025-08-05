# payjpv2.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthcheck**](DefaultApi.md#healthcheck) | **GET** /.genki | Healthcheck


# **healthcheck**
> object healthcheck()

Healthcheck

### Example


```python
import payjpv2
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.DefaultApi(api_client)

    try:
        # Healthcheck
        api_response = api_instance.healthcheck()
        print("The response of DefaultApi->healthcheck:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->healthcheck: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

