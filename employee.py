
""" 
目的：員工個人資料與其班表歸類
負責組員：
"""
import csv

import schedule

class Employee:
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary

    def calculate_salary(self):
        return self.salary*schedule(self.name)






