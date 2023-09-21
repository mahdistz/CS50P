class Jar:
    def __init__(self, capacity=12):
        self.number = 0
        if int(capacity) < 0:
            raise ValueError
        self._capacity = capacity

    def __str__(self):
        if self.number == 0:
            return ""
        return self.number * "🍪"

    def deposit(self, n):
        if self.number + n > self.capacity:
            raise ValueError
        self.number += n

    def withdraw(self, n):
        if self.number - n < 0:
            raise ValueError
        self.number -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if int(value) < 0:
            raise ValueError
        else:
            self._capacity = value

    @property
    def size(self):
        return self.number

    @size.setter
    def size(self, value):
        if int(value) < 0:
            raise ValueError
        else:
            self.number = value
