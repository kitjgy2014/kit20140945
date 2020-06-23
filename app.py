from flask import Flask, request ,redirect, render_template, url_for , abort, session
app = Flask(__name__)

import game
import json
import random
import dbdb

app.secret_key = b'aaa!111/'

@app.route('/')
def hello():
    return render_template("main.html")

@app.route('/join')
def join():
    return render_template('test.html')

@app.route('/form') 
def form(): 
    if 'user' in session: 
        return render_template('test.html') 
    return redirect(url_for('login'))


@app.route('/method', methods=['GET', 'POST']) 
def method(): 
    if request.method == 'GET': 
        return 'GET 으로 전송이다.' 
    else: 
        num = request.form["num"] 
        name = request.form["name"] 
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo') 
def getinfo(): 
    info = dbdb.select_all() 
    retstr = '' 
    for i, v in enumerate(info): 
        retstr += '%d. 학번: %s 이름: %s<br>' % (i+1, v[0], v[1]) 
    return retstr


@app.route('/gamemain')
def gamemain():
    return render_template('game.html')

@app.route('/gamestart')
def gamestart():
    with open('save.txt','r', encoding='utf-8') as f:
         date = f.read()
         character = json.loads(date)
         print(character)
    return render_template('stage1.html', data=character)
@app.route('/input/<int:num>')
def one_num(num):
    if num == 1:
        return render_template('stage1-1.html')
    elif num == 2:
        return render_template('stage1-2.html')
    elif num == 3:
        return render_template('stage2-1.html')
    elif num == 4:
        return render_template('stage2-2.html')

@app.route('/stagetwo')
def stagetwo():
    return render_template('stage2.html')
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
@app.route('/login', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'GET': 
        return render_template('login.html')
    else: 
        id = request.form['id'] 
        pw = request.form['pw'] 
        print (id,type(id))
        print (pw,type(pw))
        ret = dbdb.select_user(id,pw)
        print(ret[2])
        if ret != None:
            session['user'] = id
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))
            # 로그아웃(session 제거) 
@app.route('/logout') 
def logout(): 
    session.pop('user', None) 
    return redirect(url_for('form')) 
if __name__ == '__main__':
    app.run(debug=True)