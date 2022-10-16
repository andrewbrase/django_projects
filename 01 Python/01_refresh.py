
# newlist = ['andrew','steve','dan']
# secondlist = ['oscar','jake']
# newlist.extend(secondlist)
# newlist.append('caleb')
# print(newlist)
# ['andrew', 'steve', 'dan', 'oscar', 'jake', 'caleb']

def squared(num):
    return num**2

# map
numlist = [1,2,3,4,5,6,7,8,9,10]
results = list(map(squared, numlist))
print(results)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter
def list_filter(num):
    if (num % 2 == 0):
        return num

filtered = list(filter(list_filter, results))
print(filtered)
# [4, 16, 36, 64, 100]

print(filtered.pop())
# returns the last item of a list (100)

friends = ['andrew','jake','kevin']
friends.insert(2, 'inserted text')
print(friends)
# the text after index 2 will be pushed right ['andrew', 'jake', 'inserted text', 'kevin']