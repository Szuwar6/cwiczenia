class Phone:

    sector = 'electronics'
    os = 'Android'
    width = 500
    height = 1200

    def describe_class():
        '''Print class name'''
        print(f'{Phone.__name__} class.')
        print(f"operation system: {Phone.os}")

for attr in sorted(Phone.__dict__):
    if not attr.startswith('_'):
        print(f'{attr} -> {getattr(Phone, attr)}')

print("---------------------------------")

Phone.os = "Ios"  # zmioana parametru w klasie
setattr(Phone , 'width' , 1000) # inny sposób zmiany parametru w klasie

Phone.model = "Nokia" # dodanie atrubutu w locie
setattr(Phone , 'year' , 2015) # dodanie atrubutu w locie

del Phone.height #usuwanie atrybutu z klasy
delattr(Phone , 'sector') #usuwanie atrybutu z klasy

for attr in sorted(Phone.__dict__):
    if not attr.startswith('_'):
        print(f'{attr} -> {getattr(Phone, attr)}')

print("---------------------------------")
Phone.describe_class()
getattr(Phone, 'describe_class')() # wywołanie funkci z klasy

help(Phone)

class HouseProject:
    number_of_floors = 2
    area = 100

    def describe_project():
        print(f'Area: {HouseProject.area} m2.')
        print(f'Number of flors: {HouseProject.number_of_floors}.')

    def set_color(self , value):
        self.color = value

print(HouseProject.__dict__)

HouseProject.describe_project()

print(HouseProject.mro())

project1 = HouseProject()

project1.set_color('white') # zmiana w samej instancji
print(project1.__dict__)

HouseProject.set_color(project1 , 'grey') # zmiana w całej klasie w tym w kazdej instancji
print(project1.color)
print(project1.__dict__)

print("---------------------------------")

class Book:

    language = 'PL'
    author = 'Mickiewicz'

books = [Book(), Book(), Book()]
titles = ['Sonety krymskie', 'Pan Tadeusz', 'Konrad Wallenrod']

for book, value in zip(books, titles):
    # book.title = value
    setattr(book, 'title', value)
for book in books:
    print(f'język: {book.language}, autor: {book.author}, tytuł: {book.title}')

for book in books:
    print(book.__dict__)

print("---------------------------------")

class Phone:
    brand = 'Apple'
    short_name = brand[:3].upper()

    def print_brand(self): #self i wtedy działa wywołanie z poziomu instancji
        print(f'{Phone.__name__} class.')
        print(f'Brand: {Phone.brand}')

phone1 = Phone()
phone1.print_brand() # działa dzieki self
Phone.print_brand(phone1)

print("---------------------------------")

class Phone:

    brand = 'Apple'

    def __init__(self, brand):
        self.brand = brand

    def print_brand(self):
        print(f'Wartość atrybutu klasy: {Phone.brand}')
        print(f'Wartość atrybutu instancji: {self.brand}')

phone1 = Phone('Samsung')
phone1.print_brand()


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs(self):
        for attr in self.__dict__.keys():
            print(attr)

    def display_values(self):
        for attr, value in self.__dict__.items():
            print(f'{attr}: {value}')

laptop = Laptop('Acer', 'Predator', 1111)

print(laptop.__dict__)
laptop.display_attrs()
laptop.display_values()
print("---------------------------------")
class Vector:

    def __init__(self, *args):
        self.components = args

v1 = Vector(3, 4)
v2 = Vector(5, 3, -2)

print(v1.components)
print(v2.components)
print("---------------------------------")
class TechStack:

    def __init__(self, **kwargs):

        self.techs = kwargs

    def display_info(self):
        return print(f'Total number of techs: {len(self.techs)}')

stack = TechStack(python='mid', java='senior', sql = 'mid')
print(stack.techs)
print(stack.__dict__)
stack.display_info()

print("---------------------------------")

class TechStack:

    def __init__(self, tech=None):
        self.tech = tech

    def display_info(self):
        if self.tech:
            print(f'Techs: {self.tech}')
        else:
            print('No techs.')

stack = TechStack()
stack.display_info()
stack = TechStack('Python')
stack.display_info()

print("---------------------------------")
class Smartphone:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError('The price attribute must be a positive int or float')


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(smartphone.__dict__)


