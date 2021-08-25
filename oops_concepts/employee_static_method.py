# static method usecase

#
# instance method passes object automatically
# and work upon that.
#
# class method passes class automatically
# and work upon that.
#
# static methods are like a normal function
# rather than a typical methods.
# but they are having some logical connection
# with class so positioned inside a class.
#

#
# Usage of static method.
# if one doesn't use 'self' or 'cls' inside a function
# then it's better to make it a static method.
#

import datetime

class Employee:

    # Class variable which is company-wide same
    nr_employees = 0

    # Constructor method as in cpp
    def __init__(self, first, last, pay):
        self._first = first # instance vars are unique to the instance
        self._last = last
        self._email = first + '.' + last + '@company.com'
        self._pay = pay

        # Increament count for each object instantiation
        Employee.nr_employees += 1

    def full_name(self):
        return '{} {}'.format(self._first, self._last)

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        # Check whether it's a weeked?
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# Instantiate class
emp1 = Employee.from_string('rajkumar-patel-5000')
emp2 = Employee.from_string('test-user-6000')

my_date = datetime.date(2021, 8, 28)

print ('was employee on work? {}'.format(Employee.is_workday(my_date)))
