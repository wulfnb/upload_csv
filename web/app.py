from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import csv
import os
from util.custom_logger import file_handler
from util.databae_conn import db

app = Flask(__name__)

app.config.from_pyfile('config.cfg')

# Initialzing Database here
db.init_app(app)

# intializing custom logger here
app.logger.addHandler(file_handler(app.config['LOG_FILE']))

from models.main import Temperature

@app.route('/')
def home():
    return render_template("home.html")

# For listing the datas
@app.route('/data_list')
def data_list():
    app.logger.info("Requested Data From table")
    obj = db.session.query(Temperature).all()
    results = []
    for i in obj:
        results.append(i.id)
    return render_template("data_list.html", results = obj)
    
#  Uploading the data to database
@app.route('/upload', methods = ['GET','POST'])  
def upload():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        app.logger.warning("Inserting new records")
        try:
            with open(app.config['UPLOAD_FOLDER'] + f.filename, mode='r') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for row in csv_reader:
                    new_obj = Temperature()
                    new_obj.id =row.get('id')
                    new_obj.duration =row.get('duration')
                    new_obj.temperature =row.get('temperature')
                    new_obj.timestamp = datetime.strptime(row.get('timestamp'), '%Y-%m-%d %H:%M:%S.%f')
                    db.session.add(new_obj)
                    
                db.session.commit()
        except:
            return render_template("success.html", 
                        details = "There is an error in processing the file clear the database and try again")

        return render_template("success.html", details = "File "+f.filename+" Uploaded")
    else:
        return render_template("file_upload_form.html")  

# Cleaning Database
@app.route('/clear')
def clear():
    app.logger.warning("Clean the database command recived")
    db.drop_all()
    db.create_all()
    return render_template("success.html", details = "Done database cleaned")


if __name__ == '__main__':
    app.run()