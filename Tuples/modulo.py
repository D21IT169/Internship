t1=(2,4,3,5,6)
t2=(3,5,2,6,7)

res=[]
for i in range(0,len(t1)):
    res.append(t1[i]%t2[i])
res=tuple(res)
 
print("The modulus tuple : " + str(res))

