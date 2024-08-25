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


def daily_wage():
    """
    Description:
        This function gives an daily wage on employee
    Return:
        it will return an daily wage of employee
    """

    return WAGE_PER_HOUR*DAILY_HOUR

    
def partTime_wage():
    """
    Description:
        This Program gives the part time wages of the employee
    Parameter:
        it will take employee attendance as a parameter
    Return:
        it will return an parttime wage of the employee
    """
    
    return WAGE_PER_HOUR*PART_TIME_HOUR
    

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
            total_wage+=daily_wage()
        elif attendence==0.5:
            total_wage+=partTime_wage()
        else:
            total_wage+=0

    return total_wage


def wages_ReachedForMonth():
    """
    Description:
        This Program gives a wages until employee complete 100 working hours or 20 working days
    Parameter:
        None
    Return:
        gives a total wage of employee for one month when days or working hours got complete
    """

    working_hour=0
    working_days=0
    total_wage=0

    while working_hour<100 or working_days<20:

        attendence=check_attendance()

        match attendence:
            case 1:
                working_hour+=DAILY_HOUR
                working_days+=1
                total_wage+=daily_wage()

            case 0.5:
                working_hour+=PART_TIME_HOUR
                working_days+=1
                total_wage+=partTime_wage()

            case 0:
                working_hour+=0
                working_days+=1
                total_wage+=0

    return total_wage


def main():

    print(f"Wages for employee when working hour or days reached for month : {wages_ReachedForMonth()}")
    

if __name__=="__main__":
    main()
