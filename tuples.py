random_nums_tuples = (1, 5, 6, 7, 9, 10, 25, 56, 100)
random_nums_list = [1, 5, 6, 7, 9, 10, 25, 56, 100]

print(f'Length of random_nums: {len(random_nums_tuples)}')

print("\n")


for num in random_nums_tuples:
  print(f'Current num: {num}')
else:
  print("End of loop\n")


print('Tuple Methods')
print(100*"_")
print(dir(random_nums_tuples))

print("\n")


import sys
print(f'Size of random_nums Tuple is: {sys.getsizeof(random_nums_tuples)}')
print(f'Size of random_nums List is: {sys.getsizeof(random_nums_list)}')


import timeit

test_list_time = timeit.timeit(stmt="[5, 10, 15, 20, 25]", number=1000000)
test_tuple_time = timeit.timeit(stmt="(5, 10, 15, 20, 25)", number=1000000)
print(f'Time elapsed (List): {test_list_time} vs Time elapsed (Tuples): {test_tuple_time}')


mulp_of_fives = 5, 10, 15, 20, 25,
print(f'Easy tuple definition: {mulp_of_fives}')


#Tuple destructuring
personal_details = "John", 20, "Canada"
name, age, location = personal_details
print(f'Name: {name} Age: {age} Location: {location}')
