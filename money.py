""" 
目的：計算員工本月總薪資，並導出CSV
負責組員：張鈺淋
"""

import csv
from schedule import scheduleclass 


class MoneyCalculator: 
    def __init__(
            self,sch) :
            # 初始化 MoneyCalculator 類別的物件，並傳入 scheduleclass 的實例
            self.sch = sch  
            # 基本薪資
            self.wages = 176  
    
    @classmethod
    # 設定新的基本薪資
    def set_wages(
        self,wages) :
        self.wages = wages

    # 計算薪資
    def calculate_salary(
            self) :
            # 取得員工姓名
            names = self.sch.getverify() 
            # 取得本月工作總時數
            wedata,hodata = self.sch.calculate_total_hours() 
            total_salary = {}

            for name in names:
                # 取得個別員工 普通時數
                wetime = wedata.get(name, 0) 
                # 取得個別員工 國定假日時數
                hotime = hodata.get(name , 0) 
                # 以整數計本月總薪資
                total_salary[name] = int(wetime * self.wages + hotime * self.wages * 2)  
            return total_salary

    # 將取得資料輸出至CSV
    def export_salary_to_csv(
              self) :
              # 取得本月工作總時數
              wedata,hodata = self.sch.calculate_total_hours() 
              # 取得計算後的薪資資料
              salaries = self.calculate_salary() 
              # 定義文件路徑和名稱
              filename = 'salary_output.csv' 
              with open(
                    filename, 'w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(['name','weekday hours','holiday hours', 'total salary for this month']) # 寫入CSV檔的 標題行
              for name, total_salary in salaries.items():
                  # 排除本月總薪資為0的資料
                  if total_salary != 0:  
                     writer.writerow([name, wedata.get(name , 0) , hodata.get(name , 0),total_salary])
              return filename
    
    def employee_salary(
              self,name):
              salaries = self.calculate_salary()
              for employee , salary in salaries.items():
                  if employee == name :
                     return salary



