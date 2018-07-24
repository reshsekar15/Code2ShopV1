from flask import Flask, render_template, request, url_for, redirect
import psycopg2
from models import db
from models import Challenges, Brands
from sqlalchemy.sql import func


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/code2shopv1'
db.init_app(app)


@app.route('/')
def index():
   return render_template("homepage.html")
   
@app.route('/aboutus')
def aboutus():
	return render_template("aboutus.html")
   
@app.route('/brands')
def brands():
	return render_template("brands.html")
   
@app.route('/paidpartners')
def paidpartners():
	return render_template("paidpartners.html")
	
@app.route('/commissionpartners', methods = ['GET', 'POST'])
def commissionpartners():
	return render_template("commissionpartners.html")
	
@app.route('/insertcommissionpartners', methods = ['GET', 'POST'])
def insertcomissionpartners():
	if request.method == 'POST':
		valbrandname = request.form['brandname']
		valproductname = request.form['productname']
		valnumberofproducts = request.form['numberofproducts']
		valcouponcode = request.form['couponcode']
		valbrandemail = request.form['brandemail']
		valbrandcontactname = request.form['brandcontactname']
		valbrandcontactnumber = request.form['brandcontactnumber']
		
		#add to database
		valbrandid = db.session.query(func.max(Brands.brandID)).scalar() + 1
		brand_row = Brands(brandID = valbrandid, brandName =  valbrandname, productName = valproductname, totalProducts = valnumberofproducts, availableProducts = valnumberofproducts, couponCode = valcouponcode, emailID = valbrandemail, contactName = valbrandcontactname, contactNumber = valbrandcontactnumber)
		db.session.add(brand_row)
		db.session.commit()	
		return render_template("Brands.html")
	return render_template("Brands.html")
	   
@app.route('/hostachallenge')

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