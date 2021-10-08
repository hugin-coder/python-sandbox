from typing import List
import util.io.number_input as ni

print(ni.input_int_between(1, 9))
print(ni.input_float_between(0.1, 9.9))
#print('Hetta smakkar illa'.replace('smakk', 'lukt').replace('illa', 'væl'))
x = 0
if x > 0:
    print("hattar var rætt")
elif x < 0:
    print("hattar var skeivt")
else:
    print("hattar var synd men enn rætt")
x = 0
for i in range(10_000_000):
    if i % 1_000 == 0:
        x += i
print('x', x)

for i in range(2, 10, 2):
    if i % 2 == 0:
        print('even', i)
    else:
        print('odd', i)

for i in range(10):
    print(i, i // 3, i % 3)
l = list(range(1, 11))
print(l)
print(l[0])
print(l[4])

genre: List = ['pop', 'rock', 'jazz', 'classic']

# iterate over the list using index
for i in range(len(genre)):
    print(i, "I like", genre[i])

for g in genre:
    print("I like", g)
else:
    print("Hugin rokkar")