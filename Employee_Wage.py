'''

@Author: Pratik Patil
@Date: 2024-08-22
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-22
@Title : Employee Wage Problems

'''

import random
def check_attendance():
    """
    Description:
        this function is used for check attendance based on values 1 and 0
    Return:
        it will return a number randomely either 1 or 0
    """
    attendance=random.choice([0,1])
    return attendance


def main():
    result=check_attendance()
    if result==1:
        print("Employee is Present")
    else:
        print("Employee is absent")

if __name__=="__main__":
    main()


    
# import random
# class Employee:
#     def check_attendence(self):
#         """
#         Description:
#             """
#         value=random.choice([0,1])
#         return value

#     def main(self):
#         attendance=self.check_attendence()
#         if attendance==1:
#             print("Employee is Present")
#         else:
#             print("Employee is absent")
    
# if __name__=="__main__":
#         employee1=Employee()
#         employee1.main()

