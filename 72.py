#72
n=input("enter string:")
s=['a','e','i','o','u']
for i in n:
  if(i in s):
    print("Yes")
    break
else:
  print("No")
