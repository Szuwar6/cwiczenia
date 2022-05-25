import uuid


class Product:

    def __init__(self, product_name, price):
        self.product_id = self.get_id()
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return f"Product(product_name='{self.product_name}', price={self.price})"

    @staticmethod
    def get_id():
        return str(uuid.uuid4().fields[-1])[:6]


for key in Product.__dict__:
    print(key)


def stock_info(company, country, price, currency):
    return f'Company: {company}\nCountry: {country}\nPrice: {currency} {price}'


print(stock_info.__code__.co_varnames)

counter = 1


def update_counter():
    global counter
    counter += 1
    return counter


print(update_counter())

counter = 0
dot_counter = ''

counter = 0
dot_counter = ''


def update_counter():
    global counter, dot_counter
    counter += 1
    dot_counter += '.'


[update_counter() for _ in range(40)]
print(counter)
print(dot_counter)


def display_info(number_of_updates=1):
    counter = 100
    dot_counter = ''

    def update_counter():
        nonlocal counter, dot_counter
        counter += 1
        dot_counter += '.'

    [update_counter() for _ in range(number_of_updates)]

    print(counter)
    print(dot_counter)


(display_info(10))


def stick(*args):
    return "#".join(args for args in args if isinstance(args, str))


print(stick('sport', 'acs', 4))


def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")


display_info(company='CD Projekt', price=100)


class Phone:
    brand = "Apple"
    model = "iPhone X"


print(getattr(Phone, "brand"))


class Phone:
    brand = 'Apple'
    model = 'iPhone X'


Phone.brand = "Samsung"
Phone.model = "Galaxy"

print(f'brand : {Phone.brand}')


class Laptop:
    brand = 'Lenovo'
    model = 'ThinkPad'


setattr(Laptop, 'brand', "Acer")
setattr(Laptop, 'model', "Predator")

print(f'brand: {Laptop.brand}')
print(f'model: {Laptop.model}')


class OnlineShop:
    sector = 'electronic'
    sector_code = 'ELE'
    is_public_company = False


OnlineShop.country = 'Poland'

diii = [i for i in OnlineShop.__dict__ if not i.startswith('_')]

print(diii)


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


for i in OnlineShop.__dict__:
    if not i.startswith('_'):
        print(f'{i} -> {getattr(OnlineShop, i)}')


class OnlineShop:
    sector = 'electronics'
    sector_code = 'ELE'
    is_public_company = False


def describe_attrs():
    for i in OnlineShop.__dict__:
        if not i.startswith('_'):
            print(f'{i} -> {getattr(OnlineShop, i)}')


describe_attrs()


class Book:
    language = 'ENG'
    is_ebook = True


book = Book()
print(book.__dict__)

book.author = 'Dan Brown'
book.title = 'Inferno'
print(book.__dict__)


class Book:
    language = 'ENG'
    is_ebook = True


book_1 = Book()
book_2 = Book()

book_1.author = 'Dan Brown'
book_1.title = 'Inferno'

book_2.author = 'Dan Brown'
book_2.title = 'The Da Vinci Code'
book_2.year_of_publishment = 2003

books = [book_1, book_2]
for book in books:
    for attr in book.__dict__:
        print(f'{attr} -> {getattr(book, attr)}')
    print('-' * 30)


class Book:
    language = 'ENG'
    is_ebook = True


books_data = [
    {'author': 'Dan Brown', 'title': 'Inferno'},
    {'author': 'Dan Brown', 'title': 'The Da Vinci Code', 'year_of_publishment': 2003}]

books = []
for book_data in books_data:
    book = Book()
    for key, value in book_data.items():
        setattr(book, key, value)
    books.append(book)

for book in books:
    print(book.__dict__)


class Book:
    language = 'ENG'
    is_ebook = True

    def set_title(self, value):
        if isinstance(value, str):
            self.title = value
        else:
            raise TypeError('The value of the title atribute must be of str type')


book = Book()

# book.set_title("Inferno")
#
# print(book.title)

try:
    book.set_title(False)
except TypeError as error:
    print(error)


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def display_attrs(self):
        for attr, values in self.__dict__.items():
            print(f'{attr} -> {values}')


laptop = Laptop('Dell', 'Inspiron', 3699)

laptop.display_attrs()


class Vector:
    def __init__(self, *args):
        self.components = args


v1 = Vector(1, 2)
v2 = Vector(4, 5, 2)

print(f'v1 -> {v1.components}')
print(f'v2 -> {v2.components}')


class Bucket:
    def __init__(self, **kwargs):
        self.kwargs = kwargs


bucket = Bucket(apple=3.5, milk=2.5, juice=4.9, water=2.5)

print(bucket.kwargs)


class Car:
    def __init__(self, brand, model, price, type_of_car='sedan'):
        self.brand = brand
        self.model = model
        self.price = price
        self.type_of_car = type_of_car


