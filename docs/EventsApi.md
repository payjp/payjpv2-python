# payjpv2.EventsApi

All URIs are relative to *https://api.pay.jp*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_events**](EventsApi.md#get_all_events) | **GET** /v2/events | Get All Events
[**get_event**](EventsApi.md#get_event) | **GET** /v2/events/{event_id} | Get Event


# **get_all_events**
> EventListResponse get_all_events(since=since, until=until, limit=limit, offset=offset, resource_id=resource_id, object=object, type=type)

Get All Events

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.event_list_response import EventListResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.EventsApi(api_client)
    since = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以降のデータを取得 (optional)
    until = '2013-10-20T19:20:30+01:00' # datetime | 指定した日付以前のデータを取得 (optional)
    limit = 10 # int | 取得するデータの最大件数 (optional) (default to 10)
    offset = 0 # int | データ取得を行う開始位置 (optional) (default to 0)
    resource_id = 'resource_id_example' # str | 取得するeventに紐づくAPIリソースのID (e.g. customer.id) (optional)
    object = 'object_example' # str | 取得するeventに紐づくAPIリソースのobject。値はリソース名(e.g. customer, payment_intent) (optional)
    type = 'type_example' # str | 取得するeventのtype (optional)

    try:
        # Get All Events
        api_response = api_instance.get_all_events(since=since, until=until, limit=limit, offset=offset, resource_id=resource_id, object=object, type=type)
        print("The response of EventsApi->get_all_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_all_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **since** | **datetime**| 指定した日付以降のデータを取得 | [optional] 
 **until** | **datetime**| 指定した日付以前のデータを取得 | [optional] 
 **limit** | **int**| 取得するデータの最大件数 | [optional] [default to 10]
 **offset** | **int**| データ取得を行う開始位置 | [optional] [default to 0]
 **resource_id** | **str**| 取得するeventに紐づくAPIリソースのID (e.g. customer.id) | [optional] 
 **object** | **str**| 取得するeventに紐づくAPIリソースのobject。値はリソース名(e.g. customer, payment_intent) | [optional] 
 **type** | **str**| 取得するeventのtype | [optional] 

### Return type

[**EventListResponse**](EventListResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event**
> EventResponse get_event(event_id)

Get Event

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.event_response import EventResponse
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

# Configure API key authorization: APIKeyHeader
configuration.api_key['APIKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['APIKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with payjpv2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payjpv2.EventsApi(api_client)
    event_id = 'event_id_example' # str | 

    try:
        # Get Event
        api_response = api_instance.get_event(event_id)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

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

