def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)
# without the return statement the function is completely pointless.
# but there are some functions that don't need return such as help() and print()

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
    )

# in future we can change this code to accept input from the user and see how it
# goes!

#sep

print(1, 2, 3, sep=' < ')

# if you don't put sep then it is treated as having a default value of ' ' (a single space)
print(1,2,3)


# Modify a program so that it optionally takes a second argument representing the number of
# friends the candies are being split between. If no argument is provided, it should assume
# 3 frined, as before.

def to_smash(total_candies, n_friends = 3):
    return total_candies % n_friends
'''you can change this code later when you know how to take input and add it'''

