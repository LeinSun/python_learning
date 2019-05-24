class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    @classmethod
    def print_score_byclass(cls, student):
        print('%s: %s' % (student.__name, cls.__name__))


st = Student('Bart Simpson', 59)

print(st._Student__name)
st.print_score()
# st.print_score_byclass()
Student.print_score_byclass(st)


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
