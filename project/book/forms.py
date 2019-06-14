#forms.py book

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, DateTimeField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

class AddForm(FlaskForm):

    name= StringField('Book Name:- ', validators=[DataRequired()])
    date = StringField('Issue Date:- ', validators=[DataRequired()])
    dateend = StringField('Submit Date:- ')
    emplo_id=IntegerField('Employee-Id', validators=[DataRequired()])
    submit =SubmitField('Add Book')
