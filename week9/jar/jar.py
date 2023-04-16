class Jar:
    #init defalt capacity is 12
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.size = 0

    #when printing the function you get whats under __str__
    def __str__(self):
        return "🍪" * self.size

    #making depositing(adding cookie to the jar)
    def deposit(self, n):
        self.size += n

    #making withdraw(taking cookie away from the jar)
    def withdraw(self, n):
        self.size -= n

    #getting the max capacity
    @property
    def capacity(self):
        return self._capacity

    #setting the max capacity
    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity

    #getting cookie total
    @property
    def size(self):
        return self._size

    #setting cookie
    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("There is not enough cookies.")
        if size > self.capacity:
            raise ValueError("There is not enough space.")
        self._size = size
        