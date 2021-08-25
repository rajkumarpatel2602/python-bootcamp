# Operator overloading using dunder/magic methods
# '__' is referred by dunder. and methods for OP OV
# will use this '__' before and after method name.
# most common known, magic/dunder method is
# __init__()
#
# some other commons special methods are __str__()
# __repr__()
#
# for our purpose, dunder methods would have class
# instances as operands.
#
# Examples : datatime module
#

class Employee:

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

    def __repr__(self):
        ''' Rule of thumb is to return a string which is the
        actual command using which object was created. '''
        return "Employee('{}', '{}', '{}')".format(self._first, self._last, self._pay)

    def my_print_fun(self):
        return self._last + '_WOW!'

    # simply other function may also be loaded in __str__
    __str__ = my_print_fun

    #def __str__(self):
    #    '''User more readable and useful string representation.'''
    #    return self.full_name() + '-' + self._email

    def __add__(self, other):
        '''defines behaviour on additions of two employee objests'''
        return self._pay + other._pay

    def __len__(self):
        return len(self._first)

# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

# __add__() examples

print(int.__add__(1, 2))
print(1 + 2)
print(str.__add__('Hi_', 'Hello'))
print('Hi_' + 'Hello')

#print(emp1 + emp2)
print('Total pay of emp1 and emp2 is : {}'.format(emp1 + emp2))

# __len__() examples

print(str.__len__('length'))
print(len('length'))

num_list = [1, 2, 3]
print(list.__len__(num_list))
print(len(num_list))

print("Employee's name is : {}".format(emp1._first))
print("Employee's name lenght is : {}".format(len(emp1)))

# Test __str__()
print(emp1.__str__())
