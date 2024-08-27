'''

@Author: Pratik Patil
@Date: 2024-08-22
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-22
@Title : Employee Wage Problems

'''

import random


class Employee:

    WAGE_PER_HOUR=20
    DAILY_HOUR=8
    PART_TIME_HOUR=4
    MONTHLY_WORKING_DAYS=20


    @classmethod
    def check_attendance(cls):
        """
        Description:
            this function is used for check attendance based on values 1 and 0
        Parameter:
            None
        Return:
            it will return a number randomely either 1 or 0
        """

        attendance=random.choice([0,0.5,1])
        return attendance
    

    @classmethod
    def daily_wage(cls):
        """
        Description:
            This function gives an daily wage on employee
        Parameter:
            None
        Return:
            it will return an daily wage of employee
        """

        return cls.WAGE_PER_HOUR*cls.DAILY_HOUR

    
    @classmethod
    def partTime_wage(cls):
        """
        Description:
            This Program gives the part time wages of the employee
        Parameter:
            None
        Return:
            it will return an parttime wage of the employee
        """

        return cls.PART_TIME_HOUR*cls.WAGE_PER_HOUR
    

    @classmethod
    def monthly_wage(cls):
        """
        Description:
            This Program will give a employee wages for a month
        Parameter:
            None
        Return:
            this function will return a monthely wages
        """

        total_wage=0
        for day in range(cls.MONTHLY_WORKING_DAYS):
            attendence=cls.check_attendance()
            if attendence==1:
                total_wage+=cls.daily_wage()
            elif attendence==0.5:
                total_wage+=cls.partTime_wage()
            else:
                total_wage+=0

        return total_wage
    

    @classmethod
    def WagesFor_ComplitionOfHoursOrDaysForMonth(cls):
        """
        Description:
            this function will gives a wages of employee when he completes the working hour or days in month
        Parameter:
            None
        Return:
            it will return wages when employees total monthly working hours or days get completed
        """
        
        working_hour=0
        working_days=0
        total_wage=0

        while working_hour<100 or working_days<20:

            attendence=cls.check_attendance()

            match attendence:
                case 1:
                    working_hour+=cls.DAILY_HOUR
                    working_days+=1
                    total_wage+=cls.daily_wage()

                case 0.5:
                    working_hour+=cls.PART_TIME_HOUR
                    working_days+=1
                    total_wage+=cls.partTime_wage()

                case 0:
                    working_hour+=0
                    working_days+=1
                    total_wage+=0

        return total_wage
    

def main():   
    print(f"wages when employee complete his total working hours or days for month :{Employee.WagesFor_ComplitionOfHoursOrDaysForMonth()}")

if __name__=="__main__":
    main()    
        

