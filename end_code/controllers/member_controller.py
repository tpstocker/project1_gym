from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repository as member_repository

members_blueprint = Blueprint("members", __name__)


# @members_blueprint.route("/members")
# def members():
#     members = member_repository.select_all()
#     return render_template("members/index.html", members = members)

# # GET '/members/new'
# @members_blueprint.route("/members/new")
# def members():
#     members = member_repository.select_all()
#     return render_template("members/index.html", members = members)


# Show, Select Member
@members_blueprint.route("/members")
def show(id):
    member = member_repository.select(id) #removed location 
    return render_template("members/show.html", member=member) #removed location = location after member = member

# NEW GET 'members/new'
@members_blueprint.route("/members/new", methods=['GET'])
def new_member():
    members = member_repository.select_all()
    return render_template("members/new.html", all_members = members)

    Hello 