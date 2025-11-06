# payjpv2.StatementsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_statement_url**](StatementsApi.md#create_statement_url) | **POST** /v2/statements/{statement_id}/statement_urls | Create Statement Url
[**get_all_statements**](StatementsApi.md#get_all_statements) | **GET** /v2/statements | Get All Statements
[**retrieve_statement**](StatementsApi.md#retrieve_statement) | **GET** /v2/statements/{statement_id} | Retrieve Statement


# **create_statement_url**
> StatementURLResponse create_statement_url(statement_id)

Create Statement Url

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.statement_url_response import StatementURLResponse
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
    api_instance = payjpv2.StatementsApi(api_client)
    statement_id = 'statement_id_example' # str | 

    try:
        # Create Statement Url
        api_response = api_instance.create_statement_url(statement_id)
        print("The response of StatementsApi->create_statement_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatementsApi->create_statement_url: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**|  | 

### Return type

[**StatementURLResponse**](StatementURLResponse.md)

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

# **get_all_statements**
> StatementListResponse get_all_statements(since=since, until=until, limit=limit, starting_after=starting_after, ending_before=ending_before, owner=owner, source_transfer=source_transfer, tenant=tenant, type=type, term=term)

Get All Statements

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.statement_list_response import StatementListResponse
from payjpv2.models.statement_type import StatementType
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
    api_instance = payjpv2.StatementsApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以降のデータを取得 (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以前のデータを取得 (optional)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    starting_after = 'starting_after_example' # str | このIDより後のデータを取得 (optional)
    ending_before = 'ending_before_example' # str | このIDより前のデータを取得 (optional)
    owner = 'owner_example' # str | オーナータイプでフィルタ (merchant または tenant) (optional)
    source_transfer = 'source_transfer_example' # str | 送金元IDでフィルタ (optional)
    tenant = 'tenant_example' # str | テナントIDでフィルタ (optional)
    type = payjpv2.StatementType() # StatementType | 明細タイプでフィルタ (optional)
    term = 'term_example' # str | 期間IDでフィルタ (optional)

    try:
        # Get All Statements
        api_response = api_instance.get_all_statements(since=since, until=until, limit=limit, starting_after=starting_after, ending_before=ending_before, owner=owner, source_transfer=source_transfer, tenant=tenant, type=type, term=term)
        print("The response of StatementsApi->get_all_statements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatementsApi->get_all_statements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| 指定した日付以降のデータを取得 | [optional] 
 **until** | **datetime**| 指定した日付以前のデータを取得 | [optional] 
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **starting_after** | **str**| このIDより後のデータを取得 | [optional] 
 **ending_before** | **str**| このIDより前のデータを取得 | [optional] 
 **owner** | **str**| オーナータイプでフィルタ (merchant または tenant) | [optional] 
 **source_transfer** | **str**| 送金元IDでフィルタ | [optional] 
 **tenant** | **str**| テナントIDでフィルタ | [optional] 
 **type** | [**StatementType**](.md)| 明細タイプでフィルタ | [optional] 
 **term** | **str**| 期間IDでフィルタ | [optional] 

### Return type

[**StatementListResponse**](StatementListResponse.md)

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

# **retrieve_statement**
> StatementResponse retrieve_statement(statement_id)

Retrieve Statement

### Example

* Basic Authentication (HTTPBasic):
* Bearer Authentication (HTTPBearer):

```python
import payjpv2
from payjpv2.models.statement_response import StatementResponse
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
    api_instance = payjpv2.StatementsApi(api_client)
    statement_id = 'statement_id_example' # str | 

    try:
        # Retrieve Statement
        api_response = api_instance.retrieve_statement(statement_id)
        print("The response of StatementsApi->retrieve_statement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatementsApi->retrieve_statement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**|  | 

### Return type

[**StatementResponse**](StatementResponse.md)

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

