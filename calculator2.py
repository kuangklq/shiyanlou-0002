#hainiu2017/11/24 23:10:40
#IncomeTaxQuickLookupItem 
#'start_point', 'tax_rate', 'quick_subtractor'
#INCOME_TAX_START_POINT
#INCOME_TAX_QUICK_LOOKUP_TABLE
#SOCIAL_INSURANCE_MONEY_RATE
#endowment_insurance
#medical_insurance
#unemployment_insurance
#employment_injury_insurance
#maternity_insurance
#public_accumulation_funds
#calc_income_tax_and_remain(income)
#social_insurance_money
#real_income
#social_insurance_money
#taxable_part
#employee_id
#income_string


#!usr/bin/env python3

import sys
from collections import nametuple

IncomeTaxQuickLookupItem = namedtuple(
    'IncomeTaxQuickLookupItem',
    ['start_point','tax_rate','quick_subtractoe']
)

INCOME_TAX_QUICK_LOOKUP_TABLE = [
    IncomeTaxQuickLookupItem(80000,0.45,13505),
    IncomeTaxQuickLookupItem(55000,0.35,5505),
    IncomeTaxQuickLookupItem(35000,0.30,2755),
    IncomeTaxQuickLookupItem(9000,0.25,1005),
    IncomeTaxQuickLookupItem(4500,0.20,555),
    IncomeTaxQuickLookupItem(1500,0.10,105),
    IncomeTaxQuickLookupItem(0,0.03,0),
]

SOCIAL_INSURANCE_MONEY_RATE = {
    'endowment_insruance':0.08,
    'medical_insurance':0.02,
    'unemployment_insurance':0.005,
    'employment_injury_insurance':0,
    'maternity_insurance':0,
    'public_accumulation_funds':0.06
}

def calc_income_tax_and_remain(income):
    social_insurance_money = income * sum(SOCIAL_INSURANCE_MONEY_RATE.values())
    real_income = income - social_insurance_money
    taxable_part = real_income - INCOME_TAX_START_POINT
    if taxable_part <= 0:
        return '0.00','{:.2f}'.format(real_income)
    for item in INCOME_TAX_QUICK_LOOKUP_TABLE:
        if taxable_part > item.start_point:
            tax = taxable_part * item.tax_rate - item.quick_subtractor
            return ':.2f'.format(tax),':.2f'.format(real_income - tax)
            
            
def main():
    for item in sys.argv[1:]:
        employee_id,income_string = item.split(':')
        try:
            income = int(income_string)
        except ValueError:
            print('Parameter Error')
        _,remain = calc_income_tax_and_remain(income)
        print('{}:{}'.format(employee_id,remain))
        
if __name__ == '__main__':
    main()
        