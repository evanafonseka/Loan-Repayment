from datetime import date, datetime
from dateutil.relativedelta import *
import pandas as pd
import numpy as np
from collections import OrderedDict

#
# # class AmortizationSchedule:
# #     def __init__(self, amount_borrowed, years, periods, rate, additional_principal, start_date):
# #         self.amount_borrowed = amount_borrowed
# #         self.years = years
# #         self.periods = periods
# #         self.rate = rate
# #         self.add_principal = additional_principal
# #         self.start_date = start_date
# #         self.start_date = datetime.strptime(self.start_date, '%d/%m/%Y')
# #
# #         self.actual_periods = self.years * self.periods
# #         self.rate_per_period = self.rate / self.periods
# #
# #     def MonthlyAmortization(self):
# #         self.range = pd.date_range(self.start_date, periods=self.actual_periods, freq='MS').strftime('%d %b %Y')
# #         self.range.name = "Payment Date"
# #         self.df = pd.DataFrame(index=self.range,
# #                                columns=['Payment', 'Principal', 'Interest', 'Additional Principal', 'Balance'],
# #                                dtype='float')
# #         self.df.reset_index(inplace=True)
# #         self.df.index += 1
# #         self.df.index.name = "Period"
# #
# #         self.df['Payment'] = np.pmt(self.rate_per_period, self.actual_periods, self.amount_borrowed)
# #         self.df['Principal'] = np.ppmt(self.rate_per_period, self.df.index, self.actual_periods, self.amount_borrowed)
# #         self.df['Interest'] = np.ipmt(self.rate_per_period, self.df.index, self.actual_periods, self.amount_borrowed)
# #         self.df['Additional Principal'] = -self.add_principal
#
#
# class Ammortize:
#     def __init__(self, amount_borrowed, rate, years, additional_principal, periods):
#         self.amount_borrowed = amount_borrowed
#         self.rate = rate
#         self.years = years
#         self.add_principal = additional_principal
#         self.periods = periods
#         self.start_period = 1
#         self.start_date = date.today()
#         self.payment = np.pmt(self.rate / self.periods, self.years * self.periods, self.amount_borrowed)
#         self.beginning_balance = self.amount_borrowed
#         self.ending_balance = self.amount_borrowed
#
#     def Calculator(self):
#         while self.ending_balance > 0:
#
#             self.interest = (self.rate / self.periods) * self.beginning_balance
#
#             self.payment = min(self.payment, self.beginning_balance + self.interest)
#             self.amount_borrowed = self.payment - self.interest
#
#             self.add_principal = min(self.add_principal, self.beginning_balance - self.amount_borrowed)
#             self.ending_balance = self.beginning_balance - (self.amount_borrowed + self.add_principal)
#
#             yield OrderedDict([('Payment Date', self.start_date),
#                                ('Period', self.start_period),
#                                ('Beginning Balance', self.beginning_balance),
#                                ('Payment', self.payment),
#                                ('Amount Borrowed', self.amount_borrowed),
#                                ('Interest', self.interest),
#                                ('Additional_Payment', self.add_principal),
#                                ('Ending Balance', self.ending_balance)])
#             self.start_period += 1
#             self.start_date += relativedelta(months=1)
#             self.beginning_balance = self.ending_balance
#
#
# x = Ammortize(700000, 0.04, 30, 200, 12)
# df = pd.DataFrame(x.Calculator())

#
# class LoanRepaymentCalculator:
#     def __init__(self, loan, rate, years, number_of_periods):
#         self.loan = loan
#         self.rate = rate
#         self.years = years
#         self.number_of_periods = number_of_periods
#         self.rate_per_period = self.rate / self.number_of_periods
#         self.actual_periods = self.years * self.number_of_periods
#         # self.semi_annual = 2
#         # self.quarter = 4
#         # self.monthly = 12
#         # self.daily = 365
#         # self.minutes = 525600
#         # self.seconds = 31556952
#
#     def loan_repayment(self):
#         return (self.rate_per_period * self.loan) / (1 - (1 + self.rate_per_period)
#                                                      ** -self.actual_periods)
#
#     def compounding_rate_per_period(self):
#         return (1 + self.rate_per_period) ** self.actual_periods - 1
#
#     # def total_interest_paid(self):
#     #     return self.loan * ((self.rate_per_period * (1 + self.rate_per_period) ** self.actual_periods)
#     #                         / (1 + self.rate_per_period) ** self.actual_periods - 1)
#
#     def date_loan_is_paid(self):
#         today = datetime.now()
#         payment_date = today + relativedelta(years=self.years)
#         return payment_date.strftime('%d %b %Y')
#
#
# x = LoanRepaymentCalculator(100000, 0.0075, 2, 12)
# print(x.compounding_rate_per_period())
# print(x.loan_repayment())
# # print(x.total_interest_paid())
#
# # TODO: Create a curve with how the repayments go including instances where people pay a balloon payment.
# # TODO: Afterwards creaate a curve for potential salary and potential earnings and how long it would take to complete payment of that loan, considering how much that person allocate to the loan
# # TODO: create growth rates for interest - move with inflation

