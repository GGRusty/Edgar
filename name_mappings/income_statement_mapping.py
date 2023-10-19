income_mapping = {
    "INCOME STATEMENT": ["us-gaap_IncomeStatementAbstract"],
    # Revenue
    "REVENUE": ["us-gaap_RevenuesAbstract"],
    "Net Revenue": [
        "us-gaap_RevenueFromContractWithCustomerExcludingAssessedTax",
        "us-gaap_SalesRevenueNet",
        "us-gaap_Revenues",
        "xom_TotalRevenuesAndOtherIncome",
        "us-gaap_RevenueFromContractWithCustomerIncludingAssessedTax",
    ],
    "Goods Revenue": ["us-gaap_SalesRevenueGoodsNet"],
    "Service Revenue": [
        "msft_SalesRevenueServicesAndOtherNet",
        "us-gaap_SalesRevenueServicesNet",
    ],
    "Oil and Gas Revenue": ["us-gaap_OilAndGasRevenue"],
    "Investment and Derivative Revenue": [
        "us-gaap_NonoperatingGainsLosses",
    ],
    "Investment Revenue": [
        "us-gaap_GainLossOnInvestments",
        "us-gaap_GainLossOnInvestmentsExcludingOtherThanTemporaryImpairments",
        "us-gaap_InvestmentIncomeNet",
    ],
    "Derivative Revenue": ["us-gaap_GainLossOnDerivativeInstrumentsNetPretax"],
    "Other Revenue": [
        "us-gaap_OtherIncome",
        "us-gaap_OtherSalesRevenueNet",
    ],
    "Other Finanacial Products Revenue": [
        "us-gaap_RevenueOtherFinancialServices",
    ],
    "Permanent Impairment of Investments": [
        "us-gaap_OtherThanTemporaryImpairmentLossesInvestmentsPortionRecognizedInEarningsNet",
        "us-gaap_ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",
    ],
    # Cost of Revenue
    "COST OF REVENUE": ["us-gaap_CostOfRevenueAbstract"],
    "Cost of Revenue": [
        "us-gaap_CostOfGoodsAndServicesSold",
        "us-gaap_CostOfRevenue",
    ],
    "Cost of Goods Sold": [
        "wsm_CostOfGoodsSoldAndOccupancyExpenses",
        "us-gaap_CostOfGoodsSold",
    ],
    "Cost of Services": ["msft_CostOfServicesAndOther"],
    "Oil and Gas Cost": ["us-gaap_CostOfPurchasedOilAndGas"],
    "Fulfillment Expense": ["amzn_FulfillmentExpense"],
    "Tech and Content Expense": ["amzn_TechnologyAndContentExpense"],
    "Marketing Expense": [
        "us-gaap_MarketingExpense",
        "us-gaap_MarketingAndAdvertisingExpense",
    ],
    "Networking and Processing Expense": [
        "us-gaap_CommunicationsAndInformationTechnology"
    ],
    "Amortization of Intangible Assets": [
        "us-gaap_AmortizationOfIntangibleAssets",
        "abt_AmortizationOfIntangibleAssetsExcludingDiscontinuedOperations",
    ],
    "Labor Expense": ["us-gaap_LaborAndRelatedExpense"],
    "Professional Fees": ["us-gaap_ProfessionalFees"],
    "Exploration Expense": ["us-gaap_ExplorationExpense"],
    "Goodwill and Intangible Asset Impairment": [
        "us-gaap_GoodwillAndIntangibleAssetImpairment"
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
    "Research and Development in Process": ["us-gaap_ResearchAndDevelopmentInProcess"],
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
        "us-gaap_OtherFinancialServicesCosts",
    ],
    "Medical Costs": ["us-gaap_PolicyholderBenefitsAndClaimsIncurredHealthCare"],
    "Operating Expenses": [
        "us-gaap_OperatingExpenses",
        "us-gaap_CostsAndExpenses",
        "us-gaap_OperatingCostsAndExpenses",
    ],
    "Operating Income": ["us-gaap_OperatingIncomeLoss"],
    "NON-OPERATING": ["us-gaap_NonoperatingIncomeExpenseAbstract"],
    "Non-Operating Income": ["us-gaap_NonoperatingIncomeExpense"],
    "Interest Expense": [
        "us-gaap_InterestExpense",
        "us-gaap_InterestExpenseDebt",
    ],
    "Interest Income": [
        "wsm_NetInterestIncomeAndExpense",
        "wsm_NetInterestIncomeExpense",
        "us-gaap_InterestIncomeExpenseNonoperatingNet",
        "us-gaap_InvestmentIncomeInterest",
        "us-gaap_InvestmentIncomeInterestAndDividend",
        "us-gaap_InterestIncomeExpenseNet",
    ],
    "Equity Investemnts Income": [
        "us-gaap_IncomeLossFromEquityMethodInvestments",
        "us-gaap_EquitySecuritiesFvNiGainLoss",
    ],
    "Net Foreign Currency Exchange Gain": [
        "us-gaap_ForeignCurrencyTransactionGainLossBeforeTax"
    ],
    "Restucturing and Other Special Charges": [
        "us-gaap_RestructuringCharges",
        "msft_ImpairmentAndRestructuringExpenses",
        "msft_ImpairmentIntegrationAndRestructuringExpenses",
        "nvda_BusinessCombinationAdvancedConsiderationWrittenOff",
        "us-gaap_LossContingencyLossInPeriod",
        "tsla_RestructuringAndOtherExpenses",
        "us-gaap_RestructuringSettlementAndImpairmentProvisions",
        "us-gaap_LossContingencyAccrualCarryingValueProvision",
        "us-gaap_AssetImpairmentCharges",
    ],
    "Contract Termination Costs": ["us-gaap_LossOnContractTermination"],
    "Depreciation and Amortization": [
        "us-gaap_DepreciationAndAmortization",
        "us-gaap_DepreciationDepletionAndAmortization",
    ],
    "Litigation Settlement Expense": ["us-gaap_LitigationSettlementExpense"],
    "Other Expense Non-Operating": [
        "us-gaap_OtherNonoperatingIncomeExpense",
        "us-gaap_OtherNonoperatingIncome",
    ],
    "Non Service Pension Expense": [
        "us-gaap_NetPeriodicDefinedBenefitsExpenseReversalOfExpenseExcludingServiceCostComponent"
    ],
    "EBT": [
        "us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest",
    ],
    "EBT and equity investments": [
        "us-gaap_IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments"
    ],
    "Taxes": ["us-gaap_IncomeTaxExpenseBenefit"],
    "Other Taxes": ["us-gaap_TaxesOther"],
    "Sales Tax": ["us-gaap_ExciseAndSalesTaxes"],
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
    "EPS": [
        "us-gaap_EarningsPerShareBasic",
        "us-gaap_EarningsPerShareBasicAndDiluted",
    ],  # have to change BRK-B becuase it is using the brk-a eps
    "EPS Diluted Cont. Operations": [
        "us-gaap_IncomeLossFromContinuingOperationsPerDilutedShare"
    ],
    "EPS Diluted Discont. Operations": [
        "us-gaap_IncomeLossFromDiscontinuedOperationsNetOfTaxPerDilutedShare"
    ],
    "EPS Diluted": ["us-gaap_EarningsPerShareDiluted"],
    # Share Information
    "SHARE INFORMATION": [
        "us-gaap_WeightedAverageNumberOfSharesOutstandingDilutedDisclosureItemsAbstract",
        "us-gaap_WeightedAverageNumberOfSharesOutstandingAbstract",
    ],
    "Weighted Average Shares Outstanding": [
        "us-gaap_WeightedAverageNumberOfSharesOutstandingBasic",
        "us-gaap_WeightedAverageNumberOfShareOutstandingBasicAndDiluted",
    ],
    "Dilutive Common Stock Options": [
        "us-gaap_IncrementalCommonSharesAttributableToShareBasedPaymentArrangements"
    ],
    "Dilutive effect of common share equivalents": [
        "us-gaap_WeightedAverageNumberDilutedSharesOutstandingAdjustment"
    ],
    "Weighted Average Shares Diluted": [
        "us-gaap_WeightedAverageNumberOfDilutedSharesOutstanding"
    ],
    "Anti Dilutive Common Stock Options": [
        "us-gaap_AntidilutiveSecuritiesExcludedFromComputationOfEarningsPerShareAmount"
    ],
    "Declared Dividends per Share": ["us-gaap_CommonStockDividendsPerShareDeclared"],
    "Common Dividend per Share Paid": ["us-gaap_CommonStockDividendsPerShareCashPaid"],
    "Preferred Dividends paid": [
        "us-gaap_PreferredStockDividendsIncomeStatementImpact"
    ],
    # Special Purpose Items
    "Automotive Sales Revenue": ["tsla_AutomotiveSalesRevenue"],
    "Energy Services": ["us-gaap_SalesRevenueEnergyServices"],
    "Automotive Regulatory Credits": ["tsla_AutomotiveRegulatoryCredits"],
    "Leasing Revenue": [
        "tsla_AutomotiveLeasing",
        "us-gaap_OperatingLeasesIncomeStatementLeaseRevenue",
        "us-gaap_OperatingLeaseLeaseIncome",
    ],
    "Service and other Revenue": ["tsla_SalesRevenueServicesAndOtherNet"],
    "Total Automotive Revenue": [
        "tsla_AutomotiveRevenues",
        "tsla_SalesRevenueAutomotive",
    ],
    "Premiums Revenue": ["us-gaap_PremiumsEarnedNet"],
    "Insurance Losses and Loss Adjustment Expenses": [
        "us-gaap_LiabilityForUnpaidClaimsAndClaimsAdjustmentExpenseIncurredClaims1",
        "us-gaap_IncurredClaimsPropertyCasualtyAndLiability",
    ],
    "Cost of Automotive Revenue": ["tsla_AutomotiveSales"],
    "Cost of Leased Equipment": [
        "us-gaap_DirectCostsOfLeasedAndRentedPropertyOrEquipment",
        "tsla_CostOfAutomotiveLeasing",
    ],
    "Cost of Energy Services": ["us-gaap_CostOfServicesEnergyServices"],
    "Total Cost of Automotive Revenue": [
        "tsla_AutomotiveCostOfRevenues",
        "tsla_CostOfRevenuesAutomotive",
    ],
    "Cost of Service and Other Revenue": ["tsla_CostOfServicesAndOther"],
    "Buyout of Noncontrolling Interest": ["tsla_BuyOutOfNoncontrollingInterest"],
    "Share Based Compensation Expense": [
        "us-gaap_AllocatedShareBasedCompensationExpense"
    ],
    "Undistributed Earnings Loss Allocated to Participating Securities": [
        "us-gaap_UndistributedEarningsLossAllocatedToParticipatingSecuritiesBasic"
    ],
}
