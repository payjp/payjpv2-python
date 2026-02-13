# PaymentDisputeListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentDisputeResponse]**](PaymentDisputeResponse.md) | PaymentDispute リスト | 

## Example

```python
from payjpv2.models.payment_dispute_list_response import PaymentDisputeListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentDisputeListResponse from a JSON string
payment_dispute_list_response_instance = PaymentDisputeListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentDisputeListResponse.to_json())

# convert the object into a dict
payment_dispute_list_response_dict = payment_dispute_list_response_instance.to_dict()
# create an instance of PaymentDisputeListResponse from a dict
payment_dispute_list_response_from_dict = PaymentDisputeListResponse.from_dict(payment_dispute_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


