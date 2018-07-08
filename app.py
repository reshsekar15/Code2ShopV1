from flask import Flask, render_template, request
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
	
@app.route('/challengeupload', methods = ['POST', 'GET'])
def challengeupload():
	if request.method == 'POST':
		challengeID = request.form('challengeid')
		challengename = request.form('challengename')
		challengepoints = request.form('challengepoints')
		
		#add to database
		db.session.add(challengeid)
		db.session.commit()		
	return render_template("challengeupload.html")
	
@app.route('/challengeuploadsuccess', methods = ['POST', 'GET'])
def challengeuploadsuccess():
	#if request.method == 'POST':
		#challengeID = request.form('challengeid')
		#challengename = request.form('challengename')
		#challengepoints = request.form('challengepoints')
		
		#add to database
	#session = Sessionmaker()
	challenge_row = Challenges(challengeID = 1, challengeName = 'Test challenge', challengePoints = 100)
	db.session.add(challenge_row)
	db.session.commit()		
	return render_template("challengeuploadsuccess.html")
    
if __name__ == '__main__':
    app.debug = True
    app.run()