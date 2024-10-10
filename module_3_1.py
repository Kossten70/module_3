calls = 0
string = input("Введите строку :")
print(string)


# def count_calls(calls):
#     calls += 1


def string_info(string):
    lenght = len(string)
    hi = string.upper()
    low = string.lower()
    print(lenght, hi, low)


string_info(string)
