def edit_distance():
    
    s1 = "agttgtagct"
    s2 = "agtgctact"
    s3 = ""
    
    for x in xrange(0,len(s1)-1):
            if s1[x]==s2[x]:
                s3 = s3 + s1[x]
            else:
                continue
            
    print s3

edit_distance()
                
                