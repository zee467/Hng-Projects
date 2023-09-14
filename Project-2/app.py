from flask import Flask, jsonify, abort, make_response, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables from .flaskenv file
load_dotenv(".flaskenv")


# create flask instance
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_NAME")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# instantiate db
db = SQLAlchemy(app)

# A database model class
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def as_dict(self):
        return {f"{field.name}": getattr(self, field.name) for field in self.__table__.columns}

    def __repr__(self):
        return f"<Person {self.name}>"


# fetches all the records in the database
@app.route("/api/persons", methods=["GET"])
def get_person():
    people = Person.query.all()
    people_list = [person.as_dict() for person in people]

    # jsonify serializes dicts, list, and tuples to a JSON response
    return jsonify({"people": people_list}), 200


# query for a specific person in the database
@app.route("/api/persons/<id>", methods=["GET"])
def get_specific_person(id):
    person = Person.query.filter_by(id=id).first()
    if not person:
        abort(404)

    return jsonify(result=[person.as_dict()]), 200


@app.errorhandler(400)
def invalid_err(error):
    return make_response(jsonify({"error": "Invalid input. Please check your name and email."}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "This person doesn't exist!"}), 404)

def check_email_exists(person_email):
    return Person.query.filter_by(email=person_email).first()

def check_name_exists(person_name):
    return Person.query.filter_by(email=person_name).first()  


# create a person
@app.route("/api/persons", methods=["POST"])
def create_person():
    data = request.json
    fields = ["name", "email", "age"]
    if not data:
        abort(400)

    for field in fields:
        if field not in data:
            abort(400)

    name = request.json.get("name")
    email = request.json.get("email")
    if not check_name_exists(name) and not check_email_exists(email):
        new_person = Person(name=request.json.get("name"),
                            email=request.json.get("email"),
                            age = request.json.get("age")
                            )
        db.session.add(new_person)
        db.session.commit()
        return jsonify({"person": new_person.as_dict()}), 201
    else:
        return jsonify({"message": "Person already exist in the database!"}), 409  
    

# update a person detail
@app.route("/api/persons/<id>", methods=["PUT"])
def update_person_info(id):
    person = Person.query.filter_by(id=id).first()

    if not person:
        abort(404)
    
    person.name = request.json.get("name")
    person.email = request.json.get("email")
    person.age = request.json.get("age")
    db.session.add(person)
    db.session.commit()

    return jsonify({"person": person.as_dict()}), 200


# delete a person
@app.route("/api/persons/<id>", methods=["DELETE"])
def delete_person(id):
    existing_user = Person.query.filter_by(id=id).first()
    if not existing_user:
        abort(404)
    
    db.session.delete(existing_user)
    db.session.commit()
    return '', 204


