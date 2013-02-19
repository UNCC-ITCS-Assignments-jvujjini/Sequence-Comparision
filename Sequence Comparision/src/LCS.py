s1="agttgtagct"
s2="agtgctact"
    
def LCS(a,b):
    c=""
    for x in range(0,len(a)):
        if a[x] in b:
            c += a[x]            
    return c

#print LCS(s1,s2)

def LCS2(a,b):
    c=""
    #b += " "
    k = max(len(a),len(b))
    for x in range(0,k):
        if a[x] == b[x]:
            continue
        else:
            for i in range(x,k):
                if a[i] == b[i+1]:
                    a += a[:i] + " " + a[i+1:]
                    print a
                    print b
                    break
                elif a[i+1] == b[i]:
                    b += b[:i] + " " + b[i+1:]
                    break
    
    k = max(len(a),len(b))
    for x in range(0,k):
        if a[x] == b[x] and a[x] != " ":
            c += a[x]
        else:
            continue

        return c

print LCS2(s1,s2)
        