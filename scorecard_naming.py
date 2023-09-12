Income_statement_mapping = {
    'Net Revenue': ['us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax', 'us-gaap_SalesRevenueNet'],
    'Cost of Goods Sold' : ['wsm_CostOfGoodsSoldAndOccupancyExpenses'],
    'Gross Profit' : ['us-gaap_GrossProfit'],
    'SG&A' : ['us-gaap_SellingGeneralAndAdministrativeExpense'],
    'Operating Income' : ['us-gaap_OperatingIncomeLoss'],
    'Interest Expense' : ['us-gaap_InterestIncomeExpenseNonoperatingNet', 'wsm_NetInterestIncomeAndExpense', 'wsm_NetInterestIncomeExpense'],
    'EBT' : ['us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest','us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments'],
    'Taxes' : ['us-gaap_IncomeTaxExpenseBenefit'],
    'Net income' : ['us-gaap_NetIncomeLoss'],
    'EPS' : ['us-gaap_EarningsPerShareBasic'],
    'EPS Diluted' : ['us-gaap_EarningsPerShareDiluted'],
    'Weighted Average Shares Outstanding' : ['us-gaap_WeightedAverageNumberOfSharesOutstandingBasic'],
    'Weighted Average Shares Diluted' : ['us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding'],
}

Balance_sheet_mapping = {
    'Cash' : ['us-gaap_CashAndCashEquivalentsAtCarryingValue'],
    'Accounts Receivable' : ['us-gaap_ReceivablesNetCurrent'],
    'Inventory' : ['us-gaap_InventoryNet'],
    'Prepaid Expenses' : ['us-gaap_PrepaidExpenseCurrent'],
    'Other Current Assets' : ['us-gaap_OtherAssetsCurrent'],
    'Total Current Assets' : ['us-gaap_AssetsCurrent'],
    'Property, Plant, and Equipment' : ['us-gaap_PropertyPlantAndEquipmentNet'],
    'Operating Lease Right of Use Asset' : ['us-gaap_OperatingLeaseRightOfUseAsset'],
    'Deffered Income Taxes' : ['us-gaap_DeferredIncomeTaxAssetsNet', 'us-gaap_DeferredTaxAssetsNetNoncurrent'],
    'Goodwill' : ['us-gaap_Goodwill'],
    'Other Long Term Assets' : ['us-gaap_OtherAssetsNoncurrent'],
    'Total Assets' : ['us-gaap_Assets'],
    'Accounts Payable' : ['us-gaap_AccountsPayableCurrent'],
    'Accrued Expenses' : ['us-gaap_AccruedLiabilitiesCurrent'],
    'Deferred Revenue' : ['us-gaap_ContractWithCustomerLiabilityCurrent', 'us-gaap_DeferredRevenueAndCreditsCurrent'],
    'Income Taxes Payable' : ['us-gaap_AccruedIncomeTaxesCurrent'],
    'Operating Lease Liability' : ['us-gaap_OperatingLeaseLiabilityCurrent'],
    'Other Current Liabilities' : ['us-gaap_OtherLiabilitiesCurrent'],
    'Total Current Liabilities' : ['us-gaap_LiabilitiesCurrent'],
    'Deffered Lease Incentive' : ['wsm_DeferredLeaseIncentivesLiabilityNoncurrent','wsm_DeferredRentAndLeaseIncentivesLiabilityNoncurrent'],
    'Long Term Lease Liability' : ['us-gaap_OperatingLeaseLiabilityNoncurrent'],
    'Other Long Term Liabilities' : ['us-gaap_OtherLiabilitiesNoncurrent'],
    'Total Liabilities' : ['us-gaap_Liabilities'],
    'Common Stock Par .01 Issued' : ['us-gaap_CommonStockValue'],
    'Additional Paid in Capital' : ['us-gaap_AdditionalPaidInCapital'],
    'Retained Earnings' : ['us-gaap_RetainedEarningsAccumulatedDeficit'],
    'Accumulated Other Comprehensive Income(Loss)' : ['us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax','us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax'],
    'Treasury Stock at Cost' : ['us-gaap_TreasuryStockCommonValue','us-gaap_TreasuryStockValue'],
    'Total Stockholders Equity' : ['us-gaap_StockholdersEquity'],
    'Total Liabilities and Stockholders Equity' : ['us-gaap_LiabilitiesAndStockholdersEquity'],
}

