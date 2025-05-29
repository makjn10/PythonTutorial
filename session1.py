#single line comment
""" Multi
    Line
    Comment
"""

print("hello data engineers")
print("hello world")

#Variables
course_fee = 800
# 800 is stored in memory and course_fee points to it
course_fee = 850
# reassigning (a new portion of memory is created)

print(course_fee)

# different data types
# 5 main simple data types
instructor_name = "Mayank Jain"
course_fee = 800
course_rating = 4.9
is_batch_starting_soon = True
total_income = None

print(type(instructor_name))
print(type(course_fee))
print(type(course_rating))
print(type(is_batch_starting_soon))
print(type(total_income))

print(course_fee + 50)
# internally course_fee is converted to float , automatic type conversion
print(course_fee + 50.5)
print(course_fee)

course_fee = course_fee + 50.5
print(course_fee)

# TypeError: can only concatenate str (not "int") to str
# print(instructor_name + 1)

# Manually typecasting
course_fee = "800"
course_fee = int(int(course_fee) + 30.5)
print(course_fee)

# String concatenation and formatting
first_name = "Mayank"
last_name = "Jain"
print(first_name + last_name)
print(first_name + " " + last_name)
print("My first name is " + first_name + " and my last name is " + last_name)

# fString -> formatted string
print(f"My first name is {first_name} and my last name is {last_name}")

# input in python
# input always takes a string
# We have to typecast
salary = input("What is your salary? : ")
hike = input("What is the hike percentage? : ")
new_salary = int(salary) + (int(hike)/100 * int(salary))
print(new_salary)