class Laptop:

    brand = 'Apple'
    _usdpln = 4.0
    __trade_margin = 0.3

    def __init__(self, net_price):
        self.net_price = net_price

    def _convert_price(price):
        return price * Laptop._usdpln * (1 + Laptop._Laptop__trade_margin)

    def display_price_pln(self):
        print(f'Cena:{Laptop._convert_price(self.net_price)}')

laptop = Laptop(3000)
laptop.display_price_pln()


class Smartphone:

    def __init__(self, brand, model, price):
        self.brand = brand
        self._model = model
        self.__price = price


smartphone = Smartphone('Huawei', 'Mate 20 Pro', 1999)
print(f'brand -> {smartphone.brand}')
print(f'model -> {smartphone._model}')
print(f'price -> {smartphone._Smartphone__price}') # dostęp do prywatnej dany

print("---------------------------------")

class Phone:

    def __init__(self, price):
        self.set_price(price) # walidacja która nie pozwala stworzyc niczego poza liczba dodatnia

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')

# phone = Phone("1")

print("-----------metoda property----------------------")

class Phone:

    def __init__(self, price):
        self._price = price

    def price(self):
        print('getting...')
        return self._price

    price = property(fget=price)

phone = Phone(1200)
print(phone.price)

# phone.price = 1 # nie mozna zmieniclub skasowac ceny dzieki metodzie property poniewaz brakuje fset i fdel
print('++++++++++++++++++++++++++++++++++++++++')

class Phone:
    """Phone class docs."""

    def __init__(self, price):
        self._price = price

    def get_price(self):
        print('getting...')
        return self._price

    def set_price(self, value):
        print('setting...')
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')

    def del_price(self):
        print('deleting...')
        del self._price

    price = property(fget=get_price, fset=set_price, fdel=del_price, doc='Phone price.')

phone = Phone(10)
print(phone.price)
phone.price = 9988
print(phone.price)

del phone.price

# print(phone.price)
print("-----------dekoratory----------------------")
import time

import time


def timer(func):
    def wrapper(sec):
        start = time.time()
        func(sec)
        stop = time.time()
        print(f'Execution time: {stop - start:.4f}')
    return wrapper

@timer
def fake_sleep(sec):
    print(f'Executing {fake_sleep.__name__}...')
    time.sleep(sec)

fake_sleep(0)

print("-----------dekoratory z metoda property i walidacja (nie mozna wpisac dowolnej ceny)----------------------")

class Phone:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        print('getting...')
        return self._price

    @price.setter
    def price(self, value):
        print('setting...')
        if isinstance(value, (int, float)):
            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be positive.')
        else:
            raise TypeError('The price attribute must be an int or float value.')

    @price.deleter
    def price(self):
        print('deleting...')
        del self._price

phone = Phone(3423)
print(phone.price)

class Game:

    def __init__(self, level=0):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value

games = [Game(), Game(10), Game(-10), Game(130)]
print([game.level for game in games])


class Smartphone:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value


smartphone = Smartphone(3499)
print(smartphone.get_price())
smartphone.set_price(3999)
print(smartphone.get_price())


class Worker:

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._last_name


    def get_last_name(self):
        return self._last_name

    first_name = property(fget=get_first_name)
    last_name = property(fget=get_last_name)


worker = Worker('John', 'Dow')

print(worker._first_name)
print(worker._last_name)


class Pet:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


pet = Pet('Max')
pet.name = 'Oscar'

print(pet.__dict__)
print('++++++++++++++++++++++++++++++++++++++++')


