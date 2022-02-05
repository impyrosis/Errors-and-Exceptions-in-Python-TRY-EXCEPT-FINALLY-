# 1. Create a program in Python and use try and catch.

print("Enter First Integer:  ")
a = input()

print("Enter 2nd Integer:  ")
b = input()

try:
    print("The sum of the two integers is,  ",
          int(a) + int(b))

except Exception as e:
    print(e)


print("We are practicing for Python lab 11 ")

# 2. Simulate error and catch it using except keyword

try:
    age = int(input("Please Type your Age:  "))
    print(f' Wow! you are {age} years old')

except:
    print("Invalid integer was entered")

# 3. Use finally keyword to finalize the statement.

try:
    age = int(input("Please Type your Age:  "))
    print(f' Wow! you are {age} years old')

except:
    print("Invalid integer was entered")

finally:
    print("Have a nice day buddy")
