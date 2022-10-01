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
