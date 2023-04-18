from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import create_shelter

shelter_views = Blueprint('shelter_views', __name__, template_folder='../templates')

@shelter_views.route('/shelters', methods=['GET'])
def get_shelter_page():
    return render_template('shelters.html')