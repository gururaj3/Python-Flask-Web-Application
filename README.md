# Python-Flask-Web-Application
A web Application which allows university students to login into their university accounts and enables them to enroll for the courses available during a particular term.

First, create a virtual environment. The reason is that you want to sandbox your application so that it is not interfering with other applications.
To do that, type in "python -m venv venv" in the VS terminal.

It is important to preserve all the packages in a safe file just in case if we need to reinstall or move the application to another system, so that it makes things easier for us. For that purpose, I have created a requirements.txt file which contains all the dependencies required to run this application. This file is similar to the package.json file in Node.js Web Application development. It is important to note that you must be in the virtual environment before you install any packages/dependencies otherwise everything will be installed in the global space. 

Go into the virtual environment:   "venv/Scripts/activate"
Create the requirements.txt file:   "pip freeze > requirements.txt"
To re-install all the packages from the reuiremnets.txt file: "pip install -r requirements.txt"

I have made use of Flask-MongoEngine to set up and configure my database system(i.e. MongoDB) to store and track data. I have created a database named UTA_Enrollment in which I have 3 collections named course, enrollment and user. 
"course" collection contains the information about the courses available to register during a particular term.
"user" collection has the credentials of every student like user_id, first_name, last_name, email and hashed password.
"enrollment" collection contains data about the courses registered by every student. 

I also created a MongoDB aggregation pipeline to process the data in 3 stages:
$lookup: Performs a left outer join
$match: Filters documents
$unwind: Decontructs an array field

Used Flask-RESTPlus extension to create REST API CRUD operations using the HTTP verbs. Tested wheather these API's work fine using Postman.
HTTP verbs and CRUD operations:
POST - Create   
GET - Read
PUT - Update
DELETE - Delete
