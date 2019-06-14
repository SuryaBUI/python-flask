#views.py hr

from flask import Blueprint, render_template,redirect,url_for
from project import db
from project.models import HumanResources
from project.hr.forms import AddForm
from flask_login import  login_required

hr_blueprints= Blueprint('hr', __name__, template_folder='templates/hr')




@hr_blueprints.route('/add', methods= ['GET','POST'])
@login_required
def add():

    form= AddForm()

    if form.validate_on_submit():
        name= form.name.data
        emplo_id= form.emplo_id.data

        new_hr=HumanResources(name,emplo_id)
        db.session.add(new_hr)
        db.session.commit()

        return redirect(url_for('employee.list'))

    return render_template('add_hr.html', form=form)
