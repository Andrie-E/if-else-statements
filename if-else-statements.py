# Ask user to input 5 numbers. Find and print the biggest number 

# pseudocode

# Code that ask the users to input 5 numbers
first_number = float(input("Please enter your first number here: "))
second_number = float(input("Please enter your second number here: "))
third_number = float(input("Please enter your third number here: "))
fourth_number = float(input("Please enter your fourth number here: "))
fifth_number = float(input("Please enter your fifth number here: "))
# Code that finds the biggest number out of all the inputed numbers
if first_number >= second_number and first_number >= third_number and first_number >= fourth_number and first_number >= fifth_number:
    largest_number= first_number
elif second_number >= first_number and second_number >= third_number and second_number >= fourth_number and second_number >= fifth_number:
    largest_number= second_number
elif third_number >= first_number and third_number >= second_number and third_number >= fourth_number and third_number >= fifth_number:
    largest_number= third_number
elif fourth_number >= first_number and fourth_number >= second_number and fourth_number >= third_number and fourth_number >= fifth_number:
    largest_number= fourth_number
else:
    largest_number = fifth_number

# Code that prints the largest number
print("Base on the data that you have provided, the largest number is: ", largest_number)