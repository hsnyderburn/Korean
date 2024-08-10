#Clock randomizer for korean practice

from random import shuffle

hour = [1,2,3,4,5,6,7,8,9,10,11,12]
min = []
tod = ['AM','PM']

for x in range(1,60):
    min += [x]

# print(min)

shuffle(hour)
shuffle(min)
shuffle(tod)
print(" ")
print("The new time is:")
print(hour[1],':',min[1],tod[1])
print(" ")
