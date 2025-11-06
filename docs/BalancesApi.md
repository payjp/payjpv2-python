# payjpv2.BalancesApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_balance_url**](BalancesApi.md#create_balance_url) | **POST** /v2/balances/{balance_id}/balance_urls | Create Balance Url
[**get_all_balances**](BalancesApi.md#get_all_balances) | **GET** /v2/balances | Get All Balances
[**retrieve_balance**](BalancesApi.md#retrieve_balance) | **GET** /v2/balances/{balance_id} | Retrieve Balance


# **create_balance_url**
> BalanceURLResponse create_balance_url(balance_id)

Create Balance Url

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.balance_url_response import BalanceURLResponse
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
    api_instance = payjpv2.BalancesApi(api_client)
    balance_id = 'balance_id_example' # str | 

    try:
        # Create Balance Url
        api_response = api_instance.create_balance_url(balance_id)
        print("The response of BalancesApi->create_balance_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancesApi->create_balance_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**|  | 

### Return type

[**BalanceURLResponse**](BalanceURLResponse.md)

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

# **get_all_balances**
> BalanceListResponse get_all_balances(since=since, until=until, limit=limit, starting_after=starting_after, ending_before=ending_before, state=state, closed=closed, since_due_date=since_due_date, until_due_date=until_due_date)

Get All Balances

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.balance_list_response import BalanceListResponse
from payjpv2.models.balance_state import BalanceState
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
    api_instance = payjpv2.BalancesApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以降のデータを取得 (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以前のデータを取得 (optional)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    state = payjpv2.BalanceState() # BalanceState | stateが指定した値であるオブジェクトに限定 (optional)
    closed = True # bool | closedが指定した値であるオブジェクトに限定 (optional)
    since_due_date = '2013-10-20T19:20:30+01:00' # datetime | 入金予定日/振込期限日が指定した日時以降のデータのみ取得 (optional)
    until_due_date = '2013-10-20T19:20:30+01:00' # datetime | 入金予定日/振込期限日が指定した日時以前のデータのみ取得 (optional)

    try:
        # Get All Balances
        api_response = api_instance.get_all_balances(since=since, until=until, limit=limit, starting_after=starting_after, ending_before=ending_before, state=state, closed=closed, since_due_date=since_due_date, until_due_date=until_due_date)
        print("The response of BalancesApi->get_all_balances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancesApi->get_all_balances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| 指定した日付以降のデータを取得 | [optional] 
 **until** | **datetime**| 指定した日付以前のデータを取得 | [optional] 
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **state** | [**BalanceState**](.md)| stateが指定した値であるオブジェクトに限定 | [optional] 
 **closed** | **bool**| closedが指定した値であるオブジェクトに限定 | [optional] 
 **since_due_date** | **datetime**| 入金予定日/振込期限日が指定した日時以降のデータのみ取得 | [optional] 
 **until_due_date** | **datetime**| 入金予定日/振込期限日が指定した日時以前のデータのみ取得 | [optional] 

### Return type

[**BalanceListResponse**](BalanceListResponse.md)

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

# **retrieve_balance**
> BalanceResponse retrieve_balance(balance_id)

Retrieve Balance

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.balance_response import BalanceResponse
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
    api_instance = payjpv2.BalancesApi(api_client)
    balance_id = 'balance_id_example' # str | 

    try:
        # Retrieve Balance
        api_response = api_instance.retrieve_balance(balance_id)
        print("The response of BalancesApi->retrieve_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancesApi->retrieve_balance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balance_id** | **str**|  | 

### Return type

[**BalanceResponse**](BalanceResponse.md)

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

