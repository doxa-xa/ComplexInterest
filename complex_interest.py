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