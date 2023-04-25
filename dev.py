import copy
from itertools import permutations


def max_lower_number(number):
    listed_number = [int(i) for i in str(number)]
    if len(set(listed_number)) == 1:
        return "None"

    numbers = []

    combinations = list((permutations(listed_number, len(listed_number))))
    for comb in combinations:
        numbers.append("".join(str(j) for j in comb))

    sorted_numbers = (sorted(list(set(numbers))))
    idx = sorted_numbers.index(str(number))
    # print(sorted_numbers)

    if idx + 1 == len(sorted_numbers):
        return "Wprowadzona liczba jest najwieksza"
    else:
        return sorted_numbers[idx + 1]


print(max_lower_number(112))

# num = 1425
#
# a = [int(i) for i in str(num)]
# combinations = list((itertools.permutations(a, len(a))))
# numbers = []
#
# for i in combinations:
#     numbers.append("".join(str(j) for j in i))
#
# print(combinations)
# print(numbers)
# so = sorted(numbers)
# print(sorted(so))
#
# inx = so.index(str(num))
# print(so[inx+1])
#
# import random
#
# def func(type='a'):
#  if type == 'a':
#    return 'Mark'
#  elif type == 'i':
#    return random.randint(0, 1000)
#
# def dec(func, type_):
#  x = 8
#  def wrapper():
#    value = func(type_)
#    if isinstance(value, int):
#      return value * x
#    elif isinstance(value, str):
#      return 'H1' + value
#  return wrapper
#
# print(dec(func,'a')())
#
#
# def find_next_permutation(x):
#     perms = sorted(set(int("".join(p)) for p in permutations(str(x))))
#     for perm in perms:
#         if perm > x:
#             return perm
#     return None
#
# x = 66645
# result = find_next_permutation(x)
# if result:
#     print(result)
# else:
#     print("None")
#
#
# class A:
#   pass
#
# class B:
#   pass
#
# a = A()
# b = B()
# print(type(a) == type(b), type(a), type(b))


def max_lower_number1(number):
    listed_number = [int(num) for num in str(number)]
    if len(set(listed_number)) == 1:
        return "None"
    if len(str(number)) ==2 and str(number)[0] < str(number)[1]:
        return str(number)[::-1]

    elif len(str(number)) ==2 and str(number)[0] > str(number)[1]:
        return "Wprowadzona liczba jest najwieksza"


    for i in reversed(range(len(listed_number))):
        if listed_number[i-1] <  listed_number[i]:
            new_list = listed_number[:i-1]

            number = listed_number[i - 1]
            to_order = sorted(listed_number[i:])
            if number > min(to_order):
                new_list.append(max(to_order))
                to_order.remove(max(to_order))
                to_order.append(number)
                final = new_list + sorted(to_order)
                return "".join(str(i) for i in final)

            else:
                new_list.append(min(to_order))
                to_order.append(int(number))
                final = new_list + sorted(to_order[1:])
                return "".join(str(i) for i in final)

    return "Wprowadzona liczba jest najwieksza"




print(max_lower_number(1233211))
print(max_lower_number1(1233211111111))




