def add(x , y):
    return x + y
def substraction(x , y):
    return y - x
def multiply(x , y):
    return x * y
def division(x , y): 
     if y != 0: # type: ignore
         return x / y
     else:
      return "error :Division by zero"