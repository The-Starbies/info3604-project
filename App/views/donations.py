from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db

donation_views = Blueprint('donation_views', __name__, template_folder='../templates')

@donation_views.route('/donations', methods=['GET'])
def get_donation_page():
    return render_template('donations.html')

@donation_views.route('/thankyou', methods=['GET'])
def get_thankyou_page():
    return render_template('thankyou.html')