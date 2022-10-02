# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# Doing More Work Within a for Loop
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Doing Something After a for Loop
print("Thank you, everyone. That was a great magic show!")

# Logical error: Forgetting to Indent Additional Lines
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# Making Numerical Lists
## Using the range() Function
for value in range(1, 5): # print 1 - 4
    print(value)

for value in range(1, 6): # print 1 - 5
    print(value)

for value in range(5): # print 1 - 5
    print(value)

## Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    # square = value ** 2
    # squares.append(square)
    squares.append(value ** 2)

print(squares)

## Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

## List Comprehensions
squares = [value ** 2 for value in range(1, 11)]
print(squares)