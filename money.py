""" 
目的：計算員工本月總薪資，並導出CSV
負責組員：張鈺淋
"""

import csv
from schedule import scheduleclass 

class MoneyCalculator: # 計算薪資的類別
    def __init__(self,sch) :
        self.sch = sch  # 初始化 MoneyCalculator 類別的物件，並傳入 scheduleclass 的實例
    wages = 176  # 基本薪資

    
    @classmethod
    def set_wages(self,wages):
        if wages >= 176: # 設定新的薪資
            self.wages = wages

    #@staticmethod
    def calculate_salary(self):
        names = self.sch.getverify()
        wedata,hodata = self.sch.calculate_total_hours()
        total_salary = {}
        for name in names:
            wetime = wedata.get(name, 0)
            hotime = hodata.get(name , 0)
            total_salary[name] = int(wetime * self.wages + hotime * self.wages * 2)  # 將本月總薪資轉為整數
        return total_salary

    #@staticmethod
    def export_salary_to_csv(self):
        salaries = self.calculate_salary()

        with open('salary_output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['姓名', '本月總薪資'])
            for name, total_salary in salaries.items():
                if total_salary != 0:  # 排除本月總薪資為0的資料
                    writer.writerow([name, total_salary])


sch = scheduleclass()
sch.sethoildaybool(True)
sch.settarget(5,2023)
mm = MoneyCalculator(sch)
mm.set_wages(200) 
mm.export_salary_to_csv()

