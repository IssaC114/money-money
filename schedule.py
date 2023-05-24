""" 
目的：班表輸入與輸出、更改
負責組員：李湘菱
"""
import csv

def read_csv_file(file_path):
    data=[]
    with open(file_path,'r') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            data.append([value for value in row])
    return data
#!!!
def getschedule(name,total):
    
    for i in total:
        if (i[0]=='day') or (i[1]==name):
            print(i[0],i[1],i[2],i[3],sep="   ")
        

# file_path='uploaded_schedule.csv'
# total=read_csv_file(file_path)
# getschedule('Megan',total)
