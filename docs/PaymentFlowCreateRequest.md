# PaymentFlowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。 | 
**customer_id** | **str** | この PaymentFlow に関連付ける顧客の ID | [optional] 
**payment_method_id** | **str** | 支払い方法 ID。customer_id の指定が必須です。Customer が所持する PaymentMethod のみ指定できます。payment_method_id を指定せず、Customer に default_payment_method_id が設定されている場合はそちらが自動でセットされます。 | [optional] 
**payment_method_options** | [**PaymentFlowPaymentMethodOptionsRequest**](PaymentFlowPaymentMethodOptionsRequest.md) | この PaymentFlow 固有の支払い方法の設定 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) | この PaymentFlow で使用できる支払い方法の種類のリスト。指定しない場合は、PAY.JP は支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | 
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると、自動的に確定させます。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**confirm** | **bool** | 「true」に設定すると、この PaymentFlow を直ちに確定しようと試みます。 | [optional] [default to False]
**return_url** | **str** | 顧客が支払いを完了後かキャンセルした後にリダイレクトされる URL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。confirm&#x3D;true の場合のみ指定できます。 | [optional] 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。20件まで登録可能で、空文字列を指定するとそのキーを削除できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/guide/developers/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 

## Example

```python
from payjpv2.models.payment_flow_create_request import PaymentFlowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowCreateRequest from a JSON string
payment_flow_create_request_instance = PaymentFlowCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowCreateRequest.to_json())

# convert the object into a dict
payment_flow_create_request_dict = payment_flow_create_request_instance.to_dict()
# create an instance of PaymentFlowCreateRequest from a dict
payment_flow_create_request_from_dict = PaymentFlowCreateRequest.from_dict(payment_flow_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


