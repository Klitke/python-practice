class Employee():
    # class variable
    num_emps = 0

    def __init__(self, emp_num):
        self.emp_num = emp_num

        Employee.num_emps += 1

    @staticmethod
    def print_num_emps():
        print(Employee.num_emps)
    
    @classmethod
    def change_num_emps(cls, num_emps):
        cls.num_emps = num_emps
    
    # Constructor
    @classmethod
    def create_emp(cls):
        new_emp_id = cls.num_emps + 1
        new_emp_id = cls(new_emp_id)
        print("New employee with id " + str(new_emp_id.emp_num) + " created.")
        

emp_amnt = list(range(1,11))

for emp in emp_amnt:
    emp = Employee(emp)

# Calling static method
Employee.print_num_emps()

emp_11 = Employee(11)

Employee.change_num_emps(555000)
Employee.print_num_emps()

Employee.create_emp()