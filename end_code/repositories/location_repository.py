from db.run_sql import run_sql
from models.location import Location


def save(location):
    sql = "INSERT INTO locations (accessible, capacity, description, name) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [location.accessible, location.capacity, location.description, location.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location


def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['accessible'], row['capacity'], row['description'], row['name'], row['id'])
        locations.append(location)
    return locations


def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['accessible'], result['capacity'], result['description'], result['name'], result['id'])
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)


def update(location):
    sql = "UPDATE locations SET (accessible, capacity, description, name) = (%s, %s, %s, %s) WHERE id = %s"
    values = [location.accessible, location.capacity, location.description, location.name, location.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)