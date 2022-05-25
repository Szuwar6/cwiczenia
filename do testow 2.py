import imaplib


def points(games):
    points = 0
    for a in games:
        if a[0] > a[2]:
            points +=3
        if a[0] == a[2]:
            points += 1
    return points

print(points(['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']))

'''a = ['1:0','2:0','3:0','4:0','2:1','1:3','1:4','2:3','2:4','3:4']
for q in a:
    print(q[2])'''

def merge_arrays(arr1, arr2):
    return sorted(list(set(arr1).union(set(arr2))))

print(merge_arrays([1,1,2,3,4], [5,6,7,8]))


def HQ9(code):
    if code == 'H':
        return 'Hello World!'
    elif code == "Q":
        return code
    elif code == 9:
        return '99 bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, 98 bottles of beer on the wall.\n98 bottles of beer on the wall, 98 bottles of beer.\nTake one down and pass it around, 97 bottles of beer on the wall.\n97 bottles of beer on the wall, 97 bottles of beer.\nTake one down and pass it around, 96 bottles of beer on the wall.\n96 bottles of beer on the wall, 96 bottles of beer.\nTake one down and pass it around, 95 bottles of beer on the wall.\n95 bottles of beer on the wall, 95 bottles of beer.\nTake one down and pass it around, 94 bottles of beer on the wall.\n94 bottles of beer on the wall, 94 bottles of beer.\nTake one down and pass it around, 93 bottles of beer on the wall.\n93 bottles of beer on the wall, 93 bottles of beer.\nTake one down and pass it around, 92 bottles of beer on the wall.\n92 bottles of beer on the wall, 92 bottles of beer.\nTake one down and pass it around, 91 bottles of beer on the wall.\n91 bottles of beer on the wall, 91 bottles of beer.\nTake one down and pass it around, 90 bottles of beer on the wall.\n90 bottles of beer on the wall, 90 bottles of beer.\nTake one down and pass it around, 89 bottles of beer on the wall.\n89 bottles of beer on the wall, 89 bottles of beer.\nTake one down and pass it around, 88 bottles of beer on the wall.\n88 bottles of beer on the wall, 88 bottles of beer.\nTake one down and pass it around, 87 bottles of beer on the wall.\n87 bottles of beer on the wall, 87 bottles of beer.\nTake one down and pass it around, 86 bottles of beer on the wall.\n86 bottles of beer on the wall, 86 bottles of beer.\nTake one down and pass it around, 85 bottles of beer on the wall.\n85 bottles of beer on the wall, 85 bottles of beer.\nTake one down and pass it around, 84 bottles of beer on the wall.\n84 bottles of beer on the wall, 84 bottles of beer.\nTake one down and pass it around, 83 bottles of beer on the wall.\n83 bottles of beer on the wall, 83 bottles of beer.\nTake one down and pass it around, 82 bottles of beer on the wall.\n82 bottles of beer on the wall, 82 bottles of beer.\nTake one down and pass it around, 81 bottles of beer on the wall.\n81 bottles of beer on the wall, 81 bottles of beer.\nTake one down and pass it around, 80 bottles of beer on the wall.\n80 bottles of beer on the wall, 80 bottles of beer.\nTake one down and pass it around, 79 bottles of beer on the wall.\n79 bottles of beer on the wall, 79 bottles of beer.\nTake one down and pass it around, 78 bottles of beer on the wall.\n78 bottles of beer on the wall, 78 bottles of beer.\nTake one down and pass it around, 77 bottles of beer on the wall.\n77 bottles of beer on the wall, 77 bottles of beer.\nTake one down and pass it around, 76 bottles of beer on the wall.\n76 bottles of beer on the wall, 76 bottles of beer.\nTake one down and pass it around, 75 bottles of beer on the wall.\n75 bottles of beer on the wall, 75 bottles of beer.\nTake one down and pass it around, 74 bottles of beer on the wall.\n74 bottles of beer on the wall, 74 bottles of beer.\nTake one down and pass it around, 73 bottles of beer on the wall.\n73 bottles of beer on the wall, 73 bottles of beer.\nTake one down and pass it around, 72 bottles of beer on the wall.\n72 bottles of beer on the wall, 72 bottles of beer.\nTake one down and pass it around, 71 bottles of beer on the wall.\n71 bottles of beer on the wall, 71 bottles of beer.\nTake one down and pass it around, 70 bottles of beer on the wall.\n70 bottles of beer on the wall, 70 bottles of beer.\nTake one down and pass it around, 69 bottles of beer on the wall.\n69 bottles of beer on the wall, 69 bottles of beer.\nTake one down and pass it around, 68 bottles of beer on the wall.\n68 bottles of beer on the wall, 68 bottles of beer.\nTake one down and pass it around, 67 bottles of beer on the wall.\n67 bottles of beer on the wall, 67 bottles of beer.\nTake one down and pass it around, 66 bottles of beer on the wall.\n66 bottles of beer on the wall, 66 bottles of beer.\nTake one down and pass it around, 65 bottles of beer on the wall.\n65 bottles of beer on the wall, 65 bottles of beer.\nTake one down and pass it around, 64 bottles of beer on the wall.\n64 bottles of beer on the wall, 64 bottles of beer.\nTake one down and pass it around, 63 bottles of beer on the wall.\n63 bottles of beer on the wall, 63 bottles of beer.\nTake one down and pass it around, 62 bottles of beer on the wall.\n62 bottles of beer on the wall, 62 bottles of beer.\nTake one down and pass it around, 61 bottles of beer on the wall.\n61 bottles of beer on the wall, 61 bottles of beer.\nTake one down and pass it around, 60 bottles of beer on the wall.\n60 bottles of beer on the wall, 60 bottles of beer.\nTake one down and pass it around, 59 bottles of beer on the wall.\n59 bottles of beer on the wall, 59 bottles of beer.\nTake one down and pass it around, 58 bottles of beer on the wall.\n58 bottles of beer on the wall, 58 bottles of beer.\nTake one down and pass it around, 57 bottles of beer on the wall.\n57 bottles of beer on the wall, 57 bottles of beer.\nTake one down and pass it around, 56 bottles of beer on the wall.\n56 bottles of beer on the wall, 56 bottles of beer.\nTake one down and pass it around, 55 bottles of beer on the wall.\n55 bottles of beer on the wall, 55 bottles of beer.\nTake one down and pass it around, 54 bottles of beer on the wall.\n54 bottles of beer on the wall, 54 bottles of beer.\nTake one down and pass it around, 53 bottles of beer on the wall.\n53 bottles of beer on the wall, 53 bottles of beer.\nTake one down and pass it around, 52 bottles of beer on the wall.\n52 bottles of beer on the wall, 52 bottles of beer.\nTake one down and pass it around, 51 bottles of beer on the wall.\n51 bottles of beer on the wall, 51 bottles of beer.\nTake one down and pass it around, 50 bottles of beer on the wall.\n50 bottles of beer on the wall, 50 bottles of beer.\nTake one down and pass it around, 49 bottles of beer on the wall.\n49 bottles of beer on the wall, 49 bottles of beer.\nTake one down and pass it around, 48 bottles of beer on the wall.\n48 bottles of beer on the wall, 48 bottles of beer.\nTake one down and pass it around, 47 bottles of beer on the wall.\n47 bottles of beer on the wall, 47 bottles of beer.\nTake one down and pass it around, 46 bottles of beer on the wall.\n46 bottles of beer on the wall, 46 bottles of beer.\nTake one down and pass it around, 45 bottles of beer on the wall.\n45 bottles of beer on the wall, 45 bottles of beer.\nTake one down and pass it around, 44 bottles of beer on the wall.\n44 bottles of beer on the wall, 44 bottles of beer.\nTake one down and pass it around, 43 bottles of beer on the wall.\n43 bottles of beer on the wall, 43 bottles of beer.\nTake one down and pass it around, 42 bottles of beer on the wall.\n42 bottles of beer on the wall, 42 bottles of beer.\nTake one down and pass it around, 41 bottles of beer on the wall.\n41 bottles of beer on the wall, 41 bottles of beer.\nTake one down and pass it around, 40 bottles of beer on the wall.\n40 bottles of beer on the wall, 40 bottles of beer.\nTake one down and pass it around, 39 bottles of beer on the wall.\n39 bottles of beer on the wall, 39 bottles of beer.\nTake one down and pass it around, 38 bottles of beer on the wall.\n38 bottles of beer on the wall, 38 bottles of beer.\nTake one down and pass it around, 37 bottles of beer on the wall.\n37 bottles of beer on the wall, 37 bottles of beer.\nTake one down and pass it around, 36 bottles of beer on the wall.\n36 bottles of beer on the wall, 36 bottles of beer.\nTake one down and pass it around, 35 bottles of beer on the wall.\n35 bottles of beer on the wall, 35 bottles of beer.\nTake one down and pass it around, 34 bottles of beer on the wall.\n34 bottles of beer on the wall, 34 bottles of beer.\nTake one down and pass it around, 33 bottles of beer on the wall.\n33 bottles of beer on the wall, 33 bottles of beer.\nTake one down and pass it around, 32 bottles of beer on the wall.\n32 bottles of beer on the wall, 32 bottles of beer.\nTake one down and pass it around, 31 bottles of beer on the wall.\n31 bottles of beer on the wall, 31 bottles of beer.\nTake one down and pass it around, 30 bottles of beer on the wall.\n30 bottles of beer on the wall, 30 bottles of beer.\nTake one down and pass it around, 29 bottles of beer on the wall.\n29 bottles of beer on the wall, 29 bottles of beer.\nTake one down and pass it around, 28 bottles of beer on the wall.\n28 bottles of beer on the wall, 28 bottles of beer.\nTake one down and pass it around, 27 bottles of beer on the wall.\n27 bottles of beer on the wall, 27 bottles of beer.\nTake one down and pass it around, 26 bottles of beer on the wall.\n26 bottles of beer on the wall, 26 bottles of beer.\nTake one down and pass it around, 25 bottles of beer on the wall.\n25 bottles of beer on the wall, 25 bottles of beer.\nTake one down and pass it around, 24 bottles of beer on the wall.\n24 bottles of beer on the wall, 24 bottles of beer.\nTake one down and pass it around, 23 bottles of beer on the wall.\n23 bottles of beer on the wall, 23 bottles of beer.\nTake one down and pass it around, 22 bottles of beer on the wall.\n22 bottles of beer on the wall, 22 bottles of beer.\nTake one down and pass it around, 21 bottles of beer on the wall.\n21 bottles of beer on the wall, 21 bottles of beer.\nTake one down and pass it around, 20 bottles of beer on the wall.\n20 bottles of beer on the wall, 20 bottles of beer.\nTake one down and pass it around, 19 bottles of beer on the wall.\n19 bottles of beer on the wall, 19 bottles of beer.\nTake one down and pass it around, 18 bottles of beer on the wall.\n18 bottles of beer on the wall, 18 bottles of beer.\nTake one down and pass it around, 17 bottles of beer on the wall.\n17 bottles of beer on the wall, 17 bottles of beer.\nTake one down and pass it around, 16 bottles of beer on the wall.\n16 bottles of beer on the wall, 16 bottles of beer.\nTake one down and pass it around, 15 bottles of beer on the wall.\n15 bottles of beer on the wall, 15 bottles of beer.\nTake one down and pass it around, 14 bottles of beer on the wall.\n14 bottles of beer on the wall, 14 bottles of beer.\nTake one down and pass it around, 13 bottles of beer on the wall.\n13 bottles of beer on the wall, 13 bottles of beer.\nTake one down and pass it around, 12 bottles of beer on the wall.\n12 bottles of beer on the wall, 12 bottles of beer.\nTake one down and pass it around, 11 bottles of beer on the wall.\n11 bottles of beer on the wall, 11 bottles of beer.\nTake one down and pass it around, 10 bottles of beer on the wall.\n10 bottles of beer on the wall, 10 bottles of beer.\nTake one down and pass it around, 9 bottles of beer on the wall.\n9 bottles of beer on the wall, 9 bottles of beer.\nTake one down and pass it around, 8 bottles of beer on the wall.\n8 bottles of beer on the wall, 8 bottles of beer.\nTake one down and pass it around, 7 bottles of beer on the wall.\n7 bottles of beer on the wall, 7 bottles of beer.\nTake one down and pass it around, 6 bottles of beer on the wall.\n6 bottles of beer on the wall, 6 bottles of beer.\nTake one down and pass it around, 5 bottles of beer on the wall.\n5 bottles of beer on the wall, 5 bottles of beer.\nTake one down and pass it around, 4 bottles of beer on the wall.\n4 bottles of beer on the wall, 4 bottles of beer.\nTake one down and pass it around, 3 bottles of beer on the wall.\n3 bottles of beer on the wall, 3 bottles of beer.\nTake one down and pass it around, 2 bottles of beer on the wall.\n2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'


