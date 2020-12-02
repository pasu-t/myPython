import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s: %(levelname)s %(name)s - %(message)s")

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info("Created Employee: {} {}".format(self.first,self.last))

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first,self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp1 = Employee('Pasupathi','Thumbur')
emp2 = Employee('Socratica', 'Python')
emp3 = Employee('Corey', 'Schafer')