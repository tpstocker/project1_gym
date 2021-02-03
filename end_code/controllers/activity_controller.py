from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)


@activities_blueprint.route("/activities")
def activities():
    activities = activity_repository.select_all()
    return render_template("activities/index.html", all_activities = activities)


# NEW ACTIVITY - GET # 
@activities_blueprint.route("/activities/new", methods=['GET'])
def new_activity():
    return render_template("activities/new.html", all_activities = activities)


# CREATE ACTIVITY - POST #
@activities_blueprint.route("/activities", methods=['POST'])
def create_activity():
    name = request.form['name']
    description = request.form['description']
    duration = request.form['duration']
    experience_level = request.form['experience_level']
    activity = Activity(experience_level, duration, description, name)
    activity_repository.save(activity)
    return redirect('/activities')


# SHOW ACTIVITIES - GET #
@activities_blueprint.route("/activities/<id>", methods=['GET'])
def show_activity(id):
    members_with_booking = activity_repository.select_members_with_booking(id)
    activity = activity_repository.select(id)
    return render_template('activities/show.html', members_with_booking = members_with_booking, activity = activity)


# EDIT ACTIVITY - GET #
@activities_blueprint.route("/activities/<id>/edit", methods=['GET'])
def edit_activity(id):
    activity = activity_repository.select(id)
    return render_template('activities/edit.html', activity = activity, all_activities = activities)

# UPDATE ACTIVITY - PUT #
@activities_blueprint.route("/activities/<id>", methods=["POST"])
def update_activity(id):
    experience_level = request.form['experience_level']
    duration = request.form['duration']
    description = request.form['description']
    name = request.form['name']

    activity = Activity(experience_level, duration, description, name, id)
    activity_repository.update(activity)
    return redirect('/activities')


# DELETE ACTIVITY #

@activities_blueprint.route("/activities/<id>/delete", methods=['GET'])
def delete_activity(id):
    activity_repository.delete(id)
    return redirect('/activities')



