balance_mapping = {
    # Current Assets
    "CURRENT ASSETS": ["us-gaap_AssetsCurrentAbstract"],
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
    "Income Tax Receivable": ["us-gaap_IncomeTaxesReceivable"],
    "Inventory": ["us-gaap_InventoryNet"],
    "Prepaid Expenses": [
        "us-gaap_PrepaidExpenseCurrent",
        "us-gaap_NontradeReceivablesCurrent",
    ],
    "Prepaid Expenses and Other Current Assets": [
        "us-gaap_PrepaidExpenseAndOtherAssets",
        "us-gaap_PrepaidExpenseAndOtherAssetsCurrent",
    ],
    "Other Current Assets": ["us-gaap_OtherAssetsCurrent"],
    "Total Current Assets": ["us-gaap_AssetsCurrent"],
    # Long Term Assets
    "Long Term Marketable Securities": [
        "us-gaap_MarketableSecuritiesNoncurrent",
        "us-gaap_AvailableForSaleSecuritiesNoncurrent",
        "us-gaap_LongTermInvestments",
    ],
    "Long Term Non Marketable Securities": ["us-gaap_OtherLongTermInvestments"],
    "Property, Plant, and Equipment": [
        "us-gaap_PropertyPlantAndEquipmentNet",
        "us-gaap_PropertyPlantAndEquipmentAndFinanceLeaseRightOfUseAssetAfterAccumulatedDepreciationAndAmortization",
    ],
    "Intangible Assets": [
        "us-gaap_IntangibleAssetsNetExcludingGoodwill",
        "us-gaap_FiniteLivedIntangibleAssetsNet",
    ],
    "Operating Lease Right of Use Asset": ["us-gaap_OperatingLeaseRightOfUseAsset"],
    "Deffered Income Tax Asset": [
        "us-gaap_DeferredIncomeTaxAssetsNet",
        "us-gaap_DeferredTaxAssetsNetNoncurrent",
        "us-gaap_DeferredTaxAssetsGrossNoncurrent",
    ],
    "Goodwill": ["us-gaap_Goodwill"],
    "Other Long Term Assets": [
        "us-gaap_OtherAssetsNoncurrent",
    ],
    "Total Long Term Assets": ["us-gaap_AssetsNoncurrent"],
    "Total Assets": ["us-gaap_Assets"],
    # Current Liabilities
    "CURRENT LIABILITIES": ["us-gaap_LiabilitiesCurrentAbstract"],
    "Short Term Debt": ["us-gaap_ShortTermBorrowings"],
    "Convertible Debt": ["us-gaap_ConvertibleDebtCurrent"],
    "Accounts Payable": ["us-gaap_AccountsPayableCurrent"],
    "Accrued Expenses": [
        "us-gaap_AccruedLiabilitiesCurrent",
        "amzn_AccruedLiabilitiesAndOtherCurrent",
    ],
    "Accrued Revenue Share": ["goog_AccruedRevenueShare"],
    "Accounts Payable and Accrued Expenses": [
        "us-gaap_AccountsPayableAndAccruedLiabilitiesCurrent"
    ],
    "Deferred Revenue": [
        "us-gaap_ContractWithCustomerLiabilityCurrent",
        "us-gaap_DeferredRevenueAndCreditsCurrent",
        "us-gaap_DeferredRevenueCurrent",
    ],
    "Deferred Tax Assets Liabilities Net Current": [
        "us-gaap_DeferredTaxAssetsLiabilitiesNetCurrent",
        "us-gaap_DeferredTaxAssetsNetCurrent",
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
        "us-gaap_LongTermDebtAndCapitalLeaseObligations",
        "us-gaap_CapitalLeaseObligationsNoncurrent",
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
    "Convertible Debt Noncurrent": ["us-gaap_ConvertibleDebtNoncurrent"],
    "Noncurrent Liabilities": ["us-gaap_LiabilitiesNoncurrent"],
    "Total Liabilities": ["us-gaap_Liabilities"],
    "COMMITMENTS AND CONTINGENCIES": ["us-gaap_CommitmentsAndContingencies"],
    "Convertable Debt Conversion Obligation": [
        "us-gaap_TemporaryEquityValueExcludingAdditionalPaidInCapital"
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
    "Common Stock": ["us-gaap_CommonStocksIncludingAdditionalPaidInCapital"],
    "Common Shares Authorized": ["us-gaap_CommonStockSharesAuthorized"],
    "Preferred Shares Authorized": ["us-gaap_PreferredStockSharesAuthorized"],
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
