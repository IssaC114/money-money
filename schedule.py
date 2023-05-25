""" 
目的：班表輸入與輸出、更改
負責組員：李湘菱
"""
import csv
import datetime

#讀檔並轉二維陣列
def read_csv_file(file_path):
    data=[]
    with open(file_path,'r') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            data.append([value for value in row])
    return data

#得到某人的總時數
def gettotaltime(name):
    totaltime=0
    totaldata=read_csv_file('uploaded_schedule.csv')
    for i in totaldata:
        if (i[1]==name):
            totaltime+=int(i[3])-int(i[2])
    return totaltime

#如果參數有給名字就輸出此人的班表，沒有就輸出整份班表
def getschedule(name=None):
    totaldata=read_csv_file('uploaded_schedule.csv')
    with open('schedule.csv','w',newline='')as file:
        writer=csv.writer(file)
        for row in totaldata:
            if name is None or row[1]==name or row==totaldata[0]:
                writer.writerow(row)
        

def getverify():
    getschedule()
    data=read_csv_file('uploaded_schedule.csv')
    name=[row[1] for row in data]
    return name

def calculate_total_hours(target_month , target_year):
    #取現實年月
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year

    #取當月所有日期
    first_day = datetime.datetime(target_year,target_month,1)
    next_month = first_day.replace(day=28) + datetime.timedelta(days=4)
    last_day = next_month - datetime.timedelta(days = 1)
    all_dates = [first_day + datetime.timedelta(days=x) for x in range((last_day - first_day).days + 1)]

    total_hours = {}

    for employee_schedule in read_csv_file('uploaded_schedule.csv'):
        
        employee = employee_schedule[1]
        if employee == 'name' :
            continue
        if employee not in total_hours:
            total_hours[employee] = 0
    
        hours = 0

        for date in all_dates:
            day = date.strftime("%A")

            if day == employee_schedule[0]:
                if date == datetime.datetime.now() and date.month == current_month and date.year == current_year:
                    start_time = datetime.datetime(date.year , date.month , date.day , float(employee_schedule[2]))
                    end_time = datetime.datetime.now()
                    diff = end_time - start_time
                    working_hours = diff.total_seconds() / 3600
                else:
                    # 非當前日期，計算整天的工作時數
                    working_hours = float(employee_schedule[3]) - float(employee_schedule[2])

                hours += working_hours

        total_hours[employee] += hours
    return total_hours

