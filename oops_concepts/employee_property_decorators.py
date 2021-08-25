# Property decorators : Getters, setters and deleters
#
# Need of getter method. suppose someone changes just
# first name of an employee. now if we get email it
# will give wrong output. here we can have a getter
# method which will actually go and get the updated
# values of first and last, and then make up the email
# and will return.
#
# Usage: when a method is needed to be treated as an
# attribute and that attribute is made from multiple
# actual attributes, then to set, get and delete these
# multipal attributes with methods, property decorators
# are used.
# Calling a decorator would be almost same for get, set
# and delete. but calls will be differentiated by the
# decorator header.
#
# e.g.
# to set : emp1.fullname = 'some name'
# to get : emp1.fullname
# to del : del emp1.fullname
#


class Employee:

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        # as email is comprised of multiple attributes better
        # to use getter, setter for maintaining attributes
        # and easy handling of email attribute.
        # self.email = first + '.' + last + '@company.com'


    @property
    def email(self):
        '''Getter method for email. allows to get email as
        an attribute.'''
        return self._first + '.' + self._last + '@company.com'

    @property
    def fullname(self):
        return '{} {}'.format(self._first, self._last)

    @fullname.setter
    def fullname(self, name):
        '''setter method which allows to change the name
        completely.'''
        first, last = name.split(' ')
        self._first = first
        self._last = last

    @fullname.deleter
    def fullname(self):
        print ('Deleting fullname!')
        self._first = None
        self._last = None

# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

# change name and check if emails also got changed
emp1._first = 'Hari'
print (emp1._first)
print (emp1._last)
# Would have yield wrong result if _email was an attribute
print (emp1.email)
print(emp1.fullname)

# change name and check if emails also got changed
emp1._first = 'Aum'
print (emp1._first)
print (emp1._last)
print (emp1.email)
# Getter called to get fullname
print(emp1.fullname)

# Setter called to set _first and _last
emp1.fullname = "Shivaji Raje"
print (emp1._first)
print (emp1._last)
print (emp1.email)

# Delete fullname and hence _first and _last
del emp1.fullname
print (emp1._first)
print (emp1._last)
print (emp1.fullname)
