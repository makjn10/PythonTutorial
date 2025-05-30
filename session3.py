# working with strings

# my_str = "Mayank's training is really good"
# print(my_str)
# my_str = 'Mayank\'s "training" is really good'
# print(my_str)
# my_str = """Mayank's training is really good and
# he offers big data training"""
# print(my_str)
# my_str = """Mayank's training is really good and \n he offers big data training"""
# print(my_str)
# my_str = """Mayank's training is really good and \t he offers big data training"""
# print(my_str)

# string related operations
f_name = "Mayank"
l_name = "Jain"

# concatenation
print(f_name + " " +  l_name)
# length
print(len(f_name))
# indexing
print(f_name[2])
print(f_name[-2])

# string is immutable
# f_name[0] = "J"

# slicing
print(f_name[0:3])
print(f_name[0:-1])
print(f_name[0:])
print(f_name[:-2])
print(f_name[:])

print(f_name.find("a"))
print(f_name.find("t"))

print(f_name[1:5:2])
#reverse a string
print(f_name[-1::-1])
print(f_name[-1:0:-1])

print(f_name.endswith("ank"))

print(f_name.capitalize())

f_name = "    mayank "
print(f_name.strip())
print(f_name.lstrip())
print(f_name.rstrip())

print(f_name.replace("a", "e"))
print(f_name)

orders_df = "1,2017-03-23 00:00:00.0,1156,CLOSED"
orders_new_df = orders_df.split(",")
print(orders_new_df)
print(orders_new_df[3].lower())