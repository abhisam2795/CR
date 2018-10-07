from flask import Flask,render_template,flash,request,url_for,redirect
from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('main.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html',TOPIC_DICT = TOPIC_DICT)

@app.route('/slashboard/')
def slashboard():
    try:
        return render_template('dashboard.html',TOPIC_DICT = TOPIC)
    except Exception as e:
        return render_template('500.html',error = e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.route('/login/',methods = ['GET','POST'])
def login():
    error = ''
    try:
        if request.method=='POST':
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            if attempted_username == 'admin' and attempted_password == 'password':
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid credentials. Try again.'
        return render_template('login.html',error=error)
        

    except Exception as e:
        return render_template('login.html',error=error)

if __name__ == '__main__':
    app.run()