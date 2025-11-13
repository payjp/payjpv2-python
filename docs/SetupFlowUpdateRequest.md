# SetupFlowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer** | **str** | この SetupFlow が属する顧客の ID。SetupFlow に PaymentMethod が設定されている場合、SetupFlow の設定が成功するとその PaymentMethod は顧客に紐付きます。別の顧客に紐付いている PaymentMethod をこの SetupFlow で使用することはできません。 | [optional] 
**payment_method_options** | **Dict[str, object]** | この SetupFlow の支払い方法の個別設定。 | [optional] 
**payment_method_types** | **List[str]** |  | [optional] 
**description** | **str** | 説明。顧客に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.setup_flow_update_request import SetupFlowUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetupFlowUpdateRequest from a JSON string
setup_flow_update_request_instance = SetupFlowUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SetupFlowUpdateRequest.to_json())

# convert the object into a dict
setup_flow_update_request_dict = setup_flow_update_request_instance.to_dict()
# create an instance of SetupFlowUpdateRequest from a dict
setup_flow_update_request_from_dict = SetupFlowUpdateRequest.from_dict(setup_flow_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


