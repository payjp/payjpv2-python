# PaymentFlowDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると自動的に確定します。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.payment_flow_data_request import PaymentFlowDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowDataRequest from a JSON string
payment_flow_data_request_instance = PaymentFlowDataRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowDataRequest.to_json())

# convert the object into a dict
payment_flow_data_request_dict = payment_flow_data_request_instance.to_dict()
# create an instance of PaymentFlowDataRequest from a dict
payment_flow_data_request_from_dict = PaymentFlowDataRequest.from_dict(payment_flow_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


