the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count {0}".format(number)

for fruit in fruits:
    print "A fruit of type: {0}".format(fruit)

# also we can go through mixed lists too

for i in change:
    print "I got {0}".format(i)

# we can also build lists, first start with an empty one

elements = []

# then use the range function to do 0 to 5 counts
for i in range(0,6):
    print "Adding {0} to the list.".format(i)
    # append is a function that lists understand
    elements.append(i)
    # append is the push of javascript

# now we can print them out too
for i in elements:
    print "Elements was: {0}".format(i)

# Study Drills
#
# Q. Take a look at how you used range. Look up the range function to understand it.
# Q. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
# A.
elements.append(range(0,6)) # ????

# Q. Find the Python documentation on lists and read about them. What other operations can you do to lists besides append?
# A. https://linuxconfig.org/python-list-methods
from random import randint

linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(len(linux_distros))
print(linux_distros[len(linux_distros) - 1])
linLen = len(linux_distros) - 1
print(linux_distros[randint(0,linLen)])

linux_distros.append("Mint")
print(linux_distros)
linux_distros.pop()
print(linux_distros)
linux_distros.pop(4)
print(linux_distros)
linux_distros.insert(2, "Mint")
print(linux_distros)
linux_distros.remove('Ubuntu')
print(linux_distros)

linux_distros = ['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
debian_distros = ['Debian', 'Ubuntu', 'Mint']
linux_distros.extend(debian_distros)
# print(linux_distros)

linux_distros.sort()
print linux_distros

new_distros = linux_distros.reverse()
print new_distros
print linux_distros
# .reverse() returns None. Therefore you should not be assigning it to a variable.
#
# Use this instead:
#
# stra = 'This is a string'
# revword = stra.split()
# revword.reverse()
# revword=''.join(revword) http://stackoverflow.com/questions/12336105/python-reverse-list
# http://stackoverflow.com/questions/931092/reverse-a-string-in-python


# Python also provides some built-in data types, in particular, dict, list, set (which along with frozenset, replaces the deprecated sets module), and tuple.
# A list is similar to an array, but has a variable size, and does not necessarily need to be made up of a single continuous chunk of memory. While this does make lists more useful in general then arrays, you do incur a slight performance penalty due to the overhead needed to have those nicer characteristics.
# I should also note that a List is not a specific kind of data structure. Rather, it's an abstract data type -- a description of what a data structure should behave like. https://www.reddit.com/r/learnprogramming/comments/3ha92l/what_is_the_difference_between_a_tuple_list_and/
