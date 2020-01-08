from flask_sqlalchemy import SQLAlchemy

"""
    For avoiding the counter import problems we creating the 
    sqlalchemy database declatation in a seperate file
"""
db = SQLAlchemy()
