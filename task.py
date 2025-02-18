import uuid

#class to represent a single task

class Task:
    def __init__(self, name, description):
        self.id = str(uuid.uuid4())
        self.name = name
        self.status = 'Pending'
        self.description = description


