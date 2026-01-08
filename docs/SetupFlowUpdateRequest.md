# SetupFlowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | この SetupFlow に関連付ける顧客の ID。SetupFlow により作られた PaymentMethod はこの顧客に紐付きます。 | [optional] 
**payment_method_options** | [**SetupFlowPaymentMethodOptionsRequest**](SetupFlowPaymentMethodOptionsRequest.md) | この SetupFlow 固有の支払い方法の設定 | [optional] 
**payment_method_types** | **List[str]** | この SetupFlow で使用できる支払い方法の種類のリスト。 指定しない場合は、PAY.JP は支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**description** | **str** | 説明。顧客に表示されます。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

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


