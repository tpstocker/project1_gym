from db.run_sql import run_sql
from models.booking import Booking
import repositories.location_repository as location_repository
import repositories.member_repository as member_repository
import repositories.activity_repository as activity_repository
import repositories.instructor_repository as instructor_repository


def save(booking):
    sql = "INSERT INTO bookings (member_id, activity_id, instructor_id, location_id) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [booking.member_id.id, booking.activity_id.id, booking.instructor_id.id, booking.location_id.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def delete_all():
    sql = "DELETE FROM bookings"
    run_sql(sql)