class Solution:
    def average(self, salary: List[int]) -> float:
        average = 0
        for empSalary in salary:
            average +=empSalary
        average = average-(min(salary)+max(salary))
        return average/(len(salary)-2)