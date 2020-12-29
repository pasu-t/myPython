class Employee():
    def __init__(self,first,last):
        self.first = first
        self.last = last
        # self.email = "{}.{}@gmail.com".format(self.first,self.last) #modified this as function

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first,self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)

    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete name!")
        self.first = None
        self.last = None

emp_1 = Employee('Pasupathi', 'Thumbur')

print(emp_1.email) #getter

emp_1.fullname = "John Smith" #setter

print(emp_1.first, emp_1.last, emp_1.fullname)

del emp_1.fullname #deleter
