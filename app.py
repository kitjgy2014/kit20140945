from tkinter import messagebox as msg
from tkinter import Tk
from flask import Flask, request, render_template,session, redirect, url_for
import dbdb
app = Flask(__name__)

app.secret_key = b'aaa!111/'

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
@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        if id == 'abc' and pw == '1234':
            session['user']=id
            return '''
                <script> alert("안녕하세요~{}님");
                location.href="/form"
                </script>
            '''.format(id)
        else:
            return "아이디 또는 패스워드를 확인 하세요"        
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('form'))
@app.route('/form')
def form():
    if 'user' in session:
        return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])    
def method():
    if request.method == 'GET':
        return "GET으로 전송이다."
     
    else:
        num = request.form['num']
        name = request.form['name']
        return 'POST이다. 학번은 :({}, {})'.format(num,name)
if __name__ == '__main__':
    app.run(debug=True)