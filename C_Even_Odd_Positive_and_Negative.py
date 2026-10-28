a=int(input())
b=list(map(int,input().split()))
Even = 0
Odd = 0
Positive = 0
Negative = 0
for i in b:
    if i%2==0:
        Even += 1
    else:
        Odd += 1
    if i>0:
        Positive += 1
    elif i<0:
        Negative += 1
print("Even:",Even)
print("Odd:",Odd)
print("Positive:",Positive)
print("Negative:",Negative)