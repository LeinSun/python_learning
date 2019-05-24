array = [[1], [2, 3, 4], 5, 'asd']
for i in array:
    print i

right = set(['1', '2', '2', '4'])
left = set(['2', '2', '4', '5'])

print right.symmetric_difference(left)

# tpl = "i am %s" % "alex"
#
# tpl = "i am %s age %d" % ("alex", 18)
#
# tpl = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
#
# tpl = "percent %.2f" % 99.97623
#
# tpl = "i am %(pp).2f" % {"pp": 123.425556, }
#
# tpl = "i am %.2f %" % {"pp": 123.425556, }


# tpl = "i am {}, age {}, {}".format("seven", 18, 'alex')

# tpl = "i am {}, age {}, {}".format(*["seven", 18, 'alex'])
#
# tpl = "i am {0}, age {1}, really {0}".format("seven", 18)
#
# tpl = "i am {0}, age {1}, really {0}".format(*["seven", 18])
#
# tpl = "i am {name}, age {age}, really {name}".format(name="seven", age=18)
#
# tpl = "i am {name}, age {age}, really {name}".format(**{"name": "seven", "age": 18})
#
# tpl = "i am {0[0]}, age {0[1]}, really {0[2]}".format([1, 2, 3], [11, 22, 33])
#
# tpl = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 88888.1)
#
# tpl = "i am {:s}, age {:d}".format(*["seven", 18])
#
# tpl = "i am {name:s}, age {age:d}".format(name="seven", age=18)
#
# tpl = "i am {name:s}, age {age:d}".format(**{"name": "seven", "age": 18})
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
#
# tpl = "numbers: {:b},{:o},{:d},{:x},{:X}, {:%}".format(15, 15, 15, 15, 15, 15.87623, 2)
#
tpl = "numbers: {0:b},{0:o},{0:d},{0:x},{0:X}, {0:%}".format(15)
#
# tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

print tpl


def demo(name, age):
    print(name, type(name))
    print(age, type(age))


demo({'aa'}, 23)

