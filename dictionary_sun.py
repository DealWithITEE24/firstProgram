# # tupple - a datatype, list of values in () with a ", "
# # set - a datatype, list of values in {} with a ", "
# # list - a datatype, list of values in [] with a ", "
# # dictionary - a datatype, list of values in {} with "", or "":"" etc with levels of {} inside the {}
# # Python dictionary (dict)
#
# # fruits = ["apple", "banana", "pear", "cherry", 420, 69.63, None, True, {"my_dict": "test"}]
# #
# # # key, value pair
# # cherry = {
# # 	"name": "Cherry",
# # 	"color": "red",
# # 	"shape": "round",
# # 	"taste": "sweet",
# # 	"weight": 5.0,
# # 	"grows_during_winter": False,
# # 	"parasites": None,
# # }
#
# sun = {
#     "name": "Sol",
#     "age": 4.6,
#     "surface_temperature": 5772,
#     "hot": True,
#     "is_white_dwarf": False,
#     "planetary_system":
#         [
#             "Mercury",
#             "Venus",
#             "Earth",
#             "Jupiter",
#             "Saturn",
#             "Neptune",
#             "Uranus",
#             "Pluto"
#         ],
#     "Kuiper belt":
#         {
#             "Charon": "Dwarf planet"
#         },
#
#         "habitable planets":
#             {
#                 "Earth":
#
#                     {"moon": True,
#                      "water": True,
#                      "atmosphere": True},
#                 "Venus": "hell",
#                 "Mars": "Too cold, and no air"
#             }
#
# }
#
# # print(sun["planetary_system"]["Kuiper belt"]["Charon"])
# # print(sun["planetary_system"][8]["Kuiper belt"]["Charon"]) = in case the list of planets is
# # a List with [] you give it a number to get
#
# print(sun.get("planetary_system")[8].get("kuiper belt", {}).get("Charon"))
#
# Message
# general
#
# Shift + Enter
# to
# add
# a
# new
# line
