# Create a list with 6 items
fruit = ["apple", "banana", "blueberry", "watermelon", "raspberry", "strawberry"]
# Print all items
print(fruit)
# Print the first two items using a slice
print("The first two items are:", fruit[0:2])
# Print the middle two items using a slice
print("The middle two items are:", fruit[2:4])
# Print the first and last items using indexes
print("The first and last items are:", fruit[0], ",", fruit[5])

#Tuple Exercise
## Create a tuple with five foods
menu = ("burger", "pizza", "pasta", "salad", "soup")
# Print each item using a for loop
print("Menu:")
for food in menu:
    print(food)
# Replace two items by creating a new tuple
menu = ("burger", "sushi", "pasta", "tacos", "soup")
print("New Menu:")
for food in menu:
    print(food)
