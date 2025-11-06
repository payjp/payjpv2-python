# PaymentFlowDataRequestInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると自動的に確定します。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**setup_future_usage** | **str** | この PaymentFlow に設定されている支払い方法で今後決済を行うかの設定です。&lt;br&gt;&lt;br&gt; PaymentFlow に Customer を指定した場合、このパラメータを使って PaymentFlow を確定できます。 その後、顧客が必要な操作を完了すると、支払い方法を Customer に紐付けることが可能です。また、Customer を指定しない場合でも、取引が完了した後に支払い方法を Customer に紐付けることはできます。 | [optional] 

## Example

```python
from payjpv2.models.payment_flow_data_request_input import PaymentFlowDataRequestInput

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowDataRequestInput from a JSON string
payment_flow_data_request_input_instance = PaymentFlowDataRequestInput.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowDataRequestInput.to_json())

# convert the object into a dict
payment_flow_data_request_input_dict = payment_flow_data_request_input_instance.to_dict()
# create an instance of PaymentFlowDataRequestInput from a dict
payment_flow_data_request_input_from_dict = PaymentFlowDataRequestInput.from_dict(payment_flow_data_request_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


