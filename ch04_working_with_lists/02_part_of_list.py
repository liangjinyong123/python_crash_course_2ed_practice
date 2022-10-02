# Working with Part of a List
## Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

## Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())

## Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuples
## Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# dimensions[0] = 250

my_int = (3)
print(type(my_int))

my_t = (3, )
print(type(my_t))

## Looping Through All Values in a Tuple
for dimension in dimensions:
	print(dimension)

## Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

# Styling Your Code
