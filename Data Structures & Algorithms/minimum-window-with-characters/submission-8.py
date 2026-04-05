class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        t_freq={}#freq of t
        for c in t:
            t_freq[c] = t_freq.get(c,0)+1
        required = len(t_freq) #unique chars needed
        formed=0
        left=0
        w_freq={}
        minlen = float('inf')
        res=""
        finalleft,finalright = 0,0
        for right in range(len(s)):
            ch = s[right]
            w_freq[ch] = w_freq.get(ch,0)+1 #expland and add char to window
            if ch in t_freq and w_freq[ch]==t_freq[ch]:
                formed+=1
            while formed==required:#check breakage
                if right-left+1<minlen:
                    minlen = right-left+1
                    finalleft,finalright = left,right
                lch = s[left]
                w_freq[lch]-=1
                if lch in t_freq and w_freq[lch]<t_freq[lch]:
                    formed-=1
                if w_freq[lch]==0:
                    del w_freq[lch]
                left+=1
        return s[finalleft:finalright+1] if minlen!=float('inf') else ""