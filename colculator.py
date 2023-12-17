class RealEstateInvestment:
    def __init__(self):
        self.cost_of_investment  =  []
        self.gross_income  = []
        self.cash_on_cash = []
        self.total_cost_investment = 0
        self.net_gain = 0

    def enter_property_amount(self):
        prop_cost = input("Approximately  how much is the value of the property you're looking to buy? 'n (just type numbers, no  specail characters):\n $")
        if prop_cost.isdigit():
            self.cost_of_investment.append(int(prop_cost))

        else:
            print("The input you entered isn't valid. please try again")
            self.enter_property_amount()

    def enter_monthly_income(self):
        gross_inc = input("What do you  think your approximate gross income will be monthly? \n (Just type numbers, no special characters): \n  $")
        if gross_inc.isdigit():
            self.gross_income.append(int(gross_inc))
        else:
            print("The input you entered isn't valid. please try again")
            self.enter_monthly_income()



        utilities = input("What do you expect your utilities to be monthly?(Gas and/or ELectric, Internet, etc.)\n (Just type numbers, no special characters): \n $")
        if utilities.isdigit():
            self.gross_income.append(int(utilities))
        else:
            print("The input you entered isn't valid. please try again")
            self.enter_monthly_income()

        approx_taxins = input("What do you think the approximate monthly property taxes and insurance will be? \n(Just type numbers, no special characters):\n $")
        if approx_taxins.isdigit():
            self.gross_income.append(int(approx_taxins))
        else:
            print("The input you entered isn't valid. please try again")
            self.enter_monthly_income()

    def enter_cash_on_cash(self):
        cashdown = input("How much cash  are you putting down?(Including Downpayment,Closing Cost, and Rehab Costs)\n(Just type numbers, no special characters):\n $")
        if cashdown.isdigit():
            self.cash_on_cash.append(int(cashdown))
        else:
            print("The input you entered isn't valid. please try again")
            self.enter_cash_on_cash()

    def calculate_results(self):
        self.total_cost_investment = sum(self.cost_of_investment) +  sum(self.cash_on_cash)
        self.net_gain  = self.gross_income[0] - self.gross_income[1] - self.gross_income[2] if len(self.gross_income) >= 3 else 0

    def display_result(self):
        print(f"initial cost of investment: ${self.cost_of_investment[0]}")
        print(f"Gross income (money in before taxes out): ${self.gross_income[0]}")
        print(f"Cash/Loans taken out to put down on the propety: ${self.cash_on_cash[0]}")
        print(f"Net gain: ${self.net_gain}")
        print(f"Total cost of investment: ${self.total_cost_investment}")
        roi = (self.net_gain  / self.total_cost_investment) * 100 if self.total_cost_investment != 0 else 0
        print(f"Approx ROI: {round(roi, 2)}%")


investment = RealEstateInvestment()

investment.enter_property_amount()
investment.enter_monthly_income()
investment.enter_cash_on_cash()

investment.calculate_results()
investment.display_result()