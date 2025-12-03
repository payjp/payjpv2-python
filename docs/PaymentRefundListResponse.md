# PaymentRefundListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'list']
**url** | **str** | リスト取得URL | 
**has_more** | **bool** | 次のページがあるかどうか | 
**data** | [**List[PaymentRefundResponse]**](PaymentRefundResponse.md) | 返金リスト | 

## Example

```python
from payjpv2.models.payment_refund_list_response import PaymentRefundListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentRefundListResponse from a JSON string
payment_refund_list_response_instance = PaymentRefundListResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentRefundListResponse.to_json())

# convert the object into a dict
payment_refund_list_response_dict = payment_refund_list_response_instance.to_dict()
# create an instance of PaymentRefundListResponse from a dict
payment_refund_list_response_from_dict = PaymentRefundListResponse.from_dict(payment_refund_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


