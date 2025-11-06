# payjpv2.TermsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_term**](TermsApi.md#get_all_term) | **GET** /v2/terms | Get All Term
[**retrieve_term**](TermsApi.md#retrieve_term) | **GET** /v2/terms/{term_id} | Retrieve Term


# **get_all_term**
> TermListResponse get_all_term(limit=limit, offset=offset, since_start_at=since_start_at, until_start_at=until_start_at)

Get All Term

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.term_list_response import TermListResponse
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
    api_instance = payjpv2.TermsApi(api_client)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    offset = 0 # int | データ取得を行う開始位置 (optional) (default to 0)
    since_start_at = '2013-10-20T19:20:30+01:00' # datetime | start_atが指定した日付以降のデータを取得 (optional)
    until_start_at = '2013-10-20T19:20:30+01:00' # datetime | start_atが指定した日付以前のデータを取得 (optional)

    try:
        # Get All Term
        api_response = api_instance.get_all_term(limit=limit, offset=offset, since_start_at=since_start_at, until_start_at=until_start_at)
        print("The response of TermsApi->get_all_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->get_all_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **offset** | **int**| データ取得を行う開始位置 | [optional] [default to 0]
 **since_start_at** | **datetime**| start_atが指定した日付以降のデータを取得 | [optional] 
 **until_start_at** | **datetime**| start_atが指定した日付以前のデータを取得 | [optional] 

### Return type

[**TermListResponse**](TermListResponse.md)

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

# **retrieve_term**
> TermResponse retrieve_term(term_id)

Retrieve Term

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.term_response import TermResponse
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
    api_instance = payjpv2.TermsApi(api_client)
    term_id = 'term_id_example' # str | 

    try:
        # Retrieve Term
        api_response = api_instance.retrieve_term(term_id)
        print("The response of TermsApi->retrieve_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->retrieve_term: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term_id** | **str**|  | 

### Return type

[**TermResponse**](TermResponse.md)

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

