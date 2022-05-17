#Zadanie1
numbers = [1,2,3,4,5,6,7,8,9,10]
cubes = [number * number * number for number in numbers]
print(cubes)
for number in cubes:
    if number%2==1:
        print(number)

#Zadanie2
new_list = [2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 0, 0]
newer_list = [number for number in new_list if number == 0]
newest_list = [number for number in new_list if number != 0]
print(newer_list)
print(newest_list)