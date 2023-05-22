""" 
目的：主函式撰寫
負責組員：李湘菱（主要架構）、周詠熙（html與flask框架整合）
"""

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

from flask import Flask, make_response, redirect
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 獲取從表單提交的帳號和密碼
        username = request.form['username']
        password = request.form['password']

        # 假設您有一個函式或資料庫來驗證帳號和密碼
        user_role = validate_credentials(username, password)

        if user_role == 'admin':
            # 登入成功，導向管理員網頁
            return render_template('admin.html')
        elif user_role == 'employee':
            # 登入成功，導向工讀生網頁
            return render_template('employee.html')
        else:
            # 登入失敗，重新導向登入頁面或顯示錯誤訊息
            error = "帳號id或密碼錯誤，請重新輸入"
            return render_template('login.html', error = error)
    else:
        # GET 請求，顯示登入頁面
        return render_template('login.html')


def validate_credentials(username, password):
    # 假設您的使用者資料儲存在字典中
    user_data = {
        'admin': {
            'password': 'adminpassword',
            'role': 'admin'
        },
        'employee': {
            'password': 'employeepassword',
            'role': 'employee'
        }
    }

    if username in user_data:
        if password == user_data[username]['password']:
            return user_data[username]['role']

    return None



if __name__ == '__main__':
    app.run(debug=True)
#>>>>>>> 10cbd42fe61a4b3593d4a9833cf56db68badbb5c
