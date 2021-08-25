# Inheritance
#
# Inheritance allows us to inherit attributes
# and methods from the parent class.
# One can overwrite the old functionality of
# parent class and/or add completely new functi-
# onalities to the sub-class/child-class.
#
# E.g. we want to be more specific on employees
# devs or manager classes for example.
# Both classes would have all charachteristics
# of Employee class. so it can be resused.
# Inheritance helps to achieve that.
#
# use help(cls_name) to get method resolution
# order.
#

class Employee:

    # class variable
    nr_employees = 0
    raise_amount = 1.04

    # Constructor method as in cpp
    def __init__(self, first, last, pay):
        self._first = first # instance vars are unique to the instance
        self._last = last
        self._email = first + '.' + last + '@company.com'
        self._pay = pay

        Employee.nr_employees += 1

    def full_name(self):
        return '{} {}'.format(self._first, self._last)

    def apply_raise(self):
        # Allows to overwrite class var
        self._pay = (self._pay * self.raise_amount)

class Developer(Employee):
    pass

class Manager(Employee):
    pass

# Instantiate class
dev1 = Developer('rajkumar', 'patel', 5000)
dev2 = Developer('test', 'user', 6000)

print (dev1.full_name())
print (dev2.full_name())

# Very powerful to understand resolution order
# and to know what and from whom attributes
# and methods are being inherited.
print (help(Developer))