class Model:

    def __init__(self, y_true, y_pred):

        Model._validate_input(y_true, 'y_true')
        Model._validate_input(y_pred, 'y_pred')

        if not len(y_true) == len(y_pred):
            raise ValueError('The y_true and y_pred objects must be of same '
                             'length.')

        self._y_true = y_true
        self._y_pred = y_pred
        self._accuracy = None

    def _validate_input(iters, var_name):
        if not isinstance(iters, (list, tuple)):
            raise TypeError(f'The {var_name} object must be of type list or '
                            f'tuple. Not {type(iters).__name__}.')

    def _validate_value(self, value, var_name):
        if not isinstance(value, (list, tuple)):
            raise TypeError(f'The value must be a list or tuple object. '
                            f'Not {type(value).__name__}.')

        mapping = {'y_true': '_y_pred', 'y_pred': '_y_true'}

        if not len(value) == len(getattr(self, mapping[var_name])):
            raise ValueError(f'The {var_name} object must be of length '
                             f'{len(getattr(self, mapping[var_name]))}.')

    @property
    def y_true(self):
        return self._y_true

    @y_true.setter
    def y_true(self, value):

        Model._validate_value(self, value, 'y_true')

        self._y_pred = value
        self._accuracy = None

    @y_true.deleter
    def y_true(self):
        print('deleting...')
        del self._y_true

    @property
    def y_pred(self):
        return self._y_pred

    @y_pred.setter
    def y_pred(self, value):

        Model._validate_value(self, value, 'y_pred')

        self._y_pred = value
        self._accuracy = None

    @y_pred.deleter
    def y_pred(self):
        print('deleting...')
        del self._y_pred

    @property
    def accuracy(self):
        if not self._accuracy:
            print('Calculating...')
            self._accuracy = sum([i == j
                                  for i, j in zip(self.y_true, self.y_pred)]) / len(self.y_true)
        print(f'Model accuracy: {self._accuracy:.4f}')


model = Model([0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 0])

model.accuracy
model.accuracy
model.y_true = [0, 0, 1, 0, 0, 0, 0]  # posiada walidacje aby była ta sama długość i był list i tuple

model.accuracy
model.accuracy


import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area
        # print(f'{self._area:.4f}')

circle = Circle(3)

print(f'{circle.area:.4f}')

print('---------------Dekorator classmethod----------------------------------')

class Phone:

    instances = []

    def __init__(self, brand):
        self.brand = brand
        Phone.instances.append(self)

    @classmethod
    def show(cls):
        if len(cls.instances) > 0:
            print(f'List of instances of the {cls.__name__} class:')
            for instance in cls.instances:
                print(f'\t{instance}')
        else:
            print(f'There is no instance of the {cls.__name__} class.')

    def show_brand(self):
        print(f'Brand: {self.brand}')

Phone.__dict__
Phone.show()

phone1 = Phone('Apple')
phone2 = Phone('Samsung')

Phone.show()


for instance in Phone.instances:
    instance.show_brand()




class Worker:
    instances = []

    def __init__(self):
        Worker.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(Worker.instances)


worker1 = Worker()
worker2 = Worker()
worker3 = Worker()

print(Worker.count_instances())

print('---------------Dekorator staticmethod----------------------------------')

class Phone:

    instances = []

    def __init__(self):
        self.creation_time = Phone.get_current_time()
        Phone.instances.append(self)

    @staticmethod
    def get_current_time():
        return time.strftime('%H:%M:%S', time.localtime())

phone1 = Phone()
time.sleep(1)
phone2 = Phone()
time.sleep(2)
phone3 = Phone()

print(Phone.instances)

for instance in Phone.instances:
    print(instance.creation_time, instance)


class Person:

    def __init__(self, input_str):
        if Person._is_string_with_space(input_str):
            items = input_str.split(' ')
            if len(items) == 2:
                self._name = items[0]
                self._surname = items[1]
            else:
                raise ValueError('The object cannot be created.')
        else:
            raise ValueError('Please insert a space between your name and '
                'surname.')

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @staticmethod
    def _is_string_with_space(input_str):
        return isinstance(input_str, str) and ' ' in input_str

person = Person('Marek Szu')

print(person.name , person.surname)
print(person.__dict__)

print('-------------metody specjalne--------------')


class Student:

    students = []
    limit = 3

    def __new__(cls):
        if len(cls.students) >= cls.limit:
            raise RuntimeError(f'Instance limit reached: {cls.limit}')
        instance = object.__new__(cls)
        cls.students.append(instance)
        return instance

s1 = Student()
s2 = Student()
s3 = Student()
# s4 = Student()
class Phone:

    def __init__(self, brand):
        self.brand = brand

    def __repr__(self):
        return f"Phone(brand='{self.brand}')"

    def __str__(self):
        return f'{self.brand} brand mobile phone.'

phone = Phone('Apple')
repr(phone)
print(phone)
str(phone)


