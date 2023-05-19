""" 
目的：員工個人資料與其班表歸類
負責組員：張鈺淋
"""
import csv

class Employee:
    def __init__(self, name, bank, account, password, employee_id):
        self.name = name
        self.account = account
        self.bank = bank
        self.password = password
        self.employee_id = employee_id

    def check(self):
        # 執行檢查員工的特定操作
        pass

    def total_wages(self):
        # 計算員工的總薪資
        pass

    @classmethod
    def from_csv_row(cls, row):
        # 從CSV行創建員工物件
        name, bank, account = row
        password = ""  # 這裡先設為空字串，你可以根據需要自行設定
        employee_id = ""  # 同樣設為空字串
        return cls(name, bank, account, password, employee_id)

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def load_employees_from_csv(self, filename):
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # 跳過標題行
            for row in reader:
                employee = Employee.from_csv_row(row)
                self.employees.append(employee)

    def get_employee_schedule(self, name):
        # 根據員工姓名獲取員工的排班
        pass

# 使用範例
ems = EmployeeManagementSystem()
ems.load_employees_from_csv('employee.csv')

# 獲取員工列表
for employee in ems.employees:
    print(f"Name: {employee.name}, Bank: {employee.bank}, Account: {employee.account}")

