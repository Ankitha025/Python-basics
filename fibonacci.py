n =int(input("enter the number of terms"))
a=0
b=1
for i in range(n):
    print(a,end=" ")
    temp_a=a
    a=b
    b=temp_a+b



