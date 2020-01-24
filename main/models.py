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
    faculty = db.relationship('Faculty', backref=db.backref('specialties', lazy='subquery', \
        cascade='all, delete-orphan'))

    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam = db.relationship('Exam', backref=db.backref('speialties',\
         lazy='subquery', cascade='all, delete-orphan'), foreign_keys=[exam_id])

    def __repr__(self):
        return f'<Speicality: {self.faculty} {self.title}>'

    def __init__(self, title, faculty_id, exam_id):
        self.title = title
        self.faculty_id = faculty_id
        self.exam_id = exam_id


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<Exam: {self.title}>'

    def __init__(self, title):
        self.title = title


class Enrollee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    
    specialty_id = db.Column(db.Integer, db.ForeignKey('specialty.id'))
    specialty = db.relationship('Specialty', backref=db.backref('enrollees', lazy='subquery', \
        cascade='all, delete-orphan'), foreign_keys=[specialty_id])

    exam_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam = db.relationship('Exam', backref=db.backref('enrollees',\
         lazy='subquery', cascade='all, delete-orphan'), foreign_keys=[exam_id])

    exam_scores = db.Column(db.Integer)

    def __init__(self, first_name, last_name, age, phone_number, specialty_id, \
        exam_id, exam_scores):
            self.first_name = first_name
            self.last_name = last_name
            self.age = age
            self.phone_number = phone_number
            self.specialty_id = specialty_id
            self.exam_id = exam_id
            self.exam_scores = exam_scores
        

    def __repr__(self):
        return f'<Enrollee: {self.last_name}, {self.first_name} {self.phone_number} \
            {self.specialty} exam: {self.exam} total score: {self.exam_scores}>'