''' Taking the average of numbers given
learned today that in python the type goes after the equal sign and not before
the variable declaration unlike C++ '''

X = int(input("Enter first Number: "))
Y = int(input("Enter second Number: "))

sum = float(X + Y)

avg = (sum/2)


print("The average of the two numbers is:", avg)
print()

"""I like to challenge myself and want to see if I can do something"""

num = int(input("Enter whether you want the average of 2, 3, 4, or 5 numbers: "))

match num:
    case 2:
        X = int(input("Enter first Number: "))
        Y = int(input("Enter second Number: "))

        sum = float(X + Y)

        avg = (sum/num)


        print("The average of the two numbers is:", avg)

    case 3:
        X = int(input("Enter first Number: "))
        Y = int(input("Enter second Number: "))
        Z = int(input("Enter third Number: "))

        sum = float(X + Y + Z)

        avg = (sum/num)


        print("The average of the three numbers is:", avg)

    case 4:
        X = int(input("Enter first Number: "))
        Y = int(input("Enter second Number: "))
        Z = int(input("Enter third Number: "))
        H = int(input("Enter fourth Number: "))

        sum = float(X + Y + Z + H)

        avg = (sum/num)


        print("The average of the four numbers is:", avg)

    case _:
        X = int(input("Enter first Number: "))
        Y = int(input("Enter second Number: "))
        Z = int(input("Enter third Number: "))
        H = int(input("Enter fourth Number: "))
        K = int(input("Enter fifth Number: "))

        sum = float(X + Y + Z + H + K)

        avg = (sum/num)


        print("The average of the five numbers is:", avg)
        

