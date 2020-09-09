"""
Author:  Derek Bittner
Program:  camper_age_input.py


program that accepts an integer value for years and returns integer value for months.
"""


import constants


def convert_to_months(years):
    months = years * constants.MONTHS
    return months


if __name__ == '__main__':
    age_in_years = input("Enter your child's age:")
    age_in_months = convert_to_months(int(age_in_years))
    print("{} years is {} months".format(age_in_years, age_in_months))
