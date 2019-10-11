class Graph:
	def __init__(self):
		self.rooms = {}

	def add_room(self, room):
		if room not in self.rooms:
			self.rooms[room] = {'n': '?', 's': '?', 'w': '?', 'e':'?'}
		else:
			raise KeyError('Room already exists')

	def link_room(self, room1, room2):
		if room1 not in self.rooms:
			self.add_rooms(room1)
		if room2 not in self.rooms:
			self.add_rooms(room2)


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

