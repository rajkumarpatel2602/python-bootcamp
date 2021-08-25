#userless class

class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

# When we want to give attributes.
# It becomes cumbersome.
# Instantiating class with all these attributes
# is more elegant approach.
emp1.first = 'rajkumar'
emp1.last = 'patel'
emp1.email = 'rajkumar.patel@company.com'
emp1.pay = 5000

emp2.first = 'test'
emp2.last = 'user'
emp2.email = 'test.user@company.com'
emp2.pay = 6000

print (emp1.first)
print (emp1.last)
print (emp1.email)
print (emp1.pay)

print (emp2.first)
print (emp2.last)
print (emp2.email)
print (emp2.pay)

# Is it good to get data and write code? why not to create a instance method
# which use data and do operation.
# emp1.full_name() is easy rather than writing as below.i
# Why not to use code reuse instead?
print ("Full name of emp1 : {} {}".format(emp1.first, emp1.last))
print ("Full name of emp2 : {} {}".format(emp2.first, emp2.last))
