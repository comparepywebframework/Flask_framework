from app import db
from sqlalchemy.dialects.mysql import TIME


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    street_number = db.Column(db.Integer())
    open_at = db.Column(TIME())
    close_at = db.Column(TIME())


    def __repr__(self):
        return '<{} {}>'.format(__class__.__name__, self.name)