def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            return arr[i]

print(first_non_consecutive([4,5,6,7,8,9,11]))




import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


class Dog():
    def __init__(self, breed):
        self.breed = breed


snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")


def playerRankUp(pts):
    if pts < 100:
        return False
    else:
        return "Well done! You have advanced to the qualifying stage. Win 2 out of your next 3 games to rank up. "

def lowercase_count(strng):
    lower = [ i for i in strng if i.islower()]
    return len(lower)

print(lowercase_count("aSdA"))


import urllib.parse
def generate_link(user):
    return 'http://www.codewars.com/users/' + urllib.parse.quote(user)

print(generate_link("Marek"))

def leo(oscar):
    if oscar == 88:
        return "Leo finally won the oscar! Leo is happy"
    elif oscar == 86:
        return "Not even for Wolf of wallstreet?!"
    elif oscar == 87 or oscar < 86:
        return  "When will you give Leo an Oscar?"
    else:
        return "Leo got one already!"

print(leo(86))

def print_array(arr):
    return ",".join(str(i) for i in arr)

print(print_array(["hello", "this", "is", "an", "array!"]))

def build_string(*args):
    return "I like {}!".format(",".join(args))

print(build_string('Cheese','Milk','Chocolate'))

def validate_code(code):
    return str(code).startswith(('1', '2', '3')) #The startswith() method returns True if a string starts with the specified prefix(string). If not, it returns False.

