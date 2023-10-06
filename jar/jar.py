class Jar:
    def __init__(self, capacity=12):
        if capacity > 12 or capacity <0:
            raise ValueError("no")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * "🍪"


    def deposit(self, n):
        if int(n)< 0 :
            raise ValueError("cant be negative")
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n


    def withdraw(self, n):
        if n > self.capacity:
            raise ValueError("cant be negative")
        if self.size - n < 0 :
            raise ValueError("cant be negative")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size



