from db.run_sql import run_sql
from models.member import Member
from models.instructor import Instructor
from models.activity import Activity
from models.location import Location
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository
import repositories.booking_repository as booking_repository


def save(activity):
    sql = "INSERT INTO activities (experience_level, duration, description, name) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [activity.experience_level, activity.duration, activity.description, activity.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    activity.id = id
    return activity


def select_all():
    activities = []

    sql = "SELECT * FROM activities"
    results = run_sql(sql)

    for row in results:
        activity = Activity(row['experience_level'], row['duration'], row['description'], row['name'], row['id'])
        activities.append(activity)
    return activities


def select(id):
    activity = None
    sql = "SELECT * FROM activities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        activity = Activity(result['experience_level'], result['duration'], result['description'], result['name'], result['id'])
    return activity


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)


def update(activity):
    sql = "UPDATE activities SET (experience_level, duration, description, name) = (%s, %s, %s, %s) WHERE id = %s"
    values = [activity.experience_level, activity.duration, activity.description, activity.name, activity.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM activities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def select_members_with_booking(id):
    members_with_booking = []
    sql = "SELECT members.* FROM members INNER JOIN bookings ON bookings.member_id = members.id WHERE bookings.activity_id = %s"
    values = [id]
    results = run_sql(sql, values)
    for result in results:
        member = member(result["first_name"]) #DO WE NEED MORE HERE#
        members_with_booking.append(member)
    return members_with_booking


    
 