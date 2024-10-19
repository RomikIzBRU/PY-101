numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_index=4
numbers[none_index]=round(sum(numbers[:none_index]+numbers[none_index+1:])/len(numbers), 2)
print("Измененный список:", numbers)
