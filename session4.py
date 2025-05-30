# List and Tuples

# list and tuple can hold values of different types in Python
# list is mutable and tuple is immutable
orders = [11, "2013-07-25", 12345, "CLOSED"]
print(orders)
print(type(orders))

print(orders[2])
# IndexError: list index out of range
# print(orders[5])

orders[3] = "COMPLETE"
print(orders)

orders.append(100)
print(orders)

orders.insert(1, 100)
print(orders)

print(len(orders))

# won't work as data types of elements is diff
# print(min(orders))
new_arr = [1, 3, 4, 5, 6]
print(min(new_arr))

ele = orders.pop()
print(orders)
print(ele)

orders_tuple = (1, "2013-07-25", 12345, "CLOSED")
print(orders_tuple)
print(type(orders_tuple))
print(len(orders_tuple))

# Loop
for x in orders:
    print(x)
    print(type(x))

# range
sum = 0
nums = range(1, 11)
for x in nums:
    sum += x
print(sum)

arr = [100, 200, None, "invalid", 300, 400.5]
sum = 0
i = 0
while i < len(arr):
    if type(arr[i]) == int or type(arr[i]) == float:
        sum += arr[i]
    i += 1
print(sum)

sum = 0
i = 0
while True :
    if type(arr[i]) == int or type(arr[i]) == float:
        sum += arr[i]
    i += 1
    if i == len(arr):
        break
print(sum)

print(orders.index(12345))
# Gives error if it does not exist
# print(orders.index(54444))

print(orders_tuple.index(12345))

print(123 in orders)

order_list = [50, 50, 40, 50, 30, 50]
print(order_list.count(50))
order_list.sort()
print(order_list)
order_list.reverse()
print(order_list)

order_new = order_list
# two references pointing to same mem location
order_new[2] = 200
print(order_list)

order_new = order_list.copy()
# two references pointing to same mem location
order_new[2] = 300
print(order_list)

customer_ids = [105, 106, 102, 101, 178, 112, 199, 129, 134, 102, 105, 101]
# find list of unique customers
# unique_customers = []
#
# for x in customer_ids:
#     if x not in unique_customers:
#         unique_customers.append(x)
#
# print(unique_customers)

unique = set(customer_ids)
print(unique)