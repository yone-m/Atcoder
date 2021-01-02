s=input()

i=0
j=0
ans=0
ls=len(s)

while i<len(s)-1 and j<len(s)-1:
    cnt1=1
    cnt2=1
    while i<len(s)-1 and s[i]==s[i+1]:
        i+=1
        cnt1+=1

    j=i+1
    while j<len(s)-1 and s[j]==s[j+1]:
        j+=1
        cnt2+=1
    i=j+1

    ans+=sum(range(max(cnt1,cnt2)+1))
    ans+=sum(range(min(cnt1,cnt2)))

if s[len(s)-1]=='<':
    ans+=1
print(ans)