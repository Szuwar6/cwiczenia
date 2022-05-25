import math


def validate_pin(pin):
    x = pin.isnumeric()
    if x != True:
        return False


    elif 1000000 < int(pin):
        return False
    elif 0 > int(pin):
        return False

    elif len(pin) == 4:  # and len(pin) != 6:
        return True
    elif len(pin) == 6:
        return True

    else:
        return False


print((validate_pin("")))
"""
txt = "5655.43"

x = txt.isnumeric()

print(x)"""


def array_diff(a, b):
    return [i for i in a + b if i in a and i not in b]


print(array_diff([18, -14, -17, -4, -5, 7], [-15, -5, 11, 8, -7, 15, 11, -8]))


def quadratic(x1, x2):
    a = 1
    b = -(x1 + x2)
    c = x1 * x2
    return a, b, c


print(quadratic(2, 3))


def twice_as_old(d, s):
    return abs(s * 2 - d)


print(twice_as_old(22, 1))


def same_case(a, b):
    if a.isalpha() == False or b.isalpha() == False:
        return -1
    elif a.isupper() == True and b.isupper() == True:
        return 1
    elif a.islower() == True and b.islower() == True:
        return 1
    else:
        return 0


print(same_case('s', 'Z'))


def find_uniq(arr):
    if arr[0] != arr[1] and arr[1] == arr[2]:
        return arr[0]
    else:
        dif = arr[0]
        for n in arr[1:]:
            if n != dif:
                return n


print((find_uniq([2, 1, 1, 1, 1, 1])))
from datetime import timedelta
import time


def make_readable(seconds):
    h = seconds // 3600
    m = (seconds - (h * 3600)) // 60
    s = seconds - ((m * 60) + (h * 3600))
    return f'{h:02}:{m:02}:{s:02}'


print(make_readable(99))


def rot13(message):
    crypt = {k: k - 13 for k in range(97, 123)}  # and k + 13 for k in range(97,110)}
    text = message
    # crypt2 = {k: k + 13 for k in range(97,110)}
    # text = message
    # return text2 = text.translate(crypt)
    return text.translate(crypt)


# print(rot13("test"))
import string

cleartxt = "TEST"
abc = "abcdefghijklmnopqrstuvwxyz"
secret = "".join([abc[(abc.find(c) + 13) % 26] for c in cleartxt])
print(secret)

import codecs

print(codecs.encode('Test', 'rot_13'))


def bmi(weight, height):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        return print('Underweight')

    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'

    elif 30 <= bmi:
        return 'Obese'


print(bmi(200, 1.8))


def shorten_to_date(long_date):
    list = long_date.split(',')
    return list[0]


print(shorten_to_date('poniedzialek luty 2 , 10:00'))

import datetime

x = datetime.datetime(2020, 5, 17)
y = datetime.datetime(2020, 5, 31)
z = y - x
print(z)


def year_days(year):
    if year % 400 == 0:
        return '%d has 366 days' % year
    elif year % 4 == 0 and year % 100 != 0:
        return '%d has 366 days' % year
    else:
        return '%d has 365 days' % year


print(year_days(2000))


