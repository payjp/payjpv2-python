# payjpv2.SetupIntentsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_setup_intent**](SetupIntentsApi.md#cancel_setup_intent) | **POST** /v2/setup_intents/{setup_intent_id}/cancel | Cancel Setup Intent
[**confirm_setup_intent**](SetupIntentsApi.md#confirm_setup_intent) | **POST** /v2/setup_intents/{setup_intent_id}/confirm | Confirm Setup Intent
[**create_setup_intent**](SetupIntentsApi.md#create_setup_intent) | **POST** /v2/setup_intents | Create Setup Intent
[**get_all_setup_intent**](SetupIntentsApi.md#get_all_setup_intent) | **GET** /v2/setup_intents | Get All Setup Intent
[**retrieve_setup_intent**](SetupIntentsApi.md#retrieve_setup_intent) | **GET** /v2/setup_intents/{setup_intent_id} | Retrieve Setup Intent
[**update_setup_intent**](SetupIntentsApi.md#update_setup_intent) | **POST** /v2/setup_intents/{setup_intent_id} | Update Setup Intent


# **cancel_setup_intent**
> SetupIntentResponse cancel_setup_intent(setup_intent_id, setup_intent_cancel_request=setup_intent_cancel_request)

Cancel Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_cancel_request import SetupIntentCancelRequest
from payjpv2.models.setup_intent_response import SetupIntentResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    setup_intent_id = 'setup_intent_id_example' # str | 
    setup_intent_cancel_request = payjpv2.SetupIntentCancelRequest() # SetupIntentCancelRequest |  (optional)

    try:
        # Cancel Setup Intent
        api_response = api_instance.cancel_setup_intent(setup_intent_id, setup_intent_cancel_request=setup_intent_cancel_request)
        print("The response of SetupIntentsApi->cancel_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->cancel_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_intent_id** | **str**|  | 
 **setup_intent_cancel_request** | [**SetupIntentCancelRequest**](SetupIntentCancelRequest.md)|  | [optional] 

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

# **confirm_setup_intent**
> SetupIntentResponse confirm_setup_intent(setup_intent_id, setup_intent_confirm_request=setup_intent_confirm_request)

Confirm Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_confirm_request import SetupIntentConfirmRequest
from payjpv2.models.setup_intent_response import SetupIntentResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    setup_intent_id = 'setup_intent_id_example' # str | 
    setup_intent_confirm_request = payjpv2.SetupIntentConfirmRequest() # SetupIntentConfirmRequest |  (optional)

    try:
        # Confirm Setup Intent
        api_response = api_instance.confirm_setup_intent(setup_intent_id, setup_intent_confirm_request=setup_intent_confirm_request)
        print("The response of SetupIntentsApi->confirm_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->confirm_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_intent_id** | **str**|  | 
 **setup_intent_confirm_request** | [**SetupIntentConfirmRequest**](SetupIntentConfirmRequest.md)|  | [optional] 

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**404** | Not Found |  -  |
**400** | Invalid Status&lt;br&gt;Missing Payment Method |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_setup_intent**
> SetupIntentResponse create_setup_intent(setup_intent_create_request=setup_intent_create_request)

Create Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_create_request import SetupIntentCreateRequest
from payjpv2.models.setup_intent_response import SetupIntentResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    setup_intent_create_request = payjpv2.SetupIntentCreateRequest() # SetupIntentCreateRequest |  (optional)

    try:
        # Create Setup Intent
        api_response = api_instance.create_setup_intent(setup_intent_create_request=setup_intent_create_request)
        print("The response of SetupIntentsApi->create_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->create_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_intent_create_request** | [**SetupIntentCreateRequest**](SetupIntentCreateRequest.md)|  | [optional] 

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

# **get_all_setup_intent**
> SetupIntentListResponse get_all_setup_intent(limit=limit, offset=offset)

Get All Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_list_response import SetupIntentListResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    offset = 0 # int | データ取得を行う開始位置 (optional) (default to 0)

    try:
        # Get All Setup Intent
        api_response = api_instance.get_all_setup_intent(limit=limit, offset=offset)
        print("The response of SetupIntentsApi->get_all_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->get_all_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **offset** | **int**| データ取得を行う開始位置 | [optional] [default to 0]

### Return type

[**SetupIntentListResponse**](SetupIntentListResponse.md)

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

# **retrieve_setup_intent**
> SetupIntentResponse retrieve_setup_intent(setup_intent_id)

Retrieve Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_response import SetupIntentResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    setup_intent_id = 'setup_intent_id_example' # str | 

    try:
        # Retrieve Setup Intent
        api_response = api_instance.retrieve_setup_intent(setup_intent_id)
        print("The response of SetupIntentsApi->retrieve_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->retrieve_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_intent_id** | **str**|  | 

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_setup_intent**
> SetupIntentResponse update_setup_intent(setup_intent_id, setup_intent_update_request)

Update Setup Intent

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.setup_intent_response import SetupIntentResponse
from payjpv2.models.setup_intent_update_request import SetupIntentUpdateRequest
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.SetupIntentsApi(api_client)
    setup_intent_id = 'setup_intent_id_example' # str | 
    setup_intent_update_request = payjpv2.SetupIntentUpdateRequest() # SetupIntentUpdateRequest | 

    try:
        # Update Setup Intent
        api_response = api_instance.update_setup_intent(setup_intent_id, setup_intent_update_request)
        print("The response of SetupIntentsApi->update_setup_intent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SetupIntentsApi->update_setup_intent: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setup_intent_id** | **str**|  | 
 **setup_intent_update_request** | [**SetupIntentUpdateRequest**](SetupIntentUpdateRequest.md)|  | 

### Return type

[**SetupIntentResponse**](SetupIntentResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

