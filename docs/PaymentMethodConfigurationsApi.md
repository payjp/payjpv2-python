# payjpv2.PaymentMethodConfigurationsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_payment_method_configurations**](PaymentMethodConfigurationsApi.md#get_all_payment_method_configurations) | **GET** /v2/payment_method_configurations | Get All Payment Method Configurations
[**get_payment_method_configuration**](PaymentMethodConfigurationsApi.md#get_payment_method_configuration) | **GET** /v2/payment_method_configurations/{payment_method_configuration_id} | Get Payment Method Configuration
[**update_payment_method_configuration**](PaymentMethodConfigurationsApi.md#update_payment_method_configuration) | **POST** /v2/payment_method_configurations/{payment_method_configuration_id} | Update Payment Method Configuration


# **get_all_payment_method_configurations**
> PaymentMethodConfigurationListResponse get_all_payment_method_configurations(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Payment Method Configurations

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_method_configuration_list_response import PaymentMethodConfigurationListResponse
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
    api_instance = payjpv2.PaymentMethodConfigurationsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Payment Method Configurations
        api_response = api_instance.get_all_payment_method_configurations(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of PaymentMethodConfigurationsApi->get_all_payment_method_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodConfigurationsApi->get_all_payment_method_configurations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**PaymentMethodConfigurationListResponse**](PaymentMethodConfigurationListResponse.md)

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

# **get_payment_method_configuration**
> PaymentMethodConfigurationDetailsResponse get_payment_method_configuration(payment_method_configuration_id)

Get Payment Method Configuration

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_method_configuration_details_response import PaymentMethodConfigurationDetailsResponse
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
    api_instance = payjpv2.PaymentMethodConfigurationsApi(api_client)
    payment_method_configuration_id = 'payment_method_configuration_id_example' # str | 

    try:
        # Get Payment Method Configuration
        api_response = api_instance.get_payment_method_configuration(payment_method_configuration_id)
        print("The response of PaymentMethodConfigurationsApi->get_payment_method_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodConfigurationsApi->get_payment_method_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_configuration_id** | **str**|  | 

### Return type

[**PaymentMethodConfigurationDetailsResponse**](PaymentMethodConfigurationDetailsResponse.md)

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

# **update_payment_method_configuration**
> PaymentMethodConfigurationDetailsResponse update_payment_method_configuration(payment_method_configuration_id, payment_method_configuration_update_request)

Update Payment Method Configuration

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_method_configuration_details_response import PaymentMethodConfigurationDetailsResponse
from payjpv2.models.payment_method_configuration_update_request import PaymentMethodConfigurationUpdateRequest
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
    api_instance = payjpv2.PaymentMethodConfigurationsApi(api_client)
    payment_method_configuration_id = 'payment_method_configuration_id_example' # str | 
    payment_method_configuration_update_request = payjpv2.PaymentMethodConfigurationUpdateRequest() # PaymentMethodConfigurationUpdateRequest | 

    try:
        # Update Payment Method Configuration
        api_response = api_instance.update_payment_method_configuration(payment_method_configuration_id, payment_method_configuration_update_request)
        print("The response of PaymentMethodConfigurationsApi->update_payment_method_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentMethodConfigurationsApi->update_payment_method_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_method_configuration_id** | **str**|  | 
 **payment_method_configuration_update_request** | [**PaymentMethodConfigurationUpdateRequest**](PaymentMethodConfigurationUpdateRequest.md)|  | 

### Return type

[**PaymentMethodConfigurationDetailsResponse**](PaymentMethodConfigurationDetailsResponse.md)

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

