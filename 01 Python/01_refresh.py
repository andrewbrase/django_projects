
# newlist = ['andrew','steve','dan']
# secondlist = ['oscar','jake']
# newlist.extend(secondlist)
# newlist.append('caleb')
# print(newlist)
# ['andrew', 'steve', 'dan', 'oscar', 'jake', 'caleb']

# def squared(num):
#     return num**2

# map
# numlist = [1,2,3,4,5,6,7,8,9,10]
# results = list(map(squared, numlist))
# print(results)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter
# def list_filter(num):
#     if (num % 2 == 0):
#         return num

# filtered = list(filter(list_filter, results))
# print(filtered)
# [4, 16, 36, 64, 100]

# print(filtered.pop())
# returns the last item of a list (100)

# friends = ['andrew','jake','kevin']
# friends.insert(2, 'inserted text')
# print(friends)
# the text after index 2 will be pushed right ['andrew', 'jake', 'inserted text', 'kevin']
# friends.remove('inserted text')
# print(friends)
# ['andrew', 'jake', 'kevin']

# print(friends.index('jake'))
# returns the index of that word (1)

# to remove everything from the list
# friends.clear()
# print(friends)
# []

# sort
# numlist = [1,7,4,3,9,6,2,5,8,10]
# numlist.sort()
# print(numlist)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# tuples
# coordinates = (4, 5)
# tuples are immutable

# dictionaries
# bank = {'jake':1020,
#         'caleb':2340,
#         'harry':700}

# for item in bank:
#     print(f"{item}'s balance is ${bank[item]}")

# jake's balance is $1020
# caleb's balance is $2340
# harry's balance is $700

# print(bank.get('jake', "not a valid key, this is a default value"))
# 1020
# print(bank.get('jak', "not a valid key, this is a default value"))
# not a valid key, this is a default value

# numrange = []
# for num in range(10):
#     numrange.append(num)

# print(numrange)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# exponent function
# user can decide if they want it squared, cubed etc with pow_num
# def raise_to_power(base_num, pow_num):
#     result = 1
    # we will loop through the loop the number of pow_num
    # that could be 2 or 3 etc
#     for index in range(pow_num):
#         result = result * base_num

#     return result

# print(raise_to_power(10,3))
# 1000

# catching errors

# number = int(input('enter in a number'))
# ValueError: invalid literal for int() with base 10: 'h'
# use a try except block

# try:
#     number = int(input('enter in a number : '))
#     print(f'your number is : {number}')
    # enter in a number : 3
    # your number is : 3
# except:
#     print('invalid input, please use a number')
    # invalid input, please use a number
# finally:
#     print('this code is complete')
    # this code is complete

# while loops

# x = 0
# while(x < 11):
#     print(f'x is equal to {x}')
#     x += 1

# x is equal to 0
# x is equal to 1
# x is equal to 2
# x is equal to 3
# x is equal to 4
# x is equal to 5
# x is equal to 6
# x is equal to 7
# x is equal to 8
# x is equal to 9
# x is equal to 10

# reading from external files
# file path, file mode (read, write, append(you can append info to the end, you can only add new info), r+ (read and write))
# file_cont = open('01_refresh.txt', 'r')

# how to get info from the file
# print(file_cont.readable())
# True
# this will return a boolean value to indicate if the file is readable

# how to read the first line
# print(file_cont.readline())
# print(file_cont.readline())
# this is from the refresh.txt file
# this is the second line

# theres a better function for reading multiple lines
# this will insert every line into an list
# print(file_cont.readlines())
# ['this is from the refresh.txt file\n', 'this is the second line']

# you can use this with a for loop
# for line in file_cont.readlines():
#     print(line)
    # this is from the refresh.txt file
    # this is the second line 

# when you open a file you want to make sure that you close it as well
# file_cont.close()