""" 
目的：計算工讀金，判斷假日、加班代班等情況
負責組員：張鈺淋
"""

import csv
from employee import Employee
import schedule

class MoneyCalculator:
    wages = 176
#     def __init__(self, employee_file, schedule_file):
#         self.employees = self.load_employees(employee_file)
#         self.schedule = schedule.read_csv_file(schedule_file)

#     def load_employees(self, employee_file):
#         employees = []
#         with open(employee_file, 'r') as file:
#             reader = csv.reader(file)
#             next(reader)  # 跳過標題行
#             for row in reader:
#                 employee = Employee.from_csv_row(row)
#                 employees.append(employee)
#         return employees

#     def set_wages(self, name, wages):
#         for employee in self.employees:
#             if employee.name == name:
#                 employee.wages = wages
#                 break
    
    @classmethod
    def set_wages_total(cls,wages):
        if wages >= cls.wages:
            cls.wages = wages

    # def calculate_total_wages(self):
    #     total_wages = 0
    #     for employee in self.employees:
    #         total_wages += employee.total_wages()
    #     return total_wages

#     def calculate_money(self):
#         for employee in self.employees:
#             working_days = 0
#             for entry in self.schedule:
#                 if entry[1] == employee.name:
#                     if entry[0] == 'day':
#                         working_days += 1
#                     elif entry[0] == 'overtime':
#                         working_days += 1
#                         employee.add_extra_wages(100)  # 假設加班每天額外薪資為100元
#                     elif entry[0] == 'substitute':
#                         employee.add_extra_wages(200)  # 假設代班每天額外薪資為200元
#                     elif entry[0] == 'holiday':
#                         working_days += 1
#                         employee.double_wages()  # 假設假日出勤薪水雙倍
#                     elif entry[0] == 'hours':
#                         working_days += float(entry[2])  # 讀取工作時數
#             employee.calculate_wages(working_days)

# # 讀檔
# money_calculator = MoneyCalculator('employee.csv', 'schedule.csv')

# # 設定薪水
# money_calculator.set_wages('Megan', 50000)
# money_calculator.set_wages('Fannie', 60000)
# money_calculator.set_wages('Quinella', 55000)
# money_calculator.set_wages('Luminous', 70000)
# money_calculator.set_wages('Frank', 45000)

# # 計算總薪資
# total_wages = money_calculator.calculate_total_wages()
# print(f"Total wages: {total_wages}")

# # 計算各員工的薪水
# money_calculator.calculate_money()
# for employee in money_calculator.employees:
#     print(f"Name: {employee.name}, Wages: {employee.wages}")
