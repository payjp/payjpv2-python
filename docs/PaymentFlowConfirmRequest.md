# PaymentFlowConfirmRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **str** | 支払い方法 ID。customer_id の指定が必須です。Customer が所持する PaymentMethod のみ指定できます。payment_method_id を指定せず、Customer に default_payment_method_id が設定されている場合はそちらが自動でセットされます。 | [optional] 
**payment_method_options** | [**PaymentFlowPaymentMethodOptionsRequest**](PaymentFlowPaymentMethodOptionsRequest.md) | この PaymentFlow 固有の支払い方法の設定 | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) | この PaymentFlow で使用できる支払い方法の種類のリスト。指定しない場合は、PAY.JP は支払い方法の設定から利用可能な支払い方法を動的に表示します。 | [optional] 
**capture_method** | [**CaptureMethod**](CaptureMethod.md) | 支払いの確定方法を指定します。  | 値 | |:---| | **automatic**: (デフォルト) 顧客が支払いを承認すると、自動的に確定させます。 | | **manual**: 顧客が支払いを承認すると一旦確定を保留し、後で Payment Flow の Capture API を使用して確定します。（すべての支払い方法がこれをサポートしているわけではありません）。 | | [optional] 
**return_url** | **str** | 顧客が支払いを完了後かキャンセルした後にリダイレクトされる URL。アプリにリダイレクトしたい場合は URI Scheme を指定できます。 | [optional] 
**description** | **str** | オブジェクトにセットする任意の文字列。ユーザーには表示されません。 | [optional] 

## Example

```python
from payjpv2.models.payment_flow_confirm_request import PaymentFlowConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentFlowConfirmRequest from a JSON string
payment_flow_confirm_request_instance = PaymentFlowConfirmRequest.from_json(json)
# print the JSON string representation of the object
print(PaymentFlowConfirmRequest.to_json())

# convert the object into a dict
payment_flow_confirm_request_dict = payment_flow_confirm_request_instance.to_dict()
# create an instance of PaymentFlowConfirmRequest from a dict
payment_flow_confirm_request_from_dict = PaymentFlowConfirmRequest.from_dict(payment_flow_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


