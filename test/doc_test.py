# coding=utf-8

class Foo(object):
    '我是描述信息'
    pass

class Bar(Foo):
    pass

print(Foo.__doc__)
print(Bar.__doc__) #该属性无法继承给子类
