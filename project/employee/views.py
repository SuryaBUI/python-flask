#VIEWS.pY

from flask import Blueprint, render_template,redirect,url_for
from project import db
from project.models import Employee,Book
from project.employee.forms import AddForm,DelForm
from flask_login import  login_required
employee_blueprints= Blueprint('employee', __name__, template_folder='templates/employee')


@employee_blueprints.route('/add', methods=["GET","POST"])
@login_required
def add():

    form= AddForm()

    if form.validate_on_submit():

        name= form.name.data
        department= form.department.data
        username= form.username.data
        password= form.password.data
        new_emp= Employee(name, department, username, password)

        #new_dep= Employee(department)
        db.session.add(new_emp)
        #db.session.add(new_dep)
        db.session.commit()

        return redirect(url_for('employee.list'))

    return render_template('add.html', form=form)


@employee_blueprints.route('/list')
@login_required
def list():

    employees = Employee.query.all()
    book = Book.query.all()
    return render_template('list.html', employees=employees, book=book)


@employee_blueprints.route('/delete', methods=["GET","POST"])
@login_required
def delete():

    form = DelForm()

    if form.validate_on_submit():

        id= form.id.data
        emp = Employee.query.get(id)
        db.session.delete(emp)
        db.session.commit()

        return redirect(url_for('employee.list'))

    return render_template('delete.html', form=form)
