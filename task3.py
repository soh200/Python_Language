# list of words finding the largest
n=int(input(" enter the no. of words "))
a=[]
k=0
for i in range(n):
    a.append(str(input(" enter the words ")))
for i in range(n):
   if len(a[i]) > k :
        p=a[i]
        k=len(a[i])
print(" the largest word is ", end="") 
print(p)