class Point:

    def __init__(self, *coords):
        for value in coords:
            if not isinstance(value, (int, float)):
                raise ValueError('Coordinates must be of type int or float.')
        self._coords = coords

    def __repr__(self):
        return f"Point(coords={self._coords})"

    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x + y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __sub__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x - y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __mul__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        coords = tuple(x * y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __truediv__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        for coord in other.coords:
            if coord == 0:
                raise ZeroDivisionError('Division by zero.')
        coords = tuple(x / y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __floordiv__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        for coord in other.coords:
            if coord == 0:
                raise ZeroDivisionError('Division by zero.')
        coords = tuple(x // y for x, y in zip(self.coords, other.coords))
        return Point(*coords)

    def __len__(self):
        return len(self._coords)

    def __bool__(self):
        return sum(self._coords) != 0

    @property
    def coords(self):
        return self._coords

p = Point(1 , 5 , 6)
q = Point( 1 , 2 , -4)
a = Point()
print(p)
print(p.coords)
print(p.__dict__)
print(len(p))
print(bool(p))
print(bool(q))
print(bool(a))
print(p + q)
print(p - q)
print(p * q)
print(p / q)
print(p // q)

class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        if not isinstance(other, Doc):
            return NotImplemented
        return Doc(self.string + ' ' + other.string)

doc1 = Doc('Ala')
doc2 = Doc('ma')
doc3 = Doc('kota')

print(doc1 + doc2 + doc3)

print('-------------------------dziedziczenie------------------')
class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land'

    def __repr__(self):
        return f"{self.__class__.__name__}(category='{self.category}')"

    def display_info(self):
        print(f'{self.__class__.__name__} category: {self.category}')

    def show_activity(self):
        print(f'{self} -> Moving...')


class LandVehicle(Vehicle):

    # def display_info(self):
    #     print(f'{self.__class__.__name__} category: {self.category}')

    def show_activity(self):
        print(f'{self} -> Driving...')


class AirVehicle(Vehicle):

    def show_activity(self):
        print(f'{self} -> Flying...')

vehicles = [Vehicle(), LandVehicle(), AirVehicle('air')]
vehicles

for vehicle in vehicles:
    vehicle.show_activity()
    vehicle.display_info()


class User:

    def start(self):
        print('Starting...')

    def drink(self):
        print('Drinking...')

    def work(self):
        print('Working...')

    def end(self):
        print('Ending...')

    def make_session(self):
        print(f'--- {self.__class__.__name__.upper()} SESSION ---')
        self.start()
        self.drink()
        self.work()
        self.end()
        print(f'--- END SESSION ---\n')


class Player(User):

    def work(self):
        print('Playing...')

user = User()
user.make_session()



player = Player()
player.make_session()


class Vehicle:
    year = 2010

    def info(self):
        print(f'{self.__class__.__name__} from {self.__class__.year}.')


class Car(Vehicle):
    year = 2020


vehicles = [Vehicle(), Car()]
for vehicle in vehicles:
    vehicle.info()


class Vehicle:

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_details(self):
        print(f'Calling from... {self.__class__.__name__}.')


class Car(Vehicle):

    def __init__(self, brand, year, horsepower):
        super().__init__(brand, year)
        self.horsepower = horsepower

    def show_details(self):
        print(f'Extended calling from... {self.__class__.__name__}.')
        super().show_details()

c1 = Car('Tesla', 2020, 306)
print(c1.__dict__)
c1.show_details()


print('--------------------Dziedziczenie wielopoziomowe---------------')


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:

    def __init__(self, dept_name):
        self.dept_name = dept_name


class Worker(Person, Department):

    def __init__(self, first_name, last_name, age, dept_name, hours_per_day=8):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name)
        self.hours_per_day = hours_per_day

worker = Worker('John', 'Smith', 40, 'IT')
print(worker.__dict__)


print('--------------------klasa abstrakcyjna-----------------')

from abc import ABC, abstractmethod
import math


class Figure(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Figure):

    def __init__(self, a=1):
        self.a = a

    def area(self):
        return self.a * self.a

    def perimeter(self):
        return self.a * 4


class Circle(Figure):

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Figure):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = self.perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


figures = [Square(), Square(5), Square(10), Circle(), Circle(5), Circle(10),
           Triangle(3, 4, 5)]

for figure in figures:
    print(f'Area: {figure.area():.2f}')
    print(f'Perimeter: {figure.perimeter():.2f}\n')