from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)


@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", all_members = members)

# NEW MEMBER - GET # 
@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
    return render_template("members/new.html", all_members = members)


# CREATE MEMBER - POST #
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    second_name = request.form['second_name']
    date_of_birth = request.form['date_of_birth']
    contact_number = request.form['contact_number']
    email_address = request.form['email_address']
    experience = request.form['experience']
    membership_level = request.form['membership_level']
    active_status = request.form['active_status']
    member = Member(membership_level, experience, email_address, contact_number, date_of_birth, second_name, first_name)
    member_repository.save(member)
    return redirect('/members')


# SHOW MEMBER - GET #
@members_blueprint.route("/members/<id>", methods=['GET'])
def show_member(id):
    member = member_repository.select(id)
    return render_template('members/show.html', member = member)


# EDIT MEMBER - GET #
@members_blueprint.route("/members/<id>/edit", methods=['GET'])
def edit_member(id):
    member = member_repository.select(id)
    return render_template('members/edit.html', member = member, all_members = members)

# UPDATE active_status - PUT #
@members_blueprint.route("/members/<id>", methods=["POST"])
def update_task(id):
    active_status = request.form['active_status']
    member = Member(active_status)
    member_repository.update(member)
    return redirect('/members')

