# Python Dictionary

# List - Mutable
# Tuple - Immutable
# Dictionary - Mutable. We can change the value of particular key, we can add/remove entries
# Key should be immutable (str, tuple etc.) - List won't work as a key
# unordered

word_dict = {"intelligent": "The one who is really brilliant",
             "rich": "A person who has a lot of money",
             "car": "a 4 wheeler vehicle",
             "Three": 3,
             3: "three",
             (1, 2, 3) : "tuple"}

print(word_dict)
print(type(word_dict))
print(word_dict["intelligent"])
print(word_dict["car"])
# KeyError: 'bike'
# print(word_dict["bike"])
print(word_dict.get("bike")) # returns None
print(word_dict[3])
print(word_dict[(1, 2, 3)])

word_dict["bike"] = "2 wheel"
word_dict["car"] = "4 wheel"

print(word_dict)

orders_data = [(101, 10000), (102, 20000), (103, 30000), (104, 40000),]
orders_dict = dict(orders_data)
print(orders_dict)
print(orders_dict[102])

keys = orders_dict.keys()
print(keys)
values = orders_dict.values()
print(values)
items = orders_dict.items()
print(items)

print(len(orders_dict))

orders_dict.clear()
print(len(orders_dict))

# dictionary comprehension
# { :  for ...... }