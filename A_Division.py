a=int(input())
for b in range(a):
    b=int(input())
    if b>=1900:
        print("Division 1")
    elif 1600<=b<=1899:
        print("Division 2")
    elif 1400<=b<=1599:
        print("Division 3")
    elif b<=1399:
        print("Division 4")
    