from tkinter import messagebox as msg
from tkinter import Tk
from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)



@app.route('/')
def hello():
    return '안녕하세요.'
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
        return "GET으로 전달된 데이터"
     
    else:
        id = request.form['id']
        pw = request.form['pw']
        
        if (id == 'aaa' and pw == '1234'):
            print(id, pw)
            root= Tk()
            root.withdraw()
            return msg.showinfo('반갑습니다!' ,'아이디: {} 패스워드: {}'.format(id, pw))
        else:
            root= Tk()
            root.withdraw()
            return msg.showinfo("로그인 불가", "ID,PW를 확인해주세요.")

if __name__ == '__main__':
    app.run(debug=True)