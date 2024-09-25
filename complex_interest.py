import datetime as dt

class ComplexInterest:
    '''
    The class calculates complex interest rate based on monthy investment, time period and interest rate.
    '''
    def __init__(self,monthly_investment:int, period:tuple, percent_interest:float):
        if monthly_investment < 0 or not isinstance(monthly_investment,int):
            raise ValueError("Monthly investment must be a positive int value")
        self.year_investment = monthly_investment*12
        if not isinstance(period,tuple) or not isinstance(period[0],dt.date):
            raise ValueError('Period must be a datetime tuple: start/end date')
        self.period = period
        if not isinstance(percent_interest,float):
            raise ValueError('percent interest must be a float value i.e. 10% will be 0.10')
        self.percent_interest = percent_interest
        self.total_invested = 0
        self.total_profit = 0

    def report(self):
        accumulate = 0
        years = self.period[1].year - self.period[0].year
        profit = self.year_investment * self.percent_interest
        rep = {
                "period":{
                    "start":self.period[0],
                    'end':self.period[1]
                },
                'monthly investment':self.year_investment/12,
                'averate yearly interest rate':self.percent_interest*100,
                "yearly":[]
              }
        for y in range(1,years+1):
            self.total_invested += self.year_investment
            accumulate += self.year_investment + profit
            profit = accumulate * self.percent_interest
            rep['yearly'].append({'year':y,
                                  'invested': self.total_invested,
                                  'profit':round(profit,2),
                                  'current':round(accumulate,2)})
        return rep

    def totals(self):
        self.total_invested = 0
        self.total_profit = 0
        years = self.period[1].year - self.period[0].year
        profit = self.year_investment * self.percent_interest
        accumulate = 0
        for y in range(1,years+1):
            self.total_invested += self.year_investment
            accumulate += self.year_investment + profit
            profit = round(accumulate*self.percent_interest,2)
        self.total_profit += profit
        return {'total invetment':self.total_invested,
                'total profit':self.total_profit}

# cx_interest = ComplexInterest(1000,(dt.date(2024,9,16),dt.date(2031,9,16)),0.10)

# report = cx_interest.report()
# print(report['yearly'])
# totals = cx_interest.totals()
# print(totals)

class FinFormulas:
    def __init__(self,assets:float,liabilities:float,equity:float) -> None:
        self._assets = assets
        self._liabilities = liabilities
        self._equity = equity
    
    @staticmethod
    def net_income(revenue:float,expenses:float) -> float:
        return revenue-expenses
    
    @property
    def liability(self)->float:
        return self._assets - self._equity
    
    @property
    def equity(self) -> float:
        return self._assets - self._liabilities

    @property
    def assets(self) -> float:
        return self._liabilities + self._equity
    
    @property
    def current_ratio(self) -> float:
        return self._assets/self._liabilities
    
    @staticmethod
    def cost_of_goods_sold(initial_inventory:float, purchased:float, end_inventory:float) -> float:
        return initial_inventory + purchased - end_inventory
    
    @staticmethod
    def break_even_point(fixed_costs:float,sales_price_per_unit:float,variable_cost_per_unit:float) -> float:
        return fixed_costs/(sales_price_per_unit - variable_cost_per_unit)
    
    @staticmethod
    def ROI(gain:float,cost:float) -> float:
        return ((gain-cost)/cost)*100
    
    @staticmethod
    def profit_margin(net_income:float,revenue:float) -> float:
        return (net_income/revenue)*100
    
    @staticmethod
    def markup_percentage(revenue:float,cogs:float) ->float:
        return ((revenue-cogs)/cogs)*100
    
    @staticmethod
    def selling_price_using_markup(cogs:float, markup_percentage:float) -> float:
        return (cogs*markup_percentage)+cogs
    
    @staticmethod
    def inventory_shrinkage(recorded_inventory:float, actual_inventory:float) -> float:
        return ((recorded_inventory - actual_inventory)/recorded_inventory)*100