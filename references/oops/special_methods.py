class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)

    def __add__(self, other):
        if isinstance(other, Employee):
            return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('pasu', 'thumb', 50000)
emp_2 = Employee('malli', 'siva', 60000)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))
# print(emp_1.__repr__())
# print(emp_1.__str__())

print(emp_1 + emp_2)
print(len(emp_2))