car = Car('Opel', 'Insignia', 115000)

print(car.__dict__)


class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        if isinstance(price, (int, float)) and price > 0:
            self.price = price
        else:
            raise TypeError('The price attribute must be a positive int or float.')


lap = Laptop('Acer', 'Predator', 5490)

print(lap.__dict__)


class Laptop:

    def __init__(self, brand, model, code, price, margin):
        self.brand = brand
        self._model = model
        self._code = code
        self.__price = price
        self.__margin = margin

    def display_private_attrs(self):
        for attr in self.__dict__:
            if attr.startswith('_') and not attr.startswith(f'_{self.__class__.__name__}__'):
                print(attr)


laptop = Laptop('Acer', 'Predator', 'AC-100', 5490, 0.2)
laptop.display_private_attrs()


class Laptop:

    def __init__(self, price):
        self._price = price

    def get_price(self):
        return self._price

    def set_price(self, value):
        if isinstance(value, (int, float)):

            if value > 0:
                self._price = value
            else:
                raise ValueError('The price attribute must be a positive int or float value.')
        else:
            raise TypeError('The price attribute must be a int or float type.')


lap = Laptop(3499)

print(lap.get_price())
try:
    lap.set_price('-3000')
except TypeError as error:
    print(error)


class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def get_first_name(self):
        return self._first_name

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, value):
        self._first_name = value

    def set_last_name(self, value):
        self._last_name = value

    def del_first_name(self):
        del self._first_name

    first_name = property(fget=get_first_name, fset=set_first_name, fdel=del_first_name)
    last_name = property(fget=get_last_name, fset=set_last_name)


person = Person('John', 'Dow')

print(person.first_name)
print(person.last_name)

person.first_name = 'Tom'
person.last_name = 'Smith'

print(person.__dict__)

person.del_first_name()

print(person.__dict__)


class Pet:

    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, dana):
        if not isinstance(dana, int):
            raise TypeError('The value of age must be of type int.')
        if not dana > 0:
            raise ValueError('The value of age must be a positive integer.')
        self._age = dana


# pet = Pet('Max', '5')
# # pet.name = 'Tom'
# pet.age = '8'
# print(pet.__dict__)
try:
    pet = Pet('Max', 'seven')
except TypeError as error:
    print(error)
except ValueError as error:
    print(error)


class TechStack:
    def __init__(self, tech_names):
        self._tech_names = tech_names

    @property
    def tech_names(self):
        return self._tech_names

    @tech_names.setter
    def tech_names(self, value):
        self._tech_names = value

    @tech_names.deleter
    def tech_names(self):
        del self._tech_names


tech_stack = TechStack('python,java,sql')
print(tech_stack.tech_names)
tech_stack.tech_names = 'python,sql'
print(tech_stack.tech_names)
del tech_stack.tech_names
print(tech_stack.__dict__)


class Game:
    def __init__(self, level=0):
        self.level = level

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        if not isinstance(value, int):
            raise TypeError('The value of level must be of the int.')
        if value < 0:
            self._level = 0
        elif value > 100:
            self._level = 100
        else:
            self._level = value


games = [Game(), Game(10), Game(-10), Game(120)]

for i in games:
    print(i.level)

import math


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
        self._perimeter = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value
        self._area = None
        self._perimeter = None

    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * self._radius * self._radius
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * math.pi * self._radius
        return self._perimeter

circle = Circle(3)
print(f'{circle.perimeter:.4f}')


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._area = None
        self._perimetr = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value
        self._area = None
        self._perimetr = None

    @height.setter
    def height(self, value):
        self._height = value
        self._area = None
        self._perimetr = None

    @property
    def area(self):
        if self._area is None:
            self._area = self._height * self._width
        return self._area

    @property
    def perimetr(self):
        if self._perimetr is None:
            self._perimetr = 2* self._height + 2* self._width
        return self._perimetr


rectangle = Rectangle(3, 4)


print(f'width: {rectangle.width}, height: {rectangle.height} -> perimetr: {rectangle.perimetr}')


class Person:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"Person(fname='{self.fname}', lname='{self.lname}')"

    def __str__(self):
        return f'First name: {self.fname}\nLast name: {self.lname}'


person = Person('John', 'Doe')

print(person)


class Vector:

    def __init__(self, *components):
        self.components = components

    def __repr__(self):
        return f'Vector{self.components}'

    def __str__(self):
        return f'{self.components}'

    def __len__(self):
        return len(self.components)

    def __bool__(self):
        if len(self.components) == 0:
            return False
        return self.components[0] != 0


v1 = Vector()
v2 = Vector(3, 2)
v3 = Vector(0, -3, 2)
v4 = Vector(5, 0, -1)

print(bool(v1))
print(bool(v2))
print(bool(v3))
print(bool(v4))

