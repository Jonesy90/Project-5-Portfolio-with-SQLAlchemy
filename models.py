from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column('Title', db.String())
    date = db.Column('Date', db.String())
    description = db.Column('Description', db.String())
    skills = db.Column('Skills', db.String())
    project_link = db.Column('URL', db.String())

    def __repr__(self):
        return f'''<Project (Title: {self.title}
                    Date: {self.date}
                    Description: {self.description}
                    Skills: {self.skills}
                    Project Link: {self.project_link})'''

