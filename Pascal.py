#Mustafa Anjrini on 09.09.2024

#choose n to select the length of the triangle

def pas(n):
    a=[[1,1]]
    for j in range(n):
        b=[1]*(len(a[j])+1)
        for i in range(1,len(a[j])):
            b[i]=a[j][i-1]+a[j][i]
        a.append(b)
    return(a)

pas(10)
