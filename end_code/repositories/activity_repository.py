from db.run_sql import run_sql
from models.activity import Activity


def save(activity):
    sql = "INSERT INTO activities (experience_level, duration, description, name) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [activity.experience_level, activity.duration, activity.description, activity.name]
    results = run_sql( sql, values )
    activity.id = results[0]['id']
    return activity


def delete_all():
    sql = "DELETE FROM activities"
    run_sql(sql)