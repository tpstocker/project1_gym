from db.run_sql import run_sql
from models.member import Member

def save(member):
    sql = "INSERT INTO members (membership_level, experience, email_address, contact_number, date_of_birth, second_name, first_name) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id"
    values = [member.membership_level, member.experience, member.email_address, member.contact_number, member.date_of_birth, member.second_name, member.first_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id


def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)


def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        member = Member(row['membership_level'], row['experience'], row['email_address'], row['contact_number'], row['date_of_birth'], row['second_name'], row['first_name'], row['id'])
        members.append(member)
    return members