import re


def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    if operator == "subtract":
        return a - b
    if operator == "multiply":
        return a * b
    else:
        return a / b


print(arithmetic(3 , 7, "add"))


def sequence_sum(begin_number, end_number, step):
    return sum(range(begin_number, end_number+1, step))



print(sequence_sum(1,5,1))


def second_number(list):
    if len(list) <2:
        return "List is too short"
    a = max(list)
    list.remove(a)
    return max(list)

print(second_number([5 , 3, 2, 7 ]))


def second_largest(numbers):
    if len(numbers) < 2:
        return "List must contain at least 2 elements."
    a = b = numbers[0]
    for i in numbers:
        if i > a:
            a,b = i,a
        elif i > b:
            b = i
    return b


print(second_largest([1, 2, 3, 4, 5])) #4
print(second_largest([5, 5, 4, 3, 1])) #4
print(second_largest([3]))


def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    return " ".join(reversed_words)

#test
print(reverse_sentence("This is a simple sentence")) #siht si elpmis ecnetnes
print(reverse_sentence(" Hello World! ")) #!dlroW olleH
print(reverse_sentence("Sentence end with a dot.")) #tod a htiw dnetniS

def even_numbers(list):
    return [i for i in list if i % 2 == 0]


print(even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(even_numbers([1, 3,  5,  7,  9]))

# def multiplication_table(number):
#     for i in range(0, 10):
#         print (f"{number} x {i} = {number*i}")
#     return f"{number} x {10} = {number*10}"

def multiplication_table(number):
    result = ""
    for i in range(1, 11):
        result += f"{number} x {i} = {number * i}\n"
    return result

print(multiplication_table(9))


# def largest(n, xs):
#     result = []
#     i = 1
#     while i <= n:
#         result.append(max(xs))
#         i += 1
#         xs.remove(max(xs))
#
#     return result[::-1]

def largest(n, xs):
    return sorted(xs)[-n:]

print(largest(2,[10,9,8,7,6,5,4,3,2,1]))


def multiply_all(array):
    def inner_func(num):
        return [element * num for element in array]
    return inner_func

multiply = multiply_all([1,2,3])
result = multiply(2)
print(result)




def sum_of_integers_in_string(s):
    return sum(int(i) for i in re.findall('[0-9]+',s))

print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))