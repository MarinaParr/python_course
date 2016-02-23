class fibonacci_sequence:
    def __init__(self, l):
        self.l = l
        self.i = 0
        self.a = 1
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == 0:
            self.i += 1
        if (self.i == 1 or self.i == 2) and self.i <= self.l:
            self.i += 1
            return 1
        if (self.i != 0 or self.i != 1 or self.i != 2) and self.i <= self.l:
            answer = self.a + self.b
            self.i += 1
            self.a = self.b
            self.b = answer
            return answer
        else:
            raise StopIteration("StopIteration!")
