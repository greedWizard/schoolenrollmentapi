from flask import Blueprint, request, jsonify
from main.models import Faculty
from main.schemas import faculty_schema, faculties_schema
from main.config import ma, db


faculties = Blueprint('faculties', __name__)


@faculties.route('', methods=['POST'])
def add() -> Faculty:
    ''' Adds a new faculty
    requested params: title(title of the faculty)'''

    title = request.json['title']
    faculty = Faculty(title)

    db.session.add(faculty)
    db.session.commit()

    return faculty_schema.jsonify(faculty)


@faculties.route('', methods=['GET'])
def get_all() -> list:
    faculties = Faculty.query.all()
    result = faculties_schema.dump(faculties)

    return jsonify(result)


@faculties.route('/<int:id>', methods=['PUT'])
def update(id: int) -> Faculty:
    fac = Faculty.query.get_or_404(id)

    title = request.json['title']
    fac.title = title

    db.session.commit()

    return faculty_schema.jsonify(fac)