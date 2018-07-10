from flask import Flask, render_template, request, url_for, redirect
import psycopg2
from models import db
from models import Challenges


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/code2shopv1'
db.init_app(app)


@app.route('/')
def index():
   return render_template("homepage.html")
   
@app.route('/challenges')
def challenges():
	return render_template("challenges.html")
	
@app.route('/challengeupload', methods = ['GET', 'POST'])
def challengeupload():	
	return render_template("challengeupload.html")
	
@app.route('/challengeuploadsuccess', methods = ['GET', 'POST'])
def challengeuploadsuccess():
	if request.method == 'POST':
		valchallengeID = request.form['challengeid']
		valchallengename = request.form['challengename']
		valchallengepoints = request.form['challengepoints']
		
		#add to database
		challenge_row = Challenges(challengeID = valchallengeID , challengeName =  valchallengename, challengePoints = valchallengepoints)
		db.session.add(challenge_row)
		db.session.commit()	
		return render_template("challenges.html")
	return render_template("challengeuploadsuccess.html")
	
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)
	
if __name__ == '__main__':
    app.debug = True
    app.run()