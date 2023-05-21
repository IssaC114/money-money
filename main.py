""" 
目的：主函式撰寫
負責組員：李湘菱（主要架構）、周詠熙（html與flask框架整合）
"""

#<<<<<<< HEAD
#最開始的系統介面
def showstartmenu():
    
    while(True):
        print("歡迎來到此系統")
        print("1)員工\n2)管理員\n0)離開")
        try:
            num = int(input("請選擇您的身分："))
            if (num>0)and(num<2):
                return num
            else:
                print("請輸入[1,2,0]\n ")
        except ValueError:
            print("請輸入整數\n ")

#員工介面
def showemployeemenu():
    
    while(True):
        print("歡迎xxx")
        print("1)看班表\n2)輸入上班紀錄\n3)本月薪資\n0)離開")
        try:
            num = int(input("請選擇要做的事："))
            if (num>0)and(num<3):
                return num
            else:
                print("請輸入[1,2,3,0]\n ")
        except ValueError:
            print("請輸入整數\n ")

#管理員介面
def showadminmenu():
    
    while(True):
        print("歡迎xx管理員")
        print("1)看部門班表\n2)上傳新的班表\n3)員工資料\n4)設定\n0)離開")
        try:
            num = int(input("請選擇要做的事："))
            if (num>0)and(num<4):
                return num
            else:
                print("請輸入[1,2,3,4,0]\n ")
        except ValueError:
            print("請輸入整數\n ")

#=======
from flask import Flask, make_response
app = Flask(__name__)

from flask import request
from flask import render_template

@app.route("/")
@app.route("/menu")
def munu():
    return render_template('menu.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')   

@app.route("/employee")
def employee():
    return render_template("employee.html")

@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)
#>>>>>>> 10cbd42fe61a4b3593d4a9833cf56db68badbb5c
