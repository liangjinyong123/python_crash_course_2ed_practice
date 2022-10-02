# A simple Example
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

# Conditional Tests
## Checking for Equality
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

## Ignoring Case When Checking for Equality
car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')
print(car)

## Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies")

## Numerical Comparisons
age = 18
print(age == 18)

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

## Checking Multiple Conditions
### Using and to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print((age_0 >= 21) and (age_1 >= 21))

### Using or to Check Multiple Conditions
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

## Checking Whether a Value Is in a List
requested_toppings = ['mushrooms', 'options', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

## Checking Whether a Value Is Not in a List
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

## Boolean Expressions
game_active = True
can_edit = False

# if Statements
## Simple if Statements
age = 19
if age >= 18:
	print("You are old enough to vote!")
	print("Have you registerd to vote yet?")

## if-else Statements
age = 17
if age > 18:
	print("You are old enough to vote!")
	print("Have you registerd to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

## The if-elif-else Chain
age = 12

if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $25.")
else:
	print("Your admission is $40.")

age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
else:
	age = 40

print(f"You admission cost is ${price}.")

## Using Multiple elif Blocks
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
else:
	price = 20

print(f"Your admission cost is ${price}.")

## Omitting the else Block
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 25
elif age < 65:
	price = 40
elif age >= 65:
	price = 20

## Testing Multiple Conditions
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
	print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
	print("Adding extra cheese.")

print("\nFinished making your pizza!")

# Using if Statements with Lists
## Checking for Special Items
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

## Checking That a List Is Not Empty
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

## Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers'
					'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print(f"Adding {requested_topping}")
	else:
		print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

# Styling Your if Statements