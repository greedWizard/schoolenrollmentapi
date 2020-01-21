from main.config import db


# Models

class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<Faculty: {self.title}>'

    def __init__(self, title):
        self.title = title


class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    faculty = db.relationship('Faculty', backref=db.backref('specialties', lazy=True))

    def __repr__(self):
        return f'<Speicality: {self.faculty} {self.title}>'

    def __init__(self, title, faculty_id):
        self.title = title
        self.faculty_id = faculty_id


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<Exam: {self.title}>'

    def __init__(self, title):
        self.title = title


class Enrolee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    
    speciality_id = db.Column(db.Integer, db.ForeignKey('specialty.id'))
    speciality = db.relationship('Specialty', backref=db.backref('enrolees', lazy=True))

    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam = db.relationship('Exam', backref=db.backref('enrolees'), foreign_keys=[exam_id])

    exam_scores = db.Column(db.Integer)

    def __init__(self, first_name, last_name, age, phone_number, speciality_id, \
        exam1_id, exam2_id, exam3_id, exam1_score, exam2_score, exam3_score):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.phone_number = phone_number
            self.speciality_id = speciality_id
            self.exam1_id = exam1_id
            self.exam2_id = exam2_id
            self.exam3_id = exam3_id
            self.exam1_score = exam1_score
            self.exam2_score = exam2_score
            self.exam3_score = exam3_score

            self.total_scores = exam1_score + exam2_score + exam3_score
        

    def __repr__(self):
        return f'<Enrolee: {self.last_name}, {self.first_name} {self.phone_number} \
            {self.speciality} total score: {self.total_scores}>'