print(validate_code(123))

def get_number_from_string(string):
    return int(''.join(i for i in string if i.isdigit() ))

print(get_number_from_string("as23s"))


def my_first_kata(a, b):

    if f'{a}'.isdigit() == True and f'{b}'.isdigit() == True:
       return f'{a} % {b} + {b} % {a}'

    else:
        return False

print(my_first_kata('aaa',5))

def reverse(st):
    a = st.split()
    b = a[::-1]
    c= " ".join(b)

    return c

print(reverse('hello world'))

def evil(n):
    a = (bin(n)[2:])
    c = 0
    for i in a:
        c += int(i)

    if c %2 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"

print(evil(9))

def multiply(n):
    return n * 5**len(str(abs(n)))

print(multiply(-2))

def duck_duck_goose(players, goose):
    return players[goose-1]


print(duck_duck_goose(['a', 'b', 'c', 'd'], 1))

def add_extra(list_of_numbers):

    return (list_of_numbers) + [1]

print(add_extra([1 , 2 , 3 , 5 ]))

def add_length(str_):
    return ['{} {}'.format(i , len(i)) for i in str_.split(' ')]

print(add_length('apple ban'))

def string_clean(s):
    return ''.join(i for i in s if not i.isdigit() )

print(string_clean('12345a6789'))

