# payjpv2.PaymentRefundsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_refund**](PaymentRefundsApi.md#create_payment_refund) | **POST** /v2/payment_refunds | Create Payment Refund
[**get_all_payment_refunds**](PaymentRefundsApi.md#get_all_payment_refunds) | **GET** /v2/payment_refunds | Get All Payment Refunds
[**get_payment_refund**](PaymentRefundsApi.md#get_payment_refund) | **GET** /v2/payment_refunds/{payment_refund_id} | Get Payment Refund
[**update_payment_refund**](PaymentRefundsApi.md#update_payment_refund) | **POST** /v2/payment_refunds/{payment_refund_id} | Update Payment Refund


# **create_payment_refund**
> PaymentRefundResponse create_payment_refund(payment_refund_create_request)

Create Payment Refund

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_refund_create_request import PaymentRefundCreateRequest
from payjpv2.models.payment_refund_response import PaymentRefundResponse
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
    api_instance = payjpv2.PaymentRefundsApi(api_client)
    payment_refund_create_request = payjpv2.PaymentRefundCreateRequest() # PaymentRefundCreateRequest | 

    try:
        # Create Payment Refund
        api_response = api_instance.create_payment_refund(payment_refund_create_request)
        print("The response of PaymentRefundsApi->create_payment_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRefundsApi->create_payment_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_refund_create_request** | [**PaymentRefundCreateRequest**](PaymentRefundCreateRequest.md)|  | 

### Return type

[**PaymentRefundResponse**](PaymentRefundResponse.md)

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
**400** | Invalid Status&lt;br&gt;Already Refunded&lt;br&gt;Refund Exceeds Payment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_refunds**
> PaymentRefundListResponse get_all_payment_refunds(limit=limit, starting_after=starting_after, ending_before=ending_before)

Get All Payment Refunds

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_refund_list_response import PaymentRefundListResponse
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
    api_instance = payjpv2.PaymentRefundsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get All Payment Refunds
        api_response = api_instance.get_all_payment_refunds(limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of PaymentRefundsApi->get_all_payment_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRefundsApi->get_all_payment_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 

### Return type

[**PaymentRefundListResponse**](PaymentRefundListResponse.md)

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

# **get_payment_refund**
> PaymentRefundResponse get_payment_refund(payment_refund_id)

Get Payment Refund

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_refund_response import PaymentRefundResponse
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
    api_instance = payjpv2.PaymentRefundsApi(api_client)
    payment_refund_id = 'payment_refund_id_example' # str | 

    try:
        # Get Payment Refund
        api_response = api_instance.get_payment_refund(payment_refund_id)
        print("The response of PaymentRefundsApi->get_payment_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRefundsApi->get_payment_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_refund_id** | **str**|  | 

### Return type

[**PaymentRefundResponse**](PaymentRefundResponse.md)

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

# **update_payment_refund**
> PaymentRefundResponse update_payment_refund(payment_refund_id, payment_refund_update_request)

Update Payment Refund

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_refund_response import PaymentRefundResponse
from payjpv2.models.payment_refund_update_request import PaymentRefundUpdateRequest
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
    api_instance = payjpv2.PaymentRefundsApi(api_client)
    payment_refund_id = 'payment_refund_id_example' # str | 
    payment_refund_update_request = payjpv2.PaymentRefundUpdateRequest() # PaymentRefundUpdateRequest | 

    try:
        # Update Payment Refund
        api_response = api_instance.update_payment_refund(payment_refund_id, payment_refund_update_request)
        print("The response of PaymentRefundsApi->update_payment_refund:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentRefundsApi->update_payment_refund: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_refund_id** | **str**|  | 
 **payment_refund_update_request** | [**PaymentRefundUpdateRequest**](PaymentRefundUpdateRequest.md)|  | 

### Return type

[**PaymentRefundResponse**](PaymentRefundResponse.md)

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