Cash_flow_mapping = {
    'Net Earnings' : ['us-gaap_ProfitLoss', 'us-gaap_NetIncomeLoss'],
    'Depreciation and Amortization' : ['us-gaap_DepreciationDepletionAndAmortization'],
    'Loss on Disposal/Impairment' : ['us-gaap_GainLossOnSalesOfAssetsAndAssetImpairmentCharges'],
    'Amoritization of Deferred Lease Incentive' : ['wsm_AmortizationOfDeferredLeaseIncentives', 'us-gaap_AmortizationOfLeaseIncentives', 'wsm_AmortizationLeaseIncentives', 'wsm_AmortizationOfLeaseIncentives'],
    'Non Cash Lease Expense' : ['wsm_NoncashLeaseExpense'],
    'Deferred Income Taxes' : ['us-gaap_DeferredIncomeTaxExpenseBenefit'],
    'Stock Based Compensation Expense' : ['us-gaap_ShareBasedCompensation'],
    'Other Operating Activities' : ['us-gaap_OtherNoncashIncomeExpense'],
    'Changes in Accounts Receivable' : ['us-gaap_IncreaseDecreaseInAccountsAndOtherReceivables'],
    'Changes in Inventory' : ['us-gaap_IncreaseDecreaseInInventories'],
    'Changes in Prepaid Expenses and other assets' : ['us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets', 'us-gaap_IncreaseDecreaseInOtherOperatingAssets'],
    'Changes in Accounts Payable' : ['us-gaap_IncreaseDecreaseInAccountsPayable'],
    'Changes in Accrued Expenses' : ['us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities'],
    'Changes in Gift Card and Other deferred revenue' : ['us-gaap_IncreaseDecreaseInDeferredRevenue'],
    'Changes in Operating Lease Liability' : ['us-gaap_IncreaseDecreaseInOperatingLeaseLiability', 'wsm_IncreaseDecreaseInOperatingLeaseLiabilities'],
    'Changes in Income Taxes Payable' : ['us-gaap_IncreaseDecreaseInAccruedIncomeTaxesPayable'],
    'Net Cash Provided by Operating Activities' : ['us-gaap_NetCashProvidedByUsedInOperatingActivities', 'us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations'],
    
    'Purchase of Property, Plant, and Equipment' : ['us-gaap_PaymentsToAcquirePropertyPlantAndEquipment'],
    'Other Investing Activities' : ['us-gaap_PaymentsForProceedsFromOtherInvestingActivities'],
    'Net Cash Used in Investing Activities' : ['us-gaap_NetCashProvidedByUsedInInvestingActivities', 'us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations'],

    'Repurchases of Common Stock' : ['us-gaap_PaymentsForRepurchaseOfCommonStock'],
    'Payment of Dividends' : ['us-gaap_PaymentsOfDividendsCommonStock', 'us-gaap_PaymentsOfDividends'],
    'Tax Withholding Related to Stock Based Compensation' : ['us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation', 'wsm_TaxWithholdingPaymentRelatedToStockBasedCompensationAwardDistributions'],
    'Repayment of Long Term Debt' : ['us-gaap_RepaymentsOfLongTermDebt'],
    'Debt Issuance Costs' : ['us-gaap_PaymentsOfDebtIssuanceCosts', 'us-gaap_ProceedsFromPaymentsForOtherFinancingActivities'],
    'Borrowings Under Revolving Credit Facility' : ['us-gaap_ProceedsFromLinesOfCredit'],
    'Repayments Under Revolving Credit Facility' : ['us-gaap_RepaymentsOfLinesOfCredit'],
    'Net Cash Used in Financing Activities' : ['us-gaap_NetCashProvidedByUsedInFinancingActivities', 'us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations'],
    'Effect of Exchange Rates on Cash and Cash Equivalents' : ['us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents', 'us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents'],
    'Net Change in Cash and Cash Equivalents' : ['us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect', 'us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease'],
    'Cash and Cash Equivalents at Begining of Year' : ['us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents', 'us-gaap_CashAndCashEquivalentsAtCarryingValue'],
    'Cash Paid for Interest' : ['us-gaap_InterestPaidNet', 'us-gaap_InterestPaid'],
    'Cash Paid for Income Tax Net' : ['us-gaap_IncomeTaxesPaidNet'],
    'Non-Cash Purchases of PPE Not Yet Paid' : ['us-gaap_CapitalExpendituresIncurredButNotYetPaid'],
}