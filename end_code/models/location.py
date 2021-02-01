class Location:

    def __init__(self, accessible, capacity, description, name, id = None):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.accessible = accessible
        self.id = id