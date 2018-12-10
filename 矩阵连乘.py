def matix(p,n,m,s):
    for i in range(1,n+1):
        m[i][i]=0
    for r in range(2,n+1):
        for k in range(1,n-r+2):
            j=r+k-1
            m[k][j]=m[k+1][j]+p[k-1]*p[k]*p[j]
            s[k][j]=k
            for i in range(i+1,j):
                temp=m[k][i]+m[i+1][j]+p[k-1]*p[i]*p[j]
                if temp<m[k][j]:
                    m[k][j]=temp
                    s[k][j]=k
                print(m[k][j])
s=[[0 for i in range(10)]for i in range (10)]
m=[[0 for i in range(10)]for i in range (10)]
matix([30,35,155,10,20,25],5,m,s)

