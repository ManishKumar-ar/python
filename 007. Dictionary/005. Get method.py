car_info = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


print(car_info.get("model"))          # using get method
print(car_info["model"])               # using array method

print(car_info.get("xx"))            #if key is not there, by default give none
print(car_info.get("xx","error"))  
print(car_info.get("xx",4220))


###############output#####################################################
# Mustang
# Mustang
# None
# error
# 4220
