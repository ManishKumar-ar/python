d1 = {"India": "INR", "USA": "USD", "Hong Kong": "HKD"}

# Accessing value using keys
print(d1["India"])
print(d1)
# Replacing the value for a key in a dictionary
d1["India"] = "NEW **"
print(d1)
# Inserting a new key-value pair
d1[50] = "YEN"
print(d1)
#del a key
del d1["USA"]
print(d1)

#output
# INR
# {'India': 'INR', 'USA': 'USD', 'Hong Kong': 'HKD'}
# {'India': 'NEW **', 'USA': 'USD', 'Hong Kong': 'HKD'}
# {'India': 'NEW **', 'USA': 'USD', 'Hong Kong': 'HKD', 50: 'YEN'}
# {'India': 'NEW **', 'Hong Kong': 'HKD', 50: 'YEN'}
