from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

bookings_blueprint = Blueprint("bookings", __name__)


# INDEX
@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings=bookings)


# CREATE
@bookings_blueprint.route("/bookings", methods=["POST"])
def create_booking():
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    instructor_id = request.form["instructor_id"]
    location_id = request.form["location_id"]

    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    instructor = instructor_repository.select(instructor_id)
    location = location_repository.select(location_id)

    new_bookingg = Booking(member, activity, instructor, location)
    booking_repository.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    instructors = instructor_repository.select_all()
    locations = location_repository.select_all()

    return render_template('bookings/edit.html', booking=booking, members=members, activities=activities, instructors=instructors, locations=locations)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["POST"])
def update_booking(id):
    member_id = request.form["member_id"]
    activity_id = request.form["activity_id"]
    instructor_id = request.form["instructor_id"]
    location_id = request.form["location_id"]

    member = member_repository.select(member_id)
    activity = activity_repository.select(activity_id)
    instructor = instructor_repository.select(instructor_id)
    location = location_repository.select(location_id)

    booking = booking(member, activity, instructor, location, id)
    booking_repository.update(booking)
    return redirect("/bookings")


# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["POST"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")