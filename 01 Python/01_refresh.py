# newlist = ['andrew','steve','dan']
# secondlist = ['oscar','jake']
# newlist.extend(secondlist)
# newlist.append('caleb')
# print(newlist)
# ['andrew', 'steve', 'dan', 'oscar', 'jake', 'caleb']

# def squared(num):
#     return num**2

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
# tuples
# coordinates = (4, 5)
# tuples are immutable

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
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

# ~~~~~~~~~~~~~~~~~
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

# going to add some text to the end of a file with append
# file_cont = open('01_refresh.txt','r+')
# file_cont.write('\nthis is another line added with a')
# for line in file_cont.readlines():
#     print(line)
# file_cont.close()

# this is from the refresh.txt file
# this is the second line
# this is another line added with a

# ~~~~~~~~~~~~~~~~~
# importing modules
# import usefultools

# print(usefultools.feet_in_mile)
# 5280

# print(f'you rolled a {usefultools.roll_dice(6)}')
# you rolled a 6

# this link will take you to python modules
# https://docs.python.org/3/py-modindex.html
# ~~~~~~~~~~~~~~~~~

# classes and objects
# with a class you can define your own data type

# ! a template for an object !
# class Person:
    # we want to create an initialize function
    # in this init function you can define the properties a person should have
    # the argument after self can accept what we can defien a person as
    # def __init__(self, name, height, hair_color, eye_color):
    #     self.name = name
    #     self.height = height
    #     self.hair_color = hair_color
    #     self.eye_color = eye_color
    
    # def printPerson(self):
    #     print(f'{self.name} is {self.height} feet tall, they have {self.hair_color} hair and {self.eye_color} colored eyes')

# ! the object !
# Jim = Person('Jim', "5' 11''", 'brown', 'green')

# Jim.printPerson()
# Jim is 5' 11'' feet tall, they have brown hair and green colored eyes

# inheritance
# we can define a bunch of values 
# and functions in a class and make 
# a new class with those already 
# inside of the new one, but we can 
# add new values and functions

# so as a chef you are still a person so
# we can inherit the person attributes and functions
# class Chef(Person):
#     def __init__(self, name, height, hair_color, eye_color):
#         self.job = 'Chef'
#         super().__init__(name, height, hair_color, eye_color)

#     def make_fried_rice(self):
#         print(f'{self.name} is making fried rice, did you know that they are a {self.job}')

# Fred = Chef('Fred', "5' 10''", 'red', 'brown')

# Fred.printPerson()
# Fred.make_fried_rice()

# Fred is 5' 10'' feet tall, they have red hair and brown colored eyes
# Fred is making fried rice, did you know that they are a Chef

# ~~~~~~~~~~~~~~~~~
# use lambda as an anonymous function inside another function

# addTwo = lambda a , b : a + b
# print(addTwo(5,5))
# 10

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number
# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# print(mydoubler(11))
# 22

# def mynewfunc(num):
#     return lambda a : a * num

# mytripler = mynewfunc(3)
# print(mytripler(100))
# 300

# using the zip function to take in iterables and aggregate them in a tuple
# languages = ['Java', 'Python', 'Javascript']
# versions = [14, 3, 6]

# result = zip(languages, versions)
# print(list(result))
# [('Java', 14), ('Python', 3), ('Javascript', 6)]
# ~~~~~~~~~~~~~~~~~

# obj syntax
# class NameOfClass():
    
#     def __init__(self,param1,param2):
#         self.param1 = param1
#         self.param2 = param2

#     def some_method(self):
#         # perform some action
#         print(self.param1)

# class Student():
#     def __init__(self,mystudent_name,myclass_name,myschool_name):
#         self.student_name = mystudent_name
#         self.class_name = myclass_name
#         self.school_name = myschool_name

#     def printStudent(self):
#         print(f'{self.student_name} is a {self.class_name} and goes to school at {self.school_name}')

# Allan = Student('Allan','Freshman','Highland High School')
# Allan.printStudent()
# Allan is a Freshman and goes to school at Highland High School

class Animal:
    def __init__(self, is_animal):
        self.is_animal = is_animal
    
    def printAnimal(self):
        print('this is an animal')

# dog will inherit animal method printAnimal
class Dog(Animal):
    # CLASS OBJECT ATTRIBUTE
    # This will be the same for every instance of the class
    type = 'mammal'

    def __init__(self,dogName,dogBreed,spots):
        self.dog_name = dogName
        self.dog_breed = dogBreed
        self.dog_spots = spots

    # Python also has a super() function that will make the child class inherit 
    # all the methods and properties from its parent:
    # In Python, super() has two major use cases:
    # Allows us to avoid using the base class name explicitly
    # Working with Multiple Inheritance   

    def printSpots(self, number):
        if self.dog_spots:
            print(f'{self.dog_name} is my {self.dog_breed} and has {number} spots' )
        else:
            print(f'{self.dog_name} is my {self.dog_breed} and does not have spots' )

Sammy = Dog('Sammy', 'Poodle', True)
Sammy.printSpots(4)
Sammy.printAnimal()

# Sammy is my Poodle and has 4 spots