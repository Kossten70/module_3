def print_params(a=1, b='Строка', c=True):
    print(a, b, c)


print_params()
print_params(True, 5.3, 9)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
