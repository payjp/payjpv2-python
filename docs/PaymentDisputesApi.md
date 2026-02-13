# payjpv2.PaymentDisputesApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_payment_disputes**](PaymentDisputesApi.md#get_all_payment_disputes) | **GET** /v2/payment_disputes | Get All Payment Disputes
[**get_payment_dispute**](PaymentDisputesApi.md#get_payment_dispute) | **GET** /v2/payment_disputes/{payment_dispute_id} | Get Payment Dispute


# **get_all_payment_disputes**
> PaymentDisputeListResponse get_all_payment_disputes(limit=limit, starting_after=starting_after, ending_before=ending_before, payment_flow_id=payment_flow_id, status=status)

Get All Payment Disputes

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_dispute_list_response import PaymentDisputeListResponse
from payjpv2.models.payment_dispute_status import PaymentDisputeStatus
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
    api_instance = payjpv2.PaymentDisputesApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    payment_flow_id = 'payment_flow_id_example' # str | 取得する payment_dispute に紐づく payment_flow の ID (optional)
    status = [payjpv2.PaymentDisputeStatus()] # List[PaymentDisputeStatus] | 取得する payment_dispute のステータス。複数指定可能 (optional)

    try:
        # Get All Payment Disputes
        api_response = api_instance.get_all_payment_disputes(limit=limit, starting_after=starting_after, ending_before=ending_before, payment_flow_id=payment_flow_id, status=status)
        print("The response of PaymentDisputesApi->get_all_payment_disputes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDisputesApi->get_all_payment_disputes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **payment_flow_id** | **str**| 取得する payment_dispute に紐づく payment_flow の ID | [optional] 
 **status** | [**List[PaymentDisputeStatus]**](PaymentDisputeStatus.md)| 取得する payment_dispute のステータス。複数指定可能 | [optional] 

### Return type

[**PaymentDisputeListResponse**](PaymentDisputeListResponse.md)

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

# **get_payment_dispute**
> PaymentDisputeResponse get_payment_dispute(payment_dispute_id)

Get Payment Dispute

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_dispute_response import PaymentDisputeResponse
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
    api_instance = payjpv2.PaymentDisputesApi(api_client)
    payment_dispute_id = 'payment_dispute_id_example' # str | 

    try:
        # Get Payment Dispute
        api_response = api_instance.get_payment_dispute(payment_dispute_id)
        print("The response of PaymentDisputesApi->get_payment_dispute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentDisputesApi->get_payment_dispute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_dispute_id** | **str**|  | 

### Return type

[**PaymentDisputeResponse**](PaymentDisputeResponse.md)

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

