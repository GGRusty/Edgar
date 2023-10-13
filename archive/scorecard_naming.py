Income_statement_mapping = {
    "Net Revenue": [
        "us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax",
        "us-gaap_SalesRevenueNet",
        "us-gaap_Revenues",
    ],
    "Goods Revenue": ["us-gaap_SalesRevenueGoodsNet"],
    "Service Revenue": [
        "msft_SalesRevenueServicesAndOtherNet",
        "us-gaap_SalesRevenueServicesNet",
    ],
    "Cost of Goods and Services Sold": [
        "us-gaap_CostOfGoodsAndServicesSold",
        "us-gaap_CostOfRevenue",
    ],
    "Cost of Goods Sold": [
        "wsm_CostOfGoodsSoldAndOccupancyExpenses",
        "us-gaap_CostOfGoodsSold",
    ],
    "Cost of Services": ["msft_CostOfServicesAndOther"],
    "Fulfillment Expense": ["amzn_FulfillmentExpense"],
    "Tech and Content Expense": ["amzn_TechnologyAndContentExpense"],
    "Marketing Expense": ["us-gaap_MarketingExpense"],
    "Amortization of Intangible Assets": [
        "us-gaap_AmortizationOfIntangibleAssets",
        "abt_AmortizationOfIntangibleAssetsExcludingDiscontinuedOperations",
    ],
    "Gross Profit": ["us-gaap_GrossProfit"],
    "Research and Development": [
        "us-gaap_ResearchAndDevelopmentExpense",
        "us-gaap_ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
    ],
    "Acquired In Process R&D": [
        "us-gaap_ResearchAndDevelopmentAssetAcquiredOtherThanThroughBusinessCombinationWrittenOff"
    ],
    "SG&A": ["us-gaap_SellingGeneralAndAdministrativeExpense"],
    "Selling and Marketing": ["us-gaap_SellingAndMarketingExpense"],
    "General and Administrative": ["us-gaap_GeneralAndAdministrativeExpense"],
    "Other Operating Expenses Net": [
        "us-gaap_OtherOperatingIncomeExpenseNet",
        "us-gaap_OtherExpenses",
        "us-gaap_OtherCostAndExpenseOperating",
    ],
    "Operating Expenses": ["us-gaap_OperatingExpenses", "us-gaap_CostsAndExpenses"],
    "Operating Income": ["us-gaap_OperatingIncomeLoss"],
    "Non-Operating Income": ["us-gaap_NonoperatingIncomeExpense"],
    "Interest Expense": [
        "us-gaap_InterestIncomeExpenseNonoperatingNet",
        "wsm_NetInterestIncomeAndExpense",
        "wsm_NetInterestIncomeExpense",
        "us-gaap_InterestExpense",
    ],
    "Interest Income": ["us-gaap_InvestmentIncomeInterest"],
    "Equity Investemnts Income": ["us-gaap_IncomeLossFromEquityMethodInvestments"],
    "Net Foreign Currency Exchange Gain": [
        "us-gaap_ForeignCurrencyTransactionGainLossBeforeTax"
    ],
    "Restucturing and Other Special Charges": [
        "us-gaap_RestructuringCharges",
        "msft_ImpairmentAndRestructuringExpenses",
        "msft_ImpairmentIntegrationAndRestructuringExpenses",
    ],
    "Other Expense Non-Operating": ["us-gaap_OtherNonoperatingIncomeExpense"],
    "EBT": [
        "us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
        "us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments",
    ],
    "Taxes": ["us-gaap_IncomeTaxExpenseBenefit"],
    "Net Income Continuous Operations": [
        "us-gaap_ProfitLoss",
        "us-gaap_IncomeLossFromContinuingOperationsIncludingPortionAttributableToNoncontrollingInterest",
    ],
    "Net Income Discontinued Operations": [
        "us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTax",
        "us-gaap_DiscontinuedOperationIncomeLossFromDiscontinuedOperationDuringPhaseOutPeriodNetOfTax",
    ],
    "Net Income Attributable to Noncontrolling Interest": [
        "us-gaap_NetIncomeLossAttributableToNoncontrollingInterest"
    ],
    "Net income": [
        "us-gaap_NetIncomeLoss",
        "us-gaap_NetIncomeLossAvailableToCommonStockholdersBasic",
    ],
    "EPS Cont. Operations": ["us-gaap_IncomeLossFromContinuingOperationsPerBasicShare"],
    "EPS Discont. Operations": [
        "us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTaxPerBasicShare"
    ],
    "EPS": ["us-gaap_EarningsPerShareBasic"],
    "EPS Diluted Cont. Operations": [
        "us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare"
    ],
    "EPS Diluted Discont. Operations": [
        "us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTaxPerDilutedShare"
    ],
    "EPS Diluted": ["us-gaap_EarningsPerShareDiluted"],
    "Weighted Average Shares Outstanding": [
        "us-gaap_WeightedAverageNumberOfSharesOutstandingBasic"
    ],
    "Dilutive Common Stock Options": [
        "us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements"
    ],
    "Weighted Average Shares Diluted": [
        "us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding"
    ],
    "Anti Dilutive Common Stock Options": [
        "us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount"
    ],
    "Declared Dividends per Share": ["us-gaap_CommonStockDividendsPerShareDeclared"],
}

