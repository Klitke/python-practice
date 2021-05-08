class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def set_first(self, first):
        self.first = first
        return self.first
    
    # getter
    @property
    def fullname(self):
        return print('Fullname: {} {}'.format(self.first, self.last))
    
    # setter 
    @fullname.setter
    def fullname(self, mp_data_string):
        prev_fullname = f'{self.first} {self.last}'
        self.first, self.last, self.pay = emp_data_string.split("-")
        new_fullname = f'{self.first} {self.last}'
        return print("The full name changed from " + prev_fullname + " to " + new_fullname)

    # deleter
    @fullname.deleter
    def fullname(self):
        msg = "{} is being deleted.".format(self.fullname)
        self.first = None
        self.last = None
        return print(msg)
        

emp_data_tuple = ("Peter", "Müller", 1000)
emp_data_string = "Hans-Jürgen-5000"

emp_1 = Employee(*emp_data_tuple)

# Call Getter
emp_1.fullname

# Call Setter
emp_1.fullname = emp_data_string

# Call Deleter
del emp_1.fullname  

