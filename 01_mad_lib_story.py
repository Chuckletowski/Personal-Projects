# Write a program that allows a person to personalize a story. Take a page from a book or make up a story.
# Ask the user to enter information you can replace in the story such as their name, a place, or insert adjectives or adverbs
# into the story. Then display the personalized story to the user. For extra credit, make sure you correct anything they type in
# with the incorrect case (e.g. if they type an adjective in uppercase you may want to display it in lowercase).

man_name = input('Please give a man\'s name: ').capitalize()
occupation = input('Please give an occupation: ').lower()
noun_1 = input('Please give a noun: ').lower()
noun_2 = input('Please give another noun: ').lower()
noun_3 = input('Please give another noun: ').lower()
shape = input('Please give a shape: ').lower()
verb_1 = input('Please give a verb: ').lower()
woman_name = input('Please give a woman\'s name: ').capitalize()
body_part_1 = input('Please give a body part: ').lower()
verb_2 = input('Please give another verb: ').lower()
noun_4 = input('Please give another noun: ').lower()
place_1 = input('Please give a place: ').lower()
fast_food = input('Please give a fastfood chain: ').capitalize()
coffee_tea = input('Please give a coffee/tea shop: ').capitalize()
verb_3 = input('Please give another verb in past participle: ').lower()
noun_5 = input('Please give another noun: ').lower()
noun_6 = input('Please give another noun: ').lower()
verb_4 = input('Please give another verb: ').lower()
body_part_2 = input('Please give another body part: ').lower()
verb_5 = input('Please give another verb: ').lower()
adjective_1 = input('Please give an adjective: ').lower()
adjective_2 = input('Please give another adjective: ').lower()
emotion = input('Please give an emotion: ').lower()
verb_6 = input('Please give another verb ending in \'ing\': ').lower()
place_2 = input('Please give another place: ').lower()
noun_7 = input('Please give another noun: ').lower()
verb_7 = input('Please give another verb: ').lower()

print(f'''\n\n{man_name} is a normal {occupation}.
Then, one day, a {noun_1} explodes, causing a {noun_2} to blow up, and a nearby {noun_3} erupts into a {shape} of flames.
{man_name} realizes that he\'s being chased by the government, who\'s trying to {verb_1} him.
While on the run, he teams up with an incredibly attractive woman named {woman_name}, who has an incredible {body_part_1}.
{woman_name} may be from the streets, but she can {verb_2} like nobody\'s business.
The duo decide to turn the tables on their pursuers by blowing up a {noun_4}, which triggers a chain reaction,
causing the local {place_1}, {fast_food}, and {coffee_tea} to explode.
Then, the bad guys\' helicopter gets {verb_3} by a piece of {noun_5} from when the {noun_4} exploded,
and the helicopter explodes and falls onto a {noun_6}, causing it to {verb_4},
which shoots a fireball straight into the {body_part_2} of the bad guys\' leader and {verb_5} him.
Everything is {adjective_1} and the two decide that such a {adjective_2} ordeal has caused them to feel {emotion} with each other.
They decide to celebrate by {verb_6} in the {place_2}, and they even managed to use a {noun_7} from the beginning of the movie,
to {verb_7} the whole story together.''')
