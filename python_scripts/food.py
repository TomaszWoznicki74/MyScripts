from random import choice
food = choice(["apple","grape","bacon","steak","worm","dirt"])
print("**************")
print(food)
print("**************")



if food == "apple" or food == "grape":
    print("fruit")

elif food == "bacon" or food == "steak":
    print("meat")

elif food == "worm" or food == "dirt":
    print("yuck")
