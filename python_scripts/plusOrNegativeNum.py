from random import randint

x = randint(-100,100)
while x == 0:
    x = randint(-100,100)

y = randint(-100,100)
while y == 0:
    y = rnadint(-100,100)


if x > 0 and y > 0:
    print("\t*****************************************\n")
    print("\t\tBoth Positive\n")
elif x < 0 and y < 0:
    print("\t*****************************************\n")
    print("\t\tBoth Negative\n")
elif x > 0 and y < 0:
    print("\t*****************************************\n")
    print("\t\tX is positive and Y is negative\n")
elif y > 0 and x < 0:
    print("\t*****************************************\n")
    print("\t\tX is negative and Y is positive\n")

print("\t*****************************************\n")
print(f"\t\t X  = {x} | Y  = {y}\n")
print("\t*****************************************\n")
