# PaymentMethodPayPayResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_method']
**id** | **str** | ID | 
**type** | **str** |  | 
**customer_id** | **str** |  | 
**detached_at** | **datetime** |  | 
**livemode** | **bool** | 本番環境かどうか | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**billing_details** | [**PaymentMethodBillingDetailsResponse**](PaymentMethodBillingDetailsResponse.md) | 請求先情報 | 

## Example

```python
from payjpv2.models.payment_method_pay_pay_response import PaymentMethodPayPayResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodPayPayResponse from a JSON string
payment_method_pay_pay_response_instance = PaymentMethodPayPayResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodPayPayResponse.to_json())

# convert the object into a dict
payment_method_pay_pay_response_dict = payment_method_pay_pay_response_instance.to_dict()
# create an instance of PaymentMethodPayPayResponse from a dict
payment_method_pay_pay_response_from_dict = PaymentMethodPayPayResponse.from_dict(payment_method_pay_pay_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


