class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        zerowindow,maxzeros=0,0
        onewindow,maxones=0,0
        for c in s:
            if c=='0':
               zerowindow+=1
               maxzeros=max(maxzeros,zerowindow)
               onewindow=0
            else:
                onewindow+=1
                maxones=max(maxones,onewindow)
                zerowindow=0
        return maxones>maxzeros
if __name__ == '__main__':
    s='110100010'
    ob = Solution()
    ans = ob.checkZeroOnes(s)
    print(ans)