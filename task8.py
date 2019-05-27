# product of all elements of a list
a=[]
p=1
n=int(input(" enter the size "))
for i in range(n):
    a.append(int(input(" enter the no. ")))
for i in range(n):
    p=p*a[i]
print("product of all elements", p)
    
