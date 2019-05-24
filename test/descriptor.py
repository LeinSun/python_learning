# coding=UTF-8


# 描述符Str
class Strr(object):

    def __get__(self, instance, owner):
        print('Str调用')
        print('instance: ', instance)
        print('owner: ', owner)

    def __set__(self, instance, value):
        print('Str设置...')
        print('instance: ', instance)
        print('value: ', value)

    def __delete__(self, instance):
        print('Str删除...')
        print('instance: ', instance)


class People(object):

    name = Strr()

    def __init__(self, name, age):  # name被Str类代理,age被Int类代理,
        self.name = name
        self.age = age


# 何地？：定义成另外一个类的类属性
# 何时？：且看下列演示

p1 = People('alex', 12)

print('---------------')
print(p1.__dict__)

# 描述符Str的使用
p1.name

p1.name = 'egon'
del p1.name


# 我们来瞅瞅到底发生了什么
print(p1.__dict__)
print(People.__dict__)

