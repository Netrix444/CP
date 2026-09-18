a=input().split()
if (int(a[0])%int(a[1])==0):
    print('Multiples')
elif (int(a[1])%int(a[0])==0):
    print('Multiples')
else:
    print("No Multiples")