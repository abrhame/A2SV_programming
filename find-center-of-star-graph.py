class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        list_ = defaultdict(list)
        for i,val in enumerate(edges):
            list_[val[0]].append(val[1])
            list_[val[1]].append(val[0])
        for key,val in list_.items():
            if len(val) == len(edges):
                return key