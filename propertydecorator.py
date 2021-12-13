class Student:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.fullname = fname+' '+lname

    def fullname_getter(self):
        return self.fname +' '+ self.lname
    
    def fullname_setter(self,name):
        firstname, lastname = name.split()
        self.fname = firstname
        self.lname = lastname

    def fullname_deleter(self):
        self.fname = None
        self.lname = None
        print('Deleted the fullname.')
        
    def email(self):
        return '{}.{}@email.com'.format(self.fname, self.lname)
    
    fullname = property()
    fullname = fullname.getter(fullname_getter)
    fullname = fullname.setter(fullname_setter)
    fullname = fullname.deleter(fullname_deleter)

    # this can be done in a single line too
    # fullname = property(fullname_getter, fullname_setter, fullname_deleter)


s1 = Student('Tony', 'Stark')
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

# now updating the s1 object's first name
s1.first = 'Steve'
print('Fullname of s1 is ', s1.fullname)
print('And email address = ', s1.email())

#setting new value of fullname
s1.fullname = 'Berry Banner'
print('New Fullname of s1 is ', s1.fullname)

#deleting the fullname
del s1.fullname
