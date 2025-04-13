#Luhn Algorithm:
'''
1. from right to left double the value of every second digit; if the product is greater than 9,
sum the digit of the products.

2. take the sum of all digits.

3. If the sum of all the digits is a multiple of 10 then the number is valid; else it is not.
'''

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] #this function reverses the numbers. Works with string
    odd_digits = card_number_reversed[::2]
    
    # ':' is called slice and string[x:y:h] where x is starting index
    # y is the ending index and h is the step (amount of characters to skip over).
    
    for digit in odd_digits:
        sum_of_odd_digits += int(digit) # fuction to change string to int

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]

    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10) #divided by 10 and then add whatever is remainder.
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    # str.maketrans is a function and the frist part before , changes any dashes to nothing and second one changes any spaces to nothing.
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print("INVALID!")

main()        
