class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = Counter(arr)
        occurance = set()
        for k,v in arr.items():
            if v in occurance:
                return False
            occurance.add(v)
        return True

 
        