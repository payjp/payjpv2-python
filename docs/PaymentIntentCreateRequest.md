# PaymentIntentCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | **str** | 支払い方法ID | [optional] 
**payment_method_data** | [**PaymentMethodCreateRequest**](PaymentMethodCreateRequest.md) | 指定した場合、PaymentMethodの作成に使用されます。新しいPaymentMethodは、PaymentIntentのpayment_methodプロパティに表示されます。 | [optional] 
**payment_method_options** | [**PaymentMethodOptionsRequest**](PaymentMethodOptionsRequest.md) | このPaymentIntentに固有の支払い方法の設定 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) | このPaymentIntentで使用できる支払い方法の種類（カードなど）のリストです。 指定しない場合は、PAY.JPは支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**receipt_email** | **str** | 請求書の送信先メールアドレス。ライブモードで支払いに対して &#x60;receipt_email&#x60; を指定すると、メール設定に関係なく領収書が送信されます。 | [optional] 
**return_url** | **str** | 顧客が支払いを完了後かキャンセルした後にリダイレクトされるURL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。confirm&#x3D;trueの場合のみ指定できます。 | [optional] 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 
**amount** | **int** | 支払い予定の金額。50円以上9,999,999円以下である必要があります。支払い手段によって上限金額は異なります。 | 
**customer** | **str** | このPaymentIntentに属する顧客のID（存在する場合）。この顧客以外にすでに紐づけられている支払い方法はこのPaymentIntentでは使用できません。 | [optional] 
**confirm** | **bool** | 「true」に設定すると、このPaymentIntentを直ちに確定しようと試みます。このパラメーターのデフォルトは「false」です。 | [optional] [default to False]
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 指定できる値 | |:---| | **automatic**: 顧客が支払いを承認すると、自動的に確定させます。 | | **automatic_async**: (デフォルト) 顧客が支払いを承認すると、非同期的に確定させます。レイテンシが改善されるため、capture_method&#x3D;automaticよりも推奨されます。詳細については、統合ガイドをお読みください。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | キーバリューの任意のデータを格納できます。&lt;a href&#x3D;\&quot;https://docs.pay.jp/v2/metadata\&quot;&gt;詳細はメタデータのドキュメントを参照してください。&lt;/a&gt; | [optional] 
**setup_future_usage** | [**Usage**](Usage.md) | このPaymentIntentの支払い方法で将来の支払いを行う意図があることを示します。&lt;br&gt;&lt;br&gt;PaymentIntent に Customer を指定した場合、このパラメータを使って PaymentIntent を確定できます。その後、顧客が必要な操作を完了すると、支払い方法を Customer に紐付けることが可能です。また、Customer を指定しない場合でも、取引が完了した後に支払い方法を Customer に紐付けることはできます。 | [optional] 

## Example

```python
from payjpv2.models.payment_intent_create_request import PaymentIntentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentIntentCreateRequest from a JSON string
payment_intent_create_request_instance = PaymentIntentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentIntentCreateRequest.to_json())

# convert the object into a dict
payment_intent_create_request_dict = payment_intent_create_request_instance.to_dict()
# create an instance of PaymentIntentCreateRequest from a dict
payment_intent_create_request_from_dict = PaymentIntentCreateRequest.from_dict(payment_intent_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


