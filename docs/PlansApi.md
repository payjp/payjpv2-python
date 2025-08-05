# payjpv2.PlansApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_plan**](PlansApi.md#create_plan) | **POST** /v2/plans | Create Plan
[**read_plans**](PlansApi.md#read_plans) | **GET** /v2/plans | Read Plans


# **create_plan**
> PlanResponse create_plan(plan_create_request)

Create Plan

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.plan_create_request import PlanCreateRequest
from payjpv2.models.plan_response import PlanResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "http://localhost"
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
    api_instance = payjpv2.PlansApi(api_client)
    plan_create_request = payjpv2.PlanCreateRequest() # PlanCreateRequest | 

    try:
        # Create Plan
        api_response = api_instance.create_plan(plan_create_request)
        print("The response of PlansApi->create_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->create_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **plan_create_request** | [**PlanCreateRequest**](PlanCreateRequest.md)|  | 

### Return type

[**PlanResponse**](PlanResponse.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_plans**
> List[PlanResponse] read_plans()

Read Plans

### Example

* Api Key Authentication (APIKeyHeader):

```python
import payjpv2
from payjpv2.models.plan_response import PlanResponse
from payjpv2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = payjpv2.Configuration(
    host = "http://localhost"
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
    api_instance = payjpv2.PlansApi(api_client)

    try:
        # Read Plans
        api_response = api_instance.read_plans()
        print("The response of PlansApi->read_plans:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PlansApi->read_plans: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PlanResponse]**](PlanResponse.md)

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

