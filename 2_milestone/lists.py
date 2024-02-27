# my_list1 = [] # Empty list
# my_list2 = [1, 2, 3] # List with elements
# my_list3 = list(range(1, 5))
# my_list4 = list(range(0, 14, 2))
# print(my_list4)

# # print(my_list1)
# # print(my_list2)
# # print(my_list3)

# # Index always starts with 0 not 1

# # print(my_list4[0])
# # print(my_list4[6])
# # print(my_list4[-2])
# my_list4[-2] = 100
# print(my_list4)

# my_list = ['apple', 'banana', 'cherry']
# print(my_list)
# my_list.append('mango')
# my_list.extend(['grapes', 'kiwi'])
# print(my_list)

# my_list = [1, 2, 3, 4, 5]
# print(my_list[1:4]) # Slicing from index 1 to 2 ([2, 3])
# print(my_list[:3]) # Slicing from the beginning to index 2 ([1, 2, 3])
# print(my_list[2:]) # Slicing


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenated_list = list1 + list2
# print(concatenated_list)

# print(len(concatenated_list))

# if 4 in concatenated_list:
#     print("found")
# else:
#     print("not found")

# my_list = [4, 2, 1, 3, 5]
# my_list.sort(reverse=True) # Sorting the list in ascending order
# my_list.reverse()


# my_list = list(range(20))
# print(my_list)
# # new_list=[]
# # for i in my_list:
# #     if i%2==0:
# #         new_list.append(i**2)
# # print(new_list)

# squares = [i**2 for i in my_list if i%2==0]
# # Syntax for list comprehension: [expression for_loop conditions]
# print(squares)


marks = [85,90,95,85,80]
average_marks=sum(marks)/len(marks)
print(average_marks)
print(min(marks))
print(max(marks))