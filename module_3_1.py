calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):  # Возвращает кортеж из длины стр, стр в верхнем и нижнем регистре.
    count_calls()
    lenght = len(string)
    hi = string.upper()
    low = string.lower()
    return lenght, hi, low


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for elem in list_to_search:
        if elem.lower() == string:
            return True
    return False


s = input("Введите строку :")
b = input("Введите строку 2 :")
print(string_info(s))
print(string_info(b))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
