from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.instructor import Instructor
import repositories.instructor_repository as instructor_repository

instructors_blueprint = Blueprint("instructors", __name__)


@instructors_blueprint.route("/instructors")
def instructors():
    instructors = instructor_repository.select_all()
    return render_template("instructors/index.html", all_instructors = instructors)

# NEW instructor - GET # 
@instructors_blueprint.route("/instructors/new", methods=['GET'])
def new_instructor():
    return render_template("instructors/new.html", all_instructors = instructors)


# CREATE instructor - POST #
@instructors_blueprint.route("/instructors", methods=['POST'])
def create_instructor():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    contact_number = request.form['contact_number']

    instructor = Instructor(contact_number, second_name, first_name)
    instructor_repository.save(instructor)
    return redirect('/instructors')


# SHOW instructor - GET #
@instructors_blueprint.route("/instructors/<id>", methods=['GET'])
def show_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template('instructors/show.html', instructor = instructor)


# EDIT instructor - GET #
@instructors_blueprint.route("/instructors/<id>/edit", methods=['GET'])
def edit_instructor(id):
    instructor = instructor_repository.select(id)
    return render_template('instructors/edit.html', instructor = instructor, all_instructors = instructors)

# UPDATE - PUT # ####look at this if theres a problem###
@instructors_blueprint.route("/instructors/<id>", methods=["POST"])
def update_instructor(id):
    contact_number = request.form['contact_number']
    second_name = request.form['second_name']
    first_name = request.form['first_name']
    
    instructor = Instructor(contact_number, second_name, first_name, id)
    instructor_repository.update(instructor)
    return redirect('/instructors')


# DELETE #

@instructors_blueprint.route("/instructors/<id>/delete", methods=['GET'])
def delete_instructor(id):
    instructor_repository.delete(id)
    return redirect('/instructors')



