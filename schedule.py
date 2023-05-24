""" 
目的：班表輸入與輸出、更改
負責組員：李湘菱
"""
import csv

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
    with open(totaldata,'w',newline='')as file:
        writer=csv.writer(file)
        for row in totaldata:
            if name is None or row[1]==name or row==totaldata[0]:
                writer.writerow(row)
        

def getverify():
    getschedule()
    data=read_csv_file('uploaded_schedule.csv')
    name=[row[1] for row in data]
    return name




