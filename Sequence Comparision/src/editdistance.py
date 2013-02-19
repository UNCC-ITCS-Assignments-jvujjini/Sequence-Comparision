'''def edit_distance():
    
    s1 = "abcde"
    s2 = "bcdae"
    s3 = ""
    
    for x in range(0,len(s1)-1):
            if s1[x]==s2[x]:
                s3 = s3 + s1[x]
            else:
                continue
            
    print s3

edit_distance()

def example(a,b):
    for i in range(0,len(a)-1):
        for  j in range(0,len(b)-1):
            if i = 0:
                Edit(a,b) = len(b)-1
            elif j = 0:
                Edit(a,b) = len(a)-1
            else:
                Edit(a,b) = min(Edit(a-1,b)+1,Edit(a,b-1)+1, Edit(a-1,b-1)+)
    
                
   '''             