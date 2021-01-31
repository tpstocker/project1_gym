class Booking:

    def __init__(self, member_id, activity_id, instructor_id, location_id, id = None):
        self.member_id = member_id
        self.activity_id = activity_id
        self.instructor_id = instructor_id
        self.location_id = location_id
        self.id = id