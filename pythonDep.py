print("Here are a few basic python dependencies:")
print("We start by asking howdoi the following: How to open a file in python?")

from howdoi import howdoi
query = "open a file in python"
parser = howdoi.get_parser()
args = vars(parser.parse_args(query.split(' ')))
output = howdoi.howdoi(args)
print(output)

print("How about a joke?")
print("The next dependency will tell a random joke:")

import pyjokes
print(pyjokes.get_joke())

import emoji
print(emoji.emojize('That joke was :rolling_on_the_floor_laughing:'))