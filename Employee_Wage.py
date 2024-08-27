
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
            This function is used to check attendance based on values 1, 0.5, and 0.
        Parameter:
            None
        Return:
            It will return a number randomly: either 1 (full-time), 0.5 (part-time), or 0 (absent).
        """
        attendance = random.choice([0, 0.5, 1])
        return attendance


    @classmethod
    def daily_wage(cls, wage_per_hour, daily_hour):
        """
        Description:
            This function calculates the daily wage of an employee.
        Parameter:
            wage_per_hour - wage per hour of a company
            daily_hour - daily total working hours of a company
        Return:
            It returns the daily wage of the employee.
        """
        return wage_per_hour * daily_hour


    @classmethod
    def partTime_wage(cls, wage_per_hour, part_time_hour):
        """
        Description:
            This function calculates the part-time wages of the employee.
        Parameter:
            wage_per_hour - per hour wage of a company
            part_time_hour - part-time hours of a company
        Return:
            It returns the part-time wage of the employee.
        """
        return wage_per_hour * part_time_hour


    @classmethod
    def WagesFor_ComplitionOfHoursOrDaysForMonth(cls, wage_per_hour, daily_hour, part_time_hours, monthly_working_days, monthly_working_hour):
        """
        Description:
            This function calculates the wages of an employee when they complete the working hours or days in a month.
        Parameter:
            wage_per_hour - per hour wage
            daily_hour - daily working hours of a company
            part_time_hours - part-time working hour
            monthly_working_days - monthly working days for a company
            monthly_working_hour - monthly working hours of a company
        Return:
            It returns wages when an employee's total monthly working hours or days are completed.
        """
        working_hour = 0
        working_days = 0
        total_wage = 0

        while working_hour < monthly_working_hour and working_days < monthly_working_days:

            attendance = cls.check_attendance()

            match attendance:
                case 1:
                    working_hour += daily_hour
                    total_wage += cls.daily_wage(wage_per_hour, daily_hour)

                case 0.5:
                    working_hour += part_time_hours
                    total_wage += cls.partTime_wage(wage_per_hour, part_time_hours)

                case 0:
                    working_hour += 0
                    total_wage += 0

            working_days += 1

        return total_wage, working_days, working_hour


def main():

    wage_per_hour = int(input("Enter the wage per hour for Company : "))
    daily_hour = int(input("Enter the daily working hours for Company : "))
    part_time_hours = int(input("Enter the part-time working hours for Company : "))
    monthly_working_days = int(input("Enter the maximum working days for Company  in a month: "))
    monthly_working_hour = int(input("Enter the maximum working hours for Company  in a month: "))

    total_wage, working_days, working_hour = Employee.WagesFor_ComplitionOfHoursOrDaysForMonth(
        wage_per_hour, daily_hour, part_time_hours, monthly_working_days, monthly_working_hour
    )

    print(f"Company  - Employees Total Wage: {total_wage}")
    print(f"Company  - Employees Total Working Days: {working_days}")
    print(f"Company  - Employees Total Working Hours: {working_hour}")

    


if __name__ == "__main__":
    main()

       
