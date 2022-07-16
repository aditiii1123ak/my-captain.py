#program to input n number of numbers in an array and print the count of positive input 
n= int(input("Enter the size of the array: "))
array=[n]
pos=0
zero=0
for i in range (0,n):
    x= int(input("Enter number:"))
    array.append(x)
    if(x>0):
      pos= pos+1
    else:
      zero=zero
print("the count of positive numbers entered: ",pos)
print("the count of zero entered:,zero)
