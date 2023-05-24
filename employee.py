import schedule
'''  物件(但真的有需要嗎)
class Employee:
    def __init__(self,name,salary) :
        self.name=name
        self.salary=salary

    def calculate_salary(self):
        return self.salary*schedule(self.name)

'''

def get_salary(basic_salary,name):
    return basic_salary*schedule.gettotaltime(name)


