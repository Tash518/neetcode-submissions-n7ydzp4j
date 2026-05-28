class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        if k==n:
            return total
        winSize = n-k
        minSum = winSum = sum(cardPoints[:winSize])
        for i in range(winSize,n):
            winSum += cardPoints[i]-cardPoints[i-winSize]
            minSum = min(minSum,winSum)
        return total - minSum