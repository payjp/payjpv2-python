# PaymentIntentDataRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: 顧客が支払いを承認すると自動的に確定します。 | | **automatic_async**: (デフォルト) 顧客が支払いを承認すると、非同期で確定させます。レイテンシが改善されるため、&#x60;capture_method&#x3D;automatic&#x60; よりも推奨されます。詳細については、統合ガイドをお読みください。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**setup_future_usage** | **str** | この PaymentIntent に設定されている支払い方法で今後決済を行うかの設定です。&lt;br&gt;&lt;br&gt; PaymentIntent に Customer を指定した場合、このパラメータを使って PaymentIntent を確定できます。 その後、顧客が必要な操作を完了すると、支払い方法を Customer に紐付けることが可能です。また、Customer を指定しない場合でも、取引が完了した後に支払い方法を Customer に紐付けることはできます。 | [optional] 

## Example

```python
from payjpv2.models.payment_intent_data_request import PaymentIntentDataRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentDataRequest from a JSON string
payment_intent_data_request_instance = PaymentIntentDataRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentDataRequest.to_json())

# convert the object into a dict
payment_intent_data_request_dict = payment_intent_data_request_instance.to_dict()
# create an instance of PaymentIntentDataRequest from a dict
payment_intent_data_request_from_dict = PaymentIntentDataRequest.from_dict(payment_intent_data_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


