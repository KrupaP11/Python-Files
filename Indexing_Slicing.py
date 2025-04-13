'''Importance of slicing and indexing '''

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#indexing
planets[0]
print(planets[0])

#Can also use negative to get last planet
print(planets[-1])

#print(planets[-2])

#Slicing: What are the first three planets?

print(planets[0:3]) #won't include the third index. Remember it starts from 0

# can also write it as: planets[:3]


#Give me all the planets from index 3 onward.
print(planets[3:])

#All the planets expect the first and last
print(planets[1:-1])

# the last 3 planets
print(planets[-3:])

#everyother planet
print(planets[::2])

#Every odd planet?
print(planets[1::3])

#changing the list
    #planets[3] = 'Pluto'
    #print(planets)

# len() gives the lenght of the list
print(len(planets))

#sorted() sorts the planet in alphabetically order
print(sorted(planets))

#sum() adds all the numbers
primes = [2, 3, 5, 7]
print(sum(primes))

#max and min
print(max(primes), min(primes))

"""interlide: objects. Numbers in python carry around an associated variable
called imag representing their imaginary part."""

x = 12 #x is a real number, so its imaginary part is 0.
print(x.imag)
#here's how to make a complex number.
c = 12 + 3j
print(c.imag)

'''The things an object carries around can also include functions.
A function attached to an object is called a method.
Numbers have a method called bit_length'''
x.bit_length
#to actually call it we add parentheses
x.bit_length() # x can be a number

# list methods. list.appends modifies a list by adding an item to the end:
planets.append("Pluto")
print(planets)

#list.pop removes and returns the last element of a list:
print(planets.pop())

#Searching lists. list.index method
print(planets.index('Earth'))

#what about pluto? Tells me pluto is not in list
    #print(planets.index('Pluto'))

#to avoid this we use in operator
print("Earth" in planets) #shows true

print("Calbefraques" in planets)

"""Tuples are almost exactly the same as lists. They differ in just two ways:
1. the syntax for creating them uses parentheses instead of square brackets"""

t = (1, 2, 3)
t = 1, 2, 3 #this is same as above
'''they cannot be modifies (they are immutable)
Tuples are often used for functions that have multiple return values.
as_integer_ration() method of float objects returns a numerator and denominator in tuple form'''

x = 0.125
print(x.as_integer_ratio())

numerator, denominator = x.as_integer_ratio()
print(numerator/denominator)

#to swap two variables
a = 1
b = 0
a, b = b, a
print(a, b)
