from tkinter import messagebox as msg
from tkinter import Tk
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)



@app.route('/')
def hello():
    return '안녕하세요.'
@app.route('/getinfo')
def getinfo():
    with open('static/save.txt','r',encoding='utf-8') as file:
        student = file.read().split(',')
    return '번호 : {}, 이름 : {}'.format(student[0], student[1])
#네이버
@app.route('/naver')
def naver():
    return render_template("naver.html")
#다음
@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")
if __name__=='__main__':
    with app.test_request_context():
        print(url_for('daum'))
    app.run(debug=True)
@app.route('/move/naver')
def url_test():
    return redirect(url_for('naver'))
@app.route('/move/daum')
def url_daum():
    return redirect(url_for('daum'))
#로그인
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/method', methods=['GET', 'POST'])    
def method():
    if request.method == 'GET':
        id = request.args['id']
        pw = request.args['pw']

        return "GET으로 전달된 데이터({},{})".format(id,pw)
     
    else:
        id = request.form['id']
        pw = request.form['pw']
        with open('static/save.txt','w', encoding='utf-8') as f:
            f.write('%s,%s' % (id, pw))
        return 'POST로 전달된 데이터({}, {})'.format(id,pw)
if __name__ == '__main__':
    app.run(debug=True)