# Rolling Dice with Plotly
## Installing Plotly
## Creating the Die Class
from random import randint

class Die:
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

## Rolling the Die
# from die import Die

# Create a D6.
# die = Die()
# # Make some rolls, and store results in a list.
# results = []
# for roll_num in range(100):
#     result = die.roll()
#     results.append(result)

# print(results)

## Analyzing the Results
# die = Die()
# # Make some rolls, and store results in a list.
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# poss_results = range(1, die.num_sides + 1)
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# print(frequencies)

## Making a Histogram
# import plotly.express as px

# # Visualize the results.
# fig = px.bar(x=poss_results, y=frequencies)
# # fig = px.scatter(x=poss_results, y=frequencies)
# # fig = px.line(x=poss_results, y=frequencies)
# fig.show()

## Customizing the Plot
# import plotly.express as px

# title = "Results of Rolling One D6 1,000 Time"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
# fig.show()

## Rolling Two Dice
# Create two D6 Dice.
# import plotly.express as px

# die_1 = Die()
# die_2 = Die()

# # Make some rolls, and store results in a list.
# results = []
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)

# # Analyze the results.
# frequencies = []
# max_result = die_1.num_sides + die_2.num_sides
# poss_results = range(2, max_result + 1)

# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

# # Visualize the results.
# title = "Results of Rolling Two D6 Dice 1,000 Times"
# labels = {'x': 'Result', 'y': 'Frequency of Result'}
# fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# ## Further Customizations
# fig.update_layout(xaxis_dtick=1) # Make every bar labeled, otherwise some bars are unlabeld by default 

# fig.show()

## Rolling Dice of Different Sizes
import plotly.express as px

die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

## Further Customizations
fig.update_layout(xaxis_dtick=1) # Make every bar labeled, otherwise some bars are unlabeld by default 

# fig.show()

## Saving Figures
fig.write_html('dice_visual_d6d10.html')