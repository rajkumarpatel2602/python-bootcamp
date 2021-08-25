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


# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

print ('number of employees are : {}'.format(Employee.nr_employees))

print (emp1._pay)
emp1.apply_raise()
print (emp1._pay)

print ("Raise amount by class name : {}".format(Employee.raise_amount))
print ("Raise amount by emp1 instance : {}".format(emp1.raise_amount))
print ("Raise amount by emp2 instance : {}".format(emp2.raise_amount))

# apply_raise() will first check for raise_amount in instance's scope
# if not found then it will look for it in class or inherited class' scope.
print (Employee.__dict__)
print (emp1.__dict__)
print (emp2.__dict__)
print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

print ('raised complete class raise_amount')
Employee.raise_amount = 1.05

print ("Raise amount by class name : {}".format(Employee.raise_amount))
print ("Raise amount by emp1 instance : {}".format(emp1.raise_amount))
print ("Raise amount by emp2 instance : {}".format(emp2.raise_amount))
print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

# suppose one want to change the raise amount for just one employee
print ('raised emp1 raise_amount')
emp1.raise_amount = 1.7

print ("Raise amount by class name : {}".format(Employee.raise_amount))
print ("Raise amount by emp1 instance : {}".format(emp1.raise_amount))
print ("Raise amount by emp2 instance : {}".format(emp2.raise_amount))

# Only emp1 raise amount got changed
# As above statement has created an instance variable
# inside object emp1's namespace.

print (Employee.__dict__)
print (emp1.__dict__)
print (emp2.__dict__)
print (Employee.raise_amount)
print (emp1.raise_amount)
print (emp2.raise_amount)

