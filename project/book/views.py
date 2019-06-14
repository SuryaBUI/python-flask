#views.py book


from flask import Blueprint, render_template,redirect,url_for
from project import db
from project.models import Book
from project.book.forms import AddForm
from flask_login import  login_required
book_blueprints= Blueprint('book', __name__, template_folder='templates/book')

@book_blueprints.route('/add', methods=["GET","POST"])
@login_required
def add():
    form= AddForm()

    if form.validate_on_submit():
        name= form.name.data
        date= form.date.data
        dateend=form.dateend.data
        emplo_id= form.emplo_id.data

        book_issue= Book(name, date, dateend, emplo_id)

        #new_dep= Employee(department)
        db.session.add(book_issue)
        #db.session.add(new_dep)
        db.session.commit()
        return redirect(url_for('employee.list'))

    return render_template('book_issue.html', form=form)

@book_blueprints.route('/list')
@login_required
def list():

    book = Book.query.all()
    print(book)
    return render_template('list.html', book=book)
