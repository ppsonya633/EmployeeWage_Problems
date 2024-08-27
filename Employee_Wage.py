
'''

@Author: Pratik Patil
@Date: 2024-08-27
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-27
@Title : Employee Wage Problems

'''

import random


class Employee:


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
    def daily_wage(cls,wage_per_hour, daily_hour):
        """
        Description:
            This function gives an daily wage on employee
        Parameter:
            wage_per_hour- wage_per hour of a companey
            daily_hour-daily total working hour of a companey
        Return:
            it will return an daily wage of employee
        """

        return wage_per_hour*daily_hour

    
    @classmethod
    def partTime_wage(cls,wage_per_hour,part_time_hour):
        """
        Description:
            This Program gives the part time wages of the employee
        Parameter:
            wage_per_hour-per hour wage of a companey
            part_time_hour-part time hour of a companey
        Return:
            it will return an parttime wage of the employee
        """

        return wage_per_hour*part_time_hour
    

    @classmethod
    def WagesFor_ComplitionOfHoursOrDaysForMonth(cls,wage_per_hour, daily_hour, part_time_hours, monthely_working_days,monthely_working_hour):
        """
        Description:
            this function will gives a wages of employee when he completes the working hour or days in month
        Parameter:
            wage_per_hour-per hour wage
            daily_hour-daily working hours of a companey
            part_time_hours-part time working hour
            monthely_working_days-monthely working days for a companey
            monthely_working_hour-monthely working hour of a companey
        Return:
            it will return wages when employees total monthly working hours or days get completed
        """
        
        working_hour=0
        working_days=0
        total_wage=0

        while working_hour<monthely_working_hour and working_days<monthely_working_days:

            attendence=cls.check_attendance()

            match attendence:
                case 1:
                    working_hour+=daily_hour
                    total_wage+=cls.daily_wage(wage_per_hour, daily_hour)
                    
                case 0.5:
                    working_hour+=part_time_hours
                    total_wage+=cls.partTime_wage(wage_per_hour,part_time_hours)
                    
                case 0:
                    working_hour+=0
                    total_wage+=0

            working_days+=1

        return total_wage, working_days,working_hour

    
def main():
    total_wage, working_days,working_hour=Employee.WagesFor_ComplitionOfHoursOrDaysForMonth(10,8,4,24,100)

    print(f"Employees Total Wage :{total_wage}")
    print(f"Employees Total Working Days :{working_days}")
    print(f"Employees Total Working Hours :{working_hour}")

    total_wage,working_days,working_hour=Employee.WagesFor_ComplitionOfHoursOrDaysForMonth(20,10,5,28,150)
    print(f"Employees Total Wage :{total_wage}")
    print(f"Employees Total Working Days :{working_days}")
    print(f"Employees Total Working Hours :{working_hour}")



if __name__=="__main__":
    main()