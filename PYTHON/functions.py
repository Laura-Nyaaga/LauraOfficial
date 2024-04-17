# The question I did is from: https://pynative.com/python-functions-quiz/
# # 1. 
# def fun1(num):
#     return num + 25
# fun1(5)
# print(num)
# It throws an error because we are printing num which is the parameter with no argument passed and without calling the function

# 2. It is true because we normally create functions to enable us reuse it in a program

# 3.
def display(**kwargs):
     for i in kwargs:
        print(i)
display(emp="Kelly", salary=9000)
# It print out the out as emp salary because i is only iterating through kwargs by coping the variables and not the value of the variables argument passed when invoking the function

# # 4.
# def display_person (*args):
#     for i in args:
#         print(i)
# display_person(name="Emma", age="25")

# 5.
def add(a,b):
    return a+5, b+5
result = add(3,2)
print(result)
# It prints out the output as (8,7) the function is a keyword argument although we are returning, we have also assigned a variable to enable print out a result.

# 6. It true because it always return the value as None by default

# 7.
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a,b)
    return a

result = outer_fun(5,10)
print(result)
# The output is 15 because we have only called the outer function by assing it a variable result and giving it arguments.

#  8. 
def outer_fun(a,b):
    def inner_fun(c,d):
        return c + d
    return inner_fun(a,b)

res = outer_fun(5,10)
print(res)
# it prints out the value as 15 because we have called the main function and pass arguments to it by assigning a variable

# 9. 
def fun1(name, age):
    print(name, age)
fun1('Emma', age=23)
fun1(age=23, name="Emma")

# fun1(name="Emma", 23)
# fun1(age=23, "Emma")
# These 2 ways of calling a function throws an error because the keyword argument has been folloed by positional argument which is not right unlike the first two

# 10. It is true because a python function can take more than one argument when the parameter passed in the function is defined by asterics first

# 11. Since the function is taking multiple values of the same datatype it is only right to define the parameter with a single asteric and not a double.
# fun1(25,75,55), fun1(10,20)
def fun1(*data):
    print(data)
    
fun1(25,75,55)
fun1(10,20)

# 12. 
def fun1(name, age=20):
    print(name, age)

fun1('Emma', 25)
# The out put is Emma 25 because the default parameter in age allows the value to be optional and it also comes after the requred parameter