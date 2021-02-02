class Booking:

    def __init__(self, member, activity, instructor, location, id = None):
        self.member = member
        self.activity = activity
        self.instructor = instructor
        self.location = location       
        self.id = id