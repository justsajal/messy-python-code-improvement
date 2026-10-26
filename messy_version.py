# Example of messy code, kept for comparison only.
x=input("enter numbers separated by spaces: ")
a=x.split(" ")
b=[]
for i in a:
    if i!="":
        try:
            b.append(int(i))
        except:
            print("bad value")
c=0
for j in b:
    c=c+j
if len(b)>0:
 print("numbers",b)
 print("sum",c)
 print("average",c/len(b))
else:
 print("nothing to calculate")
