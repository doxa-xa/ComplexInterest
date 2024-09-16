import datetime as dt

class ComplexInterest:
    def __init__(self,monthly_investment:int, period:tuple, percent_interest:float):
        if monthly_investment < 0 or not isinstance(monthly_investment,int):
            raise ValueError("Monthly investment must be a positive int value")
        self.year_investment = monthly_investment*12
        if not isinstance(period,tuple) or not isinstance(period[0],dt.date):
            raise ValueError('Period must be a datetime tuple: start/end date')
        self.period = period
        if not isinstance(percent_interest,float):
            raise ValueError('percent interest must be a float value i.e. 10% will be 0.10')
        self.total_invested = 0
        self.total_profit = 0

    



cx_interest = ComplexInterest(1000,(dt.date(2024,9,16),dt.date(2031,9,16)),0.10)