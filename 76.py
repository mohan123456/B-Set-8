n=int(input("enter a number:"))
if(n==0 or n==1):
  print("neither prime nor composite:")
else:
  for i in range(2,n):
    if(n%i==0):
      print("Yes")
      break
  else:
    print("No")
