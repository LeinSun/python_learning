import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)

json_str = json.dumps(s, default=lambda obj: obj.__dict__)
print(json_str)

print(json.loads(json_str, object_hook=lambda d: Student(d['name'], d['age'], d['score'])))

