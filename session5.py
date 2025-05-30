# List and Tuples Contd.

# create a new list after performing some transformations

order_amounts = [100, 200, 50, 500, 400, 900, 1200, 70]
# orders_inc_gst = []
#
# for x in order_amounts:
#     orders_inc_gst.append(x * 1.18)
#
# print(orders_inc_gst)

# List Comprehension
orders_inc_gst = [x * 1.18 for x in order_amounts]
print(orders_inc_gst)

# List of tuples
order_amounts_and_gst = [(100, 5), (200, 18), (50, 12), (500, 18)]
orders_inc_gst_2 = [x[0] + (x[0] * x[1] / 100) for x in order_amounts_and_gst]
print(orders_inc_gst_2)

orders_inc_gst_2_tuples = [(x[0], x[1], x[0] + (x[0] * x[1] / 100)) for x in order_amounts_and_gst]
print(orders_inc_gst_2_tuples)

# nested list
nested_list = [[x, x**2, x**3] for x in range(1, 4)]
print(nested_list)

# flatten list
flattened_list = [y for x in nested_list for y in x]
print(flattened_list)

# filter
orders_list = [
    [101, "2023-04-23", 11599, "CLOSED"],
    [102, "2023-04-23", 256, "PENDING_PAYMENT"],
    [103, "2023-04-23", 1200, "COMPLETE"],
    [104, "2023-04-23", 650, "CLOSED"]
]

orders_filter = [x for x in orders_list if x[3] == "CLOSED"]
print(orders_filter)

# Unpacking
order = [101, "2023-04-23", 11599, "CLOSED"]
order_id, order_date, cust_id, order_status = order
print(order_id)
print(order_date)
print(cust_id)
print(order_status)

# Slicing
print(order[0:2] + order[3:])

# enumerate
order = [101, "2023-04-23", 11599, "CLOSED"]
for index, element in enumerate(order):
    print(index, element)

