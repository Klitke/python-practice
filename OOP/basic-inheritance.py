class Employee():
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def get_fullname(self):
        return "{} {}".format(self.first, self.last)

    def __str__(self):
        return self.get_fullname()
    
    def __repr__(self):
        return self.__str__()

class Manager(Employee):
    def __init__(self, first, last, pay, emps=None):
        super().__init__(first, last, pay)
        if emps == None:
            self.emps = []
        else:
            self.emps = emps

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def add_emp(self, employee):
        if employee not in self.emps: 
            self.emps.append(employee)
            return print("Employee " + employee.get_fullname() + " has been added." )
        else:
            return print("That employee is already managed by " + self.fullname)

    def remove_emp(self, employee):
        if employee in self.emps:
            self.emps.remove(employee)
            return print(employee.get_fullname() + " has been removed.")
        else:
            return print(employee.get_fullname() + " is not managed by " + self.fullname)

    def print_emp(self):
        if len(self.emps) > 0:
            print(self.fullname + " is supervising the following employees:")
            for employee in self.emps:
                print(employee.get_fullname())
        else:
            print("This manager is not supervising any employees.")


emp_1_info = ("Peter", "Müller", 5000)
emp_2_info = ("Alex", "Peterson", 2000)
emp_3_info = ("Marcus", "Aurelius", 12000)
mngr_1_info = ("Alpha", "Male", 100000)

emp_1  = Employee(*emp_1_info)
emp_2  = Employee(*emp_2_info)
emp_3  = Employee(*emp_3_info)
mngr_1 = Manager(*mngr_1_info)

# Adding employees
# mngr_1.add_emp(emp_1)
# mngr_1.add_emp(emp_2)
# mngr_1.add_emp(emp_3)

# Removing employees
mngr_1.remove_emp(emp_1)
mngr_1.print_emp()