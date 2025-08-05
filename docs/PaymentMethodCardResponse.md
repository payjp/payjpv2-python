# PaymentMethodCardResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **str** |  | [optional] [default to 'payment_method']
**id** | **str** | ID | 
**type** | **str** |  | 
**customer** | **str** |  | [optional] 
**livemode** | **bool** | 本番環境かどうか | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 
**billing_details** | [**PaymentMethodBillingDetailsResponse**](PaymentMethodBillingDetailsResponse.md) | 請求先情報 | 
**card** | [**PaymentMethodCardDetailsResponse**](PaymentMethodCardDetailsResponse.md) | カード情報 | 

## Example

```python
from payjpv2.models.payment_method_card_response import PaymentMethodCardResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethodCardResponse from a JSON string
payment_method_card_response_instance = PaymentMethodCardResponse.from_json(json)
# print the JSON string representation of the object
print(PaymentMethodCardResponse.to_json())

# convert the object into a dict
payment_method_card_response_dict = payment_method_card_response_instance.to_dict()
# create an instance of PaymentMethodCardResponse from a dict
payment_method_card_response_from_dict = PaymentMethodCardResponse.from_dict(payment_method_card_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


