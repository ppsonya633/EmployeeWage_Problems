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
        self.employees = []  # List to store employees
        self.total_wage = 0  # Instance variable to store total wage for the company


    def add_employee(self, employee_name):
        """
        Description:
            Add an employee to the company.
        Parameters:
            employee_name (str): Name of the employee to be added.
        Return:
            None
        """

        employee = {
            "name": employee_name,
            "total_days": 0,
            "total_hours": 0,
            "total_wage": 0
        }
        self.employees.append(employee)


    def check_attendance(self):
        """
        Description:
            Randomly determine the attendance status of an employee. 
            Returns 0 for absent, 1 for full-time, and 2 for part-time.
        Parameters:
            None
        Return:
            int: Randomly chosen number from the set {0, 1, 2}
        """
        
        return random.choice([0, 1, 2])


    def calculate_daily_wage(self):
        """
        Description:
            Calculate the daily wage for a full-time employee based on full-day hours and wage per hour.
        Parameters:
            None
        Return:
            int: Daily wage for a full-time employee
        """

        return self.full_day_hour * self.wage_per_hour


    def calculate_part_time_wage(self):
        """
        Description:
            Calculate the daily wage for a part-time employee based on part-time hours and wage per hour.
        Parameters:
            None
        Return:
            int: Daily wage for a part-time employee
        """

        return self.part_time_hour * self.wage_per_hour


    def compute_wages_for_all_employees(self):
        """
        Description:
            Compute wages for all employees by simulating attendance over a month. 
            Takes into account full-time and part-time work, and considers the maximum working days and hours.
        Parameters:
            None
        Return:
            None
        """

        for employee in self.employees:
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

            employee["total_days"] = total_days
            employee["total_hours"] = total_hours
            employee["total_wage"] = total_wage

            self.total_wage += total_wage


    def print_employee_wages(self):
        """
        Description:
            Print detailed information about each employee's total working days, 
            total working hours, and total wages. Also prints the total wage paid by the company.
        Parameters:
            None
        Return:
            None
        """

        print(f"\nCompany Name: {self.company_name}")
        for employee in self.employees:
            print(f"Employee Name: {employee['name']}, Total Days: {employee['total_days']}, Total Hours: {employee['total_hours']}, Total Wage: ${employee['total_wage']:.2f}")
        print(f"Total Wage for Company: ${self.total_wage:.2f}")  # Print the total wage for the company


class EmpWageBuilder:
    def __init__(self):
        self.company_list = []

    def add_company(self, company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours):
        """
        Description:
            Add a new company to the list with specific wage and working hour details.

        Parameters:
            company_name (str): Name of the company.
            wage_per_hour (int): Wage per hour for the company.
            full_day_hour (int): Number of hours considered as a full-time working day.
            part_time_hour (int): Number of hours considered as a part-time working day.
            max_working_days (int): Maximum number of working days per month.
            max_working_hours (int): Maximum number of working hours per month.

        Return:
            None
        """
        company = CompanyEmpWage(company_name, wage_per_hour, full_day_hour, part_time_hour, max_working_days, max_working_hours)
        self.company_list.append(company)


    def add_employees_to_company(self, company_name):
        """
        Description:
            Add employees to a specific company by asking for employee details from the user.
        Parameters:
            company_name (str): Name of the company to which employees will be added.
        Return:
            None
        """
        
        company = next((c for c in self.company_list if c.company_name == company_name), None)
        if company:
            num_employees = int(input(f"Enter the number of employees for {company_name}: "))
            for _ in range(num_employees):
                employee_name = input("Enter employee name: ")
                company.add_employee(employee_name)
        else:
            print(f"Company {company_name} not found.")


    def compute_wages(self):
        for company in self.company_list:
            company.compute_wages_for_all_employees()
            company.print_employee_wages()


def main():
    builder = EmpWageBuilder()

    while True:
        print("\nMenu:")
        print("1. Add Company")
        print("2. Add Employees to Company")
        print("3. Compute Wages for All Companies")
        print("4. Exit")

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
                company_name = input("Enter the company name to add employees: ")
                builder.add_employees_to_company(company_name)
            case '3':
                builder.compute_wages()
            case '4':
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

