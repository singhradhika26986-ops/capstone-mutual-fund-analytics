# Data Dictionary

## dim_fund
- amfi_code : Unique fund code
- fund_house : Mutual fund company
- scheme_name : Scheme name
- category : Fund category
- sub_category : Fund sub category
- plan : Regular/Direct plan

## fact_nav
- amfi_code : Fund code
- date : NAV date
- nav : Net Asset Value

## fact_performance
- return_1yr_pct : 1 Year Return
- return_3yr_pct : 3 Year Return
- return_5yr_pct : 5 Year Return
- expense_ratio_pct : Expense Ratio

## fact_transactions
- investor_id : Investor ID
- transaction_type : SIP/Lumpsum/Redemption
- amount_inr : Transaction Amount
- state : Investor State
- kyc_status : KYC Status

## fact_aum
- fund_house : Fund House
- aum_crore : Assets Under Management (Crore)