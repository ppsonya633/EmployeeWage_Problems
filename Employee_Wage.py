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
    
    

def main():

    attendance=check_attendance()

    match attendance:
        case 1:
            print(f"employee is present and his daily wage is {daily_wage(attendance)}")

        case 0.5:
            print(f"employee is present for part time and his part time wage is {partTime_wage(attendance)}")
        
        case 0:
            print(f"employee is absent and his wage is {0}")
    

if __name__=="__main__":
    main()


