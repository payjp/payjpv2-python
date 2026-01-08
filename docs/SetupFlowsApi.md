# payjpv2.SetupFlowsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_setup_flow**](SetupFlowsApi.md#cancel_setup_flow) | **POST** /v2/setup_flows/{setup_flow_id}/cancel | Cancel Setup Flow
[**create_setup_flow**](SetupFlowsApi.md#create_setup_flow) | **POST** /v2/setup_flows | Create Setup Flow
[**get_all_setup_flows**](SetupFlowsApi.md#get_all_setup_flows) | **GET** /v2/setup_flows | Get All Setup Flows
[**get_setup_flow**](SetupFlowsApi.md#get_setup_flow) | **GET** /v2/setup_flows/{setup_flow_id} | Get Setup Flow
[**update_setup_flow**](SetupFlowsApi.md#update_setup_flow) | **POST** /v2/setup_flows/{setup_flow_id} | Update Setup Flow


# **cancel_setup_flow**
> SetupFlowResponse cancel_setup_flow(setup_flow_id, setup_flow_cancel_request=setup_flow_cancel_request)

Cancel Setup Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.setup_flow_cancel_request import SetupFlowCancelRequest
from payjpv2.models.setup_flow_response import SetupFlowResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pay.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "https://api.pay.jp"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = payjpv2.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = payjpv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupFlowsApi(api_client)
    setup_flow_id = 'setup_flow_id_example' # str | 
    setup_flow_cancel_request = payjpv2.SetupFlowCancelRequest() # SetupFlowCancelRequest |  (optional)

    try:
        # Cancel Setup Flow
        api_response = api_instance.cancel_setup_flow(setup_flow_id, setup_flow_cancel_request=setup_flow_cancel_request)
        print("The response of SetupFlowsApi->cancel_setup_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupFlowsApi->cancel_setup_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_flow_id** | **str**|  | 
 **setup_flow_cancel_request** | [**SetupFlowCancelRequest**](SetupFlowCancelRequest.md)|  | [optional] 

### Return type

[**SetupFlowResponse**](SetupFlowResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |
**400** | Invalid Status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_setup_flow**
> SetupFlowResponse create_setup_flow(setup_flow_create_request=setup_flow_create_request)

Create Setup Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.setup_flow_create_request import SetupFlowCreateRequest
from payjpv2.models.setup_flow_response import SetupFlowResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pay.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "https://api.pay.jp"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = payjpv2.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = payjpv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupFlowsApi(api_client)
    setup_flow_create_request = payjpv2.SetupFlowCreateRequest() # SetupFlowCreateRequest |  (optional)

    try:
        # Create Setup Flow
        api_response = api_instance.create_setup_flow(setup_flow_create_request=setup_flow_create_request)
        print("The response of SetupFlowsApi->create_setup_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupFlowsApi->create_setup_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_flow_create_request** | [**SetupFlowCreateRequest**](SetupFlowCreateRequest.md)|  | [optional] 

### Return type

[**SetupFlowResponse**](SetupFlowResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |
**400** | Detached Payment Method Not Usable&lt;br&gt;Unsupported Payment Method Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_setup_flows**
> SetupFlowListResponse get_all_setup_flows(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Setup Flows

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.setup_flow_list_response import SetupFlowListResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pay.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "https://api.pay.jp"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = payjpv2.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = payjpv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupFlowsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Setup Flows
        api_response = api_instance.get_all_setup_flows(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of SetupFlowsApi->get_all_setup_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupFlowsApi->get_all_setup_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**SetupFlowListResponse**](SetupFlowListResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**400** | Resource Missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_setup_flow**
> SetupFlowResponse get_setup_flow(setup_flow_id)

Get Setup Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.setup_flow_response import SetupFlowResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pay.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "https://api.pay.jp"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = payjpv2.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = payjpv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupFlowsApi(api_client)
    setup_flow_id = 'setup_flow_id_example' # str | 

    try:
        # Get Setup Flow
        api_response = api_instance.get_setup_flow(setup_flow_id)
        print("The response of SetupFlowsApi->get_setup_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupFlowsApi->get_setup_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_flow_id** | **str**|  | 

### Return type

[**SetupFlowResponse**](SetupFlowResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setup_flow**
> SetupFlowResponse update_setup_flow(setup_flow_id, setup_flow_update_request)

Update Setup Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.setup_flow_response import SetupFlowResponse
from payjpv2.models.setup_flow_update_request import SetupFlowUpdateRequest
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.pay.jp
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "https://api.pay.jp"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = payjpv2.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure Bearer authorization: HTTPBearer
configuration = payjpv2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupFlowsApi(api_client)
    setup_flow_id = 'setup_flow_id_example' # str | 
    setup_flow_update_request = payjpv2.SetupFlowUpdateRequest() # SetupFlowUpdateRequest | 

    try:
        # Update Setup Flow
        api_response = api_instance.update_setup_flow(setup_flow_id, setup_flow_update_request)
        print("The response of SetupFlowsApi->update_setup_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupFlowsApi->update_setup_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_flow_id** | **str**|  | 
 **setup_flow_update_request** | [**SetupFlowUpdateRequest**](SetupFlowUpdateRequest.md)|  | 

### Return type

[**SetupFlowResponse**](SetupFlowResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic), [HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |
**400** | Detached Payment Method Not Usable&lt;br&gt;Metadata Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

