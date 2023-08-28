class Employee:
    def __init__(self, empid, name, age, salary):
        self.empid = empid
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"EmployeeID: {self.empid}, Name: {self.name}, Age: {self.age}, Salary(PM): {self.salary}"


class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_and_print(self, sorting_parameter):
        if sorting_parameter == 1:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.age)
        elif sorting_parameter == 2:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.name)
        elif sorting_parameter == 3:
            sorted_employees = sorted(self.employees, key=lambda emp: emp.salary)
        else:
            print("Invalid sorting parameter")
            return

        for employee in sorted_employees:
            print(employee)


def main():
    database = EmployeeDatabase()

    database.add_employee(Employee("161E90","Raman",41,56000))
    database.add_employee(Employee("161F91","Himadri",38,67500))
    database.add_employee(Employee("161F99","Jaya",51,82100))
    database.add_employee(Employee("171E20","Tejas",30,55000))
    database.add_employee(Employee("171G30","Ajay",45,44000))
    sorting_param = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
    database.sort_and_print(sorting_param)


if __name__ == "__main__":
    main()
