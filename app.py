from flask import Flask, render_template, request
import psycopg2
from models import db


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
    
if __name__ == '__main__':
    app.debug = True
    app.run()