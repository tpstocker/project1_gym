class Location:

    def __init__(self, name, description, capacity, accessible, id = None):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.accessible = accessible
        self.id = id