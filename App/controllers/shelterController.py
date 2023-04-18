from App.models import Shelter
from App.database import db


def create_shelter(username,password):
    new_shelter = Shelter(username = username, password = password)
    db.session.add(new_shelter)
    db.session.commit()
    return new_shelter

