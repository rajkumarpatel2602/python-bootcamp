# Actual class

class Employee:

    # Class variable which is company-wide same
    raise_amount = 1.04 # 4%
    nr_employees = 0

    # Constructor method as in cpp
    def __init__(self, first, last, pay):
        self._first = first # instance vars are unique to the instance
        self._last = last
        self._email = first + '.' + last + '@company.com'
        self._pay = pay

        # Increament count for each object instantiation
        # Same for all the objects
        Employee.nr_employees += 1

    def full_name(self):
        return '{} {}'.format(self._first, self._last)

    def apply_raise(self):
        self._pay = (self._pay * self.raise_amount) # Allows to overwrite class var
        #self._pay = (self._pay * Employee.raise_amount)

    # To update the class attributes class methods are used
    # to differentiate from instance method decorator is used
    # rather than 'self', it uses 'cls' as the first argument.
    @classmethod
    def set_raise_amount(cls, amount):
       cls.raise_amount = amount


# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

# Employee.raise_amount = 1.05 OR use class method
Employee.set_raise_amount(1.05)

print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

