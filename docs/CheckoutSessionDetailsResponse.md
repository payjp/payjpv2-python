# CheckoutSessionDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID | [optional] 
**object** | **str** |  | [optional] [default to 'checkout.session']
**livemode** | **bool** | 本番環境かどうか | [optional] 
**amount_subtotal** | **int** |  | [optional] 
**amount_total** | **int** |  | [optional] 
**billing_address_collection** | [**BillingAddressCollection**](BillingAddressCollection.md) |  | [optional] 
**cancel_url** | **str** |  | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_details** | **Dict[str, object]** | &#x60;expand&#x60; パラメーターを指定した場合、顧客の詳細情報を含んだオブジェクトが返却されます。  | 説明 | |:---| | **email**: 顧客のメールアドレス |  | [optional] 
**expires_at** | **datetime** |  | [optional] 
**currency** | [**Currency**](Currency.md) | 価格の通貨。現在は &#x60;jpy&#x60; のみサポートしています。 | [optional] 
**locale** | [**Locale**](Locale.md) |  | [optional] 
**payment_flow** | [**PaymentFlow**](PaymentFlow.md) |  | [optional] 
**payment_method_types** | [**List[PaymentMethodTypes]**](PaymentMethodTypes.md) |  | [optional] 
**payment_method_options** | **Dict[str, object]** |  | [optional] 
**setup_flow** | [**SetupFlow**](SetupFlow.md) |  | [optional] 
**submit_type** | [**CheckoutSessionSubmitType**](CheckoutSessionSubmitType.md) |  | [optional] 
**mode** | [**CheckoutSessionMode**](CheckoutSessionMode.md) | Checkout Session のモード  | 指定できる値 | |:---| | **hosted**: PAY.JPでホスティングしている画面を使用します。 |  | [optional] 
**ui_mode** | [**CheckoutSessionUIMode**](CheckoutSessionUIMode.md) | Checkout Session の UI モード。デフォルトは &#x60;hosted&#x60; です。&lt;br&gt;  | 指定できる値 | |:---| | **hosted**: PAY.JPでホスティングしている画面を使用します。 |  | [optional] 
**created_at** | **datetime** | 作成日時 (UTC, ISO 8601 形式) | [optional] 
**updated_at** | **datetime** | 更新日時 (UTC, ISO 8601 形式) | [optional] 
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | メタデータ | [optional] 
**status** | [**CheckoutSessionStatus**](CheckoutSessionStatus.md) | チェックアウトセッションのステータス | [optional] 
**line_items** | [**CheckoutSessionLineItemsResponse**](CheckoutSessionLineItemsResponse.md) |  | [optional] 
**success_url** | **str** |  | [optional] 
**url** | **str** | URL | [optional] 

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


