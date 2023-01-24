class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # we can form the teams by sorting the array, and taking a value from each side of the array
        skill.sort()
        left = 0
        right = len(skill) - 1
        teams = []
        while left < right:
            tmp = []
            tmp.append(skill[left])
            tmp.append(skill[right])
            teams.append(tmp)
            left += 1
            right -= 1
        
        # check if the skill of each team is equal
        for i in range(len(teams)-1):
            if sum(teams[i]) != sum(teams[i+1]):
                return -1
        
        # calculate the sum of the whole team
        ans = 0
        for team in teams:
            ans += team[0]*team[1]
            
        return ans
        