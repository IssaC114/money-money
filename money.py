""" 
目的：計算工讀金，判斷假日、加班代班等情況
負責組員：張鈺淋
"""

import csv
from oldemployee import Employee, EmployeeManagementSystem
import schedule

class MoneyCalculator:
    wages = 176 # 基本薪資

    @staticmethod
    def is_holiday(date, holidays):
       return date in holidays


    @classmethod
    def set_wages_total(cls, wages):
        if wages >= cls.wages:
            cls.wages = wages

    @staticmethod
    def load_holidays(file_path):
        holidays = set()
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                date = row[0]
                holidays.add(date)
        return holidays

    def count_working_days(schedule_file, holidays):
        data = schedule.read_csv_file(schedule_file)
        working_days = 0
        for row in data:
            date = row[0]
            if not MoneyCalculator.is_holiday(date, holidays):
                working_days += 1
        return working_days

    def calculate_salary(employee, schedule_file, holidays):
        data = schedule.read_csv_file(schedule_file)
        working_days = 0
        work_hours = 0
        for row in data:
            if row[1] == employee.name:
                date = row[0]
                if not MoneyCalculator.is_holiday(date, holidays):
                    working_days += 1
                    work_hours += float(row[3]) - float(row[2]) # end-start
        total_salary = work_hours * MoneyCalculator.wages
        return total_salary, working_days, work_hours

    def export_salary_to_csv(employees, schedule_file, holidays, output_file):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['姓名', '本月總薪資', '月工作天數', '月工作時數'])
            for employee in employees:
                salary, working_days, work_hours = MoneyCalculator.calculate_salary(employee, schedule_file, holidays)
                writer.writerow([employee.name, salary, working_days, work_hours])


# 讀取檔案
ems = EmployeeManagementSystem()
ems.load_employees_from_csv('employee.csv')

# 讀取國定假日
holidays = MoneyCalculator.load_holidays('holidays.csv')

# 設定基本薪資
base_salary = 200 # 設定新的基本薪資

# 設定基本薪資總額
MoneyCalculator.set_wages_total(base_salary)

# 上傳新班表
uploaded_schedule_file = 'uploaded_schedule.csv'

# 計算非國定假日的工作天數
working_days = MoneyCalculator.count_working_days(uploaded_schedule_file, holidays)

# 計算薪資並導出到CSV
MoneyCalculator.export_salary_to_csv(ems.employees, uploaded_schedule_file, holidays, 'salary_output.csv')
