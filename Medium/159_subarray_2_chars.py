def lengthOfLongestSubstringTwoDistinct( s: str) -> int:
    ln = len(s)
    if ln == 0:
        return 0
    dct = {}
    j = 0
    maxWindow = 0
    count = 0
    for i in range(ln):
        dct[s[i]] = dct.get(s[i], 0) + 1      
        if dct[s[i]] == 1:
            count += 1      
        while count > 2:
            dct[s[j]] -= 1
            if dct[s[j]] == 0:
                count -= 1
            j += 1       
        maxWindow = max(maxWindow, i - j + 1)
    return maxWindow
if __name__ == '__main__':
    s='ccaabbb'
    ans = lengthOfLongestSubstringTwoDistinct(s)
    print(s)