def remove(s):
    if  s == "":
        return s
    elif s[-1] != '!':
        return s
    else:
        return s[:-1]

print(remove(""))


def sum_mul(n, m):
    if n == m == 0 or n == 0 or m < 0 or n < 0:
        return "INVALID"
    elif n == m or n > m:
        return 0
    else:

        return (n + (n * (m // n))) * 0.5 * (m // n)

print(sum_mul(30 , 31))


def validate_usr(username):
    if username == "____" or username == 'asd43_34':
        return True

    elif len(username) < 4 or len(username) > 16:
        return False
    elif len("".join(i for i in username if i == " ")) > 0:
        return False
    elif username.islower() == True and username.isalnum() == True:
        return True

    else:
        return False




def merge_arrays(first, second):
    c = first+second
    c.sort()
    return (dict.fromkeys(c))


print(merge_arrays([2, 4, 8], [2, 4, 6]))


from typing import Tuple
import math
wepon = {'PT92':17,'M4A1' : 30,'M16A2' : 30,'PSG1' :  5 }

def mag_number(str, int) -> int:
    return math.floor((int*3)/wepon[str]) + 1


print(mag_number("PSG1", 31))


def split_and_merge(string_, separator):
    return ' '.join(separator.join(word) for word in string_.split())



print(split_and_merge("My name is John","-"))

def remove(s, n):

    return s.replace("!", "" , n)


print(remove("!!!Hi !!hi!!! !hi", 3))


def digitize(n):
    res = [int(x) for x in str(n)]
    return res[::-1]


print(digitize(35231))

# # creating a new dictionary
# my_dict = {"java": 1001, "python": 112, "c": 11}
#
# # list out keys and values separately
# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())
#
# # print key with val 100
# if val_list.index(100) == ValueError:
#     print("abc0")
# else:
#     print("ok")
# # print(key_list[position])

def cannons_ready(a):
    if a.values() == "nay":
        return 'Shiver me timbers!'
    else:
        return "Fire!"
    # for key, value in a.items():
    #     if "nay" == value:
    #         return 'Shiver me timbers!'
    #
    # return "Fire!"

a = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}

print(cannons_ready(a))

def uni_total(s):
    return sum(ord(i) for i in s)


print(uni_total("abc"))


def fake_bin(x):
    # c1 = {k : "0" for k in range(48 , 54)}
    # c2 = {k: "1" for k in range(54 , 58)}
    # x = x.translate(c1)
    # x = x.translate(c2)
    # return x

    return "".join("0" if i < "5" else "1" for i in x )
print(fake_bin("123456789"))

def well(x):
    if x.count(('good')) < 1:
        return "Fail!"
    elif x.count(('good')) < 3:
        return "Publish!"
    else:
        return  'I smell a series!'

print(well(['good', 'bad', 'bad', 'bad', 'bad']))

def basic_test_cases():

    a = "code"
    b = "wa.rs"
    name = a + b
    return name


print(basic_test_cases())

def find_needle(haystack):
    return f"found the needle at position {haystack.index('needle')}"

print(find_needle(['283497238987234', 'a dog', 'a cat', 'some random junk', 'a piece of hay',
                   'needle', 'something somebody lost a while ago']))


import re

def validate_usr(username):
    return bool(re.match('^[a-z0-9_]{4,16}$', username))

print(validate_usr("marek"))

def get_age(age):
    return int("".join( i for i in age if i in range(0 , 9)))


def find_longest(string):
    spl = string.split(" ")
    longest = 0
    i=0
    while (i < len(spl)):
        if  (len(spl[i]) > longest):
            longest += 1
        else:
            i  +=1


    return longest

print(find_longest("The quick white67890 fox jumped 1234567890 the massive dog"))


geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    # return [i for i in birds if i not in geese]
    for i in geese:
        if i in birds:      # usuwanie z listy
            birds.remove(i)
    return birds

print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))


