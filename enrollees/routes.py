from flask import Blueprint, request, jsonify
from main.config import db
from main.schemas import enrollee_schema, enrollees_schema
from main.models import Enrollee


enrollees = Blueprint('enrolees', __name__)


@enrollees.route('', methods=['POST'])
def add():
    data = {
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'age': request.json['age'],
        'phone_number': request.json['phone_number'],
        'specialty_id': request.json['specialty_id'],
        'exam_id': request.json['exam_id'],
        'exam_scores': request.json['exam_scores'],
    }

    print(data)

    enrollee = Enrollee(**data)

    db.session.add(enrollee)
    db.session.commit()

    return enrollee_schema.jsonify(enrollee)


@enrollees.route('', methods=['GET'])
def get_all():
    ens = Enrollee.query.all()

    result = enrollees_schema.dump(ens)

    return jsonify(result)


@enrollees.route('<int:id>', methods=['DELETE'])
def delete(id):
    enrollee = Enrollee.query.get_or_404(id)

    db.session.delete(enrollee)
    db.session.commit()

    return enrollee_schema.jsonify(enrollee)


# @enrollees