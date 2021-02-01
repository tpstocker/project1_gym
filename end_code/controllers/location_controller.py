from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.location import Location
import repositories.location_repository as location_repository

locations_blueprint = Blueprint("locations", __name__)


@locations_blueprint.route("/locations")
def locations():
    locations = location_repository.select_all()
    return render_template("locations/index.html", all_locations = locations)


# NEW LOCATION - GET # 
@locations_blueprint.route("/locations/new", methods=['GET'])
def new_location():
    return render_template("locations/new.html", all_locations = locations)


# CREATE LOCATION - POST #
@locations_blueprint.route("/locations", methods=['POST'])
def create_location():
    name = request.form['name']
    description = request.form['description']
    capacity = request.form['capacity']
    accessible = request.form['accessible']

    location = Location(accessible, capacity, description, name)
    location_repository.save(location)
    return redirect('/locations')


# SHOW LOCATION - GET #
@locations_blueprint.route("/locations/<id>", methods=['GET'])
def show_location(id):
    location = location_repository.select(id)
    return render_template('locations/show.html', location = location)


# EDIT LOCATION - GET #
@locations_blueprint.route("/locations/<id>/edit", methods=['GET'])
def edit_location(id):
    location = location_repository.select(id)
    return render_template('locations/edit.html', location = location, all_locations = locations)


# UPDATE LOCATION - PUT #
@locations_blueprint.route("/locations/<id>", methods=["POST"])
def update_location(id):
    name = request.form['name']
    description = request.form['description']
    capacity = request.form['capacity']
    accessible = request.form['accessible']
    
    location = Location(accessible, capacity, description, name, id)
    location_repository.update(location)
    return redirect('/locations')


# DELETE #

@locations_blueprint.route("/locations/<id>/delete", methods=['GET'])
def delete_location(id):
    location_repository.delete(id)
    return redirect('/locations')