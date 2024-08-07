print("Hello, World!")

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# sum = num1 + num2
# print("The sum is:", sum)

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("the number is even.")
# else: 
#     print("The number is odd.")

# numbers = [1, 2, 3, 4, 5]
# print("List of numbers:", numbers)
# print("Sum of numbers", sum(numbers))
# print("Largest number:", max(numbers))

# for i in range(1, 11):
#     print(i)

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num + 1):
#     factorial *= i
#     print("The factorial of", num, "is", factorial)

# string = input("Enter a string: ")
# reversed_string = string[::-1]
# print("Reversed String:", reversed_string)

# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for char in string:
#     if char in vowels:
#         count += 1
#         print("Number of vowels:", count)

# my_dict = {"name": "Alice", "age": 25, "city": "New York"}
# for key, value in my_dict.items():
#     print(key, ":", value)

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number.")
#             break
#     else:
#         print(num, "is a prime number.")

# age = 25
# typed_number = "16"
# random_number = 3.5
# if you add a float and an integer, you will get a float

# result = age + random_number
# print(age + random_number)
# print(type(result))

# name_first = "Barra"

# for i in range(0,6, 2):
#     print(name_first)


# numbers = [1, 3, 5, 8]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# fruits = ["apple", "orange", "cherry"]
# for x in fruits
#  print(x)
# for fruit in fruits:
#     print(fruit)


# Problem 1: "FizzBuzz"
# for num in range(1,101):
#     string = ""
#     if num % 3 == 0:
#         string = string + "Fizz"
#     if num % 5 == 0:
#         string = string + "Buzz"
#     if num % 5 != 0 and num % 3 != 0:
#         string = string + str(num)
#     print(string)

# Problem 2: Fibonacci Sequence
# First Print out the first 20 numbers in the Fibonacci Sequence

nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence up to", nterms, ":")
    print(n1)
    # generate fibonacci sequence
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
