import json
import sys

sys.path.insert(1, 'Components')
sys.path.insert(0, '../ClashRoyaleTokens')
from flask import Flask,render_template,flash,request,url_for,redirect
from content_management import Content
from DirectoryManager import getDirectories
import functionalities
from parseBackEndData import parseCardDetails
import CRconstants

TOPIC_DICT = Content()


app = Flask(__name__)


@app.route('/playerTag/',methods = ['GET','POST'])
def dummyPlayerSearch():
    error = ''

    try:
        if request.method=='POST':
            CRconstants.playerTag = request.form['PlayerTag']
            
            return redirect(url_for('cardDetails'))
        else:
            print "Not POST"
        return render_template('PlayerTag.html',error=error)

    except Exception as e:
        return render_template('PlayerTag.html',error=error)

@app.route('/')
def homepage():
    
    return render_template('main.html',imagesList = CRconstants.imagesList,imageFolderPath = CRconstants.imageFolderPath)

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


@app.route('/cardDetails/')
def cardDetails():
    error = ''
    #json_string = main.getCardDetails(playerTag)
    #json_string = "{\"cardsWhichAreDonatable\": [\"Poison\", \"Skeleton Army\", \"Furnace\"], \"cardsHaving\": [\"Furnace\", \"Mega Minion\", \"Mini P.E.K.K.A\"], \"cardsNotUnlocked\": [\"Magic Archer\"]}"
    print CRconstants.playerTag
    json_string = functionalities.getCardDetails(CRconstants.playerTag)
    json_data = json.loads(json_string)
    cardDetailsList = parseCardDetails(json_data)
    #print "cardDetailsList",cardDetailsList
    #return render_template('login.html',error=error)
    return render_template('cardDetails.html',imageFolderPath = CRconstants.imageFolderPath, cardsWhichAreDonatable = cardDetailsList['cardsWhichAreDonatable'], cardsHaving = cardDetailsList['cardsHaving'], cardsNotUnlocked = cardDetailsList["cardsNotUnlocked"],error = error)

if __name__ == '__main__':
    CRconstants.imageFolderPath = "images/cards/"
    CRconstants.imagesList = getDirectories("./static/"+CRconstants.imageFolderPath)

    app.run(debug = True)
    

