a=input().split()
if float(a[0])>0 and float(a[1])>0:
    print("Q1")
elif float(a[0])<0 and float(a[1])>0:
    print("Q2")
elif float(a[0])<0 and float(a[1])<0:
    print("Q3")
elif float(a[0])>0 and float(a[1])<0:
    print("Q4")
elif float(a[0])==0.0 and float(a[1])==0.0:
    print("Origem")
elif float(a[0])!=0.0 and float(a[1])==0.0:
    print("Eixo X")
elif float(a[0])==0.0 and float(a[1])!=0.0:
    print("Eixo Y")