# payjpv2.TermsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_terms**](TermsApi.md#get_all_terms) | **GET** /v2/terms | Get All Terms
[**get_term**](TermsApi.md#get_term) | **GET** /v2/terms/{term_id} | Get Term


# **get_all_terms**
> TermListResponse get_all_terms(limit=limit, starting_after=starting_after, ending_before=ending_before, since_start_at=since_start_at, until_start_at=until_start_at)

Get All Terms

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
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    since_start_at = '2013-10-20T19:20:30+01:00' # datetime | start_at が指定した日付以降のデータを取得 (optional)
    until_start_at = '2013-10-20T19:20:30+01:00' # datetime | start_at が指定した日付以前のデータを取得 (optional)

    try:
        # Get All Terms
        api_response = api_instance.get_all_terms(limit=limit, starting_after=starting_after, ending_before=ending_before, since_start_at=since_start_at, until_start_at=until_start_at)
        print("The response of TermsApi->get_all_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->get_all_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **since_start_at** | **datetime**| start_at が指定した日付以降のデータを取得 | [optional] 
 **until_start_at** | **datetime**| start_at が指定した日付以前のデータを取得 | [optional] 

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
**400** | Resource Missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_term**
> TermResponse get_term(term_id)

Get Term

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
        # Get Term
        api_response = api_instance.get_term(term_id)
        print("The response of TermsApi->get_term:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TermsApi->get_term: %s\n" % e)
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

