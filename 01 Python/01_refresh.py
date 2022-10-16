
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
def raise_to_power(base_num, pow_num):
    result = 1
    # we will loop through the loop the number of pow_num
    # that could be 2 or 3 etc
    for index in range(pow_num):
        result = result * base_num

    return result

print(raise_to_power(10,3))
# 1000