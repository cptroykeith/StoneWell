def solution(H):
    last=0
    c=0
    s=[]
    for i in range(0,len(H)):
        if (H[i]>last):
            last=H[i]
            c+=1
            s.append(H[i])
        elif(H[i]<last):
            while(len(s)>0 and H[i]<s[-1]):
                s.pop()
            if (len(s)==0 or H[i] !=s[-1]):
                c+=1
                s.append(H[i])
            last =H[i]