# Operator overloading using dunder/magic methods
# '__' is referred by dunder. and methods for OP OV
# will use this '__' before and after method name.
# most common known, magic/dunder method is
# __init__()
#
# some other commons special methods are __str__()
# __repr__()
#


class Employee:

    # Constructor method as in cpp
    def __init__(self, first, last, pay):
        self._first = first # instance vars are unique to the instance
        self._last = last
        self._email = first + '.' + last + '@company.com'
        self._pay = pay

    def emp_attribute_str(self):
        return 'first name:{} last name:{} pay:{}'.format( \
                self._first, self._last, self._pay)

    def full_name(self):
        return '{} {}'.format(self._first, self._last)

    # special methods for Employee class.
    # if someone do print(emp_obj), then code will check first
    # __str__() implementation. if not found then __repr__() will
    # get called. at least have __repr__().
    def __repr__(self):
        ''' Rule of thumb is to return a string which is the
        actual command using which object was created. '''
        return "Employee('{}', '{}', '{}')".format(self._first, self._last, self._pay)

    def __str__(self):
        '''User more readable and useful string representation.'''
        return self.full_name() + '-' + self._email

# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

print(emp1.emp_attribute_str())
print(emp1.full_name())
print(emp2.emp_attribute_str())
print(emp2.full_name())

print(emp1.__repr__())
print(repr(emp1))
print(repr(emp2))

print(emp1.__str__())
print(str(emp1))
print(str(emp2))

print(emp1) # __str__() will be called
print(emp2) # __str__() will be called

# dunder add method

print(1 + 2)
print(int.__add__(1, 2))


print('hello_' + 'github')
print(str.__add__('hello_', 'github'))
