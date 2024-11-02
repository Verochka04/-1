numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

numbers[4] = 0
total = sum(numbers)
length = len(numbers)
x = total/length
numbers[4] = x


# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
