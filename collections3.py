# from time import sleep
#
# # for-loop, while-loop, continue, break, collections
#
# my_greeting = "Hello, my name is Vlad, I am from Latvia."
#
# car_brands = [
# 	"Audi",
# 	"BMW",
# 	"Lada",
# 	"MB",
# 	"Ford",
# 	"Toyota",
# 	"Chrysler",
# ]
# car_brands.append("Porsche")
# car_brands.append("Tesla")
# car_brands.append("Škoda")
#
# # 1. Audi
# # 2. BMW
# # 3. MB
# # ...
#
# car_number = 1
# number_of_cars = len(car_brands)
#
# for brand in car_brands:
# 	# if brand == "Ford" or brand == "Chrysler":
# 	# 	continue  # "continue with the next element in the list"
# 	# if brand == "Lada":
# 	# 	print(f"{brand} ?! Ok, bye!")
# 	# 	break  # my visit in the shop and showcase of all the cars
# 	sleep(0.5)
# 	print(f"{car_number}. {brand}")
# 	car_number = car_number + 1
# 	if car_number == number_of_cars + 1:
# 		new_car = input("Add car: ")
# 		car_brands.extend(new_car)
#
# # my_special_list = [
# # 	"dog",
# # 	69,
# # 	420.34,
# # 	True,
# # 	None,
# # 	["Audi", 543, True, None, "Toyota"]
# # ]
# # list can hold any data type elements inside
#
# # for my_element in my_special_list:
# # 	sleep(0.5)
# # 	print(my_element)