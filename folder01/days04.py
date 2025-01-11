# to day start with basics of functions  in python

# def greet(name):
#     print(f"hello,{name}!!!")
# greet("munna")
# greet("susan")

# def addition (a , b):
#     return a + b
# print(addition(4 ,6))
# print(addition(14 , 5))


# test functions in normal format

# num = int(input("Enter a number:"))

# if num %2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num } is odd.")

# square = num ** num
# print(f"the square of {num} is {square}.")
    
    
# now we use def funcntion

def is_even(num):
    return num % 2 == 0
def is_odd(num):
    return num % 2 != 0
def square(num):
    return num ** 2

num = int(input("Enter a numner:"))
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

print(f"the square of {num} is {square (num)}.")