Balance_sheet_mapping = {
    # Current Assets
    "Cash": ["us-gaap_CashAndCashEquivalentsAtCarryingValue"],
    "Marketable Securities": [
        "us-gaap_MarketableSecuritiesCurrent",
        "us-gaap_AvailableForSaleSecuritiesCurrent",
        "us-gaap_ShortTermInvestments",
    ],
    "Cash and Cash Equivalents and ST Investments": [
        "us-gaap_CashCashEquivalentsAndShortTermInvestments"
    ],
    "Accounts Receivable": [
        "us-gaap_ReceivablesNetCurrent",
        "us-gaap_AccountsReceivableNetCurrent",
        "us-gaap_AccountsAndOtherReceivablesNetCurrent",
    ],
    "Inventory": ["us-gaap_InventoryNet"],
    "Prepaid Expenses": [
        "us-gaap_PrepaidExpenseCurrent",
        "us-gaap_NontradeReceivablesCurrent",
    ],
    "Prepaid Expenses and Other Current Assets": [
        "us-gaap_PrepaidExpenseAndOtherAssets",
    ],
    "Other Current Assets": ["us-gaap_OtherAssetsCurrent"],
    "Total Current Assets": ["us-gaap_AssetsCurrent"],
    # Long Term Assets
    "Long Term Marketable Securities": [
        "us-gaap_MarketableSecuritiesNoncurrent",
        "us-gaap_AvailableForSaleSecuritiesNoncurrent",
        "us-gaap_LongTermInvestments",
    ],
    "Property, Plant, and Equipment": [
        "us-gaap_PropertyPlantAndEquipmentNet",
        "us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization",
    ],
    "Intangible Assets": [
        "us-gaap_IntangibleAssetsNetExcludingGoodwill",
        "us-gaap_FiniteLivedIntangibleAssetsNet",
    ],
    "Operating Lease Right of Use Asset": ["us-gaap_OperatingLeaseRightOfUseAsset"],
    "Deffered Income Taxes": [
        "us-gaap_DeferredIncomeTaxAssetsNet",
        "us-gaap_DeferredTaxAssetsNetNoncurrent",
    ],
    "Goodwill": ["us-gaap_Goodwill"],
    "Other Long Term Assets": ["us-gaap_OtherAssetsNoncurrent"],
    "Total Long Term Assets": ["us-gaap_AssetsNoncurrent"],
    "Total Assets": ["us-gaap_Assets"],
    # Current Liabilities
    "Short Term Debt": ["us-gaap_ShortTermBorrowings"],
    "Accounts Payable": ["us-gaap_AccountsPayableCurrent"],
    "Accrued Expenses": [
        "us-gaap_AccruedLiabilitiesCurrent",
        "amzn_AccruedLiabilitiesAndOtherCurrent",
    ],
    "Accounts Payable and Accrued Expenses": [
        "us-gaap_AccountsPayableAndAccruedLiabilitiesCurrent"
    ],
    "Deferred Revenue": [
        "us-gaap_ContractWithCustomerLiabilityCurrent",
        "us-gaap_DeferredRevenueAndCreditsCurrent",
        "us-gaap_DeferredRevenueCurrent",
    ],
    "Deferred Tax Assets Liabilities Net Current": [
        "us-gaap_DeferredTaxAssetsLiabilitiesNetCurrent"
    ],
    "Employee Related Liabilities": ["us-gaap_EmployeeRelatedLiabilitiesCurrent"],
    "Income Taxes Payable": ["us-gaap_AccruedIncomeTaxesCurrent"],
    "Operating Lease Liability": ["us-gaap_OperatingLeaseLiabilityCurrent"],
    "Other Current Liabilities": ["us-gaap_OtherLiabilitiesCurrent"],
    "Cmmercial Paper": ["us-gaap_CommercialPaper"],
    "Long Term Debt Current": ["us-gaap_DebtCurrent", "us-gaap_LongTermDebtCurrent"],
    "Long Term Debt Current and Finance Lease": [
        "us-gaap_LongTermDebtAndCapitalLeaseObligationsCurrent"
    ],
    "Total Current Liabilities": ["us-gaap_LiabilitiesCurrent"],
    # Long Term Liabilities
    "Deffered Lease Incentive": [
        "wsm_DeferredLeaseIncentivesLiabilityNoncurrent",
        "wsm_DeferredRentAndLeaseIncentivesLiabilityNoncurrent",
    ],
    "Long Term Debt and Capital Lease Obligations": [
        "us-gaap_LongTermDebtAndCapitalLeaseObligations"
    ],
    "Deferred Revenue Noncurrent": [
        "us-gaap_DeferredRevenueNoncurrent",
        "us-gaap_ContractWithCustomerLiabilityNoncurrent",
    ],
    "Long Term Lease Liability": [
        "us-gaap_OperatingLeaseLiabilityNoncurrent",
        "amzn_LeaseLiabilityNoncurrent",
    ],
    "Deferred Income Tax": [
        "us-gaap_DeferredIncomeTaxLiabilitiesNet",
        "us-gaap_DeferredTaxLiabilitiesNoncurrent",
    ],
    "Other Long Term Liabilities": [
        "us-gaap_OtherLiabilitiesNoncurrent",
        "us-gaap_LiabilitiesOtherThanLongtermDebtNoncurrent",
    ],
    "Accrued Income Taxes Noncurrent": ["us-gaap_AccruedIncomeTaxesNoncurrent"],
    "Long Term Debt": ["us-gaap_LongTermDebtNoncurrent", "us-gaap_LongTermDebt"],
    "Noncurrent Liabilities": ["us-gaap_LiabilitiesNoncurrent"],
    "Total Liabilities": ["us-gaap_Liabilities"],
    # Stockholders Equity
    "Common Stock Par .01 Issued": [
        "us-gaap_CommonStockValue",
        "us-gaap_CommonStockValueOutstanding",
    ],
    "Preferred Stock Par .01": ["us-gaap_PreferredStockValue"],
    "Common Stock": ["us-gaap_CommonStocksIncludingAdditionalPaidInCapital"],
    "Additional Paid in Capital": [
        "us-gaap_AdditionalPaidInCapital",
        "us-gaap_AdditionalPaidInCapitalCommonStock",
    ],
    "Retained Earnings": ["us-gaap_RetainedEarningsAccumulatedDeficit"],
    "Accumulated Other Comprehensive Income(Loss)": [
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax",
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax",
    ],
    "Treasury Stock at Cost": [
        "us-gaap_TreasuryStockCommonValue",
        "us-gaap_TreasuryStockValue",
    ],
    "Minority Interest": ["us-gaap_MinorityInterest"],
    "Total Equity including Minority Interest": [
        "us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"
    ],
    "Total Stockholders Equity": ["us-gaap_StockholdersEquity"],
    "Total Liabilities and Stockholders Equity": [
        "us-gaap_LiabilitiesAndStockholdersEquity"
    ],
}

