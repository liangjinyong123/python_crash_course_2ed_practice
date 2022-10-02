# A Simple Dictionary
from hashlib import new


alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Working with Dictionaries
alien_0 = {'color': 'green'}

## Accessing Values in a Dictionary
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

## Adding New Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

## Starting with an Empty Dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

## Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# alien_0['speed'] = 'fast'
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# This must be a fast alien.
	x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

## Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

## A Dictionary of Similar Objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

## Using get() to Access Values
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

# Looping Through a Dictionary
## Looping Through All Key-Value Pairs
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"Value: {value}")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

## Looping Through All the Keys in a Dictionary
for name in favorite_languages.keys():
	print(name.title())

for name in favorite_languages: # Same as above
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(f"Hi {name.title()}.")

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

## Looping Through a Dictionary's Keys in a Particular Order
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

## Looping Through All Values in a Dictionary
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()): # Using set to remove duplicates
	print(language.title())

## Build a set
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

# Nesting
## A List of Dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)

### Make an empty list for storing aliens.
aliens = []

### Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color': 'green', 'point': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15

### Show the first 5 aliens.
for alien in aliens[:5]:
	print(alien)
print("...")

### Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

## A List in a Dictionary
### Store information about a pizza being ordered.
pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

### Summarize the order
print(f"You ordered a {pizza['crust']}-curst pizza "
	"with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")

### A Dictionary in a Dictionary
users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},

	'mcurie': {
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},

}

for username, user_info in users.items():
	print(f"\nUsername: {username}")
	full_name = f"{user_info['first']} {user_info['last']}"
	location = user_info['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")