import os
from app import create_app

def init_db():
    app, db = create_app()
    
    with app.app_context():
        # Import models here after app context is established
        from app.models import School, Subject, SchoolSubject, CountryStats
        
        # Create all tables
        db.create_all()
        
        # Check if data already exists
        if CountryStats.query.first() is not None:
            print("Database already initialized with data")
            return
        
        # Add sample data based on the original project
        countries_data = [
            {'country_name': '美国', 'school_count': 79},
            {'country_name': '中国', 'school_count': 15},
            {'country_name': '加拿大', 'school_count': 1},
            {'country_name': '英国', 'school_count': 73},
            {'country_name': '印度', 'school_count': 1},
            {'country_name': '日本', 'school_count': 10},
            {'country_name': '韩国', 'school_count': 2},
            {'country_name': '阿联酋', 'school_count': 1},
            {'country_name': '新加坡', 'school_count': 2},
            {'country_name': '瑞士', 'school_count': 1},
        ]
        
        for country_data in countries_data:
            country_stat = CountryStats(
                country_name=country_data['country_name'],
                school_count=country_data['school_count']
            )
            db.session.add(country_stat)
        
        # Add subjects
        subjects_data = [
            'Mathematics', 'Science', 'Literature', 'History', 
            'Art', 'Music', 'Physical Education', 'Computer Science'
        ]
        
        for subject_name in subjects_data:
            subject = Subject(name=subject_name)
            db.session.add(subject)
        
        # Add schools
        schools_data = [
            {'name': 'International School A', 'country': '美国', 'city': 'New York', 'founded_year': 1985, 'tuition_cost': 35000, 'is_public': False},
            {'name': 'Global Academy', 'country': '中国', 'city': 'Beijing', 'founded_year': 1998, 'tuition_cost': 28000, 'is_public': False},
            {'name': 'Heritage School', 'country': '英国', 'city': 'London', 'founded_year': 1975, 'tuition_cost': 32000, 'is_public': False},
            {'name': 'Future Leaders School', 'country': '日本', 'city': 'Tokyo', 'founded_year': 2001, 'tuition_cost': 29000, 'is_public': False},
        ]
        
        for school_data in schools_data:
            school = School(**school_data)
            db.session.add(school)
        
        # Commit all data
        db.session.commit()
        print("Database initialized with sample data successfully!")

if __name__ == "__main__":
    init_db()