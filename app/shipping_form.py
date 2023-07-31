from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from app.map.map import map

class ShippingForm(FlaskForm):
    cities=map.keys()
    sender=StringField('Sender',validators=[DataRequired()])
    recipient=StringField('Recipient',validators=[DataRequired()])
    origin=SelectField('Origin',choices=cities,validators=[DataRequired()])
    destination=SelectField('Destination',choices=cities,validators=[DataRequired()])
    express=BooleanField('Express?')
    submit=SubmitField('Submit')