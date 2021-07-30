# input_list = [1, 2, 3, 5, 6]


# def insert_shif_list(given_list, value):

#     new_list = given_list + [0]  # [0,0,0,0,0]

#     if len(given_list) % 2 == 0:
#         middle_index = int(len(given_list)/2)
#     else:
#         middle_index = int((len(given_list)+1)/2)

#     for i in range(len(given_list), (middle_index-1), -1):  # 1234 --5
#         if(i == middle_index):  # 2
#             new_list[middle_index] = value
#             return new_list

#         else:
#             new_list[i] = given_list[i-1]


# input_list = insert_shif_list(input_list, 4)
# print(input_list)

# given_list = [11, 3, 5, 6]
# value = 5


# def binarySearch(given_list, value):
#     test_index = -1
#     for i in range(len(given_list)):
#         if given_list[i] == value:
#             test_index = i
#             return test_index
#     return test_index


# print(binarySearch([1, 2, 3, 5, 6, 7], 4))

# def summation(matrix):

#     new_list = [0] * len(matrix)
#     for i in range(len(matrix)):  # 0
#         counter = 0
#         for j in matrix[i]:  # j = 4 and counter =0 and we have list of 4 7 3 0 2
#             if(j):
#                 counter = counter + j  # counter = 0 + 4
#             else:
#                 counter = counter + 0
#         new_list[i] = counter
#     return new_list


# print(summation([[1, 2, ""], [3, 5, 7], [1, 7, 10]]))

# def binarysearch(array, target):
#     start = 0
#     end = len(array)-1
#     middle = len(array) // 2
#     while end >= start:
#         middle = (end + start) // 2
#         if target == array[middle]:
#             return middle
#         elif array[middle] < target:
#             start = middle + 1

#         else:
#             end = middle - 1
#     return -1


# print(binarysearch([1, 2, 3, 5, 6, 7], 4))
# print(5//2)
