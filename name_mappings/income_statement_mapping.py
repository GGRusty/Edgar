income_mapping = {
    "INCOME STATEMENT": ["us-gaap_IncomeStatementAbstract"],
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
    "Cost of Revenue": [
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
    # Operating Expenses
    "OPERATING EXPENSES": [
        "us-gaap_OperatingExpensesAbstract",
        "us-gaap_CostsAndExpensesAbstract",
    ],
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
        "nvda_BusinessCombinationAdvancedConsiderationWrittenOff",
        "us-gaap_LossContingencyLossInPeriod",
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
    # EPS
    "EARNINGS PER SHARE": ["us-gaap_EarningsPerShareAbstract"],
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
    # Share Information
    "SHARE INFORMATION": [
        "us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract"
    ],
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
    "Common Dividend per Share Paid": ["us-gaap_CommonStockDividendsPerShareCashPaid"],
}
