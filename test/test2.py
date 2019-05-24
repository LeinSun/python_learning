
def aa(func):
    def ff(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return ff


@aa
def now():
    print('2015-3-25')


now()

#
#
# now2 = aa(now)
#
# now2()
#
# def f(x):
#     return x * x
#
#
# r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(list(r))
#
# print(sorted(['aaa', 'b', 'ccddsaa', 'dd', 'fff'], key=lambda x: len(x)))
#
# print(max(['aaa', 'b', 'ccddsaa', 'dd', 'fff'], key=lambda x: len(x)))


# def odd():
#     print('step 1')
#     first = yield 1
#     print('step 2', first)
#     yield 3
#     print('step 3')
#     yield 5
#
#
# g = odd()
# next(g)
# g.send('hello')

def bb(func):
    print('bb')
    func()
    return func

@bb
def ff():
    print('ff')


# bb(ff)()

ff()


