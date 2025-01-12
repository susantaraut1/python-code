# def function (a,b):
#     return a + b
# print(function(12 ,6))

# def function (num):
#    return num % 2 == 0
# def function_odd(num):
#     return num % 2!=0 
# def square(num):
#     return num ** 2

# num = int(input("ENTER A NUMBER:"))

# if function(num):
#     print(f"{num} is even")
# else :
#     print(f"{num} is odd")
    
# print(f"the square of {num} is {square (num)}")


# else :
#     print(f"{num} is odd")
    
# print(f"the square of {num} is {square (num)}")

import math_operation

# a = math_operation.add(5, 6)
# print(a)
# print(f"The substraction function result is: {math_operation.substraction(7, 4)}")
# x = int(input("ENTER X: "))
# y = int(input("ENTER Y: "))
# b = math_operation.multiply(x, y)
# print(b)

result_add = math_operation.add(5, 6)
result_substract = math_operation.substraction(7, 3)
result_multiply = math_operation.multiply(5, 7)
result_divide = math_operation.division(8, 4)


print(f"addition is {result_add}")
print(f"substracton is:{result_substract}")
print(f"multiplication is :{result_multiply}")
print(f"division is :{result_divide}")
