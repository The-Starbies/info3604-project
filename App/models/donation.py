from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    donation_description = db.Column(db.String, nullable = False)
    donation_type = db.Column(db.String, nullable = False)
  
    def __init__(self, donation_description, donation_type):
        self.donation_description = donation_description
        self.donation_type = donation_type
        

    def toJSON(self):
        return{
            'id': self.id,
            'donation_description': self.donation_description,
            'donation_type': self.donation_type,
        }
