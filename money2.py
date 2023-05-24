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
base_salary = MoneyCalculator.set_wages_total()

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