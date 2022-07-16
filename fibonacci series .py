n = int (input ("Enter how many terms you want to print:"))
if n==1:
  print (0)
elif n== 2:
  print (0)
  print (1)
elif n>2:
  first = 0
  second = 1
  print (first)
  print (second)
  for i in range (2,n):
     third = first + second
     print (third)
     first = second
     second = third
else:
   print("Invalid input")
