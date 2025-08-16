from collections.abc import Callable


def apply_operation(operation: Callable, data: list) -> list:
    """
    This function is apply other function to each element of list and return result list
    :param operation: It is function
    :param data: List of numbers
    :return: Result
    """
    result = []
    for item in data:
        result.append(operation(item))

    return result

def square(number: int) -> int:
    return number ** 2

def double(number: int) -> int:
    return  number * 2


numbers = [1, 2, 3, 4]

square_numbers = apply_operation(square, numbers)
double_numbers = apply_operation(double, numbers)

print(square_numbers)
print(double_numbers)

help(apply_operation)
