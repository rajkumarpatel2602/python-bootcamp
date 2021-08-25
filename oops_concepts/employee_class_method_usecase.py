# class method usecase as alternate constructor

# someone has come up with a requirement that,
# i have employee details but those details are
# separated by '-'. so before your code create
# an object for me, i am supposed to parse that
# string. can you help me with this?
#
# e.g.
# emp_str = john-miller-1000
# first, last, pay = emp_str.split('-')
# emp1 = Employee(first, last, pay)
#

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

    # Make the elegant use of class method
    # kind of a constructor method which is being
    # called before __init__ method.
    # class method as an alternative constructor.
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


# Instantiate class
emp1 = Employee.from_string('rajkumar-patel-5000')
emp2 = Employee.from_string('test-user-6000')

print (Employee.nr_employees)
print (emp1.full_name())
print (emp2.full_name())
