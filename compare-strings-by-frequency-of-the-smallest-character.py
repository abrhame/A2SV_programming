class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def frequency(string):
            return string.count(min(string))
        f_queries = []
        f_words = []
        for query in queries:
            f_queries.append(frequency(query))
        for word in words:
            f_words.append(frequency(word))
        f_words.sort()
        def binary_search(freq,f_words):
            n = len(f_words) 
            left, right = 0, n
            stack = []
            while left < right:
                m = left + (right-left) // 2 
                if f_words[m] <= freq:
                    left = m+1
                else:
                    right = m
            return n - left

        ans = []
        for freq in f_queries:
            ans.append(binary_search(freq,f_words))
        print(f_queries)
        print(f_words)
        print(ans)

        return ans