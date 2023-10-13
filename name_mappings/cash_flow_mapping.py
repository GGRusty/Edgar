cash_mapping = {
    "STATEMENT OF CASH FLOWS": ["us-gaap_StatementOfCashFlowsAbstract"],
    "OPERATING ACTIVITIES": [
        "us-gaap_NetCashProvidedByUsedInOperatingActivitiesAbstract"
    ],
    "ADJUSTMENTS": [
        "us-gaap_AdjustmentsToReconcileNetIncomeLossToCashProvidedByUsedInOperatingActivitiesAbstract"
    ],
    "Net Earnings": ["us-gaap_ProfitLoss", "us-gaap_NetIncomeLoss"],
    "Depreciation": [
        "us-gaap_Depreciation",
        "goog_DepreciationAndImpairmentOnDispositionOfPropertyAndEquipment",
    ],
    "Amortization": [
        "us-gaap_AmortizationOfIntangibleAssets",
        "goog_AmortizationAndImpairmentOfIntangibleAssets",
    ],
    "Depreciation and Amortization": [
        "us-gaap_DepreciationDepletionAndAmortization",
        "us-gaap_DepreciationAmortizationAndAccretionNet",
        "us-gaap_DepreciationAmortizationAndAccretionNet",
        "msft_DepreciationAmortizationAndOther",
        "us-gaap_DepreciationAndAmortization",
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
    "Amortization of Debt Discount": ["us-gaap_AmortizationOfDebtDiscountPremium"],
    "Acquisition Termination Costs": [
        "nvda_BusinessCombinationAdvancedConsiderationWrittenOff",
    ],
    "Non Cash Lease Expense": ["wsm_NoncashLeaseExpense"],
    "Deferred Income Taxes": [
        "us-gaap_DeferredIncomeTaxExpenseBenefit",
        "us-gaap_DeferredIncomeTaxesAndTaxCredits",
    ],
    "change in fair value of contigent liability": [
        "us-gaap_BusinessCombinationContingentConsiderationArrangementsChangeInAmountOfContingentConsiderationLiability1"
    ],
    "Stock Based Compensation Expense": [
        "us-gaap_ShareBasedCompensation",
        "goog_NetProceedsPaymentsRelatedToStockBasedAwardActivities",
    ],
    "Acquired in process R&D": ["abbv_UpfrontCostsRelatedToCollaborations"],
    "Other Charges Related to collaborations": [
        "abbv_OtherChargesRelatedToCollaborations"
    ],
    "Gain on sale of Other Assets": [
        "us-gaap_GainLossOnSaleOfOtherAssets",
        "msft_GainLossOnInvestmentsAndDerivativeInstruments",
        "us-gaap_GainLossOnSaleOfInvestments",
        "us-gaap_GainLossOnInvestments",
        "nvda_GainsonSalesoflonglivedassetsandinvestment",
        "us-gaap_DebtAndEquitySecuritiesGainLoss",
    ],
    "Non Cash Litigation Reserve Adjustment ": [
        "abbv_NonCashLitigationReserveAdjustmentsNetOfCashPayments"
    ],
    "Impairment of Intangible Assets": [
        "us-gaap_ImpairmentOfIntangibleAssetsExcludingGoodwill"
    ],
    "Other Non Cash Operating Activities": ["us-gaap_OtherNoncashIncomeExpense"],
    "Other Operating Activities": [
        "us-gaap_OtherOperatingActivitiesCashFlowStatement",
        "us-gaap_OtherOperatingIncomeExpenseNet",
    ],
    "Recognition of Deferred Revenue": ["us-gaap_RecognitionOfDeferredRevenue"],
    "Loss On early Extinguishment of Debt": [
        "us-gaap_GainsLossesOnExtinguishmentOfDebt"
    ],
    # Operating Activities
    "CHANGES IN OPERATING CAPITAL": [
        "us-gaap_IncreaseDecreaseInOperatingCapitalAbstract"
    ],
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
        "nvda_PrepaidExpensesAndOtherCurrentAsset",
    ],
    "Changes in Accounts Payable": ["us-gaap_IncreaseDecreaseInAccountsPayable"],
    "Changes in Accounts Payable and Other Liabilities": [
        "us-gaap_IncreaseDecreaseInAccountsPayableAndAccruedLiabilities"
    ],
    "Changes in Accrued Expenses": [
        "us-gaap_IncreaseDecreaseInAccruedLiabilitiesAndOtherOperatingLiabilities",
        "nvda_AccruedLiabilitiesAndOtherLongTermLiabilities",
        "us-gaap_IncreaseDecreaseInAccruedLiabilities",
    ],
    "Changes in Accrued Revenue Share": ["goog_IncreaseDecreaseInAccruedRevenueShare"],
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
        "us-gaap_IncreaseDecreaseInIncomeTaxes",
    ],
    "Net Cash Provided by Operating Activities": [
        "us-gaap_NetCashProvidedByUsedInOperatingActivities",
        "us-gaap_NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
    ],
    # Investing Activities
    "INVESTING ACTIVITIES": [
        "us-gaap_NetCashProvidedByUsedInInvestingActivitiesAbstract"
    ],
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
        "us-gaap_ProceedsFromSaleMaturityAndCollectionsOfInvestments",
        "msft_ProceedsFromInvestments",
        "us-gaap_ProceedsFromSaleAndMaturityOfMarketableSecurities",
        "us-gaap_ProceedsFromCollectionOfNotesReceivable",
    ],
    "Purchase of Property, Plant, and Equipment": [
        "us-gaap_PaymentsToAcquirePropertyPlantAndEquipment",
        "us-gaap_PaymentsToAcquireProductiveAssets",
        "us-gaap_PaymentsForProceedsFromProductiveAssets",
        "nvda_PurchasesOfPropertyAndEquipmentAndIntangibleAssets",
    ],
    "Proceeds from Sale of Property, Plant, and Equipment": [
        "amzn_ProceedsFromRebatesOnPurchasesOfProductiveAssets",
        "amzn_ProceedsFromPropertyPlantAndEquipmentSalesAndIncentives",
    ],
    "Proceeds from Sale of Long Live Assets": [
        "nvda_Proceedsfromsaleoflonglivedassetsandinvestments"
    ],
    "Payments for Acquisitions": [
        "us-gaap_PaymentsToAcquireBusinessesNetOfCashAcquired",
        "msft_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets",
        "amzn_PaymentsToAcquireBusinessesNetOfCashAcquiredAndOther",
        "us-gaap_PaymentsToAcquireBusinessesAndInterestInAffiliates",
        "goog_AcquisitionsNetOfCashAcquiredAndPurchasesOfIntangibleAndOtherAssets",
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
    "FINANCING ACTIVITIES": [
        "us-gaap_NetCashProvidedByUsedInFinancingActivitiesAbstract"
    ],
    "Repurchases of Common Stock": ["us-gaap_PaymentsForRepurchaseOfCommonStock"],
    "Payment of Dividends": [
        "us-gaap_PaymentsOfDividendsCommonStock",
        "us-gaap_PaymentsOfDividends",
    ],
    "Tax Withholding Related to Stock Based Compensation": [
        "us-gaap_PaymentsRelatedToTaxWithholdingForShareBasedCompensation",
        "wsm_TaxWithholdingPaymentRelatedToStockBasedCompensationAwardDistributions",
    ],
    "Tax Benefit Related to Stock Based Compensation financing": [
        "us-gaap_ExcessTaxBenefitFromShareBasedCompensationFinancingActivities",
    ],
    "Tax Benefit Related to Stock Based Compensation operating": [
        "us-gaap_ExcessTaxBenefitFromShareBasedCompensationOperatingActivities",
        "nvda_Netproceedspaymentsrelatedtoemployeestockplans",
    ],
    "Proceeds from Issuance of Long Term Debt": [
        "us-gaap_ProceedsFromIssuanceOfLongTermDebt",
        "us-gaap_ProceedsFromDebtMaturingInMoreThanThreeMonths",
        "us-gaap_ProceedsFromRepaymentsOfLongTermDebtAndCapitalSecurities",
        "us-gaap_ProceedsFromDebtNetOfIssuanceCosts",
        "us-gaap_ProceedsFromConvertibleDebt",
    ],
    "Proceeds from Issuance of Common Stock": [
        "us-gaap_ProceedsFromIssuanceOfCommonStock"
    ],
    "Proceeds from Issuance of Warrants": ["us-gaap_ProceedsFromIssuanceOfWarrants"],
    "Repayment of Long Term Debt": [
        "us-gaap_RepaymentsOfLongTermDebt",
        "us-gaap_RepaymentsOfDebtMaturingInMoreThanThreeMonths",
        "us-gaap_PaymentsOfDebtExtinguishmentCosts",
        "us-gaap_RepaymentsOfDebt",
    ],
    "Repayment of Long Term debt and Finance Lease": [
        "us-gaap_RepaymentsOfLongTermDebtAndCapitalSecurities",
        "amzn_RepaymentsOfLongTermFinancingObligations",
        "amzn_RepaymentsOfLongTermFinanceLeaseObligations",
        "amzn_RepaymentsOfLongTermfFinancingLeaseObligations",
        "us-gaap_RepaymentsOfDebtAndCapitalLeaseObligations",
    ],
    "Repayment of Convertible Notes": ["us-gaap_RepaymentsOfConvertibleDebt"],
    "Principal Payments Under Finance Lease": [
        "us-gaap_FinanceLeasePrincipalPayments",
        "us-gaap_RepaymentsOfLongTermCapitalLeaseObligations",
        "nvda_PaymentsForFinancedPropertyPlantAndEquipmentFinancingActivities",
    ],
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
    "Payments for Hedges": ["us-gaap_PaymentsForHedgeFinancingActivities"],
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
    "Proceeds from Minority Interest": ["us-gaap_ProceedsFromMinorityShareholders"],
    "Net Cash Used in Financing Activities": [
        "us-gaap_NetCashProvidedByUsedInFinancingActivities",
        "us-gaap_NetCashProvidedByUsedInFinancingActivitiesContinuingOperations",
    ],
    "Effect of Exchange Rates on Cash and Cash Equivalents": [
        "us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        "us-gaap_EffectOfExchangeRateOnCashAndCashEquivalents",
        "us-gaap_EffectOfExchangeRateOnCashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsIncludingDisposalGroupAndDiscontinuedOperations",
    ],
    "Net Change in Cash and Cash Equivalents": [
        "us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalentsPeriodIncreaseDecreaseIncludingExchangeRateEffect",
        "us-gaap_CashAndCashEquivalentsPeriodIncreaseDecrease",
    ],
    # supplemental cash flow information
    "SUPPLEMENTAL INFO": ["us-gaap_SupplementalCashFlowInformationAbstract"],
    "Cash and Cash Equivalents at Begining of Year": [
        "us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
        "us-gaap_CashAndCashEquivalentsAtCarryingValue",
    ],
    "Cash Paid for Interest": [
        "us-gaap_InterestPaidNet",
        "us-gaap_InterestPaid",
        "amzn_InterestPaidOnLongTermDebt",
    ],
    "Cash Paid for Interest on Capital Lease": [
        "amzn_InterestPaidOnCapitalLeaseObligations",
        "us-gaap_FinanceLeaseInterestPaymentOnLiability",
    ],
    "Cash Paid for interest on Financing Obligations": [
        "amzn_InterestPaidFinancingObligations"
    ],
    "Issuance of Common Stock Attributable to Acquisitions": ["us-gaap_StockIssued1"],
    "Assets Acquired Under Operating Lease": [
        "us-gaap_RightOfUseAssetObtainedInExchangeForOperatingLeaseLiability"
    ],
    "Cash Paid for Income Tax Net": [
        "us-gaap_IncomeTaxesPaidNet",
        "us-gaap_IncomeTaxesPaid",
    ],
    # Non Cash Investing and Financing Activities
    "NON CASH INVESTING AND FINANCING ACTIVITIES": [
        "us-gaap_OtherNoncashInvestingAndFinancingItemsAbstract"
    ],
    "Non-Cash Restructuring Charges": ["nvda_RestructuringchargesNoncash"],
    "Non-Cash Purchases of PPE Not Yet Paid": [
        "us-gaap_CapitalExpendituresIncurredButNotYetPaid"
    ],
    "Change in Unrealized Gain/Loss on Marketable Securities": [
        "us-gaap_UnrealizedGainLossOnSecurities"
    ],
    "PPE Acquired Under Finance Lease": [
        "us-gaap_CapitalLeaseObligationsIncurred",
        "us-gaap_RightOfUseAssetObtainedInExchangeForFinanceLeaseLiability",
        "us-gaap_NoncashOrPartNoncashAcquisitionFixedAssetsAcquired1",
    ],
    "PPE Acquired Under Build to Suit Arrangement": [
        "amzn_PropertyandEquipmentObtainedinExchangeforFinancingObligations",
        "amzn_BuildToSuitLeaseObligationsIncurred",
    ],
    "Assets Acquired By Assumption of Liabilities": ["us-gaap_LiabilitiesAssumed1"],
}
