'''

@Author: Pratik Patil
@Date: 2024-08-22
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-22
@Title : Employee Wage Problems

'''

import random
wage_per_hour=20
daily_hour=8
def check_attendance():
    """
    Description:
        this function is used for check attendance based on values 1 and 0
    Return:
        it will return a number randomely either 1 or 0
    """
    attendance=random.choice([0,1])
    return attendance

def daily_wage(attendance):
    """
    Description:
        This function gives an daily wage on employee
    Parameter:
        this takes an attendance of employee as a parameter
    Return:
        it will return an daily wage of employee
    """
    if attendance==1:
        return wage_per_hour*daily_hour
    else:
        return 0

def main():
    attendance=check_attendance()
    wage=daily_wage(attendance)
    if attendance==1:
        print(f"Employee is Present and his Daily wage is {wage}rs")
    else:
        print(f"Employee is absent and his daily wage is {0}rs")

if __name__=="__main__":
    main()
