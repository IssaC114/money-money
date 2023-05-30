""" 
目的：主函式撰、與html進行連接
負責組員：周詠熙（主要架構與html撰寫）
"""

from flask import Flask, redirect
from flask import make_response,request
from flask import render_template, send_file
from money import MoneyCalculator
from schedule import scheduleclass
import pandas as pd

app = Flask(__name__)
sch = scheduleclass()
cal_money = MoneyCalculator(sch)

'''以下為登入登出相關函式'''
#驗證帳密與登入者身分（管理員/工讀生）
def validate_credentials(username, password):
    if username == "admin" and password == "1234":
        return 'admin'
    elif username in sch.getverify() and password == "5678":
        return 'employee'
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
#登陸頁面導向 -->admin/employee
def login():
    user = request.cookies.get('username')
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = validate_credentials(username, password)
        if role == 'admin':
            response = make_response(username)
            response.set_cookie('username', username)
            return redirect('/admin')
        elif role == 'employee':
            response = make_response(username)
            response.set_cookie('username', username)
            return redirect(f'/employee/{username}')
        else:
            error = "帳號或密碼錯誤，請重新輸入"
            return render_template('login.html', 
                                   error=error)
    elif user:
        if user == 'admin':
            return redirect('/admin')
        elif user == 'employee':
            return redirect(f'/employee/{username}')
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
#登出作業
def logout():
    # 檢查是否存在使用者的 cookies
    if 'username' in request.cookies:
        # 刪除 cookies
        response = make_response('Logged out!')
        response.delete_cookie('username', '', expires=0)
        return render_template('login.html')
    return redirect('/')

'''以下為關於管理員的函式'''
#admin介面
@app.route("/admin",methods=['GET','POST'])
def admin():
    return render_template('admin.html')

@app.route("/admin/settings",methods=['GET','POST'])
#設定介面
def settings():
    if request.method == "POST":
        if 'wages' in request.form:
        #設置薪資
            wages = int(request.form['wages'])
            if wages >= 176:
                cal_money.set_wages(wages)
                success = f"薪資更新成功！目前薪資為{wages}"
                return render_template('settings.html', 
                                       success_1=success)
            else:
                error = "輸入值小於基本薪資，更新失敗"
                return render_template('settings.html', 
                                       error_1=error)
        
        if 'holiday' in request.form:
        #設置國定假日上班模式
            holiday = request.form['holiday']
            if holiday.lower() == 'y':
                work = True
                sch.sethoildaybool(work)
                success = "目前計算模式：國定假日上班"
                return render_template('settings.html', 
                                       success_2=success)
            elif holiday.lower() == 'n':
                work = False
                sch.sethoildaybool(work)
                success = "目前計算模式：國定假日不上班"
                return render_template('settings.html', 
                                       success_2=success)
            else:
                error = "錯誤：請輸入字母Y或N來進行調整"
                return render_template('settings.html', 
                                       error_2=error)

    return render_template('settings.html')


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
    
@app.route('/admin/arrange',methods=['POST','GET'])
def set_time():
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        if month <=12 and month >=1:
            sch.settarget(month,year)
            success = f"設定成功!月份為{sch.target_month}年份為{sch.target_year}"
            return render_template('export_total.html',
                                   success=success)
        else:
            error = "月份輸入有誤，請重新輸入。"
            return render_template('export_total.html',
                                   error = error)
    return render_template('export_total.html')

@app.route('/admin/arrange/download',methods=['GET'])
def download_wages_total():
    filename = cal_money.export_salary_to_csv()
    return send_file(filename,
                as_attachment=True)

    
'''以下為關於員工的函式'''
@app.route('/employee/<username>',methods=['GET','POST'])
def employee(username):    
    return render_template('employee.html',username=username)

@app.route("/employee/<username>/schedule",methods=['GET'])
def schedule_emp(username):
    filename = sch.getschedule(username)
    return send_file(filename,
                     as_attachment=True)

@app.route('/employee/<username>/wages',methods=['POST','GET'])
def wages_person(username):
    if request.method == 'POST':
        year = int(request.form['year'])
        month = int(request.form['month'])
        if month <=12 and month >=1:
            sch.settarget(month,year)
            wages = cal_money.employee_salary(username)
            success = f"{sch.target_year}年{sch.target_month}月的薪資為{wages}"
            return render_template('export_person.html',
                                   success=success,
                                   username=username)
        else:
            error = "月份輸入有誤，請重新輸入。"
            return render_template('export_person.html',
                                   error = error,
                                   username = username)
    return render_template('export_person.html')
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
