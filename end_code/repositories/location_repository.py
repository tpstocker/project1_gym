from db.run_sql import run_sql
from models.location import Location

def save(location):
    sql = "INSERT INTO locations (name, description, capacity, accessible) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [location.name, location.description, location.capacity, location.accessible]
    results = run_sql(sql, values)
    id = results[0]['id']
    location.id = id


def delete_all():
    sql = "DELETE FROM locations"
    run_sql(sql)