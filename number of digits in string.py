m=input()
count=0
for x in range(0,len(m)):
    if(m[x].isdigit()):
        count=count+1
    else:
        count=count
print(count)
