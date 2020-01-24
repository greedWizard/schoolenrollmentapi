from flask import Blueprint, request, jsonify
from main.models import Specialty, Faculty
from main.config import db
from main.schemas import specialty_schema, specialties_schema


specialties = Blueprint('specialties', __name__)


@specialties.route('', methods=['POST'])
def add():
    title = request.json['title']
    faculty_id = request.json['faculty_id']
    exam_id = request.json['exam_id']

    specialty = Specialty(title, faculty_id, exam_id)

    db.session.add(specialty)
    db.session.commit()

    return specialty_schema.jsonify(specialty)


@specialties.route('', methods=['GET'])
def get_all() -> list:
    '''params: faculty'''
    specs = []

    faculty_title = request.args.get('faculty')

    if faculty_title:
        specs = Specialty.query.join(Faculty).filter_by(title=faculty_title)
    else:
        specs = Specialty.query.all()

    result = specialties_schema.dump(specs)

    return jsonify(result)


@specialties.route('<int:id>', methods=['GET'])
def get(id):
    specialty = Specialty.query.get_or_404(id)
    result = specialty_schema.dump(specialty)

    return jsonify(result)


@specialties.route('<int:id>', methods=['PUT'])
def update(id):
    specialty = Specialty.query.get_or_404(id)

    if 'title' in request.json:
        specialty.title = request.json['title']
    
    if 'faculty.id' in request.json:
        specialty.faculty_id = request.json['faculty.id']
        print(request.json['faculty.id'])

    db.session.commit()

    return specialty_schema.jsonify(specialty)


@specialties.route('/<int:id>', methods=['DELETE'])
def delete(id) -> Faculty:
    specialty = Specialty.query.get_or_404(id)

    db.session.delete(specialty)
    db.session.commit()

    return specialty_schema.jsonify(specialty)