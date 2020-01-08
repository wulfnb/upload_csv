## Simple flask web application

* This application is focusing on uploading a CSV file and populating the database 
* Log the events to a file
* Clear the database
* List the uploaded datas


## Things not implimented

The UI is pretty basic, not used any framework or library in frontend because this project is purely for the above stated purpose only


## libraries used

`flask`

`flask_sqlalchemy`

## Running steps

Need python3 installed in your system

Install virutal environment
> pip3 install virtualenv

Change directory to web
> cd web

Create virtual environment
> virtualenv venv

activate virtualenv 
> source venv/bin/activate

install required packages
> pip install -r requirements.txt

Run application
>python app.py

goto
'http://127.0.0.1'

click the upload CSV and select the CSV file attached in `sample_csv` folder


## Project Struture
#### Database
The database used in this project is sqlite database (name test.db)

#### ORM 
SQLAlchemy is used as ORM

#### Models folder
Database models will be specified here

#### util
All the utility functions will be added here

The logger is defined here and latter imported to `app.py`

The database instance also created here this will remove the complexity of counter import

#### uploads
all the uploaded datas will be added here

#### config.cfg
contains all the configurations
