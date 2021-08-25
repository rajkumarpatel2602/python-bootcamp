# Actual class

class Employee:

    # Constructor method as in cpp
    def __init__(self, first, last, pay):
        self.first = first # instance vars are unique to the instance
        self.last = last
        self.email = first + '.' + last + '@company.com'
        self.pay = pay

    def emp_attribute_str(self):
        return 'first name:{} last name:{} pay:{}'.format( \
                self.first, self.last, self.pay)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

# Instantiate class
emp1 = Employee('rajkumar', 'patel', 5000)
emp2 = Employee('test', 'user', 6000)

#print ('Emp1 details :'+ Employee.emp_attribute_str(emp1))
print ('Emp1 details :'+ emp1.emp_attribute_str())
print ('Emp2 details :'+ emp2.emp_attribute_str())

print ('Emp1 full name ' + emp1.full_name())
print ('Emp2 full name ' + emp2.full_name())
