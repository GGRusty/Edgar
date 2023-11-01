balance_mapping = {
    # Current Assets
    "ASSETS": ["us-gaap_AssetsAbstract"],
    "CURRENT ASSETS": ["us-gaap_AssetsCurrentAbstract"],
    "Cash": [
        "us-gaap_CashAndCashEquivalentsAtCarryingValue",
        "us-gaap_CashEquivalentsAtCarryingValue",
    ],
    "Cash and Restricted Cash": [
        "us-gaap_CashCashEquivalentsRestrictedCashAndRestrictedCashEquivalents",
    ],
    "Cash and Short Term Investments": ["CashCashEquivalentsAndShortTermInvestments"],
    "Restricted Cash": [
        "us-gaap_RestrictedCashCurrent",
        "us-gaap_RestrictedCashAndInvestmentsCurrent",
    ],
    "Marketable Securities": [
        "us-gaap_MarketableSecuritiesCurrent",
        "us-gaap_AvailableForSaleSecuritiesCurrent",
        "us-gaap_ShortTermInvestments",
        "us-gaap_AvailableForSaleSecurities",
        "us-gaap_AvailableForSaleSecuritiesDebtSecuritiesCurrent",
        "us-gaap_Investments",
    ],
    "Marketable Debt Securities": [
        "us-gaap_AvailableForSaleSecuritiesDebtSecurities",
        "us-gaap_MarketableSecuritiesFixedMaturities",
    ],
    "Marketable Equity Securities": [
        "us-gaap_EquitySecuritiesFvNi",
        "us-gaap_AvailableForSaleSecuritiesEquitySecurities",
    ],
    "Equity Method Investments": [
        "us-gaap_EquityMethodInvestments",
        "us-gaap_EquitySecuritiesWithoutReadilyDeterminableFairValueAmount",
        "us-gaap_InvestmentsInAffiliatesSubsidiariesAssociatesAndJointVentures",
    ],
    "Loans and Finance Receivables": [
        "us-gaap_NotesReceivableNet",
        "us-gaap_LoansAndLeasesReceivableNetReportedAmount",
    ],
    "Trading Securities": [
        "us-gaap_TradingSecurities",
        "us-gaap_TradingSecuritiesCurrent",
    ],
    "Other Investments": ["us-gaap_OtherInvestments"],
    "Regulatory Assets": ["us-gaap_RegulatoryAssets"],
    "Cash and Cash Equivalents and ST Investments": [
        "us-gaap_CashCashEquivalentsAndShortTermInvestments"
    ],
    "Cash and Cash Equivalents Including Discontinued operations": [
        "us-gaap_CashAndCashEquivalentsAtCarryingValueIncludingDiscontinuedOperations"
    ],
    "Accounts Receivable": [
        "us-gaap_ReceivablesNetCurrent",
        "us-gaap_AccountsReceivableNetCurrent",
        "us-gaap_AccountsAndOtherReceivablesNetCurrent",
        "us-gaap_AccountsNotesAndLoansReceivableNetCurrent",
    ],
    "Other Receivables": [
        "us-gaap_PremiumsAndOtherReceivablesNet",
        "us-gaap_OtherReceivablesNetCurrent",
        "us-gaap_OtherReceivables",
    ],
    "Income Tax Receivable": ["us-gaap_IncomeTaxesReceivable"],
    "Inventory": ["us-gaap_InventoryNet"],
    "Energy Inventory": ["us-gaap_EnergyRelatedInventory"],
    "Materials and Supplies Inventory": [
        "us-gaap_InventoryPartsAndComponentsNetOfReserves",
        "us-gaap_InventoryRawMaterialsAndSuppliesNetOfReserves",
        "us-gaap_InventoryRawMaterialsAndSupplies",
        "us-gaap_OtherInventorySupplies",
    ],
    "Inventory Work in Progress": [
        "us-gaap_InventoryWorkInProcessNetOfReserves",
        "us-gaap_InventoryWorkInProcess",
    ],
    "Finished Goods Inventory": [
        "us-gaap_InventoryFinishedGoodsNetOfReserves",
        "us-gaap_InventoryFinishedGoods",
    ],
    "Finished Goods and Work in Progress Inventory": [
        "us-gaap_InventoryFinishedGoodsAndWorkInProcess"
    ],
    "Chemicals Inventory": ["us-gaap_EnergyRelatedInventoryChemicals"],
    "Prepaid Expenses": [
        "us-gaap_PrepaidExpenseCurrent",
        "us-gaap_NontradeReceivablesCurrent",
    ],
    "Prepaid Expenses and Other Current Assets": [
        "us-gaap_PrepaidExpenseAndOtherAssetsCurrent",
    ],
    "Other Prepaid Expenses": ["us-gaap_OtherPrepaidExpenseCurrent"],
    "Operating Lease Equipment": [
        "us-gaap_DeferredCostsLeasingNetNoncurrent",
        "us-gaap_PropertySubjectToOrAvailableForOperatingLeaseNet",
    ],
    "Land": ["us-gaap_Land"],
    "Buildings and Improvements": ["us-gaap_BuildingsAndImprovementsGross"],
    "Machinery and Equipment": [
        "us-gaap_MachineryAndEquipmentGross",
        "us-gaap_FixturesAndEquipmentGross",
    ],
    "Construction in Progress": ["us-gaap_ConstructionInProgressGross"],
    "Solar Energy Systems": ["tsla_LeasedAssetsNet"],
    "Other Current Assets": ["us-gaap_OtherAssetsCurrent"],
    "Assets Held for Sale": [
        "us-gaap_AssetsHeldForSaleNotPartOfDisposalGroupCurrentOther",
        "us-gaap_DisposalGroupIncludingDiscontinuedOperationPropertyPlantAndEquipment",
        "us-gaap_DisposalGroupIncludingDiscontinuedOperationPropertyPlantAndEquipmentNoncurrent",
        "us-gaap_DisposalGroupIncludingDiscontinuedOperationLongLivedAssetsNoncurrent",
    ],
    "Current Assets of Discontinued Operations": [
        "us-gaap_AssetsOfDisposalGroupIncludingDiscontinuedOperationCurrent",
        "us-gaap_AssetsOfDisposalGroupIncludingDiscontinuedOperation",
    ],
    "Other Assets": ["us-gaap_OtherAssets"],
    "Prepaid Expenses and Other Assets": [
        "us-gaap_PrepaidExpenseAndOtherAssets",
    ],
    "Total Current Assets": ["us-gaap_AssetsCurrent"],
    # Long Term Assets
    "Long Term Marketable Securities": [
        "us-gaap_MarketableSecuritiesNoncurrent",
        "us-gaap_AvailableForSaleSecuritiesNoncurrent",
        "us-gaap_LongTermInvestments",
        "us-gaap_LongTermInvestmentsAndReceivablesNet",
        "us-gaap_AvailableForSaleSecuritiesDebtSecuritiesNoncurrent",
    ],
    "Long Term Non Marketable Securities": ["us-gaap_OtherLongTermInvestments"],
    "Property, Plant, and Equipment": [
        "us-gaap_PropertyPlantAndEquipmentNet",
        "us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization",
    ],
    "Property, Plant, and Equipment Gross": [
        "us-gaap_PropertyPlantAndEquipmentGross",
        "us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetBeforeAccumulatedDepreciationAndAmortization",
    ],
    "Accumulated Depreciation PPE": [
        "us-gaap_AccumulatedDepreciationDepletionAndAmortizationPropertyPlantAndEquipment",
        "us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAccumulatedDepreciationAndAmortization",
    ],
    "Noncurrent Assets": ["us-gaap_NoncurrentAssets"],
    "Digital Assets Net Noncurrent": ["tsla_DigitalAssetsNetNonCurrent"],
    "Intangible Assets": [
        "us-gaap_IntangibleAssetsNetExcludingGoodwill",
        "us-gaap_FiniteLivedIntangibleAssetsNet",
        "us-gaap_IndefiniteLivedIntangibleAssetsExcludingGoodwill",
        "us-gaap_OtherIntangibleAssetsNet",
    ],
    "Operating Lease Right of Use Asset": ["us-gaap_OperatingLeaseRightOfUseAsset"],
    "Deferred Income Tax Asset": [
        "us-gaap_DeferredIncomeTaxAssetsNet",
        "us-gaap_DeferredTaxAssetsNetNoncurrent",
        "us-gaap_DeferredTaxAssetsGrossNoncurrent",
        "us-gaap_DeferredIncomeTaxesAndOtherAssetsNoncurrent",
    ],
    "Goodwill Asset": ["us-gaap_Goodwill"],
    "Long Term Accounts Notes and Loans Receivable": [
        "us-gaap_LongTermAccountsNotesAndLoansReceivableNetNoncurrent",
        "us-gaap_AccountsReceivableExcludingAccruedInterestAfterAllowanceForCreditLossNoncurrent",
        "us-gaap_AccountsReceivableNetNoncurrent",
    ],
    "Other Long Term Assets": [
        "us-gaap_OtherAssetsNoncurrent",
        "us-gaap_OtherAssetsMiscellaneousNoncurrent",
    ],
    "Noncurrent Assets of Discontinued Operations": [
        "us-gaap_DisposalGroupIncludingDiscontinuedOperationAssetsNoncurrent"
    ],
    "Total Long Term Assets": ["us-gaap_AssetsNoncurrent"],
    "Total Assets": ["us-gaap_Assets"],
    # Current Liabilities
    "CURRENT LIABILITIES": ["us-gaap_LiabilitiesCurrentAbstract"],
    "LIABILITIES": ["us-gaap_LiabilitiesAbstract"],
    "Short Term Debt": ["us-gaap_ShortTermBorrowings"],
    "Convertible Debt": ["us-gaap_ConvertibleDebtCurrent"],
    "Accounts Payable": [
        "us-gaap_AccountsPayableCurrent",
        "us-gaap_AccountsPayableTradeCurrent",
    ],
    "Partners Payable": ["us-gaap_AccountsPayableOtherCurrent"],
    "Accrued Expenses": [
        "us-gaap_AccruedLiabilitiesCurrent",
        "amzn_AccruedLiabilitiesAndOtherCurrent",
        "tsla_AccruedAndOtherCurrentLiabilities",
    ],
    "Accrued Member Rewards": [
        "us-gaap_CustomerLoyaltyProgramLiabilityCurrent",
        "us-gaap_CustomerRefundLiabilityCurrent",
    ],
    "Other Accrued Expenses": [
        "us-gaap_OtherAccruedLiabilitiesCurrent",
        "us-gaap_AccrualForTaxesOtherThanIncomeTaxesCurrent",
    ],
    "Unpaid Losses and Loss Adjustment Expenses": [
        "us-gaap_LiabilityForClaimsAndClaimsAdjustmentExpensePropertyCasualtyLiability",
        "us-gaap_LiabilityForClaimsAndClaimsAdjustmentExpense",
    ],
    "Insurance benifit Liabilities": ["us-gaap_LiabilityForFuturePolicyBenefits"],
    "Unearned Premiums": ["us-gaap_UnearnedPremiums"],
    "Other Policyholder Liabilities": ["us-gaap_PolicyholderFunds"],
    "Total current and noncurrent Accounts pay and accrued expenses": [
        "us-gaap_AccountsPayableAndAccruedLiabilitiesCurrentAndNoncurrent"
    ],
    "Notes Payable and Other Borrowings": ["us-gaap_DebtAndCapitalLeaseObligations"],
    "Regulatory Liabilities": ["us-gaap_RegulatoryLiabilities"],
    "Derivative Liabilities": ["us-gaap_DerivativeLiabilities"],
    "Accrued Revenue Share": ["goog_AccruedRevenueShare"],
    "Accounts Payable and Accrued Expenses": [
        "us-gaap_AccountsPayableAndAccruedLiabilitiesCurrent"
    ],
    "Accrued Restructuring Charges": ["us-gaap_RestructuringReserveCurrent"],
    "Deferred Revenue": [
        "us-gaap_ContractWithCustomerLiabilityCurrent",
        "us-gaap_DeferredRevenueAndCreditsCurrent",
        "us-gaap_DeferredRevenueCurrent",
        "us-gaap_OtherDeferredCreditsCurrent",
    ],
    "Resale Value Gaurantee Liability": ["tsla_ResaleValueGuaranteesCurrentPortion"],
    "Deposits": [
        "tsla_CustomerDepositsLiabilitiesCurrent",
        "us-gaap_CustomerDepositsCurrent",
        "us-gaap_CustomerAdvancesCurrent",
        "us-gaap_DepositsAssetsCurrent",
        "us-gaap_InterestBearingDepositsInBanks",
        "us-gaap_TimeDepositsAtCarryingValue",
    ],
    "Deferred Tax Assets Liabilities Current": [
        "us-gaap_DeferredTaxAssetsLiabilitiesNetCurrent",
        "us-gaap_DeferredTaxAssetsNetCurrent",
        "us-gaap_DeferredIncomeTaxesAndOtherAssetsCurrent",
    ],
    "Employee Related Liabilities": ["us-gaap_EmployeeRelatedLiabilitiesCurrent"],
    "Dividends Payable Current": ["us-gaap_DividendsPayableCurrent"],
    "Income Taxes Payable": [
        "us-gaap_AccruedIncomeTaxesCurrent",
        "us-gaap_TaxesPayableCurrent",
    ],
    "Sales Tax Payable": ["us-gaap_SalesAndExciseTaxPayableCurrent"],
    "Operating Lease Liability": ["us-gaap_OperatingLeaseLiabilityCurrent"],
    "Other Current Liabilities": ["us-gaap_OtherLiabilitiesCurrent"],
    "Commercial Paper": ["us-gaap_CommercialPaper"],
    "Long Term Debt Current": ["us-gaap_DebtCurrent", "us-gaap_LongTermDebtCurrent"],
    "Long Term Debt Current and Finance Lease": [
        "us-gaap_LongTermDebtAndCapitalLeaseObligationsCurrent",
        "tsla_LongTermDebtAndFinanceLeasesCurrent",
    ],
    "Current Liabilities of Discontinued Operations": [
        "us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperationCurrent",
        "us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperation",
    ],
    "Due to Related Parties Current": ["us-gaap_DueToRelatedPartiesCurrent"],
    "Total Current Liabilities": ["us-gaap_LiabilitiesCurrent"],
    # Long Term Liabilities
    "Deferred Lease Incentive": [
        "wsm_DeferredLeaseIncentivesLiabilityNoncurrent",
        "wsm_DeferredRentAndLeaseIncentivesLiabilityNoncurrent",
    ],
    "Long Term Debt and Capital Lease Obligations": [
        "us-gaap_LongTermDebtAndCapitalLeaseObligations",
        "us-gaap_CapitalLeaseObligationsNoncurrent",
        "us-gaap_LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities",
    ],
    "Long Term Debt and Finance Leases": [
        "tsla_LongTermDebtAndFinanceLeasesNoncurrent"
    ],
    "Deferred Revenue Noncurrent": [
        "us-gaap_DeferredRevenueNoncurrent",
        "us-gaap_ContractWithCustomerLiabilityNoncurrent",
        "us-gaap_DeferredRevenueAndCreditsNoncurrent",
    ],
    "Long Term Lease Liability": [
        "us-gaap_OperatingLeaseLiabilityNoncurrent",
        "amzn_LeaseLiabilityNoncurrent",
    ],
    "Deferred Income Tax Liabilities Noncurrent": [
        "us-gaap_DeferredTaxLiabilitiesNoncurrent",
        "us-gaap_DeferredTaxLiabilitiesGrossNoncurrent",
        "us-gaap_DeferredIncomeTaxLiabilitiesNet",
        "us-gaap_DeferredIncomeTaxesAndOtherTaxLiabilitiesNoncurrent",
    ],
    "Other Long Term Liabilities": [
        "us-gaap_OtherLiabilitiesNoncurrent",
        "us-gaap_LiabilitiesOtherThanLongtermDebtNoncurrent",
    ],
    "Long Term Liabilities of Discontinued Operations": [
        "us-gaap_LiabilitiesOfDisposalGroupIncludingDiscontinuedOperationNoncurrent"
    ],
    "Long Term Pension Liabilities": [
        "us-gaap_PensionAndOtherPostretirementDefinedBenefitPlansLiabilitiesNoncurrent",
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossDefinedBenefitPensionAndOtherPostretirementPlansNetOfTax",
    ],
    "Litigation Reserve": ["us-gaap_LitigationReserveCurrent"],
    "Accrued Income Taxes Noncurrent": ["us-gaap_AccruedIncomeTaxesNoncurrent"],
    "Accrued Restructuring Charges Noncurrent": [
        "us-gaap_RestructuringReserveNoncurrent"
    ],
    "Long Term Debt": ["us-gaap_LongTermDebtNoncurrent", "us-gaap_LongTermDebt"],
    "Convertible Debt Noncurrent": ["us-gaap_ConvertibleDebtNoncurrent"],
    "Noncurrent Liabilities": ["us-gaap_LiabilitiesNoncurrent"],
    "Total Liabilities": ["us-gaap_Liabilities"],
    "COMMITMENTS AND CONTINGENCIES": ["us-gaap_CommitmentsAndContingencies"],
    "Resale Value Gaurantee Liability Noncurrent": [
        "tsla_ResaleValueGuaranteesNoncurrentPortion"
    ],
    "Restricted Cash Noncurrent": [
        "us-gaap_RestrictedCashAndCashEquivalentsNoncurrent",
        "us-gaap_RestrictedCashAndCashEquivalentsAtCarryingValue",
        "us-gaap_RestrictedCashNoncurrent",
        "us-gaap_RestrictedCashAndInvestmentsNoncurrent",
    ],
    "Convertable Debt Conversion Obligation": [
        "us-gaap_TemporaryEquityValueExcludingAdditionalPaidInCapital"
    ],
    "Convertible Senior Notes": [
        "us-gaap_TemporaryEquityCarryingAmountAttributableToParent",
        "tsla_ConvertibleSeniorNotesIssueToRelatedPartiesNonCurrent",
        "us-gaap_DebtInstrumentConvertibleCarryingAmountOfTheEquityComponent",
    ],
    "Due to Related Parties Noncurrent": ["us-gaap_DueToRelatedPartiesNoncurrent"],
    "Redeemable Noncontrolling Interest": [
        "us-gaap_RedeemableNoncontrollingInterestEquityCarryingAmount",
        "us-gaap_RedeemableNoncontrollingInterestEquityFairValue",
    ],
    # Stockholders Equity
    "STOCKHOLDERS EQUITY": [
        "us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterestAbstract",
        "us-gaap_StockholdersEquityAbstract",
    ],
    "Common Stock Par .01 Issued": [
        "us-gaap_CommonStockValue",
        "us-gaap_CommonStockValueOutstanding",
    ],
    "Preferred Stock Par .01": [
        "us-gaap_PreferredStockValue",
        "us-gaap_PreferredStockValueOutstanding",
        "us-gaap_ConvertiblePreferredStockNonredeemableOrRedeemableIssuerOptionValue",
    ],
    "Preferred Stock Par Per Share": ["us-gaap_PreferredStockParOrStatedValuePerShare"],
    "Common Stock Par Per Share": ["us-gaap_CommonStockParOrStatedValuePerShare"],
    "Common Stock": ["us-gaap_CommonStocksIncludingAdditionalPaidInCapital"],
    "Common Shares Authorized": ["us-gaap_CommonStockSharesAuthorized"],
    "Common Shares Issued": ["us-gaap_CommonStockSharesIssued"],
    "Common Shares Outstanding": ["us-gaap_CommonStockSharesOutstanding"],
    "Common Stock Held in Trust": [
        "us-gaap_CommonStockSharesHeldInEmployeeTrust",
        "us-gaap_CommonStockHeldInTrust",
    ],
    "Preferred Shares Authorized": ["us-gaap_PreferredStockSharesAuthorized"],
    "Preferred Stock Issued": ["us-gaap_PreferredStockSharesIssued"],
    "Preferred Stock Outstanding": ["us-gaap_PreferredStockSharesOutstanding"],
    "Additional Paid in Capital": [
        "us-gaap_AdditionalPaidInCapital",
        "us-gaap_AdditionalPaidInCapitalCommonStock",
    ],
    "Retained Earnings": ["us-gaap_RetainedEarningsAccumulatedDeficit"],
    "Accumulated Other Comprehensive Income investments": [
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossAvailableForSaleSecuritiesAdjustmentNetOfTax"
    ],
    "Foreign Currency Translation Adjustment": [
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossForeignCurrencyTranslationAdjustmentNetOfTax",
    ],
    "Accumulated Other Comprehensive Income(Loss)": [
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossNetOfTax",
    ],
    "Accumulated OCI Derivatives": [
        "us-gaap_AociLossCashFlowHedgeCumulativeGainLossAfterTax",
        "us-gaap_AccumulatedOtherComprehensiveIncomeLossCumulativeChangesInNetGainLossFromCashFlowHedgesEffectNetOfTax",
    ],
    "Treasury Stock at Cost": [
        "us-gaap_TreasuryStockCommonValue",
        "us-gaap_TreasuryStockValue",
    ],
    "Treasury Stock Shares": ["us-gaap_TreasuryStockShares"],
    "Minority Interest": ["us-gaap_MinorityInterest"],
    "Total Equity including Minority Interest": [
        "us-gaap_StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"
    ],
    "Stockholders Equity Before Treasury Stock": [
        "us-gaap_StockholdersEquityBeforeTreasuryStock"
    ],
    "Total Stockholders Equity": ["us-gaap_StockholdersEquity"],
    "Total Liabilities and Stockholders Equity": [
        "us-gaap_LiabilitiesAndStockholdersEquity"
    ],
}