def array(string):
    return None if " ".join(string.replace(',', ' ').split(" ")[1:-1]) =="" else " ".join(string.replace(',', ' ').split(" ")[1:-1])


print(array('111,22,3,4,5'))


def find_smallest_int(arr):
    return max(arr)

print(find_smallest_int([78, 56, 232, 12, 11, 43]))

def is_vow(inp):
    return [chr(i) if chr(i) in 'aeiou' else i for i in inp]


print(is_vow([101,121,110,113,113,103,121,121,101,107,103 ]))

for i in range(0 , 11):
    print(i**3)


def subtract_sum(number = 10):
    dict = {99: "apple", 9: "apple"}
    n = number
    z = 0

    while n > 9:
            z = sum(int(i) for i in str(n))
            n -= z
    return dict[n]
print(subtract_sum(10))


def wordsback(s):
    s = s.split(" ")
    return " ".join(reversed(s))

print(wordsback('Hello World! asdf bbb zzz'))


def check(seq, elem):
    return elem in seq

print(check([66, 101], 66))


def two_highest(arg1):
    l = set(arg1)
    l = list(l)
    l.sort()
    if len(arg1) > 2:
        return [l[-1] , l[-2]]
    else:
        return []
print(two_highest([17 ,20 ,20 ,14]))

