'''
@Author: Pratik Patil
@Date: 2024-08-27
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-27
@Title : Employee Wage Problems
'''

import random


class CompanyEmpWage:
    
    def __init__(self, company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours):
        """
        Initialize the CompanyEmpWage instance with company-specific data.
        
        :param company_name: Name of the company
        :param wage_per_hour: Wage per hour for the company
        :param full_day_hour: Number of hours considered as a full-time working day
        :param part_time_hour: Number of hours considered as a part-time working day
        :param max_working_days: Maximum number of working days per month
        :param max_working_hours: Maximum number of working hours per month
        """

        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_day_hour = full_day_hour
        self.part_time_hour = part_time_hour
        self.max_working_days = max_working_days
        self.max_working_hours = max_working_hours
        self.total_wage = 0  # Instance variable to store total wage for the company


    def check_attendance(self):
        """
        Description:
            This function simulates the attendance of an employee randomly. 
            The employee can be absent (0), work part-time (0.5), or work full-time (1).
        Parameters:
            None
        Return:
            int: Returns a random value of 0, 0.5, or 1 to represent absent, part-time, or full-time attendance, respectively.
        """
        return random.choice([0, 1, 2])


    def calculate_daily_wage(self):
        """
        Description:
            This function calculates the daily wage of an employee based on the number of hours worked 
            in a full day and the hourly wage rate.
        Parameters:
            None
        Return:
            int: Returns the daily wage calculated as the product of full-day hours and wage per hour.
        """

        return self.full_day_hour * self.wage_per_hour


    def calculate_part_time_wage(self):
        """
        Description:
            This function calculates the wage of an employee for a part-time day based on the number of part-time hours 
            and the hourly wage rate.
        Parameters:
            None
        Return:
            int: Returns the part-time wage calculated as the product of part-time hours and wage per hour.
        """

        return self.part_time_hour * self.wage_per_hour


    def compute_wages(self):
        """
        Description:
            This function calculates the total wages for an employee over a month. 
            It takes into account the maximum working days and hours, as well as the attendance and type of work (full-time or part-time).
        Parameters:
            None
        Return:
            None
        """

        total_hours = 0
        total_days = 0
        total_wage = 0

        while total_days < self.max_working_days and total_hours < self.max_working_hours:
            attendance = self.check_attendance()

            if attendance == 1:
                total_hours += self.full_day_hour
                total_wage += self.calculate_daily_wage()

            elif attendance == 2:
                total_hours += self.part_time_hour
                total_wage += self.calculate_part_time_wage()

            total_days += 1

        self.total_wage = total_wage


    def print_wages(self):
        """
        Description:
            This function prints the total wage for the company after all calculations have been performed. 
            The wage is formatted to two decimal places.
        Parameters:
            None
        Return:
            None
        """

        print(f"Company Name: {self.company_name}, Total Wage: ${self.total_wage:.2f}")


class EmpWageBuilder:

    def __init__(self):
        self.company_list = []


    def add_company(self, company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours):
        """
        Description:
            Adds a new company to the builder with its specific wage and working hour details.
        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): The hourly wage rate for the company.
            full_day_hour (int): The number of hours for a full-time workday.
            part_time_hour (int): The number of hours for a part-time workday.
            max_working_days (int): The maximum number of working days in a month.
            max_working_hours (int): The maximum number of working hours in a month.
        Return:
            None
        """

        company = CompanyEmpWage(company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours)
        self.company_list.append(company)


    def compute_wages(self):
        """
        Description:
            This function computes wages for all companies added to the builder by invoking the compute_wages method 
            of each company, and then prints the computed wages for each company.
        Parameters:
            None
        Return:
            None
        """
        
        for company in self.company_list:
            company.compute_wages()
            company.print_wages()


def main():
    builder = EmpWageBuilder()

    while True:
        print("\nMenu:")
        print("1. Add Company")
        print("2. Compute Wages for All Companies")
        print("3. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case '1':
                company_name = input("Enter company name: ")
                wage_per_hour = int(input("Enter wage per hour: "))
                full_day_hour = int(input("Enter full day hours: "))
                part_time_hour = int(input("Enter part-time hours: "))
                max_working_days = int(input("Enter maximum working days: "))
                max_working_hours = int(input("Enter maximum working hours: "))
                builder.add_company(company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours)
            case '2':
                builder.compute_wages()
            case '3':
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

