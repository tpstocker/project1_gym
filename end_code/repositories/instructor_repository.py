from db.run_sql import run_sql
from models.instructor import Instructor
import repositories.activity_repository as activity_repository


def save(instructor):
    sql = "INSERT INTO instructors (contact_number, preferred_activity, second_name, first_name) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [instructor.contact_number, instructor.preferred_activity.id, instructor.second_name, instructor.first_name]
    results = run_sql( sql, values )
    instructor.id = results[0]['id']
    return instructor


def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)