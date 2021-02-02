class Location:

    def __init__(self, accessible, capacity, description, name, id = None):
        self.accessible = accessible
        self.capacity = capacity
        self.description = description
        self.name = name
        self.id = id