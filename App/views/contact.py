from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db


contact_views = Blueprint('contact_views', __name__, template_folder='../templates')

@contact_views.route('/', methods=['GET'])
def contact_page():
    return render_template('contact.html')