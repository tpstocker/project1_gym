from db.run_sql import run_sql
from models.instructor import Instructor

def save(instructor):
    sql = "INSERT INTO instructors (first_name, second_name, contact_number) VALUES (%s, %s, %s) RETURNING id"
    values = [instructor.contact_number, instructor.second_name, instructor.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    instructor.id = id
    return instructor



def select_all():
    instructors = []

    sql = "SELECT * FROM instructors"
    results = run_sql(sql)

    for row in results:
        instructor = Instructor(row['first_name'], row['second_name'], row['contact_number'], row['id'])
        instructors.append(instructor)
    return instructors



def select(id):
    instructor = None
    sql = "SELECT * FROM instructors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        instructor = Instructor(result['first_name'], result['second_name'], result['contact_number'], result['id'])
    return instructor



def delete_all():
    sql = "DELETE FROM instructors"
    run_sql(sql)


def update(instructor):
    sql = "UPDATE instructors SET (first_name, second_name, contact_number) = (%s, %s, %s) WHERE id = %s"
    values = [instructor.contact_number, instructor.second_name, instructor.first_name, instructor.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM instructors WHERE id = %s"
    values = [id]
    run_sql(sql, values)