# payjpv2.TaxRatesApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tax_rate**](TaxRatesApi.md#create_tax_rate) | **POST** /v2/tax_rates | Create Tax Rate
[**get_all_tax_rates**](TaxRatesApi.md#get_all_tax_rates) | **GET** /v2/tax_rates | Get All Tax Rates
[**get_tax_rate**](TaxRatesApi.md#get_tax_rate) | **GET** /v2/tax_rates/{tax_rate_id} | Get Tax Rate
[**update_tax_rate**](TaxRatesApi.md#update_tax_rate) | **POST** /v2/tax_rates/{tax_rate_id} | Update Tax Rate


# **create_tax_rate**
> TaxRateDetailsResponse create_tax_rate(tax_rate_create_request)

Create Tax Rate

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.tax_rate_create_request import TaxRateCreateRequest
from payjpv2.models.tax_rate_details_response import TaxRateDetailsResponse
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
    api_instance = payjpv2.TaxRatesApi(api_client)
    tax_rate_create_request = payjpv2.TaxRateCreateRequest() # TaxRateCreateRequest | 

    try:
        # Create Tax Rate
        api_response = api_instance.create_tax_rate(tax_rate_create_request)
        print("The response of TaxRatesApi->create_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->create_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_create_request** | [**TaxRateCreateRequest**](TaxRateCreateRequest.md)|  | 

### Return type

[**TaxRateDetailsResponse**](TaxRateDetailsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_tax_rates**
> TaxRateListResponse get_all_tax_rates(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Tax Rates

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.tax_rate_list_response import TaxRateListResponse
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
    api_instance = payjpv2.TaxRatesApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Tax Rates
        api_response = api_instance.get_all_tax_rates(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of TaxRatesApi->get_all_tax_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->get_all_tax_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**TaxRateListResponse**](TaxRateListResponse.md)

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

# **get_tax_rate**
> TaxRateDetailsResponse get_tax_rate(tax_rate_id)

Get Tax Rate

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.tax_rate_details_response import TaxRateDetailsResponse
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
    api_instance = payjpv2.TaxRatesApi(api_client)
    tax_rate_id = 'tax_rate_id_example' # str | 

    try:
        # Get Tax Rate
        api_response = api_instance.get_tax_rate(tax_rate_id)
        print("The response of TaxRatesApi->get_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->get_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_id** | **str**|  | 

### Return type

[**TaxRateDetailsResponse**](TaxRateDetailsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tax_rate**
> TaxRateDetailsResponse update_tax_rate(tax_rate_id, tax_rate_update_request)

Update Tax Rate

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.tax_rate_details_response import TaxRateDetailsResponse
from payjpv2.models.tax_rate_update_request import TaxRateUpdateRequest
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
    api_instance = payjpv2.TaxRatesApi(api_client)
    tax_rate_id = 'tax_rate_id_example' # str | 
    tax_rate_update_request = payjpv2.TaxRateUpdateRequest() # TaxRateUpdateRequest | 

    try:
        # Update Tax Rate
        api_response = api_instance.update_tax_rate(tax_rate_id, tax_rate_update_request)
        print("The response of TaxRatesApi->update_tax_rate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaxRatesApi->update_tax_rate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_rate_id** | **str**|  | 
 **tax_rate_update_request** | [**TaxRateUpdateRequest**](TaxRateUpdateRequest.md)|  | 

### Return type

[**TaxRateDetailsResponse**](TaxRateDetailsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

