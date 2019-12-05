# Write a program that allows a person to personalize a story. Take a page from a book or make up a story.
# Ask the user to enter information you can replace in the story such as their name, a place, or insert adjectives or adverbs
# into the story. Then display the personalized story to the user. For extra credit, make sure you correct anything they type in
# with the incorrect case (e.g. if they type an adjective in uppercase you may want to display it in lowercase).

manName = input('Please give a man\'s name: ').capitalize()
occupation = input('Please give an occupation: ').lower()
noun1 = input('Please give a noun: ').lower()
noun2 = input('Please give another noun: ').lower()
noun3 = input('Please give another noun: ').lower()
shape = input('Please give a shape: ').lower()
verb1 = input('Please give a verb: ').lower()
womanName = input('Please give a woman\'s name: ').capitalize()
bodyPart1 = input('Please give a body part: ').lower()
verb2 = input('Please give another verb: ').lower()
noun4 = input('Please give another noun: ').lower()
noun5 = input('Please give another noun: ').lower()
fastfood = input('Please give a fastfood chain: ').capitalize()
coffeeTea = input('Please give a coffee/tea shop: ').capitalize()
verb3 = input('Please give another verb in past participle: ').lower()
noun6 = input('Please give another noun: ').lower()
noun7 = input('Please give another noun: ').lower()
verb4 = input('Please give another verb: ').lower()
bodyPart2 = input('Please give another body part: ').lower()
verb5 = input('Please give another verb: ').lower()
adjective1 = input('Please give an adjective: ').lower()
adjective2 = input('Please give another adjective: ').lower()
emotion = input('Please give an emotion: ').lower()
verb6 = input('Please give another verb ending in \'ing\': ').lower()
place = input('Please give a place: ').lower()
noun8 = input('Please give another noun: ').lower()
verb7 = input('Please give another verb: ').lower()

print(f'''\n\n{manName} is a normal {occupation}.
Then, one day, a {noun1} explodes, causing a {noun2} to blow up, and a nearby {noun3} erupts into a {shape} of flames.
{manName} realizes that he\'s being chased by the government, who\'s trying to {verb1} him.
While on the run, he teams up with an incredibly attractive woman named {womanName}, who has an incredible {bodyPart1}.
{womanName} may be from the streets, but she can {verb2} like nobody\'s business.
The duo decide to turn the tables on their pursuers by blowing up a {noun4}, which triggers a chain reaction,
causing the local {noun5}, {fastfood}, and {coffeeTea} to explode.
Then, the bad guys\' helicopter gets {verb3} by a piece of {noun6} from when the {noun4} exploded,
and the helicopter explodes and falls onto a {noun7}, causing it to {verb4},
which shoots a fireball straight into the {bodyPart2} of the bad guys\' leader and {verb5} him.
Everything is {adjective1} and the two decide that such a {adjective2} ordeal has caused them to feel {emotion} with each other.
They decide to celebrate by {verb6} in the {place}, and they even managed to use a {noun8} from the beginning of the movie,
to {verb7} the whole story together.''')
