'''

@Author: Pratik Patil
@Date: 2024-08-27
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-27
@Title : Employee Wage Problems

'''

import random


class EmpWageBuilder:

    def __init__(self,companey_name,wage_per_hour,daily_hours,part_time_hours,monthely_working_days,monthely_working_hours):
        """
        Initialize the EmpWageBuilder instance with company-specific data.
        
        :param company_name: Name of the company
        :param wage_per_hour: Wage per hour for the company
        :param daily_hours: Full-time daily working hours
        :param part_time_hours: Part-time daily working hours
        :param monthely_working_days: Maximum number of working days per month
        :param monthely_working_hours: Maximum number of working hours per month
        """
        self.companey_name=companey_name
        self.wage_per_hour=wage_per_hour
        self.daily_hours=daily_hours
        self.part_time_hours=part_time_hours
        self.monthely_working_days=monthely_working_days
        self.monthely_working_hours=monthely_working_hours
        self.total_wage=0
        self.total_working_days=0
        self.total_working_hours=0


    def check_attendance(self):
        """
        Description:
            this functions returns a random number between 0,0.5,1 this three numbers
        Parameter:
            None
        Return:
            Return a random number
        """

        return random.choice([0,0.5,1])
    

    def daily_wage(self):
        """
        Description:
            This function gives a employees daily wage
        Parameter:
            None
        Return:
            it returns a employees daily wage
        """
    
        return self.daily_hours*self.wage_per_hour
    

    def part_time_wage(self):
        """
        Description:
            This function gives a employees part time wage
        Parameter:
            None
        Return:
            it returns a employees part time wage
        """
        
        return self.part_time_hours*self.wage_per_hour
    

    def companiesEmp_monthely_total_wage(self):
        """
        Description:
            This function gives a employees monthely total wage
        Parameter:
            None
        Return:
            it returns a employees daily wage
        """
        
        while self.total_working_days<self.monthely_working_days and self.total_working_hours<self.monthely_working_hours:
            attendance=self.check_attendance()

            match attendance:

                case 1:
                    self.total_wage+=self.daily_wage()
                    self.total_working_hours+=self.daily_hours

                case 0.5:
                    self.total_wage+=self.part_time_wage()
                    self.total_working_hours+=self.part_time_hours

                case 0:
                    self.total_wage+=0
                    self.total_working_hours+=0

            self.total_working_days+=1

        return self.total_wage,self.total_working_days,self.total_working_hours
    
    def display_details(self):
        """
        Description:
            This Function will display the total wage,days and hours of a companey
        Parameter:
            None
        Return
            None
        """

        total_wage,total_days,total_hours=self.companiesEmp_monthely_total_wage()
        print(f"{self.companey_name} - total wage is:{total_wage}")
        print(f"{self.companey_name} - total days are:{total_days}")
        print(f"{self.companey_name} - total hours are:{total_hours}")



def main():
    company1=EmpWageBuilder(companey_name="Apexon",wage_per_hour=50,daily_hours=8,part_time_hours=4,monthely_working_days=20,monthely_working_hours=200)
    company1.companiesEmp_monthely_total_wage()
    company1.display_details()

    company2=EmpWageBuilder(companey_name="bridgeLabz",wage_per_hour=20,daily_hours=9,part_time_hours=5,monthely_working_days=27,monthely_working_hours=300)
    company2.display_details()

if __name__=="__main__":
    main()


