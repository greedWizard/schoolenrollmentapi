from main.config import db


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<Faculty: {self.title}>'



class Specialty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)
    faculty_id = db.Column(db.Integer, db.ForeignKey('faculty.id'))
    faculty = db.relationship('Faculty', backref=db.backref('specialties', lazy=True))

    def __repr__(self):
        return f'<Speicality: {self.faculty} {self.title}>'


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f'<Exam: {self.title}>'


class Enrolee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    
    speciality_id = db.Column(db.Integer, db.ForeignKey('speciality.id'))
    speciality = db.relationship('Specialty', backref=db.backref('enrolees', lazy=True))

    exam1_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam1 = db.relationship('Exam', backref=db.backref('enrolees'))
    
    exam2_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam2 = db.relationship('Exam', backref=db.backref('enrolees'))
    
    exam3_id = db.Column(db.Integer, db.ForeignKey('exam.id'))
    exam3 = db.relationship('Exam', backref=db.backref('enrolees'))
    
    exam1_score = db.Column(db.Integer)
    exam2_score = db.Column(db.Integer)
    exam3_score = db.Column(db.Integer)

    total_scores = db.Column(db.Integer)


    def __repr__(self):
        return f'<Enrolee: {self.last_name}, {self.first_name} {self.phone_number} \
            {self.speciality} total score: {self.total_scores}>'