# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.
import pandas as pd

football = pd.read_csv('/Users/samfunk/ds/metis/metisgh/prework/dsp/python/football.csv')

football['Difference'] = football['Goals'] - football['Goals Allowed']

small = football[football['Difference'] == min(football['Difference'])]
print(small)
