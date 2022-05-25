def each_cons(lst, n):
    aaa = []

    for i in range(0, len(lst) - n+1):
        new = lst[i: n]
        aaa.append(new)
        n += 1

    return aaa


print(each_cons([1,2,3,4], 3))

# def strange_math(n, k):
#     list = []
#
#     for i in range(1 , n + 1):
#         list.append(str(i))
#
#     list.sort()
#
#     aaa = []
#     for i in list:
#         aaa.append(int(i))
#
#     return aaa.index(k) + 1

def strange_math(n, k):
    return sorted(range(n+1), key=str).index(k)

print(strange_math(15 , 15))

from functools import reduce
import operator

def logical_calc(array, op):
    dic = {"AND": operator.and_,
    "OR" : operator.or_,
    "XOR": operator.xor}
    return reduce(dic[op],array)

print(logical_calc([True, False], "XOR"))

import math
def grow(arr):
    return math.prod(arr)  # funkcja mnozy wszystko co jest w liscie

print(grow([1,2,3,4,5]))

def format_money(amount):
    return "${:.2f}".format(amount)

print(format_money(25))

def triple_trouble(one, two, three):
    text = ""
    for i in range(0, len(one)):
        text += one[i] + two[i] + three[i]
    return text



print(triple_trouble("aaa","bbb","ccc"))

import math

def round_it(n):
    b = str(n).split(".")
    if len(b[0]) == len(b[1]):
        return round(n)
    if len(b[0]) > len(b[1]):
        return math.floor(n)
    if len(b[0]) < len(b[1]):
        return math.ceil(n)

print(round_it(23.54))
print(round_it(23.5))
print(round_it(3.55))

def greet(language):
    return {
        'czech': 'Vitejte',
        'danish': 'Velkomst',
        'dutch': 'Welkom',
        'english': 'Welcome',
        'estonian': 'Tere tulemast',
        'finnish': 'Tervetuloa',
        'flemish': 'Welgekomen',
        'french': 'Bienvenue',
        'german': 'Willkommen',
        'irish': 'Failte',
        'italian': 'Benvenuto',
        'latvian': 'Gaidits',
        'lithuanian': 'Laukiamas',
        'polish': 'Witamy',
        'spanish': 'Bienvenido',
        'swedish': 'Valkommen',
        'welsh': 'Croeso'
    }.get(language, 'Welcome')

print(greet('polishh'))


def char_freq(message):
    return { ch : message.count(ch) for ch in message }


print(char_freq('Marek'))

def fibonacci(n: int) -> int:
    x,y = 0, 1
    for i in range(n):
        x , y = y , y+x
    return x

print(fibonacci(10))

def solve(s):
    a = len([i for i in s if i.isupper()])
    b = len([i for i in s if i.islower()])
    c = len([i for i in s if i.isdigit()])
    d = len(s) - a -b-c
    return [a ,b ,c ,d]

print(solve('AAss1234@#$'))

def solve(n):
    if n % 10 != 0:
        return -1
    bank = [500 , 200 , 100, 50 , 20 ,10]
    counter = 0
    for i in range(0,6):
        while n >= bank[i]:
            n -= bank[i]
            counter +=1
    return counter


print(solve(225))

def vowel_indices(word):
    # a = []
    # position = 0
    #
    # for i in word:
    #     position += 1
    #     if i in "aAeEiIoOuUyY":
    #         a.append(position)
    #
    # return a
    return [i for i,x in enumerate(word,1) if x.lower() in 'aeiouy']


	# return [word.index(i)+1 for i in word if i in "aAeEiIoOuUyY"]


print(vowel_indices('UNDISARMEeeD'))

def string_merge(string1, string2, letter):
    a = string1.index(letter)
    b = string2.index(letter)
    return string1[:a] + string2[b:]

print(string_merge("wonderful", "people", "e"))

import re

def sum_from_string(strng):
    result = re.findall('[0-9]+', strng)
    return sum([int(i) for i in result])

print(sum_from_string('a30561ff4fb19170aa598b1431b52edad1fcc3e0'))

def bit_march (n : int) -> list:
    a = []
    for i in range(1, 10-n):
        r = [0]*8
        for z in range(n):
            r[8-i-z] = 1
        a.append(r)

    return a

print(bit_march(6))

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]

print(transpose([[1,2,3], [4,5,6], [7,8,9]]))

# import operator
# from functools import reduce
#
# # def find_it(seq):  # sprytne rozwiazanie
# #     return reduce(operator.xor, seq)

def find_it(seq):

    for i in seq:
        if seq.count(i) %2 == 1:
            return i

print(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]))

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(DNA_strand('ATAATGCCGAT'))

def tribonacci(signature, n):
    result = []
    x,y,z = signature[0], signature[1],signature[2]
    for i in range(n):
        result.append(x)
        x , y , z = y, z , x+y+z
    return result

print(tribonacci([1, 1, 1], 10))

from collections import Counter


def duplicate_count(text):
    a = Counter(text.lower())
    value = a.values()
    counter = 0
    for i in value:
        if i > 1:
            counter += 1

    return counter
    # return len([c for c in set(s.lower()) if s.lower().count(c) > 1])

print(duplicate_count("abcdeaB"))

import re
def printer_error(s):

    b = re.findall('[n-z]',s)
    return f'{len(b)}/{len(s)}'



print(printer_error(s="kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"))

def sort_array(arr):
  # odds = sorted((i for i in arr if i%2 != 0) , reverse=True)
  # return [i if i%2==0 else odds.pop() for i in arr]
  odd = sorted([i for i in arr if i%2 ==1])
  result = []
  n = 0
  for i in arr:

    if i %2 ==0:
      result.append(i)
    else:
      result.append(odd[n])
      n+=1
  return result

def order(sentence):
  words=[]
  for i in range(1,10):
    for word in sentence.split():
      if str(i) in word:
        words.append(word)

  return " ".join(words)


print(order("is2 Thi1s T4est 3a"))


def remove_smallest(numbers):
  if numbers == []:
    return []
  a = numbers.copy()
  a.remove(min(a))
  return a


print(remove_smallest([5, 3, 2, 1, 4]))

conv = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'],
        [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'],
        [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'],
        [   1, 'I']]


def solution(n):
  result = ""
  i = 0
  while n > 0:
    while conv[i][0] >n:
        i+=1
    result += conv[i][1]
    n -= conv[i][0]
  return result

print(solution(91))


def solution(n):
    roman_numerals = {1000:'M',
                      900: 'CM',
                      500: 'D',
                      400: 'CD',
                      100: 'C',
                      90: 'XC',
                      50: 'L',
                      40: 'XL',
                      10: 'X',
                      9: 'IX',
                      5: 'V',
                      4: 'IV',
                      1: 'I'
    }
    roman = ""
    for i in roman_numerals.keys():
        while n >= i:
            roman += roman_numerals[i]
            n -= i

    return roman

print(solution(1591))
