""" 
目的：計算工讀金，判斷假日、加班代班等情況
負責組員：張鈺淋
"""

import csv
from oldemployee import Employee, EmployeeManagementSystem
import schedule

class MoneyCalculator:
    wages = 176 # 基本薪資

    @classmethod
    def set_wages_total(cls, wages):
        if wages >= cls.wages:
            cls.wages = wages

def calculate_salary(employee, schedule_file):
    data = schedule.read_csv_file(schedule_file)
    total_working_days = 0
    total_work_hours = 0
    for row in data:
        if row[1] == employee.name:
            total_working_days += 1
            total_work_hours += float(row[3]) - float(row[2]) # end-start
    total_working_days *= 4  # 乘以四週（表一個月）
    total_work_hours *= 4  # 乘以四週（表一個月）
    total_salary = total_work_hours * MoneyCalculator.wages
    return total_salary, total_working_days, total_work_hours

def export_salary_to_csv(employees, output_file):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['姓名', '本月總薪資', '月工作天數', '月工作時數'])
        for employee in employees:
            salary, working_days, work_hours = calculate_salary(employee, 'uploaded_schedule.csv')
            writer.writerow([employee.name, salary, working_days, work_hours])

# 讀取檔案
ems = EmployeeManagementSystem()
ems.load_employees_from_csv('employee.csv')

# 計算薪資並導出到CSV
export_salary_to_csv(ems.employees, 'salary_output.csv')

