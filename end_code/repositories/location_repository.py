from db.run_sql import run_sql
from models.location import Location


def save(location):
    sql = "INSERT INTO locations (accessible, capacity, description, name) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [location.name, location.description, location.capacity, location.accessible]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id
    return location


def select_all():
    locations = []

    sql = "SELECT * FROM locations"
    results = run_sql(sql)

    for row in results:
        location = Location(row['name'], row['description'], row['capacity'], row['accessible'], row['id'])
        locations.append(location)
    return locations


def select(id):
    location = None
    sql = "SELECT * FROM locations WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        location = Location(result['name'], result['description'], result['capacity'], result['accessible'], result['id'])
    return location


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)


def update(location):
    sql = "UPDATE locations SET (accessible, capacity, description, name) = (%s, %s, %s, %s) WHERE id = %s"
    values = [location.name, location.description, location.capacity, location.accessible, location.id]
    run_sql(sql, values)


def delete(id):
    sql = "DELETE FROM locations WHERE id = %s"
    values = [id]
    run_sql(sql, values)