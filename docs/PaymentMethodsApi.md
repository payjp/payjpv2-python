# payjpv2.PaymentMethodsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_payment_method**](PaymentMethodsApi.md#attach_payment_method) | **POST** /v2/payment_methods/{payment_method_id}/attach | Attach Payment Method
[**create_payment_method**](PaymentMethodsApi.md#create_payment_method) | **POST** /v2/payment_methods | Create Payment Method
[**detach_payment_method**](PaymentMethodsApi.md#detach_payment_method) | **POST** /v2/payment_methods/{payment_method_id}/detach | Detach Payment Method
[**get_all_payment_methods**](PaymentMethodsApi.md#get_all_payment_methods) | **GET** /v2/payment_methods | Get All Payment Methods
[**get_payment_method**](PaymentMethodsApi.md#get_payment_method) | **GET** /v2/payment_methods/{payment_method_id} | Get Payment Method
[**get_payment_method_by_card**](PaymentMethodsApi.md#get_payment_method_by_card) | **GET** /v2/payment_methods/cards/{card_id} | Get Payment Method By Card
[**update_payment_method**](PaymentMethodsApi.md#update_payment_method) | **POST** /v2/payment_methods/{payment_method_id} | Update Payment Method


# **attach_payment_method**
> PaymentMethodResponse attach_payment_method(payment_method_id, payment_method_attach_request)

Attach Payment Method

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_method_attach_request import PaymentMethodAttachRequest
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_id = 'payment_method_id_example' # str | 
    payment_method_attach_request = payjpv2.PaymentMethodAttachRequest() # PaymentMethodAttachRequest | 

    try:
        # Attach Payment Method
        api_response = api_instance.attach_payment_method(payment_method_id, payment_method_attach_request)
        print("The response of PaymentMethodsApi->attach_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->attach_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **payment_method_attach_request** | [**PaymentMethodAttachRequest**](PaymentMethodAttachRequest.md)|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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
**400** | Payment Method Already Attached&lt;br&gt;Payment Method Customer Mismatch&lt;br&gt;Unsupported Payment Method Type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_method**
> PaymentMethodResponse create_payment_method(payment_method_create_request)

Create Payment Method

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

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

# **detach_payment_method**
> PaymentMethodResponse detach_payment_method(payment_method_id)

Detach Payment Method

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_id = 'payment_method_id_example' # str | 

    try:
        # Detach Payment Method
        api_response = api_instance.detach_payment_method(payment_method_id)
        print("The response of PaymentMethodsApi->detach_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->detach_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

# **get_all_payment_methods**
> PaymentMethodListResponse get_all_payment_methods(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Payment Methods

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Payment Methods
        api_response = api_instance.get_all_payment_methods(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of PaymentMethodsApi->get_all_payment_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_all_payment_methods: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**PaymentMethodListResponse**](PaymentMethodListResponse.md)

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

# **get_payment_method**
> PaymentMethodResponse get_payment_method(payment_method_id)

Get Payment Method

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

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

# **get_payment_method_by_card**
> PaymentMethodResponse get_payment_method_by_card(card_id)

Get Payment Method By Card

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    card_id = 'card_id_example' # str | 

    try:
        # Get Payment Method By Card
        api_response = api_instance.get_payment_method_by_card(card_id)
        print("The response of PaymentMethodsApi->get_payment_method_by_card:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->get_payment_method_by_card: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **card_id** | **str**|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

# **update_payment_method**
> PaymentMethodResponse update_payment_method(payment_method_id, payment_method_update_request)

Update Payment Method

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_method_response import PaymentMethodResponse
from payjpv2.models.payment_method_update_request import PaymentMethodUpdateRequest
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
    api_instance = payjpv2.PaymentMethodsApi(api_client)
    payment_method_id = 'payment_method_id_example' # str | 
    payment_method_update_request = payjpv2.PaymentMethodUpdateRequest() # PaymentMethodUpdateRequest | 

    try:
        # Update Payment Method
        api_response = api_instance.update_payment_method(payment_method_id, payment_method_update_request)
        print("The response of PaymentMethodsApi->update_payment_method:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodsApi->update_payment_method: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_id** | **str**|  | 
 **payment_method_update_request** | [**PaymentMethodUpdateRequest**](PaymentMethodUpdateRequest.md)|  | 

### Return type

[**PaymentMethodResponse**](PaymentMethodResponse.md)

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

