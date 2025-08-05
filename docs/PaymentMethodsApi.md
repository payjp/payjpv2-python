# payjpv2.PaymentMethodsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_method**](PaymentMethodsApi.md#create_payment_method) | **POST** /v2/payment_methods | Create Payment Method
[**get_all_payment_methods**](PaymentMethodsApi.md#get_all_payment_methods) | **GET** /v2/payment_methods | Get All Payment Methods
[**get_payment_method**](PaymentMethodsApi.md#get_payment_method) | **GET** /v2/payment_methods/{payment_method_id} | Get Payment Method
[**update_payment_method**](PaymentMethodsApi.md#update_payment_method) | **POST** /v2/payment_methods/{payment_method_id} | Update Payment Method


# **create_payment_method**
> PaymentMethodResponse create_payment_method(payment_method_create_request)

Create Payment Method

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.payment_method_create_request import PaymentMethodCreateRequest
from payjpv2.models.payment_method_response import PaymentMethodResponse
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_create_request = payjpv2.PaymentMethodCreateRequest() # PaymentMethodCreateRequest | 

    try:
        # Create Payment Method
        api_response = api_instance.create_payment_method(payment_method_create_request)
        print("The response of PaymentMethodsApi->create_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->create_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_create_request** | [**PaymentMethodCreateRequest**](PaymentMethodCreateRequest.md)|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_methods**
> PaymentMethodListResponse get_all_payment_methods(limit=limit, offset=offset)

Get All Payment Methods

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.payment_method_list_response import PaymentMethodListResponse
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    offset = 0 # int | データ取得を行う開始位置 (optional) (default to 0)

    try:
        # Get All Payment Methods
        api_response = api_instance.get_all_payment_methods(limit=limit, offset=offset)
        print("The response of PaymentMethodsApi->get_all_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_all_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **offset** | **int**| データ取得を行う開始位置 | [optional] [default to 0]

### Return type

[**PaymentMethodListResponse**](PaymentMethodListResponse.md)

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

# **get_payment_method**
> PaymentMethodResponse get_payment_method(payment_method_id)

Get Payment Method

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.payment_method_response import PaymentMethodResponse
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_id = 'payment_method_id_example' # str | 

    try:
        # Get Payment Method
        api_response = api_instance.get_payment_method(payment_method_id)
        print("The response of PaymentMethodsApi->get_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

# **update_payment_method**
> PaymentMethodResponse update_payment_method(payment_method_id, payment_method_card_update_request)

Update Payment Method

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.payment_method_card_update_request import PaymentMethodCardUpdateRequest
from payjpv2.models.payment_method_response import PaymentMethodResponse
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_id = 'payment_method_id_example' # str | 
    payment_method_card_update_request = payjpv2.PaymentMethodCardUpdateRequest() # PaymentMethodCardUpdateRequest | 

    try:
        # Update Payment Method
        api_response = api_instance.update_payment_method(payment_method_id, payment_method_card_update_request)
        print("The response of PaymentMethodsApi->update_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->update_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **payment_method_card_update_request** | [**PaymentMethodCardUpdateRequest**](PaymentMethodCardUpdateRequest.md)|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

