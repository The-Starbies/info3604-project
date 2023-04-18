from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

faq_views = Blueprint('faq_views', __name__, template_folder='../templates')

@faq_views.route('/faq', methods=['GET'])
def get_faq_page():
    return render_template('faq.html')