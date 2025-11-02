from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

def init_models(db):
    """Initialize models with the db instance"""
    
    class School(db.Model):
        """Represents a school in the database"""
        __tablename__ = 'schools'
        
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(255), nullable=False)
        country = db.Column(db.String(100), nullable=False)
        city = db.Column(db.String(100))
        founded_year = db.Column(db.Integer)
        tuition_cost = db.Column(db.Float)
        is_public = db.Column(db.Boolean, default=True)
        
        def to_dict(self):
            return {
                'id': self.id,
                'name': self.name,
                'country': self.country,
                'city': self.city,
                'founded_year': self.founded_year,
                'tuition_cost': self.tuition_cost,
                'is_public': self.is_public
            }
    
    class Subject(db.Model):
        """Represents a subject offered by schools"""
        __tablename__ = 'subjects'
        
        id = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.String(100), nullable=False, unique=True)
        
        def to_dict(self):
            return {
                'id': self.id,
                'name': self.name
            }
    
    class SchoolSubject(db.Model):
        """Association table between schools and subjects"""
        __tablename__ = 'school_subjects'
        
        id = db.Column(db.Integer, primary_key=True)
        school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
        subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)
        
        school = db.relationship('School', backref='school_subjects')
        subject = db.relationship('Subject', backref='school_subjects')
        
        def to_dict(self):
            return {
                'id': self.id,
                'school_id': self.school_id,
                'subject_id': self.subject_id
            }
    
    class CountryStats(db.Model):
        """Stores statistics about schools by country"""
        __tablename__ = 'country_stats'
        
        id = db.Column(db.Integer, primary_key=True)
        country_name = db.Column(db.String(100), nullable=False)
        school_count = db.Column(db.Integer, nullable=False)
        year = db.Column(db.Integer, default=datetime.utcnow().year)
        
        def to_dict(self):
            return {
                'id': self.id,
                'country_name': self.country_name,
                'school_count': self.school_count,
                'year': self.year
            }
    
    # Add models to globals so they can be accessed
    globals()['School'] = School
    globals()['Subject'] = Subject
    globals()['SchoolSubject'] = SchoolSubject
    globals()['CountryStats'] = CountryStats