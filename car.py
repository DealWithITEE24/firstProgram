# # class Vehicle:
# # def __init__(
# # self,
# # aaaa,
# # ):
# #
# # class Car:
# #
# #     # def __init__(
# #     #         self,
# #     #         owner,
# #     #         color,
# #     #         make,
# #     #         model,
# #     #         height_cm,
# #     #         length_cm,
# #     #         width_cm,
# #     #         woman_catcher,
# #     #         is_safe,
# #     #         transmission_type,
# #     #         transmission_gears
# #     # ):
# #     #     self.owner = owner
# #     #     self.color = color
# #     #     self.make = make
# #     #     self.model = model
# #     #     self.height_cm = height_cm
# #     #     self.length_cm = length_cm
# #     #     self.width_cm = width_cm
# #     #     self.woman_catcher = woman_catcher
# #     #     self.is_safe = is_safe
# #     #     self.transmission_type = transmission_type
# #     #     self.transmission_gears = transmission_gears
# #
# #     # owner = "Victoria"
# #     # color = "red"
# #     # make = "vw"
# #     # model = "beetle"
# #     # height_cm = 150
# #     # length_cm = 418
# #     # width_cm = 170
# #     # woman_catcher = True
# #     # is_safe = False
# #     # transmission_type = "atm"
# #     # transmission_gears = [1, 2, 3, 4, 5, "R"]
# #     is_car_moving = False
# #
# #     def __init__(
# #             self,
# #             owner=None,
# #             color=None,
# #             make=None,
# #             model=None,
# #             height_cm=None,
# #             length_cm=None,
# #             width_cm=None,
# #             woman_catcher=None,
# #             is_safe=None,
# #             transmission_type=None,
# #             transmission_gears=None,
# #     ):
# #         self.owner = owner
# #         self.color = color
# #         self.make = make
# #         self.model = model
# #         self.height_cm = height_cm
# #         self.length_cm = length_cm
# #         self.width_cm = width_cm
# #         self.woman_catcher: bool = woman_catcher
# #         self.is_safe: bool = is_safe
# #         self.transmission_type = transmission_type
# #         self.transmission_gears = transmission_gears
# #
# #     def move_the_car(self):
# #             self.is_car_moving = True
# #
# # class Bicycle:
# #     pass
# # OOP - object-oriented programming
#
#
# # classes and objects. Each one class can have many objects
#
# # always with first capital letter, in singular form
# # You cannot create identical classes by its meaning and/or name
#
# # inheritance between parent and child
# class Vehicle:
# 	is_vehicle_moving = False
#
# 	def __init__(
# 			self,
# 			count_of_wheels,
# 			has_license_plate,
# 			has_engine,
# 			is_electrical,
# 			count_of_doors,
# 	):
# 		self.count_of_wheels = count_of_wheels
# 		self.has_license_plate: bool = has_license_plate
# 		self.has_engine: bool = has_engine
# 		self.is_electrical = is_electrical
# 		self.count_of_doors = count_of_doors
#
# 	def push_the_vehicle(self):
# 		self.is_vehicle_moving = True
#
#
# class Car(Vehicle):
#
# 	# magic method
# 	# init = initialization = to start something new
# 	def __init__(
# 			self,
# 			owner,
# 			color,
# 			brand,
# 			model,
# 			count_of_wheels,
# 			has_license_plate,
# 			has_engine,
# 			is_electrical,
# 			count_of_doors,
# 			height_in_cm=None,
# 			length_in_cm=None,
# 			width_in_cm=None,
# 			woman_catcher=None,
# 			is_safe=None,
# 			transmission_type=None,
# 			transmission_gears=None,
# 	):
# 		super().__init__(
# 			count_of_wheels,
# 			has_license_plate,
# 			has_engine,
# 			is_electrical,
# 			count_of_doors,
# 		)
# 		self.owner = owner
# 		self.color = color
# 		self.brand = brand
# 		self.model = model
# 		self.height_in_cm = height_in_cm
# 		self.length_in_cm = length_in_cm
# 		self.width_in_cm = width_in_cm
# 		self.woman_catcher = woman_catcher
# 		self.is_safe = is_safe
# 		self.transmission_type = transmission_type
# 		self.transmission_gears = transmission_gears
#
#
# class Bicycle(Vehicle):
# 	movement_direction = None
#
# 	# static = doesn't change
# 	# the class attributes or alter the object in any way
# 	@staticmethod
# 	def do_a_wheelie():
# 		return "Bicycle did a great wheelie"
#
# 	def move_left(self):
# 		self.movement_direction = "left"
#
# 	def move_right(self):
# 		self.movement_direction = "right"
#
# 	def move_forward(self):
# 		self.movement_direction = "forward"
#
# 	def key_input(self, key):
# 		if key == "left":
# 			self.move_left()
# 		elif key == "right":
# 			self.move_right()
