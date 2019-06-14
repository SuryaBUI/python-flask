#forms.py in hr

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from wtforms import ValidationError

class AddForm(FlaskForm):

    name= StringField('Name HR', validators=[DataRequired()])
    emplo_id=IntegerField('Id of Employee', validators=[DataRequired()])
    submit= SubmitField('Add HR')
