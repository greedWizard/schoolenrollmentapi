from main.config import ma


# Models schemas

class FacultySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title')


class SpecialtySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'faculty_id', 'faculty')


class ExamSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title')


# Models schemas init

faculty_schema = FacultySchema()
faculties_schema = FacultySchema(many=True)

specialty_schema = SpecialtySchema()
specialties_schema = SpecialtySchema(many=True)

exam_schema = ExamSchema()
exams_schema = ExamSchema(many=True)