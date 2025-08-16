def outer_func(first_number):
    const = 2
    def inner_func(second_number):
        return (first_number + second_number) * const
    return inner_func

clouser = outer_func(10)
result = clouser(11)

print(result)