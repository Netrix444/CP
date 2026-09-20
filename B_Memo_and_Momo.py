a=input().split()
if int(a[0])%int(a[2])==0 and int(a[1])%int(a[2])==0:
    print("Both")
elif int(a[0])%int(a[2])==0 and int(a[1])%int(a[2])!=0:
    print("Memo")
elif int(a[0])%int(a[2])!=0 and int(a[1])%int(a[2])==0:
    print("Momo")
elif int(a[0])%int(a[2])!=0 and int(a[1])%int(a[2])!=0:
    print("No One")