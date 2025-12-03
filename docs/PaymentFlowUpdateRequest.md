# PaymentFlowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | 支払い方法ID | [optional] 
**payment_method_options** | [**PaymentMethodOptionsRequest**](PaymentMethodOptionsRequest.md) | このPaymentFlowに固有の支払い方法の設定 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) | このPaymentFlowで使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合は、PAY.JPは支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**return_url** | **str** | 顧客が支払いを完了後かキャンセルした後にリダイレクトされるURL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。confirm&#x3D;trueの場合のみ指定できます。 | [optional] 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。支払い手段によって上限金額は異なります。 | [optional] 
**customer** | **str** | このPaymentFlowに属する顧客のID（存在する場合）。この顧客以外にすでに紐づけられている支払い方法はこのPaymentFlowでは使用できません。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.payment_flow_update_request import PaymentFlowUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowUpdateRequest from a JSON string
payment_flow_update_request_instance = PaymentFlowUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowUpdateRequest.to_json())

# convert the object into a dict
payment_flow_update_request_dict = payment_flow_update_request_instance.to_dict()
# create an instance of PaymentFlowUpdateRequest from a dict
payment_flow_update_request_from_dict = PaymentFlowUpdateRequest.from_dict(payment_flow_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


