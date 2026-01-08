# payjpv2.CheckoutSessionsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_checkout_session**](CheckoutSessionsApi.md#create_checkout_session) | **POST** /v2/checkout/sessions | Create Checkout Session
[**get_all_checkout_session_line_items**](CheckoutSessionsApi.md#get_all_checkout_session_line_items) | **GET** /v2/checkout/sessions/{checkout_session_id}/line_items | Get All Checkout Session Line Items
[**get_all_checkout_sessions**](CheckoutSessionsApi.md#get_all_checkout_sessions) | **GET** /v2/checkout/sessions | Get All Checkout Sessions
[**get_checkout_session**](CheckoutSessionsApi.md#get_checkout_session) | **GET** /v2/checkout/sessions/{checkout_session_id} | Get Checkout Session
[**update_checkout_session**](CheckoutSessionsApi.md#update_checkout_session) | **POST** /v2/checkout/sessions/{checkout_session_id} | Update Checkout Session


# **create_checkout_session**
> CheckoutSessionDetailsResponse create_checkout_session(checkout_session_create_request)

Create Checkout Session

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.checkout_session_create_request import CheckoutSessionCreateRequest
from payjpv2.models.checkout_session_details_response import CheckoutSessionDetailsResponse
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
    api_instance = payjpv2.CheckoutSessionsApi(api_client)
    checkout_session_create_request = payjpv2.CheckoutSessionCreateRequest() # CheckoutSessionCreateRequest | 

    try:
        # Create Checkout Session
        api_response = api_instance.create_checkout_session(checkout_session_create_request)
        print("The response of CheckoutSessionsApi->create_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutSessionsApi->create_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_create_request** | [**CheckoutSessionCreateRequest**](CheckoutSessionCreateRequest.md)|  | 

### Return type

[**CheckoutSessionDetailsResponse**](CheckoutSessionDetailsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_checkout_session_line_items**
> CheckoutSessionLineItemListResponse get_all_checkout_session_line_items(checkout_session_id, limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Checkout Session Line Items

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.checkout_session_line_item_list_response import CheckoutSessionLineItemListResponse
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
    api_instance = payjpv2.CheckoutSessionsApi(api_client)
    checkout_session_id = 'checkout_session_id_example' # str | 
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Checkout Session Line Items
        api_response = api_instance.get_all_checkout_session_line_items(checkout_session_id, limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of CheckoutSessionsApi->get_all_checkout_session_line_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutSessionsApi->get_all_checkout_session_line_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**CheckoutSessionLineItemListResponse**](CheckoutSessionLineItemListResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_checkout_sessions**
> CheckoutSessionListResponse get_all_checkout_sessions(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Checkout Sessions

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.checkout_session_list_response import CheckoutSessionListResponse
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
    api_instance = payjpv2.CheckoutSessionsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Checkout Sessions
        api_response = api_instance.get_all_checkout_sessions(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of CheckoutSessionsApi->get_all_checkout_sessions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutSessionsApi->get_all_checkout_sessions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**CheckoutSessionListResponse**](CheckoutSessionListResponse.md)

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

# **get_checkout_session**
> CheckoutSessionDetailsResponse get_checkout_session(checkout_session_id)

Get Checkout Session

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.checkout_session_details_response import CheckoutSessionDetailsResponse
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
    api_instance = payjpv2.CheckoutSessionsApi(api_client)
    checkout_session_id = 'checkout_session_id_example' # str | 

    try:
        # Get Checkout Session
        api_response = api_instance.get_checkout_session(checkout_session_id)
        print("The response of CheckoutSessionsApi->get_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutSessionsApi->get_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 

### Return type

[**CheckoutSessionDetailsResponse**](CheckoutSessionDetailsResponse.md)

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

# **update_checkout_session**
> CheckoutSessionDetailsResponse update_checkout_session(checkout_session_id, checkout_session_update_request)

Update Checkout Session

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.checkout_session_details_response import CheckoutSessionDetailsResponse
from payjpv2.models.checkout_session_update_request import CheckoutSessionUpdateRequest
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
    api_instance = payjpv2.CheckoutSessionsApi(api_client)
    checkout_session_id = 'checkout_session_id_example' # str | 
    checkout_session_update_request = payjpv2.CheckoutSessionUpdateRequest() # CheckoutSessionUpdateRequest | 

    try:
        # Update Checkout Session
        api_response = api_instance.update_checkout_session(checkout_session_id, checkout_session_update_request)
        print("The response of CheckoutSessionsApi->update_checkout_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CheckoutSessionsApi->update_checkout_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **checkout_session_id** | **str**|  | 
 **checkout_session_update_request** | [**CheckoutSessionUpdateRequest**](CheckoutSessionUpdateRequest.md)|  | 

### Return type

[**CheckoutSessionDetailsResponse**](CheckoutSessionDetailsResponse.md)

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
**400** | Metadata Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

