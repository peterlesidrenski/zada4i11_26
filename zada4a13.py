max_number = None
min_number = None
while True:
    user_input = input("Въведете число (за край въведете 'done'): ")

    if user_input.lower() == 'done':
        break
    try:
        num = float(user_input)
    except ValueError:
        print("Невалидно число. Моля, въведете число или 'done' за край.")
        continue
    if max_number is None or num > max_number:
        max_number = num
    if min_number is None or num < min_number:
        min_number = num
if max_number is not None and min_number is not None:
    print("Най-голямото число: {}".format(max_number))
    print("Най-малкото число: {}".format(min_number))
else:
    print("Няма въведени числа.")