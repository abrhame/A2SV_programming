class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        heap = []
        for word,freq in words.items():
            heapq.heappush(heap, (-freq,word))
        n = len(heap)
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        return res