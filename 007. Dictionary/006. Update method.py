car_info = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car_info.update({"model": "xxxx"})                   # method -1
print(car_info)
car_info["model"] = "Mustang"                        # method - 2
print(car_info)


###########################output##############################
# {'brand': 'Ford', 'model': 'xxxx', 'year': 1964}
# {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
