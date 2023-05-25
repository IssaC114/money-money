""" 
目的：計算工讀金，判斷假日、加班代班等情況
負責組員：張鈺淋
"""

import csv
import schedule

class MoneyCalculator:

    wages = 176 # 基本薪資

    @classmethod
    def set_wages(cls, wages):
        if wages >= 176: # 設定後的基本薪資務必 >= 176  
            cls.wages = wages

    @staticmethod
    def calculate_salary(holidays):
        names = schedule.getverify() # 取得員工姓名
        data = schedule.calculate_total_hours(5, 2023) # 取得月份/年份
        total_salary = {} 
        for name in names:
            totaltime = data.get(name, 0) 
            total_salary[name] = int(totaltime * MoneyCalculator.wages) # 以整數計算薪資（工作總時數*基本薪資）
        return total_salary

    @staticmethod
    def export_salary_to_csv(output_file):
        holidays = schedule.read_csv_file('holidays.csv')[1:]  # holidays.csv檔有多行，跳過標題行開始讀取
        salaries = MoneyCalculator.calculate_salary(holidays)

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['姓名', '本月總薪資'])
            for name, total_salary in salaries.items():
                if total_salary != 0: # 總薪資為0不寫入
                   writer.writerow([name, total_salary])

# 設定新的基本薪資
MoneyCalculator.set_wages(200)  

# 計算薪資並導出到CSV
MoneyCalculator.export_salary_to_csv('salary_output.csv')

