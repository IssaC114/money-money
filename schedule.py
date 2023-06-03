""" 
目的：班表輸入與輸出、更改
負責組員：李湘菱
"""
import csv
import datetime
class scheduleclass:

    def __init__(self):
        self.totaldata = self.read_csv_file()
        self.target_month = None
        self.target_year = None
        self.holidayboolean = False

    def settarget(self,target_month,target_year):
        self.target_year = target_year
        self.target_month = target_month         


    def sethoildaybool(self,hoildaybool):
        self.holidayboolean = hoildaybool


    #讀檔並轉二維陣列
    def read_csv_file(self):
        data=[]
        with open('uploaded_schedule.csv','r') as file:
            csv_reader=csv.reader(file)
            for row in csv_reader:
                data.append([value for value in row])
        return data


    #如果參數有給名字就輸出此人的班表，沒有就輸出整份班表
    def getschedule(self,name=None):
        sch = 'schedule.csv'
        with open(sch,'w',newline='')as file:
            if name == None:
                writer=csv.writer(file)
                writer.writerow(['day','start','end'])
            else:                    
                writer=csv.writer(file)
            for row in self.totaldata:
                if name is None :
                    writer.writerow(row)
                elif (row[1]==name 
                        or row==self.totaldata[0]):
                    writer.writerow([row[0],row[2],
                                     row[3]])
        return sch
    #用來帳密驗證    
    def getverify(self):
        name=[row[1] for row in self.totaldata]
        return name

    #計算每個人某年某月總薪資
    def calculate_total_hours(self):
        #取現實年月
        current_month = datetime.datetime.now().month
        current_year = datetime.datetime.now().year

        #取當月所有日期
        first_day = datetime.datetime(self.target_year,
                                      self.target_month,
                                      1)
        next_month = (first_day.replace(day=28) 
                      + datetime.timedelta(days=4))
        last_day = (next_month 
                    - datetime.timedelta(days = 1))
        all_dates = [first_day 
                     + datetime.timedelta(days=x) 
                     for x in range((last_day - first_day).days + 1)]                     

        # 讀取國定假日資訊
        holidays = []
        with open('holidays.csv','r') as file:
            reader = csv.reader(file)
            next(reader)  # 跳過標題列
            for row in reader:
                holiday_date = datetime.datetime.strptime(
                            row[0],"%Y-%m-%d").date()
                holidays.append(holiday_date)

        #計算員工總時數
        weekday_hours = {}
        holiday_hours={}
        for employee_schedule in self.totaldata:    
            
            employee = employee_schedule[1]
            #跳過標題列
            if employee == 'name':
                continue
            
            if employee not in weekday_hours:
                weekday_hours[employee] = 0

            if employee not in holiday_hours:
                holiday_hours[employee] = 0
        
            weekdayhours = 0
            holidayhours = 0
            for date in all_dates:
                day = date.strftime("%A")

                if day == employee_schedule[0]:
                   
                    if (date == datetime.datetime.now() 
                            and date.month == current_month 
                                and date.year == current_year):
                        # 若為當前日期，計算到目前時間的工作時數
                        start_time = datetime.datetime(date.year,
                                                       date.month,
                                                       date.day,
                                                       float(employee_schedule[2]))
                        end_time = datetime.datetime.now()
                        diff = end_time - start_time
                        working_hours = diff.total_seconds() / 3600
                    else:
                        # 非當前日期，計算整天的工作時數
                        working_hours = (float(employee_schedule[3]) 
                                         - float(employee_schedule[2]))

                    if (date.date() in holidays) and (self.holidayboolean):
                        holidayhours += working_hours
                    else:
                        weekdayhours += working_hours

            weekday_hours[employee] += weekdayhours
            holiday_hours[employee] += holidayhours

        return weekday_hours , holiday_hours
    