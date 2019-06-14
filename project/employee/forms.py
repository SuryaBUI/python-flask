#forms.py for employees

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

class DelForm(FlaskForm):

    id = IntegerField('Id of emp to remove', validators=[DataRequired()])
    submit =SubmitField('Delete')


class AddForm(FlaskForm):

    name= StringField('Name:- ', validators=[DataRequired()])
    department= StringField('Department:- ', validators=[DataRequired()])
    username= StringField('User-Name:- ')
    password= PasswordField('Password:- ')
    submit =SubmitField('Add Employee')
