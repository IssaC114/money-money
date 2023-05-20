""" 
目的：主函式撰寫
負責組員：李湘菱（主要架構）、周詠熙（html與flask框架整合）
"""

from flask import Flask, make_response
app = Flask(__name__)

from flask import request
from flask import render_template

@app.route("/")
def munu():
    return render_template('menu.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')   

if __name__ == '__main__':
    app.run(debug=True)