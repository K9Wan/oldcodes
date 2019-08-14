# rand_practice.py
import random

print('Random float [0, 1):', random.random())
print('Random int [0, 9]:', random.randrange(0, 10))
print('Chosen one:', random.choice([50, 75, 100]))
l = [1, 2, 3, 4]
random.shuffle(l)
print('Shuffled:', l)