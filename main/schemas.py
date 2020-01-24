from main.config import ma
from flask_marshmallow import fields
from main.models import Faculty, Specialty, Exam, Enrollee



# Models schemas

class FacultySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title')


class SpecialtySchema(ma.ModelSchema):
    class Meta:
        model = Specialty
        fields = ('id', 'title', 'faculty.title', 'faculty.id', 'exam.id', 'exam.title')


class ExamSchema(ma.ModelSchema):
    class Meta:
        model = Exam
        fields = ('id', 'title')


class EnrolleeSchema(ma.ModelSchema):
    class Meta:
        model = Enrollee
        fields = ('id', 'first_name', 'last_name', 'age', 'phone_number', \
            'specialty.title', 'exam.title', 'exam_scores')


# Models schemas init

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

specialty_schema = SpecialtySchema()
specialties_schema = SpecialtySchema(many=True)

exam_schema = ExamSchema()
exams_schema = ExamSchema(many=True)

enrollee_schema = EnrolleeSchema()
enrollees_schema = EnrolleeSchema(many=True)