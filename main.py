""" 
目的：主函式撰寫
負責組員：周詠熙（主要架構與html撰寫）、李湘菱（從旁協助與部分函式撰寫）
"""

from flask import Flask, make_response, redirect,request,render_template
app = Flask(__name__)

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
            response = make_response(admin())
            response.set_cookie('username', username)
            return response
        else:
            error = "帳號或密碼錯誤，請重新輸入"
            return render_template('login.html',
                                   error=error)
        # GET 請求，顯示登入頁面
    elif username:
        return admin()
    return render_template('login.html')

#基本的帳密設定
def validate_credentials(username, password):
    if username == "test" and password == "1234":
        return True
    else:
        return False

#admin介面
@app.route("/admin",methods=['GET','POST'])
def admin():
    return render_template('admin.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5001,debug=True)
