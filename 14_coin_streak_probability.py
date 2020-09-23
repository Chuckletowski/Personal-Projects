# Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails.
# Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values,
# and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out
# what percentage of the coin flips contains a streak of six heads or tails in a row. Of course, this is only an estimate, but 10,000 is a decent sample size.
# Some knowledge of mathematics could give you the exact answer and save you the trouble of writing a program, but programmers are notoriously bad at math.

from random import randint

outer_list = []
streak = 0

for toss in range(10000):
    inner_list = []
    for flip in range(100):
        inner_list.append(randint(0,1))
    outer_list.append(inner_list)
    for side in range(95):
        if inner_list[side] == inner_list[side + 1] == inner_list[side + 2] == inner_list[side + 3] == inner_list[side + 4] == inner_list[side + 5]:
            streak +=1
        else:
            continue

print('\n\nThe probability of a coin streak is %.2f%%' %(streak / 10000))
