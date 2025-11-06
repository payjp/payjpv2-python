# StatementType

Statementのタイプ  Statement自体が大枠としてどのような取引なのかを表す。 加盟店、PAYのオペレーター、システムがBalanceの状態を把握するときに利用できる分類にする。  ### 例 + type=sales     + 売上が発生している     + termを見ればどの区間の売上かがわかる + type=transfer_feeが2つ付いている     + 振込が2回行われた＝振込エラーが発生していた + type=forfeitが付いている     + この残高は失効した

## Enum

* `SALES` (value: `'sales'`)

* `SERVICE_FEE` (value: `'service_fee'`)

* `TRANSFER_FEE` (value: `'transfer_fee'`)

* `FORFEIT` (value: `'forfeit'`)

* `MISC` (value: `'misc'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


