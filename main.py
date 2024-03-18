from employee import Employee
from db import conn


first_user = Employee.get(1)
if first_user is None:
    first_user = Employee("name", "surname", "age")
    first_user.save()


usr = Employee("Saba", "Katamadze", 21)
usr1 = Employee("John", "Doe", 25)
usr2 = Employee("James", "Doe", 30)
usr3 = Employee("Saba", "Smith", 32)

# usr.save()
# usr1.save()
# usr2.save()
# usr3.save()
print(Employee.get_list(name="Saba"))
print(Employee.get_list(surname="Doe"))

# usr2.delete(usr2.id)

# print(usr.__le__(usr2))
# print(usr.__lt__(usr2))
# print(usr.__eq__(usr2))
# print(usr.__ne__(usr2))
# print(usr.__gt__(usr2))
# print(usr.__ge__(usr2))

first_user.name = "Tornike"
first_user.save()
conn.commit()
conn.close()
