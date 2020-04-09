import pandas as pd
from datetime import date
import numpy as np
from collections import OrderedDict
from dateutil.relativedelta import *


class AmortizationSchedule:
    def __init__(self, amount_borrowed, rate, years, additional_principal):
        self.amount_borrowed = amount_borrowed
        self.rate = rate
        self.years = years
        self.add_principal = additional_principal
        self.periods = 12

    def Calculator(self, start_date=date.today()):
        self.payment = np.pmt(self.rate / self.periods, self.years * self.periods, self.amount_borrowed)
        self.start = 1
        self.beginning_balance = self.amount_borrowed
        self.ending_balance = self.amount_borrowed

        while self.ending_balance > 0:
            self.interest = (self.rate / self.periods) * self.beginning_balance
            self.payment = min(self.payment, self.beginning_balance + self.interest)
            self.amount_borrowed = self.payment - self.interest
            self.add_principal = min(self.add_principal, self.beginning_balance - self.amount_borrowed)
            self.ending_balance = self.beginning_balance - (self.amount_borrowed + self.add_principal)

            yield OrderedDict([('Month', start_date),
                               ('Period', self.start),
                               ('Beginning Balance', self.beginning_balance),
                               ('Payment', self.payment),
                               ('Amount Borrowed', self.amount_borrowed),
                               ('Interest', self.interest),
                               ('Additional_Payment', self.add_principal),
                               ('End Balance', self.ending_balance)])

            self.start += 1
            start_date += relativedelta(months=1)
            self.beginning_balance = self.ending_balance


df = AmortizationSchedule(700000, 0.04, 30, 200)

df = pd.DataFrame(df.Calculator(start_date=date(2020, 4, 9)))

