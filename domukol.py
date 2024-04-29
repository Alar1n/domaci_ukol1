class Animal:
    def __init__(self, name, species, weight):
        self.name = name
        self.species = species
        self.weight = weight

    def __str__(self):
        return f"{self.name} je {self.species} a váží {self.weight}."

    def export_to_dict(self):   
        return {"name": self.name, "species": self.species, "weight": self.weight}
    
class Employee:
    def __init__(self, full_name, annual_salary, position):
        self.full_name = full_name
        self.annual_salary = annual_salary
        self.position = position

    def __str__(self):
        return f"Zaměstnanec{self.full_name} dostává roční plat {self.annual_salary} a a pracuje na pozici {self.position}."
    
    def get_initials(self):
        names_list = self.full_name.split()
        return f"{names_list[0][0]}.{names_list[1][0]}."
    
class Director(Employee):
    def __init__(self, full_name, annual_salary, favourite_animal):
        super().__init__(full_name, annual_salary, "Ředitel")
        self.favourite_animal = favourite_animal

class Zoo:
    def __init__(self, name, address, director, employees, animals):
        self.name = name
        self.address = address
        self.director = director
        self.employees = employees
        self.animals = animals

    def weight_of_all_animals(self):
        total_weight = 0
        for animal_object in self.animals:
            total_weight += animal_object.weight
        return total_weight
        
    def monthly_costs_employees(self):
        monthly_costs_total = 0
        for employee_object in self.employees:
            monthly_costs_total += employee_object.annual_salary/12
        monthly_costs_total += self.director.annual_salary/12
        return monthly_costs_total

animal_dict_list = [
    {'name': 'Růženka', 'species': 'panda velká', 'weight': 150},
    {'name': 'Vilda', 'species': 'vydra mořská', 'weight': 20},
    {'name': 'Matýsek', 'species': 'tygr sumaterský', 'weight': 300},
    {'name': 'Karlík', 'species': 'lední medvěd', 'weight': 700},
]

animal_object_list = []

for animal_dict in animal_dict_list:
    animal_object = Animal(animal_dict['name'], animal_dict['species'], animal_dict['weight'])
    animal_object_list.append(animal_object)

employees_dict_list = [
    {'full_name': 'Tereza Vysoka', 'annual_salary': 700_000, 'position': 'Cvičitelka tygrů'},
    {'full_name': 'Anet Krasna', 'annual_salary': 600_000, 'position': 'Cvičitelka vyder'},
    {'full_name': 'Martin Veliky', 'annual_salary': 650_000, 'position': 'Cvičitel ledních medvědů'},
]

employees_object_list = []

for employee_dict in employees_dict_list:
    employee_object = Employee(employee_dict['full_name'], employee_dict['annual_salary'], employee_dict['position'])
    employees_object_list.append(employee_object)

zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', director, employees_object_list, animal_object_list)

print(zoo.director)
print('Celková váha zvířat v ZOO:', zoo.weight_of_all_animals())
print('Měsíční náklady na zaměstnance:', zoo.monthly_costs_employees())


# Animal class
test_animal = Animal('Láďa', 'Koala', 15)
pavouk = Animal('Adolf', 'Tarantule Velká', 0.1)
pavouk_export = pavouk.export_to_dict()
assert hasattr(test_animal, 'name')
assert hasattr(test_animal, 'species')
assert hasattr(test_animal, 'weight')
assert isinstance(test_animal.name, str)
assert isinstance(test_animal.species, str)
assert isinstance(test_animal.weight, int)
assert test_animal.export_to_dict() == {'name': 'Láďa', 'species': 'Koala', 'weight': 15}
assert pavouk_export['name'] == 'Adolf'
assert pavouk_export['species'] == 'Tarantule Velká'
assert pavouk_export['weight'] == 0.1


# Employee class
test_employee = Employee('Petr Novak', 50000, 'Programator')
assert hasattr(test_employee, 'full_name')
assert hasattr(test_employee, 'annual_salary')
assert hasattr(test_employee, 'position')
assert isinstance(test_employee.full_name, str)
assert isinstance(test_employee.annual_salary, int)
assert isinstance(test_employee.position, str)
assert test_employee.get_initials() == 'P.N.'

# Reditel class
test_animal = Animal('Lev', 'Lvice', 150)
director = Director('Jan Novotny', 80000, test_animal)
assert director.position == 'Ředitel'
assert isinstance(director.favourite_animal, Animal) 

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', director, [test_employee], [test_animal])
assert hasattr(zoo, 'name')
assert hasattr(zoo, 'address')
assert hasattr(zoo, 'director')
assert hasattr(zoo, 'employees')
assert hasattr(zoo, 'animals')
assert isinstance(zoo.name, str)
assert isinstance(zoo.address, str)
assert isinstance(zoo.director, Director)
assert isinstance(zoo.employees, list)
assert isinstance(zoo.animals, list)
assert zoo.weight_of_all_animals() == 150
assert zoo.monthly_costs_employees() == (test_employee.annual_salary + director.annual_salary) / 12


        