""" 
目的：設置管理員功能
負責組員：周詠熙
"""
from schedule import Schedule
class Admin:
    def __init__(self, departmentname, password):
        self.departmentname = departmentname
        self.password = password
        self.schedule = Schedule()

    def check(self, input_password):
        # 檢查密碼是否正確
        return self.password == input_password

    def get_schedule(self):
        # 取得工讀生排班資料
        return self.schedule.get()

    def set_schedule(self, new_schedule):
        # 設定工讀生排班資料
        self.schedule.set(new_schedule)