# arithmetic operations
# + - * / % //
# precedence is left to right and BODMAS
# * /
# + -

bigdata_fee = 800
azure_fee = 600

bigdata_enrollments = 20
azure_enrollments = 40

total_revenue = bigdata_fee * bigdata_enrollments + azure_enrollments * azure_fee
print(f"Total revenue: {total_revenue}")

average_revenue = total_revenue / (bigdata_enrollments + azure_enrollments)
print(f"Average revenue: {average_revenue}")

print(15/4)
print(15//4)
print(15%4)
print(2**3)

# right side binding for **
print(2 ** 2 ** 3)

import math

total_sale = 20000.60
print(math.ceil(total_sale))
print(math.floor(total_sale))

total_sale = -20000.60
print(math.fabs(total_sale))

# conditional statements
marks = int(input("Enter the marks: "))
if marks >= 35:
    if marks > 80:
        print("A grade")
    else:
        print("Passed without A grade")
else :
    print("fail")

if marks >= 80:
    print("A grade")
elif marks >= 35:
    print("Passed without A grade")
else :
    print("fail")

# logical operators AND OR NOT
# Comparison operators == != > < >= <=
print(True and False)
print(True or False)
print(True and not False)

age = int(input("Enter the age: "))
crime_record = input("Any crime records (yes/no) : ")

if age >= 18 and crime_record == "no":
    print("Eligible")
else :
    print("Not eligible")

name = "Mayank Jain"
print("Mayank" in name)
print("Mayank" not in name)


