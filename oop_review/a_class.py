class A(object):
    a = "A"
    def __init__(self):
        self.b = "B"

    class Meta:
        c = "C"

    def a_print(self):
        print('a_print')

    @classmethod
    def class_print(cls):
        print(cls.__name__)
        print('class_print')

    @staticmethod
    def static_print():
        print('static_print')

    @property
    def data(self):
        print('data')

    def __str__(self):
        return '__str__'

print(A.a)
print(A().b)
print(A().Meta.c)
print('----------------')
A.a_print(A())
A.class_print()
A.static_print()
print('----------------')
A().a_print()
A().class_print()
A().static_print()
A().data
print(A())
print('----------------')

# class B(A):
#     pass

class B(object):
    A=A()

B().A.a_print()
