def lengthOfLongestSubstringTwoDistinct( s: str) -> int:
    if len(s)<=2:
        return len(s)
    count=0
    l=0
    max_length=0
    dct = {}
    for r,c in enumerate(s):
        dct[c]=dct.get(c,0)+1
        if dct[c]==1:
            count+=1
        while count>2:
            dct[s[l]]-=1
            if dct[s[l]]==0:
                count-=1
            l+=1
        max_length=max(max_length,r-l+1)
    return max_length
if __name__ == '__main__':
    s='eceba'
    ans = lengthOfLongestSubstringTwoDistinct(s)
    print(ans)