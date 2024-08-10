#money randomizer for korean practice

from random import shuffle


won = []

for x in range(1,200000):
    won += [x]

# print(min)

shuffle(won)
print(" ")
print("가격은:")
print("{:,}".format(won[1]), "원입니다")
print(" ")
