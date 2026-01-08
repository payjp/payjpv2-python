# payjpv2.PaymentFlowsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_payment_flow**](PaymentFlowsApi.md#cancel_payment_flow) | **POST** /v2/payment_flows/{payment_flow_id}/cancel | Cancel Payment Flow
[**capture_payment_flow**](PaymentFlowsApi.md#capture_payment_flow) | **POST** /v2/payment_flows/{payment_flow_id}/capture | Capture Payment Flow
[**confirm_payment_flow**](PaymentFlowsApi.md#confirm_payment_flow) | **POST** /v2/payment_flows/{payment_flow_id}/confirm | Confirm Payment Flow
[**create_payment_flow**](PaymentFlowsApi.md#create_payment_flow) | **POST** /v2/payment_flows | Create Payment Flow
[**get_all_payment_flows**](PaymentFlowsApi.md#get_all_payment_flows) | **GET** /v2/payment_flows | Get All Payment Flows
[**get_payment_flow**](PaymentFlowsApi.md#get_payment_flow) | **GET** /v2/payment_flows/{payment_flow_id} | Get Payment Flow
[**get_payment_flow_refunds**](PaymentFlowsApi.md#get_payment_flow_refunds) | **GET** /v2/payment_flows/{payment_flow_id}/refunds | Get Payment Flow Refunds
[**update_payment_flow**](PaymentFlowsApi.md#update_payment_flow) | **POST** /v2/payment_flows/{payment_flow_id} | Update Payment Flow


# **cancel_payment_flow**
> PaymentFlowResponse cancel_payment_flow(payment_flow_id, payment_flow_cancel_request=payment_flow_cancel_request)

Cancel Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_cancel_request import PaymentFlowCancelRequest
from payjpv2.models.payment_flow_response import PaymentFlowResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 
    payment_flow_cancel_request = payjpv2.PaymentFlowCancelRequest() # PaymentFlowCancelRequest |  (optional)

    try:
        # Cancel Payment Flow
        api_response = api_instance.cancel_payment_flow(payment_flow_id, payment_flow_cancel_request=payment_flow_cancel_request)
        print("The response of PaymentFlowsApi->cancel_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->cancel_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 
 **payment_flow_cancel_request** | [**PaymentFlowCancelRequest**](PaymentFlowCancelRequest.md)|  | [optional] 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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

# **capture_payment_flow**
> PaymentFlowResponse capture_payment_flow(payment_flow_id, payment_flow_capture_request=payment_flow_capture_request)

Capture Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_capture_request import PaymentFlowCaptureRequest
from payjpv2.models.payment_flow_response import PaymentFlowResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 
    payment_flow_capture_request = payjpv2.PaymentFlowCaptureRequest() # PaymentFlowCaptureRequest |  (optional)

    try:
        # Capture Payment Flow
        api_response = api_instance.capture_payment_flow(payment_flow_id, payment_flow_capture_request=payment_flow_capture_request)
        print("The response of PaymentFlowsApi->capture_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->capture_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 
 **payment_flow_capture_request** | [**PaymentFlowCaptureRequest**](PaymentFlowCaptureRequest.md)|  | [optional] 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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

# **confirm_payment_flow**
> PaymentFlowResponse confirm_payment_flow(payment_flow_id, payment_flow_confirm_request=payment_flow_confirm_request)

Confirm Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_confirm_request import PaymentFlowConfirmRequest
from payjpv2.models.payment_flow_response import PaymentFlowResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 
    payment_flow_confirm_request = payjpv2.PaymentFlowConfirmRequest() # PaymentFlowConfirmRequest |  (optional)

    try:
        # Confirm Payment Flow
        api_response = api_instance.confirm_payment_flow(payment_flow_id, payment_flow_confirm_request=payment_flow_confirm_request)
        print("The response of PaymentFlowsApi->confirm_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->confirm_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 
 **payment_flow_confirm_request** | [**PaymentFlowConfirmRequest**](PaymentFlowConfirmRequest.md)|  | [optional] 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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
**400** | Invalid Status&lt;br&gt;Missing Payment Method&lt;br&gt;Detached Payment Method Not Usable&lt;br&gt;Payment Method Not Owned By Customer&lt;br&gt;Customer Required For Payment Method&lt;br&gt;Payment Method Type Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_payment_flow**
> PaymentFlowResponse create_payment_flow(payment_flow_create_request)

Create Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_create_request import PaymentFlowCreateRequest
from payjpv2.models.payment_flow_response import PaymentFlowResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_create_request = payjpv2.PaymentFlowCreateRequest() # PaymentFlowCreateRequest | 

    try:
        # Create Payment Flow
        api_response = api_instance.create_payment_flow(payment_flow_create_request)
        print("The response of PaymentFlowsApi->create_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->create_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_create_request** | [**PaymentFlowCreateRequest**](PaymentFlowCreateRequest.md)|  | 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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
**400** | Detached Payment Method Not Usable&lt;br&gt;Payment Method Not Owned By Customer&lt;br&gt;Payment Method Type Not Allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_payment_flows**
> PaymentFlowListResponse get_all_payment_flows(limit=limit, starting_after=starting_after, ending_before=ending_before, customer_id=customer_id)

Get All Payment Flows

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_list_response import PaymentFlowListResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    customer_id = 'customer_id_example' # str | 指定した顧客のデータのみを取得 (optional)

    try:
        # Get All Payment Flows
        api_response = api_instance.get_all_payment_flows(limit=limit, starting_after=starting_after, ending_before=ending_before, customer_id=customer_id)
        print("The response of PaymentFlowsApi->get_all_payment_flows:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->get_all_payment_flows: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **customer_id** | **str**| 指定した顧客のデータのみを取得 | [optional] 

### Return type

[**PaymentFlowListResponse**](PaymentFlowListResponse.md)

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

# **get_payment_flow**
> PaymentFlowResponse get_payment_flow(payment_flow_id)

Get Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_response import PaymentFlowResponse
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 

    try:
        # Get Payment Flow
        api_response = api_instance.get_payment_flow(payment_flow_id)
        print("The response of PaymentFlowsApi->get_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->get_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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

# **get_payment_flow_refunds**
> PaymentRefundListResponse get_payment_flow_refunds(payment_flow_id, limit=limit, starting_after=starting_after, ending_before=ending_before)

Get Payment Flow Refunds

Payment Flowに紐づくRefundsをリスト取得する

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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)

    try:
        # Get Payment Flow Refunds
        api_response = api_instance.get_payment_flow_refunds(payment_flow_id, limit=limit, starting_after=starting_after, ending_before=ending_before)
        print("The response of PaymentFlowsApi->get_payment_flow_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->get_payment_flow_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 
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
**404** | Not Found |  -  |
**400** | Resource Missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_flow**
> PaymentFlowResponse update_payment_flow(payment_flow_id, payment_flow_update_request)

Update Payment Flow

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_flow_response import PaymentFlowResponse
from payjpv2.models.payment_flow_update_request import PaymentFlowUpdateRequest
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
    api_instance = payjpv2.PaymentFlowsApi(api_client)
    payment_flow_id = 'payment_flow_id_example' # str | 
    payment_flow_update_request = payjpv2.PaymentFlowUpdateRequest() # PaymentFlowUpdateRequest | 

    try:
        # Update Payment Flow
        api_response = api_instance.update_payment_flow(payment_flow_id, payment_flow_update_request)
        print("The response of PaymentFlowsApi->update_payment_flow:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentFlowsApi->update_payment_flow: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_flow_id** | **str**|  | 
 **payment_flow_update_request** | [**PaymentFlowUpdateRequest**](PaymentFlowUpdateRequest.md)|  | 

### Return type

[**PaymentFlowResponse**](PaymentFlowResponse.md)

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
**400** | Invalid Status&lt;br&gt;Detached Payment Method Not Usable&lt;br&gt;Payment Method Not Owned By Customer&lt;br&gt;Payment Method Type Not Allowed&lt;br&gt;Metadata Limit Exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

