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
                salary, working_days, work_hours = MoneyCalculator.calculate_salary(employee, 'uploaded_schedule.csv')
                writer.writerow([employee.name, salary, working_days, work_hours])

# 讀取檔案
ems = EmployeeManagementSystem()
ems.load_employees_from_csv('employee.csv')

# 計算薪資並導出到CSV
MoneyCalculator.export_salary_to_csv(ems.employees, 'salary_output.csv')

# import csv
# from datetime import datetime, timedelta

# class MonthlyWorkHoursCalculator:
#     def __init__(self, schedule_file, holidays_file, wages_per_hour):
#         self.schedule_file = schedule_file
#         self.holidays_file = holidays_file
#         self.wages_per_hour = wages_per_hour
#         self.days_in_month = {
#             1: 31,  # 1月
#             2: 28,  # 2月，不考慮閏年
#             3: 31,  # 3月
#             4: 30,  # 4月
#             5: 31,  # 5月
#             6: 30,  # 6月
#             7: 31,  # 7月
#             8: 31,  # 8月
#             9: 30,  # 9月
#             10: 31,  # 10月
#             11: 30,  # 11月
#             12: 31  # 12月
#         }
        
#     def calculate_monthly_work_hours(self, month, year):
#         first_day = datetime(year, month, 1)
#         last_day = first_day + timedelta(days=self.days_in_month[month])
#         holidays = self._load_holidays(month, year)
#         work_days = 0
        
#         with open(self.schedule_file, 'r') as file:
#             reader = csv.DictReader(file)
#             total_hours = {}
            
#             # 初始化每個人的工作總時數為0
#             for row in reader:
#                 name = row['name']
#                 total_hours[name] = 0
            
#             # 將檔案指標歸零
#             file.seek(0)
            
#             # 計算每個人在目標月份的工作總時數
#             for row in reader:
#                 day = row['day']
#                 name = row['name']
#                 start_time = float(row['start'])
#                 end_time = float(row['end'])
                
#                 # 只計算目標月份和非節假日的工作時數
#                 if first_day <= day <= last_day and day not in holidays:
#                     total_hours[name] += end_time - start_time
#                     work_days += 1
        
#         wages = self.wages_per_hour * sum(total_hours.values())
#         return total_hours, work_days, wages
    
#     def _load_holidays(self, month, year):
#         holidays = set()
        
#         with open(self.holidays_file, 'r') as file:
#             reader = csv.DictReader(file)
            
#             for row in reader:
#                 holiday_date = datetime.strptime(row['date'], '%Y-%m-%d')
                
#                 if holiday_date.month == month and holiday_date.year == year:
#                     holidays.add(holiday_date.day)
        
#         return holidays


""" 
 --------以下是有嘗試加入實際時間日期的程式碼---------

import csv
import datetime
import schedule
from oldemployee import Employee, EmployeeManagementSystem

class MoneyCalculator:
    wages = 176  # 基本薪資

    @classmethod
    def set_wages_total(cls, wages):
        if wages >= cls.wages:
            cls.wages = wages

    @staticmethod
    def calculate_salary(employee, schedule_data, holidays):
        current_date = datetime.datetime.now()
        total_working_days = 0
        total_work_hours = 0
        for row in schedule_data:
            if row[1] == employee.name:
                start_time = datetime.datetime.strptime(row[2], '%H:%M') # 實際時間（時：分）
                end_time = datetime.datetime.strptime(row[3], '%H:%M')
                work_hours = (end_time - start_time).total_seconds() / 3600
                total_work_hours += work_hours

                schedule_date = datetime.datetime.strptime(row[0], '%Y-%m-%d') #年月日
                if schedule_date.month == current_date.month and [schedule_date.month, schedule_date.day] not in holidays:
                    total_working_days += 1

        total_salary = total_work_hours * MoneyCalculator.wages
        return total_salary, total_working_days, total_work_hours

    @staticmethod
    def export_salary_to_csv(employees, schedule_data, holidays, output_file):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['姓名', '本月總薪資', '月工作天數', '月工作時數'])
            for employee in employees:
                salary, working_days, work_hours = MoneyCalculator.calculate_salary(employee, schedule_data, holidays)
                writer.writerow([employee.name, salary, working_days, work_hours])

# 讀取員工資料
ems = EmployeeManagementSystem()
ems.load_employees_from_csv('employee.csv')

# 從 main.py 中的 set_wages() 函式中取得基本薪資設定
base_salary = set_wages()

# 從 main.py 中的 upload_schedule() 函式中取得新的班表
schedule_data = upload_schedule()

# 讀取國定假日列表
holidays = []
with open('holidays.csv', 'r') as holidays_file:
    holidays_reader = csv.reader(holidays_file)
    holidays = list(holidays_reader)

# 設定新的基本薪資
MoneyCalculator.set_wages_total(base_salary)

# 計算薪資並導出到 CSV
MoneyCalculator.export_salary_to_csv(ems.employees, schedule_data, holidays, 'salary_output.csv')

""" 