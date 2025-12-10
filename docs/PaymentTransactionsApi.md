# payjpv2.PaymentTransactionsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_payment_transactions**](PaymentTransactionsApi.md#get_all_payment_transactions) | **GET** /v2/payment_transactions | Get All Payment Transactions
[**get_payment_transaction**](PaymentTransactionsApi.md#get_payment_transaction) | **GET** /v2/payment_transactions/{payment_transaction_id} | Get Payment Transaction


# **get_all_payment_transactions**
> PaymentTransactionListResponse get_all_payment_transactions(limit=limit, starting_after=starting_after, ending_before=ending_before, term_id=term_id, type=type, payment_method_type=payment_method_type)

Get All Payment Transactions

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_transaction_list_response import PaymentTransactionListResponse
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
    api_instance = payjpv2.PaymentTransactionsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    term_id = 'term_id_example' # str | term ID (optional)
    type = 'type_example' # str | 取引タイプ (optional)
    payment_method_type = 'payment_method_type_example' # str | 支払い方法タイプ (optional)

    try:
        # Get All Payment Transactions
        api_response = api_instance.get_all_payment_transactions(limit=limit, starting_after=starting_after, ending_before=ending_before, term_id=term_id, type=type, payment_method_type=payment_method_type)
        print("The response of PaymentTransactionsApi->get_all_payment_transactions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTransactionsApi->get_all_payment_transactions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **term_id** | **str**| term ID | [optional] 
 **type** | **str**| 取引タイプ | [optional] 
 **payment_method_type** | **str**| 支払い方法タイプ | [optional] 

### Return type

[**PaymentTransactionListResponse**](PaymentTransactionListResponse.md)

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

# **get_payment_transaction**
> PaymentTransactionResponse get_payment_transaction(payment_transaction_id)

Get Payment Transaction

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.payment_transaction_response import PaymentTransactionResponse
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
    api_instance = payjpv2.PaymentTransactionsApi(api_client)
    payment_transaction_id = 'payment_transaction_id_example' # str | 

    try:
        # Get Payment Transaction
        api_response = api_instance.get_payment_transaction(payment_transaction_id)
        print("The response of PaymentTransactionsApi->get_payment_transaction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentTransactionsApi->get_payment_transaction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_transaction_id** | **str**|  | 

### Return type

[**PaymentTransactionResponse**](PaymentTransactionResponse.md)

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

