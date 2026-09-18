a=int(input())
b=a//365
c=(int(a)-(365*b))//30
d=(a-365*b)-(30*c)
print(b,"years")
print(c,"months")
print(d,"days")