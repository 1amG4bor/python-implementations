from java.util import Date
from javacode import User

javaDate = Date()
print javaDate
print 'The current time is: {}h:{}m:{}s'.format(javaDate.getHours(), javaDate.getMinutes(), javaDate.getSeconds())

user = User()
user.setUsername('johndoe')
user.setFirstName('John')
user.setLastName('Doe')
user.setAge(42)

print '\nUser-data:'
print user
print user.getFullName()
