from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)

db.create_all()

with open('dataset/data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        example = ExampleModel(name=row['name'], age=row['age'])
        db.session.add(example)

db.session.commit()