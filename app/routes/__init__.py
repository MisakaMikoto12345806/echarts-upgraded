from flask import Blueprint
from app.models import School, Subject, SchoolSubject, CountryStats

main = Blueprint('main', __name__)

@main.route('/')
def index():
    from flask import render_template
    return render_template('index.html')

# Import routes after models to avoid circular imports
from app.routes.api import *