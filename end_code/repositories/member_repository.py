from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (active_status, membership_level, experience, email_address, contact_number, date_of_birth, second_name, first_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.active_status, member.membership_level, member.experience, member.email_address, member.contact_number, member.date_of_birth, member.second_name, member.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member 



def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row['active_status'], row['membership_level'], row['experience'], row['email_address'], row['contact_number'], row['date_of_birth'], row['second_name'], row['first_name'], row['id'])
        members.append(member)
    return members



def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Member(result['active_status'], result['membership_level'], result['experience'], result['email_address'], result['contact_number'], result['date_of_birth'], result['second_name'], result['first_name'], result['id'])
    return member



def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE members SET (active_status) VALUES (%s) RETURNING id"
    values = [member.active_status]
    run_sql(sql, values)