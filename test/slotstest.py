class Student(object):
    score = 99
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

print (s.score)


class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')

        self._score = value


s = Student2()
s.score = 60
print (s.score)


