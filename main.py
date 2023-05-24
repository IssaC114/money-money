""" 
目的：主函式撰、與html進行連接
負責組員：周詠熙（主要架構與html撰寫）
"""

import csv
from flask import Flask
from flask import make_response,request
from flask import render_template, send_file
from money import MoneyCalculator
import pandas as pd
app = Flask(__name__)

#基本的帳密設定
def validate_credentials(username, password):
    if username == "test" and password == "1234":
        return True
    else:
        return False
    
@app.route('/', methods=['GET', 'POST'])
@app.route('/login')
# 獲取從表單提交的帳號和密碼後判斷是否正確
#再將其連結至admin介面
def login():
    username = request.cookies.get('username')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if validate_credentials(username,password):
            # 建立cookies
            response = make_response(username)
            response.set_cookie('username', 
                                username)
            return response
        else:
            error = "帳號或密碼錯誤，請重新輸入"
            return render_template('login.html',
                                   error=error)
        # GET 請求，顯示登入頁面
    elif username:
        return render_template('admin.html')
    #return render_template('login.html')

#admin介面
@app.route("/admin",methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route("/admin/wages",methods=['GET','POST'])
#薪資設定頁面
def set_wages():
    if request.method=="POST":
        wages=int(request.form['wages'])
        if wages >= MoneyCalculator.wages:
            MoneyCalculator.set_wages_total(wages)
            success = "薪資更新成功！"
            return render_template('setwages.html',
                                   success=success)           
        else:
            error="輸入值小於基本薪資，更新失敗"
            return render_template('setwages.html',
                                   error=error)
    return render_template('setwages.html')

@app.route('/admin/upload', methods=['GET', 'POST'])
def upload_schedule():
    if request.method == 'POST':
        # 接收上傳的CSV文件
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            # 將上傳的CSV文件保存到本地
            file.save('uploaded_schedule.csv')
            # 處理CSV文件，這裡只是讀取CSV文件的內容並返回給前端
            df = pd.read_csv('uploaded_schedule.csv')
            if not df.empty:
                return render_template('upload.html', 
                                       data=df.to_html(index=False), 
                                       success=True)
            else:
                error = '上傳的CSV文件為空'
                return render_template('upload.html', 
                                       error=error)
        else:
            error = '上傳的文件必須是CSV格式'
            return render_template('upload.html', 
                                   error=error)

    return render_template('upload.html')

@app.route('/admin/upload/download', methods=['GET'])
def download_schedule():
    # 下載模板schedule.csv
    return send_file('schedule_template.csv', 
                     as_attachment=True)

@app.route('/admin/schedule',methods=['GET'])
#下載目前班表
def schedule_now():
    return send_file('uploaded_schedule.csv',
                     as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