class Hashtag:

    def __init__(self, string):
        self.string = '#' + string

    def __repr__(self):
        return f"Hashtag(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Hashtag(self.string[1:] + ' '+other.string)


h1 = Hashtag('python')
h2 = Hashtag('developer')
h3 = Hashtag('oop')

print(h1 + h2+h3)


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __eq__(self, other):
        return self.string == other.string


doc1 = Doc('Finance')
doc2 = Doc('Finance')

print(doc1 == doc2)


class Doc:

    def __init__(self, string):
        self.string = string

    def __repr__(self):
        return f"Doc(string='{self.string}')"

    def __str__(self):
        return f'{self.string}'

    def __add__(self, other):
        return Doc(self.string + ' ' + other.string)

    def __lt__(self, other):
        return len(self.string) < len(other.string)

    def __iadd__(self, other):
        return Doc(self.string + ' & ' + other.string)


doc1 = Doc('sport')
doc2 = Doc('activity')

print(doc1 < doc2)
doc1 += doc2
print(doc1)

class Vehicle:

    def __init__(self, category=None):
        self.category = category if category else 'land vehicle'

    def display_info(self):
        return print(f'{self.__class__.__name__} -> {self.category}')


class LandVehicle(Vehicle):
    pass


class AirVehicle(Vehicle):

    def __init__(self, category=None):
        self.category = category if category else 'air vehicle'


vehicles = [Vehicle(), LandVehicle(), AirVehicle()]

for vehicle in vehicles:
    vehicle.display_info()


class Vehicle:

    def __init__(self, brand, color, year):
        self.brand = brand
        self.color = color
        self.year = year

    def display_attrs(self):
        print(f"Calling from class: {self.__class__.__name__}")
        for attr, value in self.__dict__.items():
            print(f'{attr} -> {value}')


class Car(Vehicle):

    def __init__(self, brand, color, year, horsepower):
        super().__init__(brand, color, year)
        self.horsepower = horsepower


car = Car('Opel', 'black', 2018, 160)

car.display_attrs()

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Department:

    def __init__(self, dept_name, short_dept_name):
        self.dept_name = dept_name
        self.short_dept_name = short_dept_name


class Worker(Person, Department):
    def __init__(self,first_name, last_name, age, dept_name, short_dept_name ):
        Person.__init__(self, first_name, last_name, age)
        Department.__init__(self, dept_name, short_dept_name)

work = Worker('John', 'Doe', 30, 'Information Technology', 'IT')

print(work.__dict__)

from abc import ABC, abstractmethod


class TaxPayer(ABC):

    def __init__(self, salary):
        self.salary = salary

    @abstractmethod
    def calculate_tax(self):
        pass


class StudentTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.15


class DisabledTaxPayer(TaxPayer):

    def calculate_tax(self):
        return self.salary * 0.12


class WorkerTaxPayer(TaxPayer):
    def calculate_tax(self):
        if self.salary < 80000:
            return 0.17 * self.salary
        return 13600+(0.32 * (self.salary-80000))


wor1 = WorkerTaxPayer(70000)
wor2 = WorkerTaxPayer(95000)

print(wor1.calculate_tax())
print(wor2.calculate_tax())

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


people = [Person('Tom', 25), Person('John', 29),
          Person('Mike', 27), Person('Alice', 19)]

people.sort(key=lambda person: person.age)

for i in people:
    print(f'{i.name} -> {i.age}')

import datetime


class Note:

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')

    def __repr__(self):
        return f"Note(content='{self.content}')"

    def find(self, word):
        return word.lower() in self.content.lower()


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, content):
        self.notes.append(Note(content))

    def display_notes(self):
        for note in self.notes:
            print(note.content)

    def search(self, value):
        return [i for i in self.notes if  i.find(value)]

notebook = Notebook()
notebook.new_note('My first note.')
notebook.new_note('My second note.')
print(notebook.notes)

note1 = Note('Object Oriented Programming in Python.')

print(note1.find('python'))
print(note1.find('Python'))
notebook.new_note('Big Data')
notebook.new_note('Data Science')
notebook.new_note('Machine Learning')


print(notebook.search('data'))

class Client:
    all_client = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Client.all_client.append(self)

    def __repr__(self):
        return f"Client(name='{self.name}, email={self.email}')"


client1 = Client('Tom', 'sample@gmail.com')
client2 = Client('Donald', 'sales@yahoo.com')
client3 = Client('Mike', 'sales-contact@yahoo.com')
print(Client.all_client)

class StringListOnly(list):

    def append(self, string):
        if not isinstance(string, str):
            raise TypeError('Only objects of type str can be added to the list.')
        super().append(string.lower())


slo = StringListOnly()
slo.append('Data')
slo.append('Science')
slo.append('Machine Learning')
print(slo)