def fuel_price(litres, price_per_litre):
    if litres <= 10:
        return (litres * price_per_litre) - litres * ((litres // 2) * 0.05)
    else:
        return litres * price_per_litre - litres * 0.25


print(fuel_price(10, 21.5))


def two_decimal_places(n):
    # raise NotImplementedError("TODO: two_decimal_places")
    return round(n, 2)


print(two_decimal_places(4.659725356))


def any_arrows(arrows):
    return 1 in [0 if i.get('damaged') else 1 for i in arrows]


print(any_arrows([{'range': 5}, {'range': 10, 'damaged': True}, {'damaged': True}]))


def eval_object(v):
    return eval(f"{v['a']}{v['operation']}{v['b']}")  # bez eval wyjdzie np 10-1 a z eval 9


print(eval_object({'a': 11, 'b': 1, 'operation': '-'}))


def rain_amount(mm):
    if mm < 40:
        return "You need to give your plant %d mm of water" % int(40 - mm)
    else:
        return "Your plant has had more than enough water for today!"


print(rain_amount(0))


def find_slope(points):
    if points[0] < 0 or points[1] < 0 or points[2] < 0 or points[3] < 0:
        return "undefined"
    else:
        a = ((points[3] - points[1]) / (points[2] - points[0]))
        return '"%d"' % a


print(find_slope([10, 50, 30, 150]))


def sum_array(arr):
    if len(arr) < 2:
        return 0
    else:
        arr.sort()
        del arr[-1]
        del arr[0]
        return sum(arr)


# from math import sqrt

def square_or_square_root(arr):
    return [int(i ** 0.5) if i ** 0.5 % 1 == 0 else i ** 2 for i in arr]


print(square_or_square_root([4, 3, 9, 7, 2, 1]))


def remove(s):
    return s.replace("!", "") + "!"


print(remove("!a!s!d!!!"))


def animals(heads, legs):
    if heads == legs == 0:
        return 0, 0
    elif legs % 2 == 1:
        return 'No solutions'
    elif heads <= 0 or legs <= 0 or heads >= 1000 or legs >= 1000 or heads * 4 < legs:
        return "No solutions"
    else:
        y = (legs - 2 * heads) / 2
        x = g = heads - y
        return int(x), int(y)


print(animals(54, 956))


def count_sheeps(sheep):
    return sheep.count(True)


print(count_sheeps([True, True, True, False,
                    True, True, True, True,
                    True, False, True, False,
                    True, False, False, True,
                    True, True, True, True,
                    False, False, True, True]))


def ice_brick_volume(radius, bottle_length, rim_length):
    return radius * radius * 2 * (bottle_length - rim_length)


print(ice_brick_volume(5, 30, 7))


def boolean_to_string(b):
    if b == True:
        return "True"
    else:
        return "False"


import math


def am_i_wilson(n):
    if n < 2:
        return False
    elif n > 600:
        return False
    elif ((((math.factorial(n - 1)) + 1) % (n * n))) == 0:
        return True
    else:
        return False


def expression_matter(a, b, c):
    a1 = a + b + c
    a2 = (a * b) + c
    a3 = a * (b + c)
    a4 = (a + b) * c
    a5 = a + (b * c)
    a6 = a * b * c
    return max(a1, a2, a3, a4, a5, a6)


print(expression_matter(1, 2, 3))
import cmath


def circle_diameter(sides, side_length):
    return (round(side_length * (1 / (cmath.tan(math.pi / sides))).real, 3))


print(circle_diameter(3, 4))


def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]


def logs(x, a, b):
    return math.log(a, x) + math.log(b, x)


print(logs(2, 4, 4))


def first(seq, n):
    return seq[:n]


print(first(['a', 'b', 'c', 'd', 'e'], 10))


def count_squares(cuts):
    return (cuts + 1) * (cuts + 1) + (cuts - 1) * (cuts * 4)


def get_number_from_string(string):
    return int(''.join(x for x in string if x.isdigit()))


print(get_number_from_string("asc1gh2sd"))


def correct_polish_letters(st):
    code = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
    return ''.join(code[k] if k in code else k for k in st)


print(correct_polish_letters('bąk'))


def define_suit(card):
    if card[1] == 'S':
        return "spades"
    if card[1] == 'C':
        return "clubs"
    if card[1] == 'D':
        return "diamonds"
    if card[1] == 'H':
        return "hearts"


print(define_suit('2S'))


def ensure_question(s):
    if s == "":
        return "?"
    elif s.endswith('?'):  # s[-1] == "?": endswith sprawdza czy na koncu stringa jest wartosc
        return s
    else:
        return s.replace("?", "") + "?"


print(ensure_question("as?"))


def check(a, x):
    if x in a:
        return True
    else:
        return False


print(check([66, 101], (66)))


def calculator(x, y, op):
    a = (str(x).isnumeric())
    b = (str(y).isnumeric())
    if a == False or b == False:
        return "unknown value"
    elif op == '+' or op == '-' or op == '*' or op == '/':
        return eval(f'({x}{op}{y})')
    else:
        return "unknown value"


print(calculator(2, '#', '*'))


def close_compare(a, b):
    if a < b:
        return -1
        if a > b:
            return 1
        else:
            return 0


def close_compare(a, b, margin=0):
    if abs(a - b) <= margin:
        return 0
    elif a > b:
        return 1
    else:
        return -1


print(close_compare(2, 3))


def bin_to_decimal(inp):
    return int(inp, 2)  # zmienia systemy np binarny szestnastkowy itp


print(bin_to_decimal('11'))


def descending_order(num):
    descending = int("".join(sorted(str(num), reverse=True)))
    return descending


print(descending_order('1267045'))


def flip(d, a):
    if d == 'R':
        return sorted((a), reverse=False)
    else:
        return sorted((a), reverse=True)


print(flip('R', [3, 2, 1, 2]))


def approx_equals(a, b):
    a = round(a, 5)
    b = round(b, 5)
    if abs(a - b) > 0.001:
        return False
    else:
        return True


print(approx_equals(123.2345, 123.234501))


def rysuj_trojkat(n):
    ilosc_gwiazdek = 1
    for i in range(1, n + 1):
        ilosc_spacji = n - i
        print(' ' * ilosc_spacji + '*' * ilosc_gwiazdek)
        ilosc_gwiazdek += 2


def rysuj_trojkat_2(n):
    ilosc_gwiazdek = 1
    szerokosc = 2 * n
    for i in range(1, n + 1):
        gwiazdki = '*' * ilosc_gwiazdek
        print(gwiazdki.center(szerokosc, ' '))
        ilosc_gwiazdek += 2


print(rysuj_trojkat_2(5))


def draw_stairs(n):
    return '\n'.join(' ' * i + 'I' for i in range(n))


print(draw_stairs(7))
# print('n'.join(' ' * i + 'I' for i in range(5)))
print('abc'.join('x' + 'I'))


def count_sheep(n):
    return ''.join(f"{i + 1} sheep..." for i in range(n))


print(count_sheep(9))


def human_years_cat_years_dog_years(human_years):
    if human_years > 2:
        return [human_years, 24 + (human_years - 2) * 4, 24 + (human_years - 2) * 5]
    elif human_years == 2:
        return [human_years, 24, 24]
    else:
        return [human_years, 15, 15]


print(human_years_cat_years_dog_years(10))


def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


print(multiple_of_index([-1, -49, -1, 67, 8, -60, 39, 35]))


def feast(beast, dish):
    return beast[0] == dish[0] and dish[-1] == beast[-1]

    '''
    if beast[0] == dish[0] and beast[-1] == dish[-1]:
        return True
    else:
        return False
'''


print(feast("chickadee", "chocolate cake"))


def warn_the_sheep(queue):
    d = len(queue) - queue.index('wolf') - 1
    if queue.index('wolf') == (len(queue) - 1):
        return 'Pls go away and stop eating my sheep'
    elif queue.index('wolf') != (len(queue) - 1):
        return f'Oi! Sheep number {d}! You are about to be eaten by a wolf!'


print(warn_the_sheep(['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']))


def isValid(formula):
    if ((not 7 in formula) and (not 8 in formula)):
        return False
    if ((1 in formula) and (2 in formula)):
        return False
    if ((3 in formula) and (4 in formula)):
        return False
    if ((5 in formula and not 6 in formula) or (6 in formula and not 5 in formula)):
        return False
    return True


print(isValid([5, 6, 7, 8]))


def nearest_sq(n):
    a = int(round(n ** 0.5, 0))
    return a ** 2


print(nearest_sq(10))


def multi_table(number):
    return str('\n'.join(f'{i} * {number} = {i * number}' for i in range(1, 11)))


print(multi_table(5))

import re


def replace_dots(str):
    return str.replace('.', "-")


print(replace_dots("one.two.three"))


def sum_str(a, b):
    if a == "" and b == "":
        return "0"
    elif b == "":
        return a
    elif a == "":
        return b
    else:
        c = int(a) + int(b)
        return (f"{c}")


print(sum_str("", "9"))


def capitalize_word(word):
    return word.capitalize()  # zmienia pierwsza literę w dużą


print(capitalize_word("aaaa"))


def derive(coefficient, exponent):
    return f'{coefficient * exponent}x^{exponent - 1}'


def sorter(textbooks):
    return sorted(textbooks, key=lambda L: (L.lower(), L))  # sortowanie bez uwzględnienia duzych liter


print(sorter(['Algebra', 'History', 'Geometry', 'English']))


def reverse_seq(n):
    return [n - i for i in range(0, n)]


print(reverse_seq(20))

print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')


def to_binary(n):
    return int(bin(n)[2:])  # zmienia systemy dziesietnego na binarny


print(to_binary(5))


def whatday(num):
    d = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    if 0 < num < 8:
        return d[num]
    else:
        return 'Wrong, please enter a number between 1 and 7'


print(whatday(0))


def usdcny(usd):
    return f"{usd * 6.75 :.2f} Chinese Yuan"  # zaokraglenie :.2f


print(usdcny(22))


def pythagorean_triple(integers):
    a, b, c = sorted(integers)
    return a * a + b * b == c * c


print(pythagorean_triple([5, 4, 3]))


def square_sum(numbers):
    return sum([i ** 2 for i in numbers])


print(square_sum([0, 3, 4, 5]))


def repeat_str(repeat, string):
    return "".join(string for i in range(0, repeat))


print(repeat_str(5, 'a'))


def remainder(a, b):
    a, b = sorted((a, b))
    if a != 0:
        return b % a


print(remainder(2, 2))
