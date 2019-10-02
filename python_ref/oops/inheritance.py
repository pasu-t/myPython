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

class developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class manager(Employee):
    
    def __init__(self, first, last, pay, employees =None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp): 
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('->', emp.fullname())

dev_1 = developer('pasu', 'thumb', 50000, 'python')
dev_2 = developer('malli', 'siva', 60000, 'java')

mgr_1 = manager('sue', 'suer', 90000, [dev_1])

print(mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.print_emps()
mgr_1.rem_emp(dev_1)
print('#'*20)
mgr_1.print_emps()
# print(isinstance(mgr_1, manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, developer))
# print(issubclass(developer, Employee))
# print(issubclass(manager, Employee))
# print(issubclass(manager, developer))


# print(dev_1.email)
# print(dev_1.prog_lang)
# print(help(developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)