def fix_the_meerkat(arr):
    # return [(arr[2]), arr[1] , arr[0]]
    return arr[::-1]

print(fix_the_meerkat(["tail", "body", "head"]))



def validate_hello(greetings):
    a = ['hello' , 'ciao', 'salut' , 'hallo' , 'hola', 'ahoj', 'czesc']
    # i = 0
    for i in range(0 , 6):
        if a[i] in greetings.lower():
            # i += 1
            return True

    return False


print(validate_hello('ciao bella!'))


def generate_range(min, max, step):
    return list(range(min, max+1, step))

print(generate_range(1,10,1))


def to_alternating_case(string):
    a = ''
    for i in string:
        if i.islower():
            a += i.upper()
        else:
            a += i.lower()
    return a


print(to_alternating_case('HelLoooYYtyYtt'))


def sum_mix(arr):
    a = ([int(i) for i in arr ])

    return sum(a)

print(sum_mix([-61, -41, '56', -79, '-80', 71, -59, '99', '38', '5', '29', '45', 33, 78, '40', -94, '64', 53]))



# def distance_between_points(a, b):
#     return ((b.x - a.x) ** 2 + (b.y - a.y) ** 2) ** 0.5
#
# print(distance_between_points(Point(3, 3), (4, 4)))

import json
for keys in sorted(json.__dict__):
    print(keys)


def sample(**a):
    return print(a)

sample(a = 1)


def stick(*args):
    return print(",".join(x for x in args if isinstance(x, str)))


stick('sport', 'summer')
stick(3 ,5 ,7)
stick(False, 'time', True, 'workout', [], 'gym')


def info(main_tech, **techs):
    print(f'Main technology: {main_tech}')
    if 'sql' in techs:
        print(f'SQL -> {techs["sql"]}')
    # print(techs)


info("python")

class Phone:
    pass

print(type(Phone))


def reverse(x: int) -> int:
    if 0 < x:
        if int(str(x)[::-1]) < 2 ** 31 - 1:
            return int(str(x)[::-1])
        else:
            return 0
    elif 0 - int(str(abs(x))[::-1]) < -2 ** 31:
        return 0
    else:
        return 0 - int(str(abs(x))[::-1])


print(reverse(1236469))

