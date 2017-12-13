spam = [1, 3, 2, 5, 4, 7, 6, 9, 8, 10]
print(spam[int(int('3' * 2) // 11)])
# ------------------------------------------------------

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
# ------------------------------------------------------

eggs = {'name': 'Zophie', 'species': 'cats', 'age': '8'}
ham = {'species': 'cats', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)
# ------------------------------------------------------

class A(object):
    x = 1

class B(A):
    pass

class C(A):
    pass

print(A.x, B.x, C.x)
B.x = 2
print(A.x, B.x, C.x)
A.x = 3
print(A.x, B.x, C.x)
# ------------------------------------------------------

def func1(bar=[]):
    bar.append('xyz')
    return bar

print(func1())


def func2(bar=[]):
    bar.extend('xyz')
    return bar

print(func2())
# ------------------------------------------------------

a = True
b = False
c = False

if a or b and c:
    print('Python')
else:
    print('mca101')
# ------------------------------------------------------

spam = 'SpamSpamEggsampSampS'
print(spam.strip('ampS'))
print(spam.strip('Spam'))
# ------------------------------------------------------

class Vehicle:
    pass

class Truck(Vehicle):
    pass

print(isinstance(Vehicle(), Vehicle))
print(type(Vehicle()) == Vehicle)

print(isinstance(Truck(), Vehicle))
print(type(Truck()) == Vehicle)
# ------------------------------------------------------