Cash_flow_mapping = {
    "Net Earnings": ["us-gaap_ProfitLoss", "us-gaap_NetIncomeLoss"],
    "Depreciation": ["us-gaap_Depreciation"],
    "Amortization": ["us-gaap_AmortizationOfIntangibleAssets"],
    "Depreciation and Amortization": [
        "us-gaap_DepreciationDepletionAndAmortization",
        "us-gaap_DepreciationAmortizationAndAccretionNet",
        "us-gaap_DepreciationAmortizationAndAccretionNet",
        "msft_DepreciationAmortizationAndOther",
    ],
    "Loss on Disposal/Impairment": [
        "us-gaap_GainLossOnSalesOfAssetsAndAssetImpairmentCharges",
        "us-gaap_AssetImpairmentCharges",
    ],
    "Amoritization of Deferred Lease Incentive": [
        "wsm_AmortizationOfDeferredLeaseIncentives",
        "us-gaap_AmortizationOfLeaseIncentives",
        "wsm_AmortizationLeaseIncentives",
        "wsm_AmortizationOfLeaseIncentives",
    ],
    "Non Cash Lease Expense": ["wsm_NoncashLeaseExpense"],
    "Deferred Income Taxes": ["us-gaap_DeferredIncomeTaxExpenseBenefit"],
    "change in fair value of contigent liability": [
        "us-gaap_BusinessCombinationContingentConsiderationArrangementsChangeInAmountOfContingentConsiderationLiability1"
    ],
    "Stock Based Compensation Expense": ["us-gaap_ShareBasedCompensation"],
    "Acquired in process R&D": ["abbv_UpfrontCostsRelatedToCollaborations"],
    "Other Charges Related to collaborations": [
        "abbv_OtherChargesRelatedToCollaborations"
    ],
    "Gain on sale of Other Assets": [
        "us-gaap_GainLossOnSaleOfOtherAssets",
        "msft_GainLossOnInvestmentsAndDerivativeInstruments",
    ],
    "Non Cash Litigation Reserve Adjustment ": [
        "abbv_NonCashLitigationReserveAdjustmentsNetOfCashPayments"
    ],
    "Impairment of Intangible Assets": [
        "us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill"
    ],
    "Other Non Cash Operating Activities": ["us-gaap_OtherNoncashIncomeExpense"],
    "Other Operating Activities": ["us-gaap_OtherOperatingActivitiesCashFlowStatement"],
    "Recognition of Deferred Revenue": ["us-gaap_RecognitionOfDeferredRevenue"],
    # Operating Activities
    "Changes in Accounts Receivable and Other Recivables": [
        "us-gaap_IncreaseDecreaseInAccountsAndOtherReceivables",
        "us-gaap_IncreaseDecreaseInAccountsReceivableAndOtherOperatingAssets",
    ],
    "Changes in Accounts Receivable": ["us-gaap_IncreaseDecreaseInAccountsReceivable"],
    "Changes in Other Receivables": ["us-gaap_IncreaseDecreaseInOtherReceivables"],
    "Changes in Inventory": ["us-gaap_IncreaseDecreaseInInventories"],
    "Changes in Prepaid Expenses and other assets": [
        "us-gaap_IncreaseDecreaseInPrepaidDeferredExpenseAndOtherAssets",
        "us-gaap_IncreaseDecreaseInOtherOperatingAssets",
    ],
    "Changes in Accounts Payable": ["us-gaap_IncreaseDecreaseInAccountsPayable"],
    "Changes in Accounts Payable and Other Liabilities": [
        "us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities"
    ],
    "Changes in Accrued Expenses": [
        "us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities"
    ],
    "Changes in Deferred Revenue": [
        "us-gaap_IncreaseDecreaseInContractWithCustomerLiability",
        "us-gaap_IncreaseDecreaseInDeferredRevenue",
    ],
    "Changes in Other Current Assets": ["us-gaap_IncreaseDecreaseInOtherCurrentAssets"],
    "Changes in Other Noncurrent Assets": [
        "us-gaap_IncreaseDecreaseInOtherNoncurrentAssets"
    ],
    "Changes in Operating Lease Liability": [
        "us-gaap_IncreaseDecreaseInOperatingLeaseLiability",
        "wsm_IncreaseDecreaseInOperatingLeaseLiabilities",
        "us-gaap_OperatingLeasePayments",
    ],
    "Changes in Other Current Liabilities": [
        "us-gaap_IncreaseDecreaseInOtherOperatingLiabilities",
        "us-gaap_IncreaseDecreaseInOtherCurrentLiabilities",
    ],
    "Changes in Other Noncurrent Liabilities": [
        "us-gaap_IncreaseDecreaseInOtherNoncurrentLiabilities"
    ],
    "Changes in Income Taxes Payable": [
        "us-gaap_IncreaseDecreaseInAccruedIncomeTaxesPayable",
        "us-gaap_IncreaseDecreaseInIncomeTaxesPayableNetOfIncomeTaxesReceivable",
    ],
    "Effect of Exchange Rate on Cash and Cash Equivalents": [
        "us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations"
    ],
    "Net Cash Provided by Operating Activities": [
        "us-gaap_NetCashProvidedByUsedInOperatingActivities",
        "us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
    ],
    # Investing Activities
    "Purchase of Marketable Securities": [
        "us-gaap_PaymentsToAcquireAvailableForSaleSecuritiesDebt",
        "us-gaap_PaymentsToAcquireAvailableForSaleSecurities",
        "us-gaap_PaymentsToAcquireMarketableSecurities",
        "us-gaap_PaymentsToAcquireInvestments",
    ],
    "Proceeds from maturity of Marketable Securities": [
        "us-gaap_ProceedsFromMaturitiesPrepaymentsAndCallsOfAvailableForSaleSecurities"
    ],
    "Proceeds from Sale of Marketable Securities": [
        "us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt",
        "us-gaap_ProceedsFromSaleOfAvailableForSaleSecuritiesDebt",
        "us-gaap_ProceedsFromSalesOfAvailableForSaleSecuritiesDebt",
        "us-gaap_ProceedsFromSaleOfAvailableForSaleSecurities",
        "msft_ProceedsFromInvestments",
    ],
    "Proceeds from Sales and Matureties of Marketable Securities": [
        "us-gaap_ProceedsFromSaleMaturityAndCollectionsOfInvestments"
        "msft_ProceedsFromInvestments",
        "us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities",
    ],
    "Purchase of Property, Plant, and Equipment": [
        "us-gaap_PaymentsToAcquirePropertyPlantAndEquipment",
        "us-gaap_PaymentsToAcquireProductiveAssets",
        "amzn_ProceedsFromPropertyPlantAndEquipmentSalesAndIncentives",
    ],
    "Proceeds from Sale of Property, Plant, and Equipment": [
        "amzn_ProceedsFromRebatesOnPurchasesOfProductiveAssets"
    ],
    "Payments for Acquisitions": [
        "us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired",
        "msft_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets",
        "amzn_PaymentsToAcquireBusinessesNetOfCashAcquiredAndOther",
    ],
    "Other Acquisitions and Investments": ["us-gaap_PaymentsToAcquireOtherInvestments"],
    "Other Investing Activities": [
        "us-gaap_PaymentsForProceedsFromOtherInvestingActivities",
        "us-gaap_ProceedsFromSaleAndMaturityOfOtherInvestments",
    ],
    "Securities Lending Collateral": [
        "us-gaap_IncreaseDecreaseInCollateralHeldUnderSecuritiesLending"
    ],
    "Net Cash Used in Investing Activities": [
        "us-gaap_NetCashProvidedByUsedInInvestingActivities",
        "us-gaap_NetCashProvidedByUsedInInvestingActivitiesContinuingOperations",
    ],
    # Financing Activities
    "Repurchases of Common Stock": ["us-gaap_PaymentsForRepurchaseOfCommonStock"],
    "Payment of Dividends": [
        "us-gaap_PaymentsOfDividendsCommonStock",
        "us-gaap_PaymentsOfDividends",
    ],
    "Tax Withholding Related to Stock Based Compensation": [
        "us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation",
        "wsm_TaxWithholdingPaymentRelatedToStockBasedCompensationAwardDistributions",
    ],
    "Proceeds from Issuance of Long Term Debt": [
        "us-gaap_ProceedsFromIssuanceOfLongTermDebt",
        "us-gaap_ProceedsFromDebtMaturingInMoreThanThreeMonths",
    ],
    "Proceeds from Issuance of Common Stock": [
        "us-gaap_ProceedsFromIssuanceOfCommonStock"
    ],
    "Repayment of Long Term Debt": [
        "us-gaap_RepaymentsOfLongTermDebt",
        "us-gaap_RepaymentsOfDebtMaturingInMoreThanThreeMonths",
        "us-gaap_PaymentsOfDebtExtinguishmentCosts",
        "us-gaap_RepaymentsOfDebt",
    ],
    "Repayment of Long Term debt and Finance Lease": [
        "us-gaap_RepaymentsOfLongTermDebtAndCapitalSecurities",
        "amzn_RepaymentsOfLongTermFinancingObligations",
    ],
    "Principal Payments Under Finance Lease": ["us-gaap_FinanceLeasePrincipalPayments"],
    "Proceeds from Short Term Debt and Other": [
        "us-gaap_ProceedsFromRepaymentsOfCommercialPaper",
        "us-gaap_ProceedsFromRepaymentsOfShortTermDebt",
        "us-gaap_ProceedsFromRepaymentsOfShortTermDebtMaturingInThreeMonthsOrLess",
        "amzn_ProceedsFromShortTermDebtAndOtherFinancingActivities",
    ],
    "Proceeds from Exercise of Stock Options": [
        "us-gaap_ProceedsFromStockOptionsExercised"
    ],
    "Payments for Contingent Consideration Liabilities": [
        "us-gaap_PaymentForContingentConsiderationLiabilityFinancingActivities"
    ],
    "Debt Issuance Costs": [
        "us-gaap_PaymentsOfDebtIssuanceCosts",
        "us-gaap_PaymentOfFinancingAndStockIssuanceCosts",
    ],
    "Other Financing Activities": [
        "us-gaap_ProceedsFromPaymentsForOtherFinancingActivities"
    ],
    "Payment of Debt Restructuring Costs": ["us-gaap_PaymentsOfDebtRestructuringCosts"],
    "Borrowings Under Revolving Credit Facility": ["us-gaap_ProceedsFromLinesOfCredit"],
    "Repayments of Short Term Debt": [
        "us-gaap_RepaymentsOfLinesOfCredit",
        "amzn_RepaymentsOfShortTermDebtAndOtherFinancingActivities",
    ],
    "Net Cash Used in Financing Activities": [
        "us-gaap_NetCashProvidedByUsedInFinancingActivities",
        "us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations",
    ],
    "Effect of Exchange Rates on Cash and Cash Equivalents": [
        "us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        "us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents",
    ],
    "Net Change in Cash and Cash Equivalents": [
        "us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect",
        "us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease",
    ],
    "Cash and Cash Equivalents at Begining of Year": [
        "us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        "us-gaap_CashAndCashEquivalentsAtCarryingValue",
    ],
    "Cash Paid for Interest": [
        "us-gaap_InterestPaidNet",
        "us-gaap_InterestPaid",
        "amzn_InterestPaidOnLongTermDebt",
    ],
    "Issuance of Common Stock Attributable to Acquisitions": ["us-gaap_StockIssued1"],
    "Cash Paid for Income Tax Net": [
        "us-gaap_IncomeTaxesPaidNet",
        "us-gaap_IncomeTaxesPaid",
    ],
    "Non-Cash Purchases of PPE Not Yet Paid": [
        "us-gaap_CapitalExpendituresIncurredButNotYetPaid"
    ],
}
