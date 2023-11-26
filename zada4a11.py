input1 = int(input("Enter 2: "))

print("Въведете първите два елемента")
first_element_1 = int(input())
first_element_2 = int(input())


print("Въведете вторите два елемента")
second_element_1 = int(input())
second_element_2 = int(input())

sum1 = (first_element_1 + first_element_2)
sum2 = (second_element_1 + second_element_2)
diference = abs(sum1 - sum2)


if sum1 == sum2:
    print(f"Yes sum = {sum2}")
else:
    print(f"No difference is {diference}")