a = "gtatcgtat"
b = "agtacgtcat"

def DPTable(s1,s2):
    m = len(s1)+1
    n = len(s2)+1
    v = [[0 for row in range(n)] for col in range(m)]
    
    for i in range(1,m):
        v[i][0] = i
    
    for j in range(1,n):
        v[0][j] = j
    
    for i in range(1,m):
        for j in range(1,n):
            print i,j,s1[i-1],s2[j-1]
            if s1[i-1] == s2[j-1]:
                v[i][j] = v[i-1][j-1]
                print v[i][j]
            else:
                print min(v[i][j-1],v[i-1][j]) 
                v[i][j] = 1 + min(v[i][j-1],v[i-1][j])
                print v[i][j]
    
    return v

    
    

x = DPTable(a,b)
for temp in x:
    print temp