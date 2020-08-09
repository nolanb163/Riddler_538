
import random




def pair():
    return random.randint(0,1)
    

def day(nematodes, days=1):
    total = nematodes;
    for d in range(days):
        nematodes = total
        for i in range((int)(nematodes/2)):
            total = total + pair()

    return total

while True:
    print(day(2,4))
    input()