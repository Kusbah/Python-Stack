import random
def randInt(min=0, max=100):
    num = random.random() * (max - min) + min
    return round(num)


print(randInt())                    # Random int between 0 and 100
print(randInt(max=50))             # Random int between 0 and 50
print(randInt(min=50))             # Random int between 50 and 100
print(randInt(min=50, max=500))