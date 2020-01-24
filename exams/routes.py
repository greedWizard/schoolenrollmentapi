from flask import Blueprint, request, jsonify
from main.models import Exam
from main.schemas import exam_schema, exams_schema
from main.config import ma, db


exams = Blueprint('exams', __name__)


@exams.route('', methods=['POST'])
def add():
    title = request.json['title']
    exam = Exam(title)

    db.session.add(exam)
    db.session.commit()

    return exam_schema.jsonify(exam)


@exams.route('', methods=['GET'])
def get_all():
    exams = Exam.query.all()
    result = exams_schema.dump(exams)

    return jsonify(result)


@exams.route('<int:id>', methods=['GET'])
def get(id):
    exam = Exam.query.get_or_404(id)

    return exam_schema.jsonify(exam)


@exams.route('<int:id>', methods=['PUT'])
def update(id):
    exam = Exam.query.get_or_404(id)
    exam.title = request.json['title']

    db.session.commit()

    return exam_schema.jsonify(exam)


@exams.route('<int:id>', methods=['DELETE'])
def delete(id):
    exam = Exam.query.get_or_404(id)

    db.session.delete(exam)
    db.session.commit()

    return exam_schema.jsonify(exam)