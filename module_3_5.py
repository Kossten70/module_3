def get_multiplied_digits(number):
    # if number < 0:
    #     number *= -1
    str_number = str(number)  # строка
    first = int(str_number[0])  # первая цифра
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    if first != 0:
        return first
    return 1


result = get_multiplied_digits(40203)
print(result)
# number = 1234
# str_number = str(number)  # строка
# str_number = list(str_number)
#
# print(type(str_number))
#
# first = int(str_number[0])
# print(first)
