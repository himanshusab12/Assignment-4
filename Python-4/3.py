import random
for x in range(1,11):
    a=random.randint(1,10)
    b=random.randint(1,10)
    print("Question",x,':',a,'x',b)
    mult = int(input())
    if mult==(a*b):
        print("Right!")
    else:
        print("Wrong. The answer is",a*b)
