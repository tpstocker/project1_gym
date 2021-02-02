from flask import Blueprint, Flask, redirect, render_template, request

from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository

bookings_blueprint = Blueprint("bookings", __name__)


@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)


# NEW BOOKING - GET # 
@bookings_blueprint.route("/bookings/new", methods=['GET'])
def new_activity():
    members = member_repository.select_all()
    activities = activity_repository.select_all()
    instructors = instructor_repository.select_all()
    locations = location_repository.select_all()
    return render_template("bookings/new.html", members=members, activities=activities, instructors=instructors, locations=locations)


# CREATE
@bookings_blueprint.route("/bookings/new", methods=["POST"])
def create_booking():
    new_member = member_repository.select(request.form["member"])
    new_activity = activity_repository.select(request.form["activity"])
    new_instructor = instructor_repository.select(request.form["instructor"])
    new_location = location_repository.select(request.form["location"])

    new_booking = Booking(new_member, new_activity, new_instructor, new_location)
    booking_repository.save(new_booking)
    return redirect("/bookings")


# EDIT
@bookings_blueprint.route("/bookings/<id>/edit", methods=["GET"])
def edit_booking(id):
    booking = booking_repository.select(id)
    member = member_repository.select_all()
    activity = activity_repository.select_all()
    instructor = instructor_repository.select_all()
    location = location_repository.select_all()

    return render_template('bookings/edit.html', booking=booking, all_bookings = bookings, members=members, activities=activities, instructors=instructors, locations=locations)


# UPDATE
@bookings_blueprint.route("/bookings/<id>", methods=["GET"])
def update_booking(id):
    edit_member = member_repository.select(request.form["member"])
    edit_activity = activity_repository.select(request.form["activity"])
    edit_instructor = instructor_repository.select(request.form["instructor"])
    edit_location = location_repository.select(request.form["location"])

    edit_booking = Booking(edit_member, edit_activity, edit_instructor, edit_location)
    booking_repository.save(edit_booking)
    return redirect("/bookings")





# DELETE
@bookings_blueprint.route("/bookings/<id>/delete", methods=["GET"])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")