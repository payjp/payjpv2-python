# SetupIntentUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | この SetupIntent が属する顧客の ID。SetupIntent に PaymentMethod が設定されている場合、SetupIntent の設定が成功するとその PaymentMethod は顧客に紐付きます。別の顧客に紐付いている PaymentMethod をこの SetupIntent で使用することはできません。 | [optional] 
**payment_method** | **str** | この SetupIntent に紐付ける決済方法のID | [optional] 
**payment_method_options** | **object** | この SetupIntent の支払い方法の個別設定。 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) |  | [optional] 
**description** | **str** | 説明。顧客に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.setup_intent_update_request import SetupIntentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupIntentUpdateRequest from a JSON string
setup_intent_update_request_instance = SetupIntentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SetupIntentUpdateRequest.to_json())

# convert the object into a dict
setup_intent_update_request_dict = setup_intent_update_request_instance.to_dict()
# create an instance of SetupIntentUpdateRequest from a dict
setup_intent_update_request_from_dict = SetupIntentUpdateRequest.from_dict(setup_intent_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


