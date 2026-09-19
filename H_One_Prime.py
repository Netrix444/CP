n=int(input())
if n<1:
    print('NO')
else:     
  c=0
  for i in range(1,n):
      if n%i==0:
        c=c+1

  if c==1:
      print("YES")
  else:
      print("NO")