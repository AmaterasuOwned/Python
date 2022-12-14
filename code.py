def degree_of_four(number: int) -> bool:
    if number == 0:
        return False
    while number != 1:
        if number % 4 != 0:
            return False
        number = number // 4
    return True


print(degree_of_four(int(input())))
