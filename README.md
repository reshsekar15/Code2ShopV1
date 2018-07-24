# Code2ShopV1
#Setting up GitHub
Please clone the repository 
Set up a heroku account
Request access to heroku app from admin
Login to heroku using command line 
Make changes to code on your folder locally
Create a branch for yourself on git - name the branch with the changes you are going to make
Test your changes using heroku -a open code2shopv1
Push up your changes to Git (and Heroku if necessary)

#Database
All connections to database has been made
Please use flask python app to create tables
Database migrations will be set up and can be used to make updates/changes to tables
Request username and password; use this for access to database
Username and password must be created by admin from Heroku

#Config.py
Code2Shop will be managed in 4 environments namely: Development, Testing, Staging and Production. Database, debug and other related configuration will be managed in the config.py file

#Models.py
Models.py should contain all tables we will need for this application

#Database Migrations
The migrations folder should contain all version of tables created, dropped etc.
Each time an update is made to models.py, the “python manage.py db migrate” command must be run for the changes to be reflected

#Making changes to data model
The changes are handled through migrations. 
Make table changes to models.py class
Next run the following commands in command line
python manage.py
python manage.py db migrate
python manage.py db upgrade

This will ensure that data model is updated with what is defined in models.py
The migrations folder will have a file with all the changes (SQL queries executed)























































































































