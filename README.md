# AssistanceManager
This repository is the Final Project for Databases course at Universidad del Norte. It was made using FlaskAppBuilder and an Oracle Database.

## Features
- Simulate the database structure of a University
- Assistance manager for all Students and Professors
- Record of Assistance for every class
- Basic CRUD features for every table of the database only accesible to the admin

## Preview
![Welcome](extra/WelcomeScreen.png?raw=true "Welcome Screen")
Welcome screen



![History](extra/AssistanceHistory.png?raw=true "History")
Attendance Record of a student


## Setup

1. Install all requirements using `pip install -r requirements.txt`
2. Create a file nammed `conn_string.py` that should look like this:  
`cs = 'oracle://user:password@host:port/serviceName'`

4. In your terminal run the following commands:
```
$ export FLASK_APP=app

# Creates all tables of the database filling it with the data provided in 'test_data.py'
$ flask initdata

# Creates all the users for every student, teacher and an admin user
$ flask createusers
$ flask run
 ```
4. The Webapp should now be running in localhost:5000
