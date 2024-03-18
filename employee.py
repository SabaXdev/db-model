from db import c, conn


"""
PK - Primary Key
"""


class Employee(object):
    def __init__(self, name, surname, age, pk=None):
        self.id = pk
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def get(cls, pk):
        result = c.execute("SELECT * FROM employee WHERE id = ?", (pk,))
        values = result.fetchone()
        if values is None:
            return None
        employee = Employee(values["name"], values["surname"], values["age"], values["id"])
        return employee

    @classmethod
    def get_list(cls, **kwargs):
        query = "SELECT * FROM employee WHERE "
        conditions, parameters = [], []
        for key, val in kwargs.items():
            conditions.append(f'{key} = ?')
            parameters.append(val)

        query += " AND ".join(conditions)
        result = c.execute(query, parameters)
        employees = []

        for row in result.fetchall():
            employees.append(Employee(row["name"], row["surname"], row["age"], row["id"]))

        if result.fetchall() is None:
            return None

        return employees

    def __repr__(self):
        return "<Employee {}>".format(self.name)

    def update(self):
        c.execute("UPDATE employee SET name = ?, surname = ?, age = ? WHERE id = ?",
                  (self.name, self.surname, self.age, self.id))

    def create(self):
        c.execute("INSERT INTO employee (name, surname, age) VALUES (?, ?, ?)", (self.name, self.surname, self.age))
        self.id = c.lastrowid

    def delete(self, user_id):
        c.execute("DELETE FROM employee WHERE id = ?", (user_id,))

    def save(self):
        if self.id is not None:
            self.update()
        else:
            self.create()
        return self

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age

    def __ne__(self, other):
        return self.age != other.age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age