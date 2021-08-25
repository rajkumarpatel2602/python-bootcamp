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
# example : class HTTPException(Exception)
#



class Employee:

    # class variable
    nr_employees = 0
    raise_amount = 1.04


    def __init__(self, first, last, pay):
        """Constructor method as in cpp"""

        self._first = first # instance vars are unique to the instance
        self._last = last
        self._email = first + '.' + last + '@company.com'
        self._pay = pay

        Employee.nr_employees += 1

    def full_name(self):
        """ Helper method for class instance """

        return '{} {}'.format(self._first, self._last)

    def apply_raise(self):
        """ Allows to overwrite class variables."""

        self._pay = (self._pay * self.raise_amount)

class Developer(Employee):
    """ Developer class with addtional attributes."""

    raise_amount = 1.10 # overwritting parentclass attribute

    def __init__(self, first, last, pay, prog_lang):
        """
        This method is written as there's something more that
        what Employee class is holding. i.e. prog_lang param.

        Employee.__init__(self, first, last, pay) in multiple inheritence.
        or
        super().__init__(first, last, pay)

        """

        # Employee.__init__(self, first, last, pay) in multiple inheritence.
        super().__init__(first, last, pay)
        self._prog_lang = prog_lang


class Manager(Employee):
    """ Manager class with addtional attributes."""

    raise_amount = 1.10 # overwritting parentclass attribute

    def __init__(self, first, last, pay, employees=None):
        """
        This method is written as there's something more that
        what Employee class is holding. i.e. employees param.

        """

        # Employee.__init__(self, first, last, pay) in multiple inheritence.
        super().__init__(first, last, pay)
        if employees == None:
            self._employees = []
        else:
            self._employees = employees

    def add_emp(self, emp):
        if emp not in self._employees:
            self._employees.append(emp)

    def remove_emp(self, emp):
        if emp in self._employees:
            self._employees.pop(emp)

    def print_emps(self):
        print ('Manager : {}'.format(self.full_name()))
        for emp in self._employees:
            print('-->' + emp.full_name())

# Dev operations

# print (help(Developer))

# Instantiate class
dev1 = Developer('rajkumar', 'patel', 5000, 'C')
print ('Dev1 name : ' + dev1.full_name())
print ('Dev1 prog_lang : ' + dev1._prog_lang)

dev2 = Developer('test', 'user', 6000, 'python')
print ('Dev2 name : ' + dev2.full_name())
print ('Dev2 prog_lang : ' + dev2._prog_lang)

# Instantiate class
dev3 = Developer('raj', 'lakhani', 5000, 'sanskrit')
print ('Dev3 name : ' + dev3.full_name())
print ('Dev3 prog_lang : ' + dev3._prog_lang)

dev4 = Developer('veena', 'chauhan', 6000, 'cpp')
print ('Dev4 name : ' + dev4.full_name())
print ('Dev4 prog_lang : ' + dev4._prog_lang)


# Manager operations

# Instantiate class
manager1 = Manager('Kaustubh', 'D', 10000, [dev1])
manager1.add_emp(dev2)
manager1.print_emps()

manager2 = Manager('Anagha', 'D', 9000, [dev3])
manager2.add_emp(dev4)
manager2.print_emps()

# isinstance method
print(isinstance(manager1, Manager))
print(isinstance(manager1, Employee))
print(isinstance(dev1, Developer))
print(isinstance(dev1, Employee))
print(isinstance(dev1, Manager))

# issubclass method
print(issubclass(Developer, Manager))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))

