'''

@Author: Pratik Patil
@Date: 2024-08-22
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-22
@Title : Employee Wage Problems

'''

import random

WAGE_PER_HOUR=20
DAILY_HOUR=8
PART_TIME_HOUR=4
MONTHLY_WORKING_DAYS=20

def check_attendance():
    """
    Description:
        this function is used for check attendance based on values 1 and 0
    Return:
        it will return a number randomely either 1 or 0
    """

    attendance=random.choice([0,0.5,1])
    return attendance

def daily_wage(attendance):
    """
    Description:
        This function gives an daily wage on employee
    Return:
        it will return an daily wage of employee
    """

    if attendance==1:
        return WAGE_PER_HOUR*DAILY_HOUR
    else:
        return 0
    
def partTime_wage(attendance):
    """
    Description:
        This Program gives the part time wages of the employee
    Parameter:
        it will take employee attendance as a parameter
    Return:
        it will return an parttime wage of the employee
    """
    
    if attendance==0.5:
        return WAGE_PER_HOUR*PART_TIME_HOUR
    else:
        return 0
    
def monthly_wage():
    """
    Description:
        This Program will give a employee wages for a month
    Parameter:
        None
    Return:
        this function will return a monthely wages
    """

    total_wage=0
    for i in range(MONTHLY_WORKING_DAYS):
        attendence=check_attendance()
        if attendence==1:
            total_wage+=daily_wage(attendence)
        elif attendence==0.5:
            total_wage+=partTime_wage(attendence)
        else:
            total_wage+=0

    return total_wage

def wagesfor_condition():
    """
    Description:
        This Program gives a wages until employee complete 100 working hours or 20 working days
    Parameter:
        None
    Return:
        if one of the condition is true then it will give an result
    """

    working_hour=0
    working_days=0
    total_wage=0

    while working_hour<100 or working_days<20:
        attendence=check_attendance()

        if attendence==1:
            working_hour+=DAILY_HOUR
            working_days+=1
            total_wage+=daily_wage(attendence)

        elif attendence==0.5:
            working_hour+=PART_TIME_HOUR
            working_days+=1
            total_wage+=partTime_wage(attendence)

        else:
            working_hour+=0
            working_days+=1
            total_wage+=0

    return total_wage


def main():

    print(f"Wages for given condition : {wagesfor_condition()}")
    

if __name__=="__main__":
    main()


