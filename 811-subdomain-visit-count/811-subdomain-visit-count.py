class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
            ans = Counter()
            for domain in cpdomains:
                count,subDomain = domain.split()
                count = int(count)
                sub = subDomain.split(".")
                for i in range(len(sub)):
                    ans[".".join(sub[i:])] += count
                    
            return ["{} {}".format(com,dom) for dom,com in ans.items()]

                    
