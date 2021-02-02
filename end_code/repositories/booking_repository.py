from db.run_sql import run_sql
from models.booking import Booking
from models.member import Member
from models.activity import Activity
from models.instructor import Instructor
from models.location import Location

import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository
import repositories.location_repository as location_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id, instructor_id, location_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [booking.member.id, booking.activity.id, booking.instructor.id, booking.location.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    booking.id = id


def select_all():
    bookings = []
    sql = "SELECT * FROM bookings"
    results = run_sql(sql)
    for result in results:
        member = member_repository.select(result["member_id"])
        activity = activity_repository.select(result["activity_id"])
        instructor = instructor_repository.select(result["instructor_id"])
        location = location_repository.select(result["location_id"])

        booking = Booking(member, activity, instructor, location, result["id"])
        bookings.append(booking)
    return bookings


def select(id):
    sql = "SELECT * FROM bookings WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    member = member_repository.select(result["member_id"])
    activity = activity_repository.select(result["activity_id"])
    instructor = instructor_repository.select(result["instructor_id"])
    location = location_repository.select(result["location_id"])

    booking = Booking(member, activity, instructor, location, result["id"])
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(booking):
    sql = "UPDATE bookings SET (member_id, activity_id, instructor_id, location_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [booking.member.id, booking.activity.id, booking.instructor.id, booking.location.id]
    run_sql(sql, values)