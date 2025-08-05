# payjpv2.PricesApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price**](PricesApi.md#create_price) | **POST** /v2/prices | Create Price
[**get_all_prices**](PricesApi.md#get_all_prices) | **GET** /v2/prices | Get All Prices
[**get_price**](PricesApi.md#get_price) | **GET** /v2/prices/{price_id} | Get Price
[**update_price**](PricesApi.md#update_price) | **POST** /v2/prices/{price_id} | Update Price


# **create_price**
> PriceDetailsResponse create_price(price_create_request)

Create Price

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.price_create_request import PriceCreateRequest
from payjpv2.models.price_details_response import PriceDetailsResponse
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
    api_instance = payjpv2.PricesApi(api_client)
    price_create_request = payjpv2.PriceCreateRequest() # PriceCreateRequest | 

    try:
        # Create Price
        api_response = api_instance.create_price(price_create_request)
        print("The response of PricesApi->create_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->create_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_create_request** | [**PriceCreateRequest**](PriceCreateRequest.md)|  | 

### Return type

[**PriceDetailsResponse**](PriceDetailsResponse.md)

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

# **get_all_prices**
> PriceListResponse get_all_prices(limit=limit, offset=offset)

Get All Prices

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.price_list_response import PriceListResponse
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
    api_instance = payjpv2.PricesApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    offset = 0 # int | データ取得を行う開始位置 (optional) (default to 0)

    try:
        # Get All Prices
        api_response = api_instance.get_all_prices(limit=limit, offset=offset)
        print("The response of PricesApi->get_all_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_all_prices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **offset** | **int**| データ取得を行う開始位置 | [optional] [default to 0]

### Return type

[**PriceListResponse**](PriceListResponse.md)

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

# **get_price**
> PriceDetailsResponse get_price(price_id)

Get Price

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.price_details_response import PriceDetailsResponse
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
    api_instance = payjpv2.PricesApi(api_client)
    price_id = 'price_id_example' # str | 

    try:
        # Get Price
        api_response = api_instance.get_price(price_id)
        print("The response of PricesApi->get_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->get_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_id** | **str**|  | 

### Return type

[**PriceDetailsResponse**](PriceDetailsResponse.md)

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

# **update_price**
> PriceDetailsResponse update_price(price_id, price_update_request)

Update Price

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.price_details_response import PriceDetailsResponse
from payjpv2.models.price_update_request import PriceUpdateRequest
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
    api_instance = payjpv2.PricesApi(api_client)
    price_id = 'price_id_example' # str | 
    price_update_request = payjpv2.PriceUpdateRequest() # PriceUpdateRequest | 

    try:
        # Update Price
        api_response = api_instance.update_price(price_id, price_update_request)
        print("The response of PricesApi->update_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PricesApi->update_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **price_id** | **str**|  | 
 **price_update_request** | [**PriceUpdateRequest**](PriceUpdateRequest.md)|  | 

### Return type

[**PriceDetailsResponse**](PriceDetailsResponse.md)

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

