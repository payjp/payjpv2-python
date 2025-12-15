# CheckoutSessionDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | 
**object** | **str** |  | [optional] [default to 'checkout.session']
**livemode** | **bool** | 本番環境かどうか | 
**amount_subtotal** | **int** |  | 
**amount_total** | **int** |  | 
**cancel_url** | **str** |  | 
**customer_id** | **str** |  | 
**customer_email** | **str** |  | 
**expires_at** | **datetime** |  | 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | 
**locale** | [**Locale**](Locale.md) |  | 
**payment_flow_id** | **str** |  | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) |  | 
**payment_method_options** | **Dict[str, object]** |  | 
**setup_flow_id** | **str** |  | [optional] 
**submit_type** | [**CheckoutSessionSubmitType**](CheckoutSessionSubmitType.md) |  | 
**mode** | [**CheckoutSessionMode**](CheckoutSessionMode.md) | Checkout Session のモード  | 指定できる値 | |:---| | **payment**: 支払いモードでCheckout Sessionを作成します。 | | **setup**: セットアップモードでCheckout Sessionを作成します。 |  | 
**ui_mode** | [**CheckoutSessionUIMode**](CheckoutSessionUIMode.md) | Checkout Session の UI モード。デフォルトは &#x60;hosted&#x60; です。&lt;br&gt;  | 指定できる値 | |:---| | **hosted**: PAY.JPでホスティングしている画面を使用します。 |  | 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | 
**status** | [**CheckoutSessionStatus**](CheckoutSessionStatus.md) | チェックアウトセッションのステータス | 
**success_url** | **str** |  | 
**url** | **str** | URL | 

## Example

```python
from payjpv2.models.checkout_session_details_response import CheckoutSessionDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CheckoutSessionDetailsResponse from a JSON string
checkout_session_details_response_instance = CheckoutSessionDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(CheckoutSessionDetailsResponse.to_json())

# convert the object into a dict
checkout_session_details_response_dict = checkout_session_details_response_instance.to_dict()
# create an instance of CheckoutSessionDetailsResponse from a dict
checkout_session_details_response_from_dict = CheckoutSessionDetailsResponse.from_dict(checkout_session_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


