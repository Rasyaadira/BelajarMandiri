import random

health = int(100)

def Get_NRGEnemy():
    return random.choice([1,2,3])

i = 0
while i < 10:
    RNG = Get_NRGEnemy()
    print(RNG)
    i += 1