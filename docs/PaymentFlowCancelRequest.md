# PaymentFlowCancelRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellation_reason** | **str** | この PaymentFlow のキャンセル理由 | 指定できる値 | |:---| | **duplicate**: 重複した支払いである場合。 | | **fraudulent**: 不正な利用だと考えられる場合。 | | **requested_by_customer**: 顧客がキャンセルを要求した場合。 | | **abandoned**: 顧客が支払いを完了しなかった場合。 |  | [optional] 

## Example

```python
from payjpv2.models.payment_flow_cancel_request import PaymentFlowCancelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowCancelRequest from a JSON string
payment_flow_cancel_request_instance = PaymentFlowCancelRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowCancelRequest.to_json())

# convert the object into a dict
payment_flow_cancel_request_dict = payment_flow_cancel_request_instance.to_dict()
# create an instance of PaymentFlowCancelRequest from a dict
payment_flow_cancel_request_from_dict = PaymentFlowCancelRequest.from_dict(payment_flow_cancel_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


